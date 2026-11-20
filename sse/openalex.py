"""OpenAlex (research papers) — text domain with a 4-level topic tree, plus Authors / Institutions tables.

Example query:  "papers whose subfield is like THIS RAG paper, by authors whose research area is like it,
                 at institutions whose research profile is like UIC's"

Data   : ~100k papers (articles, English, 2015-2024, with an abstract), sampled evenly over the 26 OpenAlex
         fields -> all 4 domains.  Text = title + abstract.
Tree   : OpenAlex topics: domain (4) > field (26) > subfield (~250)   [v2: topic level (~4k) dropped, too sparse]
Split  : 20% of topics fully held out ("unseen"); other papers 70% train / 30% "seen_test".
Encoder: SPECTER2 (allenai/specter2_base + proximity adapter, 768 numbers), frozen.  --encoder specter2_base
         (no adapter, no extra package) or bge (BAAI/bge-base-en-v1.5, as MovieLens) are alternatives.
SSE    : [ taxonomy 128 | rest 640 ], prefixes 16 / 64 / 128 = domain / field / subfield (as iNat).
Truth  : tree similarity (same subfield > same field > same domain > unrelated).

Relations for VecJOIN / institutions:
  Authors      : ~300 institutions (random, >= 15 distinct authors in the paper sample) x up to 20 authors;
                 for each author up to 30 of their OTHER papers (not in the 100k sample) are fetched.
                 Author vector (per block/prefix) = normalised mean of the SSE of their papers.
  Institutions : vector = normalised mean of their authors' vectors.
  Truth        : an author's research area at a level = share of their papers with each label at that level;
                 an institution's profile = sum of its authors' shares.  No author/institution label is ever
                 used for training — only paper topics.

Usage:
  .venv/bin/python -m sse.openalex fetch                       # papers (needs OPENALEX_API_KEY in .env)
  .venv/bin/python -m sse.openalex fetch_authors               # authors' other papers
  .venv/bin/python -m sse.openalex build                       # tables (no GPU)
  .venv/bin/python -m sse.openalex encode [--encoder specter2] # text vectors (GPU)
  .venv/bin/python -m sse.openalex train --method treesc|tree|main|mrl|b3sc|csnsc --seed 0
  .venv/bin/python -m sse.openalex eval --seed 0               # E2, E2b, E3 (+ B1 labels, encoder, PCA prefix)
  .venv/bin/python -m sse.openalex join --seed 0               # E8: Papers VecJOIN Authors, institution similarity
  .venv/bin/python -m sse.openalex e6 --seed 0                 # roll-up / drill-down inside one domain
"""
import argparse
import json
import math
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from pathlib import Path

import numpy as np
import pandas as pd
import scipy.sparse as sp

# torch and the shared training / scoring code are imported lazily (_gpu()), so `fetch`, `fetch_authors`
# and `build` run on a machine with only requests / numpy / pandas / pyarrow / scipy.
ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/openalex"
CACHE = ROOT / "cache/openalex"
OUT = ROOT / "results/openalex"
# v2 (2026-11-20): topic level dropped (4k topics x ~9 papers: too sparse; 58% of papers had no matching author).
# Tree = domain > field > subfield (like Order > Family > Genus); topic is kept only for the E3 search test.
LEVELS = ("domain", "field", "subfield")
PREFIX = {"domain": 16, "field": 64, "subfield": 128}
CODE_LEVELS = (*LEVELS, "topic")
TAX_DIM = 128
N_PAPERS = 100_000
MIN_WORDS = 30
API = "https://api.openalex.org"
WORK_SELECT = ("id,title,abstract_inverted_index,publication_year,type,language,primary_topic,"
               "cited_by_count,primary_location,authorships")
SSE_METHODS = (("SSE-treeSC", "treesc"), ("SSE-tree", "tree"), ("SSE (yes/no levels)", "main"),
               ("SSE-MRL (finest level everywhere)", "mrl"))
BASE_METHODS = (("B3 separate (graded+contrastive)", "b3sc"), ("B4 CSN (graded+contrastive)", "csnsc"))


def note(step, status):
    line = f"| {time.strftime('%m-%d %H:%M:%S')} | {step} | {status} |"
    print(line, flush=True)
    prog = ROOT / "logs/PROGRESS.md"
    if prog.exists():
        with open(prog, "a") as f:
            f.write(line + "\n")


def _gpu(torch_only=False):
    """Import torch (+ the shared training / scoring code unless torch_only: `encode` runs in the small
    .venv-specter env that has torch + adapters but not the rest of the project's packages)."""
    global torch, nn, F, Scorer, ap, md_table, Projector, cos_matrix, supcon
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    if torch_only:
        return
    from .evaluate import Scorer, ap, md_table
    from .train_sse import Projector, cos_matrix, supcon


# ------------------------------------------------------------------ OpenAlex API
def api_key():
    k = os.environ.get("OPENALEX_API_KEY")
    env = ROOT / ".env"
    if not k and env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if line.startswith("OPENALEX_API_KEY") and "=" in line:
                k = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not k:
        raise SystemExit("OPENALEX_API_KEY missing: add a line OPENALEX_API_KEY=... to .env in the repo root")
    return k


def get(path, params, tries=15):
    import random
    import requests
    q = {**params, "api_key": api_key()}
    wait = lambda i: min(120, 2 ** i) * (0.5 + random.random())         # jitter: parallel workers don't retry in sync
    for i in range(tries):
        try:
            r = requests.get(f"{API}/{path}", params=q, timeout=60)
        except requests.RequestException as e:        # network hiccup: back off and retry
            print(f"  retry {i} ({type(e).__name__})", flush=True); time.sleep(wait(i)); continue
        if r.status_code == 200:
            return r.json()
        if r.status_code in (429, 500, 502, 503, 504):
            ra = r.headers.get("Retry-After", "")
            if r.status_code == 429 and r.headers.get("X-RateLimit-Remaining") == "0":
                raise RuntimeError("OpenAlex daily credit used up — rerun after the reset "
                                   f"({r.headers.get('X-RateLimit-Reset')} s); fetching resumes where it stopped")
            print(f"  retry {i} (HTTP {r.status_code})", flush=True)
            time.sleep(float(ra) if ra.replace(".", "", 1).isdigit() else wait(i)); continue
        raise RuntimeError(f"OpenAlex {path} HTTP {r.status_code}: {r.text[:300]}")   # never print the key
    raise RuntimeError(f"OpenAlex {path}: gave up after {tries} tries (filter={params.get('filter')})")


def short(oa_id):
    return oa_id.rsplit("/", 1)[-1] if oa_id else None


def abstract(inv):
    """OpenAlex stores abstracts as {word: [positions]}; rebuild the text."""
    if not inv:
        return ""
    return " ".join(w for _, w in sorted((i, w) for w, idx in inv.items() for i in idx))


def parse_work(w):
    pt = w.get("primary_topic") or {}
    if not pt.get("subfield"):
        return None
    auth = []
    for a in w.get("authorships") or []:
        aid = short((a.get("author") or {}).get("id"))
        inst = (a.get("institutions") or [{}])[0] if a.get("institutions") else {}
        if aid:
            auth.append([aid, short(inst.get("id")), inst.get("display_name"), inst.get("country_code"), inst.get("type")])
    return {"id": short(w["id"]), "title": (w.get("title") or "").strip(), "abstract": abstract(w.get("abstract_inverted_index")),
            "year": w.get("publication_year"), "cited_by": w.get("cited_by_count"),
            "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
            "domain": short(pt["domain"]["id"]), "field": short(pt["field"]["id"]),
            "subfield": short(pt["subfield"]["id"]), "topic": short(pt["id"]),
            "domain_name": pt["domain"]["display_name"], "field_name": pt["field"]["display_name"],
            "subfield_name": pt["subfield"]["display_name"], "topic_name": pt["display_name"],
            "topic_score": pt.get("score"), "authorships": json.dumps(auth)}


def read_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def fetch_papers(per_field=4000, seed=0):
    """A random sample of `per_field` papers from each of the 26 fields (one field file at a time, resumable)."""
    (D / "papers").mkdir(parents=True, exist_ok=True)
    fields = get("fields", {"per_page": 200})["results"]
    (D / "fields.json").write_text(json.dumps(fields, indent=1))
    print(f"{len(fields)} fields", flush=True)
    for f in fields:
        fid = short(f["id"])
        p = D / "papers" / f"field_{fid}.jsonl"
        if p.exists():
            continue
        flt = (f"primary_topic.field.id:{fid},has_abstract:true,type:article,language:en,"
               f"publication_year:2015-2024")
        rows = []
        for page in range(1, math.ceil(per_field / 200) + 1):          # sample + page: max 10k per sample
            r = get("works", {"filter": flt, "sample": per_field, "seed": seed, "per_page": 200, "page": page,
                              "select": WORK_SELECT})
            rows += r["results"]
            if len(r["results"]) < 200:
                break
        tmp = p.with_suffix(".tmp")
        tmp.write_text("".join(json.dumps(x) + "\n" for x in rows))
        tmp.rename(p)
        note("openalex-fetch", f"{f['display_name']}: {len(rows)} papers")
    (D / "papers" / "DONE").write_text(time.strftime("%Y-%m-%d %H:%M:%S"))


def fetch_meta():
    """Subfield + topic descriptions/keywords (for the semantic-relatedness answer key; ~25 requests)."""
    D.mkdir(parents=True, exist_ok=True)
    for kind in ("subfields", "topics"):
        rows, page = [], 1
        while True:
            r = get(kind, {"per_page": 200, "page": page})
            rows += r["results"]
            if len(rows) >= r["meta"]["count"] or not r["results"]:
                break
            page += 1
        (D / f"{kind}.json").write_text(json.dumps(rows))
        note("openalex-meta", f"{kind}: {len(rows)}")


def _rescale(Rm):
    """Relatedness -> credit: 1 on the diagonal, 0 for anything at or below the row's median, linear in between."""
    G = np.zeros_like(Rm)
    for i in range(len(Rm)):
        off = np.delete(Rm[i], i)
        med = np.median(off)
        G[i] = np.clip((Rm[i] - med) / max(1e-6, Rm[i, i] - med), 0, 1)
        G[i, i] = 1
    return G


def related(text_model="BAAI/bge-large-en-v1.5"):
    """Semantic answer key between SUBFIELDS, from two independent sources (indexed like the subfield codes):
       text   : cosine of bge-large embeddings of each subfield's name + description + its topics' names/keywords
                (a different model than the SPECTER2 encoder, so the answer key does not favour our encoder)
       coact  : how often the same authors publish in both subfields (cosine of the author-share columns)
       Each is rescaled per row: same subfield = 1, below-median relatedness = 0."""
    from sentence_transformers import SentenceTransformer
    df, aw = pd.read_parquet(CACHE / "papers.parquet"), pd.read_parquet(CACHE / "aw.parquet")
    codes, acodes = level_codes(df, aw)
    ids = pd.Index(pd.concat([df.subfield, aw.subfield]).unique())          # same order as level_codes
    subs = {short(x["id"]): x for x in json.loads((D / "subfields.json").read_text())}
    by_sub = {}
    for t in json.loads((D / "topics.json").read_text()):
        by_sub.setdefault(short(t["subfield"]["id"]), []).append(t)
    texts = []
    for sid in ids:
        s, ts = subs.get(sid, {}), by_sub.get(sid, [])
        kw = list(dict.fromkeys(k["display_name"] for t in ts for k in (t.get("keywords") or [])))[:40]
        texts.append(f"{s.get('display_name', sid)}. {s.get('description') or ''} "
                     f"Topics: {'; '.join(t['display_name'] for t in ts)}. Keywords: {', '.join(kw)}.")
    enc = SentenceTransformer(text_model, device="cuda")
    E = enc.encode(texts, normalize_embeddings=True, batch_size=32)
    R_text = (E @ E.T).astype(np.float32)
    L = pd.read_parquet(CACHE / "aw_links.parquet")
    n_a = int(L.author_idx.max() + 1)
    W = sp.csr_matrix((np.ones(len(L)), (L.author_idx, L.work_idx)), shape=(n_a, len(aw)))
    P = _rownorm(W @ _onehot(acodes["subfield"], len(ids))).toarray()           # author x subfield shares
    C = _normed(P.T)                                                             # subfield x author
    R_co = (C @ C.T).astype(np.float32)
    G_text, G_co = _rescale(R_text), _rescale(R_co)
    np.savez(CACHE / "related.npz", text=G_text, coact=G_co, raw_text=R_text, raw_coact=R_co, ids=np.array(ids))
    # human check: closest and far subfields for a few examples
    names = [subs.get(i, {}).get("display_name", i) for i in ids]
    md = ["# Subfield relatedness — sanity check\n", "credit: 1 = same subfield, 0 = at/below median relatedness\n"]
    for nm in ("Artificial Intelligence", "Computer Vision and Pattern Recognition", "Oncology",
               "Statistical and Nonlinear Physics", "Economics and Econometrics", "Ecology"):
        if nm not in names:
            continue
        i = names.index(nm)
        for lab, G in (("text", G_text), ("co-activity", G_co)):
            o = np.argsort(-G[i])
            md.append(f"**{nm}** ({lab}) — closest: " + "; ".join(f"{names[j]} {G[i, j]:.2f}" for j in o[1:6]) +
                      f" · e.g. far: {names[o[-1]]} {G[i, o[-1]]:.2f}\n")
    a, b = G_text[np.triu_indices(len(ids), 1)], G_co[np.triu_indices(len(ids), 1)]
    from scipy.stats import spearmanr
    md.append(f"\nAgreement of the two answer keys (Spearman over subfield pairs): {spearmanr(a, b).correlation:.2f}\n")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "related_examples.md").write_text("\n".join(md))
    print("\n".join(md))


def load_raw_papers():
    rows = [parse_work(w) for p in sorted((D / "papers").glob("field_*.jsonl")) for w in read_jsonl(p)]
    df = pd.DataFrame([r for r in rows if r]).drop_duplicates("id")
    ok = (df.title.str.len() > 0) & (df.abstract.str.split().str.len() >= MIN_WORDS)
    return df[ok].reset_index(drop=True)


def fetch_authors(n_inst=300, per_inst=20, min_auth=15, per_author=30, seed=0, workers=3):
    """Pick institutions + authors from the paper sample, then fetch each author's other papers (resumable)."""
    sel_path, out = D / "authors_selected.json", D / "author_works.jsonl"
    if sel_path.exists():
        sel = json.loads(sel_path.read_text())
    else:
        df = load_raw_papers()
        a = pd.DataFrame([x for s in df.authorships for x in json.loads(s)],
                         columns=["author", "inst", "inst_name", "country", "inst_type"]).dropna(subset=["inst"])
        a = a.drop_duplicates(["author", "inst"])
        n = a.groupby("inst").author.nunique()
        rng = np.random.default_rng(seed)
        insts = rng.choice(n[n >= min_auth].index.values, min(n_inst, int((n >= min_auth).sum())), replace=False)
        info = a.drop_duplicates("inst").set_index("inst")
        sel = {"institutions": {i: {k: info.at[i, k] for k in ("inst_name", "country", "inst_type")} for i in insts},
               "authors": {}}
        # many OpenAlex author records are fragments with 1-2 papers: keep candidates with >= 10 works
        cand = a[a.inst.isin(insts)].author.unique()
        wc = {}
        for k in range(0, len(cand), 100):
            r = get("authors", {"filter": "openalex:" + "|".join(cand[k:k + 100]), "per_page": 200,
                                "select": "id,works_count"})
            wc.update({short(x["id"]): x["works_count"] for x in r["results"]})
        print(f"{len(cand)} candidate authors, {sum(v >= 10 for v in wc.values())} with >= 10 works", flush=True)
        for i in insts:
            members = np.array([m for m in a[a.inst == i].author.unique() if wc.get(m, 0) >= 10])
            for au in rng.choice(members, min(per_inst, len(members)), replace=False):
                sel["authors"].setdefault(au, i)                       # an author keeps their first institution
        sel_path.write_text(json.dumps(sel, indent=1))
    print(f"{len(sel['institutions'])} institutions, {len(sel['authors'])} authors", flush=True)

    done = {json.loads(l)["author"] for l in open(out)} if out.exists() else set()
    todo = [a for a in sel["authors"] if a not in done]
    lock, n_done = threading.Lock(), [len(done)]
    sel_fields = WORK_SELECT.replace(",authorships", "")

    def one(au):
        r = get("works", {"filter": f"author.id:{au},has_abstract:true,type:article,language:en",
                          "per_page": per_author, "sort": "publication_year:desc", "select": sel_fields})
        line = json.dumps({"author": au, "works": r["results"]}) + "\n"
        with lock:
            with open(out, "a") as f:
                f.write(line)
            n_done[0] += 1
            if n_done[0] % 500 == 0:
                note("openalex-authors", f"{n_done[0]}/{len(sel['authors'])} authors")
    with ThreadPoolExecutor(workers) as pool:
        list(pool.map(one, todo))
    (D / "AUTHORS_DONE").write_text(time.strftime("%Y-%m-%d %H:%M:%S"))
    note("openalex-authors", f"done {n_done[0]}/{len(sel['authors'])} authors")


# ------------------------------------------------------------------ tables + text vectors
def encode(texts, encoder, bs=128):
    if encoder == "bge":
        from sentence_transformers import SentenceTransformer
        enc = SentenceTransformer("BAAI/bge-base-en-v1.5", device="cuda")
        return enc.encode(texts, batch_size=bs, normalize_embeddings=True, show_progress_bar=True).astype(np.float16)
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained("allenai/specter2_base")
    if encoder == "specter2":
        try:
            from adapters import AutoAdapterModel
        except ImportError:
            raise SystemExit("SPECTER2 proximity adapter needs `pip install adapters` "
                             "(or run prep with --encoder specter2_base)")
        model = AutoAdapterModel.from_pretrained("allenai/specter2_base")
        model.load_adapter("allenai/specter2", source="hf", load_as="proximity", set_active=True)
        model.set_active_adapters("proximity")
        print("active adapters:", model.active_adapters, flush=True)       # must show "proximity"
    else:
        from transformers import AutoModel
        model = AutoModel.from_pretrained("allenai/specter2_base")
    model = model.cuda().eval().half()
    X = np.zeros((len(texts), 768), np.float16)
    order = np.argsort([len(t) for t in texts])                       # similar lengths per batch = less padding
    for i in range(0, len(texts), bs):
        idx = order[i:i + bs]
        b = tok([texts[j] for j in idx], padding=True, truncation=True, max_length=512,
                return_tensors="pt", return_token_type_ids=False).to("cuda")
        with torch.no_grad():
            h = model(**b).last_hidden_state[:, 0]                   # [CLS], as on the SPECTER2 model card
        X[idx] = F.normalize(h.float(), dim=-1).cpu().numpy().astype(np.float16)
        if (i // bs) % 100 == 0:
            print(f"  encoded {i + len(idx)}/{len(texts)}", flush=True)
    return X


def text_of(df, encoder):
    sep = " [SEP] " if encoder.startswith("specter2") else ". "      # SPECTER2: title [SEP] abstract
    return (df.title + sep + df.abstract).tolist()


def build(seed=0):
    """Tables only (no GPU): papers / authors' papers / author->paper links / authors / institutions."""
    CACHE.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    df = load_raw_papers()
    if len(df) > N_PAPERS:
        df = df.iloc[np.sort(rng.choice(len(df), N_PAPERS, replace=False))].reset_index(drop=True)
    topics = df.topic.unique()
    unseen = set(rng.choice(topics, int(0.2 * len(topics)), replace=False))
    split = np.where(df.topic.isin(unseen), "unseen", "train").astype(object)
    split[(split == "train") & (rng.random(len(df)) < 0.3)] = "seen_test"
    df["split"] = split
    df.to_parquet(CACHE / "papers.parquet")
    print("papers", len(df), df.split.value_counts().to_dict(), {l: df[l].nunique() for l in LEVELS}, flush=True)

    # authors' other papers -> works table, author->work links, authors, institutions
    sel = json.loads((D / "authors_selected.json").read_text())
    in_sample = set(df.id)
    works, links = {}, []
    for rec in read_jsonl(D / "author_works.jsonl"):
        for w in rec["works"]:
            r = parse_work(w)
            if r and r["id"] not in in_sample and r["title"] and len(r["abstract"].split()) >= MIN_WORDS:
                works.setdefault(r["id"], r); links.append((rec["author"], r["id"]))
    links = pd.DataFrame(links, columns=["author", "work"]).drop_duplicates()
    n_w = links.groupby("author").work.size()
    keep = n_w[n_w >= 5].index
    links = links[links.author.isin(keep)]
    au = pd.DataFrame({"author": keep, "inst": [sel["authors"][a] for a in keep], "n_works": n_w[keep].values})
    n_i = au.groupby("inst").size()
    au = au[au.inst.isin(n_i[n_i >= 3].index)].reset_index(drop=True)        # institutions need >= 3 authors
    links = links[links.author.isin(au.author)]
    aw = pd.DataFrame([works[w] for w in links.work.unique()]).drop(columns=["authorships"])
    inst = pd.DataFrame([{"inst": i, **sel["institutions"][i]} for i in au.inst.unique()])
    a_idx = pd.Series(np.arange(len(au)), au.author.values)
    w_idx = pd.Series(np.arange(len(aw)), aw.id.values)
    i_idx = pd.Series(np.arange(len(inst)), inst.inst.values)
    au["inst_idx"] = i_idx[au.inst].values
    pd.DataFrame({"author_idx": a_idx[links.author].values, "work_idx": w_idx[links.work].values}).to_parquet(CACHE / "aw_links.parquet")
    aw.to_parquet(CACHE / "aw.parquet"); au.to_parquet(CACHE / "authors.parquet"); inst.to_parquet(CACHE / "institutions.parquet")
    print(f"authors {len(au)}, their papers {len(aw)}, links {len(links)}, institutions {len(inst)} "
          f"({inst.inst_type.value_counts().to_dict()})", flush=True)


def encode_all(encoder="specter2"):
    """Text vectors for the papers and the authors' papers (GPU)."""
    df, aw = pd.read_parquet(CACHE / "papers.parquet"), pd.read_parquet(CACHE / "aw.parquet")
    note("openalex-encode", f"started ({encoder}, {len(df) + len(aw)} texts)")
    np.save(CACHE / "text_emb.npy", encode(text_of(df, encoder), encoder))
    np.save(CACHE / "aw_emb.npy", encode(text_of(aw, encoder), encoder))
    (CACHE / "encoder.json").write_text(json.dumps({"encoder": encoder}))
    note("openalex-encode", "done")


def level_codes(*dfs):
    """Integer codes per level, consistent across tables (papers first, so paper codes never change)."""
    cats = {l: pd.Index(pd.concat([d[l] for d in dfs]).unique()) for l in CODE_LEVELS}
    return [{l: cats[l].get_indexer(d[l]) for l in CODE_LEVELS} for d in dfs]


def load(authors=False):
    df = pd.read_parquet(CACHE / "papers.parquet")
    X = np.load(CACHE / "text_emb.npy").astype(np.float32)
    if not authors:
        return df, X, level_codes(df)[0]
    aw = pd.read_parquet(CACHE / "aw.parquet")
    XA = np.load(CACHE / "aw_emb.npy").astype(np.float32)
    codes, acodes = level_codes(df, aw)
    rel = {"links": pd.read_parquet(CACHE / "aw_links.parquet"), "authors": pd.read_parquet(CACHE / "authors.parquet"),
           "inst": pd.read_parquet(CACHE / "institutions.parquet")}
    return df, X, codes, aw, XA, acodes, rel


def tree_targets(C):
    """Graded tree similarity per level: at level i, sharing level j < i gives (j+1)/(i+1)."""
    same = {l: (C[l][:, None] == C[l][None, :]).float() for l in LEVELS}
    T = {}
    for i, l in enumerate(LEVELS):
        t = same[l]
        for j in range(i):
            t = torch.maximum(t, (j + 1) / (i + 1) * same[LEVELS[j]])
        T[l] = t
    return T


# ------------------------------------------------------------------ training
def train(method, seed, epochs=30, bs=2048, lr=1e-3):
    torch.manual_seed(seed)
    df, X, codes = load()
    tr = torch.tensor(np.flatnonzero(df.split.values == "train"))
    Xt = torch.tensor(X).cuda()
    XA = torch.tensor(np.load(CACHE / "aw_emb.npy").astype(np.float32)).cuda() if (CACHE / "aw_emb.npy").exists() else None
    C = {l: torch.tensor(codes[l]).long().cuda() for l in LEVELS}

    def batches():
        for _ in range(epochs):
            perm = tr[torch.randperm(len(tr))]
            for b in range(len(tr) // bs):
                yield perm[b * bs:(b + 1) * bs].cuda()

    graded = method in ("tree", "treesc", "b3", "csn", "b3sc", "csnsc")          # graded tree-similarity loss
    contrast = method in ("main", "mrl", "treesc", "b3sc", "csnsc")              # yes/no contrastive loss

    def level_loss(z, lvl, idx):
        loss = 0
        if graded:
            loss = loss + 10 * F.mse_loss(cos_matrix(z), tree_targets({l: C[l][idx] for l in LEVELS})[lvl])
        if contrast:
            loss = loss + supcon(z, C[LEVELS[-1] if method == "mrl" else lvl][idx])
        return loss

    def both(fn):          # apply a trained map to the papers and to the authors' papers
        with torch.no_grad():
            return fn(Xt).cpu().numpy(), (fn(XA).cpu().numpy() if XA is not None else None)

    views = {}
    if method in ("tree", "main", "mrl", "treesc"):
        net = Projector(768, 768).cuda()
        opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
        for idx in batches():
            x = Xt[idx]; e = net(x)
            loss = F.mse_loss(cos_matrix(e), x @ x.T)
            for lvl in LEVELS:
                loss = loss + 0.5 * level_loss(e[:, :PREFIX[lvl]], lvl, idx)
            opt.zero_grad(); loss.backward(); opt.step()
        E, EA = both(net)
        views["full"] = (E, EA)
        for l in LEVELS:
            views[l] = (E[:, :PREFIX[l]], None if EA is None else EA[:, :PREFIX[l]])
    elif method in ("b3", "b3sc"):
        views["full"] = (X, None if XA is None else XA.cpu().numpy())
        for lvl in LEVELS:
            net = Projector(768, PREFIX[lvl], hidden=1024).cuda()
            opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
            for idx in batches():
                loss = level_loss(net(Xt[idx]), lvl, idx)
                opt.zero_grad(); loss.backward(); opt.step()
            views[lvl] = both(net)
    elif method in ("csn", "csnsc"):
        net = Projector(768, 768).cuda()
        masks = nn.Parameter(torch.randn(len(LEVELS), 768, device="cuda") * 0.7 + 0.9)
        opt = torch.optim.AdamW(list(net.parameters()) + [masks], lr=lr, weight_decay=1e-4)
        for idx in batches():
            x = Xt[idx]; e = net(x); m = F.relu(masks)
            loss = F.mse_loss(cos_matrix(e), x @ x.T) + 5e-4 * m.abs().sum()
            for i, lvl in enumerate(LEVELS):
                loss = loss + 0.5 * level_loss(e * m[i], lvl, idx)
            opt.zero_grad(); loss.backward(); opt.step()
        m = F.relu(masks).detach()
        views["full"] = both(net)
        for i, l in enumerate(LEVELS):
            views[l] = both(lambda z, i=i: net(z) * m[i])
        print("CSN active dims per mask:", {l: int((m[i] > 1e-3).sum()) for i, l in enumerate(LEVELS)}, flush=True)
    else:
        raise ValueError(method)
    out = {k: v[0] for k, v in views.items()}
    out.update({f"aw_{k}": v[1] for k, v in views.items() if v[1] is not None})
    np.savez(CACHE / f"{method}_s{seed}.npz", **out)
    print("saved", method, seed, "final loss", float(loss), flush=True)


# ------------------------------------------------------------------ evaluation
def b1_labels(X, df, codes, seed, extra=None):
    """Classifiers per level on train papers; vocabulary = labels seen in training. Predicts X (and `extra`)."""
    torch.manual_seed(seed)
    tr = np.flatnonzero(df.split.values == "train")
    Xt = torch.tensor(X).cuda()
    pred, pred_extra = {}, {}
    for lvl in LEVELS:
        vocab = np.unique(codes[lvl][tr]); remap = {v: i for i, v in enumerate(vocab)}
        y = torch.tensor([remap[v] for v in codes[lvl][tr]]).cuda()
        lin = nn.Linear(768, len(vocab)).cuda()
        opt = torch.optim.AdamW(lin.parameters(), lr=1e-3, weight_decay=1e-4)
        idx = torch.tensor(tr).cuda()
        for _ in range(30):
            perm = torch.randperm(len(idx), device="cuda")
            for i in range(0, len(perm), 4096):
                b = perm[i:i + 4096]
                loss = F.cross_entropy(lin(Xt[idx[b]]), y[b])
                opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            pred[lvl] = vocab[lin(Xt).argmax(1).cpu().numpy()]
            if extra is not None:
                pred_extra[lvl] = vocab[lin(torch.tensor(extra).cuda()).argmax(1).cpu().numpy()]
    return (pred, pred_extra) if extra is not None else pred


def method_files(seed, tags):
    return {lab: np.load(CACHE / f"{tag}_s{seed}.npz") for lab, tag in tags if (CACHE / f"{tag}_s{seed}.npz").exists()}


def evaluate(seed, nq=400):
    rng = np.random.default_rng(0)
    df, X, codes = load()
    res, md = {}, [f"# OpenAlex results (seed {seed})\n"]
    embs = {lab: Z["full"] for lab, Z in method_files(seed, SSE_METHODS).items()}
    tr = df.split.values == "train"
    mu = X[tr].mean(0); _, _, Vt = np.linalg.svd(X[tr][::4] - mu, full_matrices=False)
    embs["Encoder-PCA"] = (X - mu) @ Vt[:TAX_DIM].T

    # E2: prefix length sweep
    note("openalex-E2", "started")
    rows = []
    for split in ("seen_test", "unseen"):
        db = np.flatnonzero(df.split.values == split)
        qs = rng.choice(db, nq, replace=False)
        for m, E in embs.items():
            for L in (8, 16, 32, 64, 128):
                sc = Scorer((E[:, :L], "cos"))
                for lvl in LEVELS:
                    aps = [ap(sc(q, db[db != q]), codes[lvl][db[db != q]] == codes[lvl][q]) for q in qs]
                    rows.append({"split": split, "method": m, "prefix_len": L, "level": lvl, "mAP": float(np.nanmean(aps))})
    res["E2"] = rows
    piv = pd.DataFrame(rows)
    md.append("### E2 — topic prefix length vs level (mAP)\n")
    for split in ("seen_test", "unseen"):
        t = piv[piv.split == split].pivot_table(index=["method", "level"], columns="prefix_len", values="mAP").round(3)
        md.append(f"**{split}**\n\n" + t.to_markdown() + "\n")
    note("openalex-E2", "done")

    # E2b: does each level's view keep its own and coarser levels? (pair AUC)
    note("openalex-E2b", "started")
    from sklearn.metrics import roc_auc_score
    db = np.flatnonzero(df.split.values != "train")
    a, b = rng.choice(db, 400_000), rng.choice(db, 400_000); k = a != b; a, b = a[k], b[k]
    depth = sum((codes[l][a] == codes[l][b]).astype(int) for l in LEVELS)
    auc = lambda s: {f"same-{l} AUC": float(roc_auc_score(depth >= i + 1, s)) for i, l in enumerate(LEVELS)}
    rows = []
    for m, Z in method_files(seed, SSE_METHODS[:3] + BASE_METHODS).items():
        for lvl in LEVELS:
            rows.append({"method": m, "view": lvl, **auc(Scorer((Z[lvl], "cos")).pairs(a, b))})
    pred = b1_labels(X, df, codes, seed)
    s = sum((pred[l][a] == pred[l][b]).astype(float) for l in LEVELS) + 1e-3 * (X[a] * X[b]).sum(1)
    rows.append({"method": "B1 labels", "view": "all levels", **auc(s)})
    rows.append({"method": "B6 plain encoder", "view": "full", **auc((X[a] * X[b]).sum(1))})
    res["E2b"] = rows
    md.append(md_table(rows, ["method", "view", *[f"same-{l} AUC" for l in LEVELS]],
                       "E2b — does each level's view keep its own and coarser levels? (pair AUC)"))
    note("openalex-E2b", "done")

    # E2s: paper -> papers at each level's own view, strict (same label) and soft (tree credit)
    note("openalex-E2s", "started")
    views = {lab: {l: Z[l] for l in LEVELS} for lab, Z in method_files(seed, SSE_METHODS + BASE_METHODS).items()}
    views["Encoder-PCA"] = {l: embs["Encoder-PCA"][:, :PREFIX[l]] for l in LEVELS}
    views["B6 plain encoder"] = {l: X for l in LEVELS}
    rows = []
    REL = {k: np.load(CACHE / "related.npz")[k] for k in ("text", "coact")} if (CACHE / "related.npz").exists() else {}
    for split in ("seen_test", "unseen"):
        db = np.flatnonzero(df.split.values == split)
        qs = rng.choice(db, nq, replace=False)
        for li, l in enumerate(LEVELS):
            def credit(q, d):
                t = np.zeros(len(d), np.float32)
                for j in range(li + 1):
                    t = np.maximum(t, (j + 1) / (li + 1) * (codes[LEVELS[j]][d] == codes[LEVELS[j]][q]))
                return t
            sc = {m: Scorer((v[l], "cos")) for m, v in views.items()}
            Xs = Scorer((X, "cos"))
            sc["B1 labels"] = lambda q, d: (sum((pred[LEVELS[j]][d] == pred[LEVELS[j]][q]).astype(float) for j in range(li + 1))
                                            + 1e-3 * Xs(q, d))
            sem = list(REL) and l == "subfield"           # semantic credit only between subfields
            keys = ["P@10", "tree_credit@10"] + (["credit_text@10", "credit_coact@10"] if sem else [])
            acc = {m: {k: [] for k in keys} for m in [*sc, "Random"]}
            for q in qs:
                d = db[db != q]
                g = {"P@10": (codes[l][d] == codes[l][q]).astype(float), "tree_credit@10": credit(q, d)}
                if sem:
                    g["credit_text@10"] = REL["text"][codes[l][q], codes[l][d]]
                    g["credit_coact@10"] = REL["coact"][codes[l][q], codes[l][d]]
                for m, f in sc.items():
                    top = np.argsort(-f(q, d))[:10]
                    for k in keys:
                        acc[m][k].append(g[k][top].mean())
                for k in keys:
                    acc["Random"][k].append(g[k].mean())
            rows += [{"split": split, "level": l, "method": m, **{k: float(np.mean(v)) for k, v in a.items()}}
                     for m, a in acc.items()]
    res["E2s"] = rows
    md.append(md_table([r for r in rows if r["level"] != "subfield"], ["split", "level", "method", "P@10", "tree_credit@10"],
                       "E2s (coarse levels)"))
    md.append(md_table([r for r in rows if r["level"] == "subfield"], ["split", "level", "method", "P@10", "tree_credit@10",
                        *(["credit_text@10", "credit_coact@10"] if REL else [])],
                       "E2s — paper -> 10 nearest papers at the level's own view: exact label (P@10) and tree credit "
                       "(1 same label, partial credit for sharing a coarser level)"))
    note("openalex-E2s", "done")

    # E3: general search — same-topic mAP and overlap of top-10 with the plain encoder
    note("openalex-E3", "started")
    qs = rng.choice(db, 400, replace=False)
    base = Scorer((X, "cos")); rows = []
    for m in [k for k in embs if k.startswith("SSE")]:
        full = Scorer((embs[m], "cos")); ov, a1, a2 = [], [], []
        for q in qs:
            d = db[db != q]; s1, s2 = base(q, d), full(q, d); rel = codes["topic"][d] == codes["topic"][q]
            ov.append(len(set(d[np.argsort(-s1)[:10]]) & set(d[np.argsort(-s2)[:10]])) / 10)
            a1.append(ap(s1, rel)); a2.append(ap(s2, rel))
        rows.append({"method": m, "overlap@10_with_encoder": float(np.mean(ov)),
                     "topic_mAP_encoder": float(np.nanmean(a1)), "topic_mAP_SSE": float(np.nanmean(a2))})
    res["E3"] = rows
    if rows:
        md.append(md_table(rows, list(rows[0]), "E3 — general search preserved"))
    note("openalex-E3", "done")

    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(res, indent=1))
    (out / "results.md").write_text("\n".join(md))
    print("\n".join(md))


# ------------------------------------------------------------------ E8: joins + institutions
def _normed(M):
    M = np.asarray(M, np.float32)
    return M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-8)


def _rownorm(S):
    s = np.asarray(S.sum(1)).ravel()
    return sp.diags(1 / np.maximum(s, 1e-12)) @ S


def _onehot(c, n):
    return sp.csr_matrix((np.ones(len(c)), (np.arange(len(c)), c)), shape=(len(c), n))


def ndcg(S, G, k=10):
    top = np.argsort(-S, axis=1)[:, :k]
    disc = 1 / np.log2(np.arange(2, k + 2))
    dcg = (np.take_along_axis(G, top, 1) * disc).sum(1)
    ideal = (-np.sort(-G, axis=1)[:, :k] * disc).sum(1)
    ok = ideal > 0
    return float(np.mean(dcg[ok] / ideal[ok]))


def best_tau(S, rel):
    """Join threshold that maximises F1 (chosen on TRAIN papers, then applied to test papers)."""
    taus = np.unique(np.quantile(S, np.linspace(0.5, 0.999, 60)))
    f1 = [2 * (rel & (S >= t)).sum() / max(1, (S >= t).sum() + rel.sum()) for t in taus]
    return float(taus[int(np.argmax(f1))])


def join(seed, nq=1000):
    """E8a  Papers VecJOIN Authors ON topic prefix (per level): does sim(paper, author) follow how much of the
            author's work is in the paper's area?  Graded truth g = share of the author's papers with the
            paper's label at that level; a join pair is "correct" when g >= 0.5.
            Binary truth (P@10, join F1): the paper's label is the author's MAIN area (most common label among
            their papers) at that level.  "Random" = P@10 of picking authors at random (the base rate).
       E8b  Institution similarity per level: truth = cosine of the institutions' label profiles."""
    from scipy.stats import spearmanr
    rng = np.random.default_rng(0)
    df, X, codes, aw, XA, acodes, rel = load(authors=True)
    L, A, I = rel["links"], rel["authors"], rel["inst"]
    W = sp.csr_matrix((np.ones(len(L)), (L.author_idx, L.work_idx)), shape=(len(A), len(aw)))       # author x work
    WI = sp.csr_matrix((np.ones(len(A)), (A.inst_idx, np.arange(len(A)))), shape=(len(I), len(A)))  # inst x author
    n_cat = {l: int(max(codes[l].max(), acodes[l].max()) + 1) for l in LEVELS}
    P = {l: _rownorm(W @ _onehot(acodes[l], n_cat[l])).tocsc() for l in LEVELS}        # author label shares
    TI = {l: _normed((WI @ P[l]).toarray()) for l in LEVELS}                          # institution profiles

    # views: per method, per level -> (paper matrix, author matrix, institution matrix)
    def lift(Mp, Ma):
        Av = _normed(W @ _normed(Ma)); return _normed(Mp), Av, _normed(WI @ Av)
    views = {"B6 plain encoder": {l: lift(X, XA) for l in LEVELS}}
    for lab, Z in method_files(seed, SSE_METHODS + BASE_METHODS).items():
        if f"aw_{LEVELS[0]}" in Z:
            views[lab] = {l: lift(Z[l], Z[f"aw_{l}"]) for l in LEVELS}
    pred, pred_a = b1_labels(X, df, codes, seed, extra=XA)

    q_by = {s: rng.choice(np.flatnonzero(df.split.values == s), nq, replace=False) for s in ("train", "seen_test", "unseen")}
    rows8a, rows8b = [], []
    mains = {l: np.asarray(P[l].tocsr().argmax(1)).ravel() for l in LEVELS}            # author's main area per level
    REL = {k: np.load(CACHE / "related.npz")[k] for k in ("text", "coact")} if (CACHE / "related.npz").exists() else {}
    Psub = P["subfield"].toarray() if REL else None                                 # author x subfield shares
    for li, l in enumerate(LEVELS):
        G = {s: P[l][:, codes[l][q]].toarray().T for s, q in q_by.items()}           # (queries x authors)
        main = mains[l]
        R = {s: codes[l][q][:, None] == main[None, :] for s, q in q_by.items()}
        # soft truths: "active" = >= 20% of the author's papers are in the paper's area;
        # tree credit = 1 same main area, else (j+1)/(li+1) for the finest shared coarser level j (as in training)
        ACT = {s: G[s] >= 0.2 for s in q_by}
        TC = {}
        for s, q in q_by.items():
            t = np.zeros((len(q), len(A)), np.float32)
            for j in range(li + 1):
                t = np.maximum(t, (j + 1) / (li + 1) * (codes[LEVELS[j]][q][:, None] == mains[LEVELS[j]][None, :]))
            TC[s] = t
        # semantic credit (subfield level): relatedness of the paper's subfield to everything the author publishes in
        SEM = {k: {s: REL[k][codes[l][q]][:, :Psub.shape[1]] @ Psub.T for s, q in q_by.items()}
               for k in ("text", "coact")} if (REL and l == "subfield") else {}
        Pb = _rownorm(W @ _onehot(pred_a[l], n_cat[l])).tocsc()                        # B1: predicted shares
        Tb = _normed((WI @ Pb).toarray())
        sims = {m: (lambda q, v=v: v[l][0][q] @ v[l][1].T, v[l][2]) for m, v in views.items()}
        sims["B1 labels"] = (lambda q: Pb[:, pred[l][q]].toarray().T, Tb)
        for m, (S_of, Iv) in sims.items():
            tau = best_tau(S_of(q_by["train"]), R["train"])
            for s in ("seen_test", "unseen"):
                S, g, relv = S_of(q_by[s]), G[s], R[s]
                k = rng.choice(S.size, min(200_000, S.size), replace=False)
                hit = S >= tau
                top = np.argsort(-S, axis=1)[:, :10]
                rows8a.append({"method": m, "level": l, "query_split": s,
                               "P@10": float(np.take_along_axis(relv, top, 1).mean()),
                               "P@10_active": float(np.take_along_axis(ACT[s], top, 1).mean()),
                               "tree_credit@10": float(np.take_along_axis(TC[s], top, 1).mean()),
                               **{f"credit_{k}@10": float(np.take_along_axis(v[s], top, 1).mean()) for k, v in SEM.items()},
                               "Spearman": float(spearmanr(S.ravel()[k], g.ravel()[k]).correlation),
                               "NDCG@10": ndcg(S, g), "join_F1": float(2 * (hit & relv).sum() / max(1, hit.sum() + relv.sum())),
                               "authors_per_paper": float(hit.sum(1).mean()), "tau": tau})
            Si, Gi = Iv @ Iv.T, TI[l] @ TI[l].T
            iu = np.triu_indices(len(Gi), 1)
            np.fill_diagonal(Si, -np.inf); np.fill_diagonal(Gi, 0)
            rows8b.append({"method": m, "level": l, "Spearman": float(spearmanr(Si[iu], Gi[iu]).correlation),
                           "NDCG@10": ndcg(Si, Gi)})
        for s in ("seen_test", "unseen"):
            rows8a.append({"method": "Random (base rate)", "level": l, "query_split": s, "P@10": float(R[s].mean()),
                           "P@10_active": float(ACT[s].mean()), "tree_credit@10": float(TC[s].mean()),
                           **{f"credit_{k}@10": float(v[s].mean()) for k, v in SEM.items()},
                           "Spearman": 0.0, "NDCG@10": float("nan"), "join_F1": float(2 * R[s].mean() / (1 + R[s].mean())),
                           "authors_per_paper": float(len(A)), "tau": float("nan")})
        note("openalex-E8", f"level {l} done")
    md = [f"# OpenAlex E8 — joins and institutions (seed {seed})\n",
          f"{len(A)} authors ({len(aw)} of their papers, none in the 100k sample), {len(I)} institutions.\n",
          md_table(rows8a, ["method", "level", "query_split", "P@10", "P@10_active", "tree_credit@10", "Spearman", "NDCG@10", "join_F1", "authors_per_paper", "tau"],
                   "E8a — Papers VecJOIN Authors (P@10 / F1: paper's area = author's main area; Spearman / NDCG: share of the author's papers in it)"),
          md_table(rows8b, ["method", "level", "Spearman", "NDCG@10"],
                   "E8b — institution vs institution similarity (truth: cosine of research profiles)")]
    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "e8.json").write_text(json.dumps({"E8a": rows8a, "E8b": rows8b}, indent=1))
    (out / "e8.md").write_text("\n".join(md))
    print("\n".join(md))


# ------------------------------------------------------------------ E6: roll-up / drill-down
def e6(seed, domain="Physical Sciences", n_db=8000, n_tune=4000):
    """Roll-up / drill-down inside one domain (field > subfield > topic), both grouping rules.
    kappa tuned on TRAINING papers of that domain with ARI."""
    from .e6_grouping import POLICY, KAPPAS, normed, describe
    from sklearn.metrics import adjusted_rand_score as ARI
    rng = np.random.default_rng(0)
    df, X, codes = load()
    lv = LEVELS[1:]
    in_d = df.domain_name.values == domain
    assert in_d.any(), f"unknown domain {domain!r}: {df.domain_name.unique().tolist()}"
    db = np.flatnonzero(in_d & (df.split.values != "train")); db = np.sort(rng.choice(db, min(n_db, len(db)), replace=False))
    tr_d = np.flatnonzero(in_d & (df.split.values == "train"))
    tune = rng.choice(tr_d, min(n_tune, len(tr_d)), replace=False)
    methods = {"B6 plain encoder": {l: X for l in lv}}
    for lab, Z in method_files(seed, SSE_METHODS[:3] + BASE_METHODS).items():
        methods[lab] = {l: Z[l] for l in lv}
    methods = {m: {l: normed(v[l]) for l in lv} for m, v in methods.items()}
    rows = []
    for policy in ("connected", "center"):
        for m, vs in methods.items():
            kap = {l: max((ARI(codes[l][tune], POLICY[policy](vs[l][tune], k)), k) for k in KAPPAS)[1] for l in lv}
            labels = np.zeros(len(db), int)
            for l in lv:
                new = np.zeros(len(db), int); nxt = 0
                for g in np.unique(labels):
                    idx = np.flatnonzero(labels == g)
                    sub = POLICY[policy](vs[l][db[idx]], kap[l]); new[idx] = sub + nxt; nxt += sub.max() + 1
                labels = new
                rows.append({"policy": policy, "method": m, "level": l, "kappa": float(kap[l]),
                             "n_true": int(len(np.unique(codes[l][db]))), **describe(codes[l][db], labels)})
            note("openalex-E6", f"{domain} {policy} {m} done")
    tag = domain.split()[0].lower()
    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / f"e6_{tag}.json").write_text(json.dumps(rows, indent=1))
    (out / f"e6_{tag}.md").write_text(md_table(rows, ["policy", "method", "level", "kappa", "n_groups", "n_main_groups",
                                                      "n_true", "coverage", "NMI", "NMI_main", "ARI"],
                                               f"E6 — roll-up / drill-down within {domain} ({len(db)} test papers; kappa tuned on training papers by ARI)"))


# ------------------------------------------------------------------ 3-seed summary (pandas only)
def summarize():
    """results/openalex/seed*/ -> results/openalex/summary_tables.md (mean over seeds, ± = half the max-min spread)."""
    seeds = sorted(OUT.glob("seed*"))

    def agg(rows, keys, metrics):
        d = pd.DataFrame(rows)
        metrics = [c for c in metrics if c in d]                 # optional columns (e.g. semantic credit)
        g = d.groupby(keys, sort=False)[metrics]
        m, s = g.mean(), (g.max() - g.min()) / 2
        return m.round(3).astype(str) + " ±" + s.round(3).astype(str)

    def tbl(df, title):
        return f"### {title}\n\n" + df.reset_index().to_markdown(index=False) + "\n"

    load_all = lambda f, key=None: [r for p in seeds for r in (json.loads((p / f).read_text())[key] if key
                                                               else json.loads((p / f).read_text()))]
    md = [f"# OpenAlex — summary over {len(seeds)} seeds\n"]
    e2 = pd.DataFrame(load_all("results.json", "E2"))
    own = e2[e2.prefix_len == e2.level.map(PREFIX)]
    t = agg(own, ["split", "method", "level"], ["mAP"])["mAP"].unstack("level")[list(LEVELS)]
    md.append(tbl(t, "E2 — mAP of each level at its OWN prefix (domain@16, field@64, subfield@128)"))
    best = e2.groupby(["split", "method", "level", "prefix_len"]).mAP.mean().reset_index()
    best = best.loc[best.groupby(["split", "method", "level"]).mAP.idxmax()]
    md.append(tbl(best.pivot_table(index=["split", "method"], columns="level", values="prefix_len")[list(LEVELS)],
                  "E2 — prefix length where each level peaks (should be 16 / 64 / 128)"))
    md.append(tbl(agg(load_all("results.json", "E2b"), ["method", "view"], [f"same-{l} AUC" for l in LEVELS]),
                  "E2b — pair AUC per view (does a finer view keep coarser levels?)"))
    md.append(tbl(agg(load_all("results.json", "E2s"), ["split", "level", "method"], ["P@10", "tree_credit@10", "credit_text@10", "credit_coact@10"]),
                  "E2s — paper -> 10 nearest papers: exact label (P@10) and tree credit"))
    md.append(tbl(agg(load_all("results.json", "E3"), ["method"],
                      ["overlap@10_with_encoder", "topic_mAP_encoder", "topic_mAP_SSE"]), "E3 — general search"))
    md.append(tbl(agg(load_all("e8.json", "E8a"), ["query_split", "level", "method"],
                      ["P@10", "P@10_active", "tree_credit@10", "credit_text@10", "credit_coact@10", "join_F1", "Spearman", "NDCG@10"]),
                  "E8a — Papers VecJOIN Authors (P@10 / F1: paper's area = author's main area)"))
    md.append(tbl(agg(load_all("e8.json", "E8b"), ["level", "method"], ["Spearman", "NDCG@10"]),
                  "E8b — institution similarity (truth: cosine of research profiles)"))
    md.append(tbl(agg(load_all("e6_physical.json"), ["policy", "level", "method"], ["ARI", "NMI", "n_main_groups", "coverage"]),
                  "E6 — roll-up / drill-down inside Physical Sciences"))
    (OUT / "summary_tables.md").write_text("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["fetch", "fetch_authors", "fetch_meta", "related", "build", "encode", "train", "eval", "join", "e6", "summary"])
    p.add_argument("--method", default="treesc")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--encoder", default="specter2", choices=["specter2", "specter2_base", "bge"])
    p.add_argument("--domain", default="Physical Sciences")
    a = p.parse_args()
    if a.cmd in ("encode", "train", "eval", "join", "e6"):
        _gpu(torch_only=a.cmd == "encode")
    if a.cmd == "fetch":
        fetch_papers()
    elif a.cmd == "fetch_authors":
        fetch_authors()
    elif a.cmd == "fetch_meta":
        fetch_meta()
    elif a.cmd == "related":
        related()
    elif a.cmd == "build":
        build()
    elif a.cmd == "summary":
        summarize()
    elif a.cmd == "encode":
        encode_all(a.encoder)
    elif a.cmd == "train":
        train(a.method, a.seed)
    elif a.cmd == "eval":
        evaluate(a.seed)
    elif a.cmd == "join":
        join(a.seed)
    else:
        e6(a.seed, a.domain)
