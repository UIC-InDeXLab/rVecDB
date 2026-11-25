"""OpenAlex extra experiments for the paper (2026-11-25).

E9  Trained shared join keys (paper Sec. "Schema Compatibility Across Relations").
    Two relations with DIFFERENT encoders and separately trained SSEs:
      Papers  (S, reference): SPECTER2(title+abstract) -> SSE-treeSC  [topic 128 | rest 640]   (already trained)
      Authors (T)           : bge-base(profile = titles of the author's papers) -> its own SSE [topic 128 | rest 640]
    The Authors SSE is trained on 70% of the authors ("known associations" M = authorship) and the join is
    tested on the other 30% (never seen in training).
      SSE aligned      = L_ret + L_align: each topic prefix (16/64/128) of an author is pulled to the frozen Papers
                         prefix of one of the author's papers (1 - cos), as in the paper.
      SSE independent  = same relation, same SSE losses on the author's own labels, but NO L_align
                         (the blocks mean the same thing but live in rotated coordinate systems).
      B1 labels        = classifiers predict a label for each paper and each author; join = equal label.
      Raw encoders     = SPECTER2 paper vector vs bge author vector (different spaces: not joinable).
    Score: P@10 of returned authors whose main area = the paper's area; at subfield level also semantic credit.

E10 Join threshold sweep (aligned SSE): output size (authors per paper), precision and recall vs tau.
    Labels give one point (equality join); the SSE join is a dial.

E11 GROUP BY_k (paper's definition: k centers, each tuple goes to its most similar center = spherical k-means).
    (a) impact of k at the field and subfield level; (b) roll-up / drill-down with k = number of true groups.

Usage: .venv/bin/python -m sse.oa_extra joinkeys --seed 0 | sweep --seed 0 | groupk --seed 0 | summary
"""
import argparse
import json

import numpy as np
import pandas as pd
import scipy.sparse as sp

from . import openalex as oa
from .openalex import CACHE, OUT, LEVELS, PREFIX, note

ALIGN_W = 1.0


def _gpu():
    oa._gpu()
    global torch, F, Projector, cos_matrix, supcon, md_table
    import torch
    import torch.nn.functional as F
    from .train_sse import Projector, cos_matrix, supcon
    from .evaluate import md_table


def author_profile_emb():
    """bge-base embedding of each author's profile text (titles of their papers). Cached."""
    f = CACHE / "author_bge.npy"
    if f.exists():
        return np.load(f)
    from sentence_transformers import SentenceTransformer
    aw = pd.read_parquet(CACHE / "aw.parquet"); L = pd.read_parquet(CACHE / "aw_links.parquet")
    A = pd.read_parquet(CACHE / "authors.parquet")
    titles = aw.title.values
    prof = L.groupby("author_idx").work_idx.apply(list)
    texts = ["; ".join(titles[w][:30]) for w in prof.reindex(range(len(A))).values]
    m = SentenceTransformer("BAAI/bge-base-en-v1.5", device="cuda")
    E = m.encode(texts, batch_size=128, normalize_embeddings=True, show_progress_bar=False).astype(np.float32)
    np.save(f, E)
    return E


def author_tables():
    df, X, codes, aw, XA, acodes, rel = oa.load(authors=True)
    L, A = rel["links"], rel["authors"]
    W = sp.csr_matrix((np.ones(len(L)), (L.author_idx, L.work_idx)), shape=(len(A), len(aw)))
    n_cat = {l: int(max(codes[l].max(), acodes[l].max()) + 1) for l in LEVELS}
    P = {l: oa._rownorm(W @ oa._onehot(acodes[l], n_cat[l])).tocsr() for l in LEVELS}   # author label shares
    mains = {l: np.asarray(P[l].argmax(1)).ravel() for l in LEVELS}
    rng = np.random.default_rng(0)
    a_split = np.where(rng.random(len(A)) < 0.7, "train", "test")
    return df, X, codes, W, P, mains, a_split, n_cat


def train_author_sse(XB, W, mains, a_split, paper_views, mode, seed, epochs=60, bs=512, lr=1e-3):
    """Authors SSE from bge profile vectors. mode: 'aligned' (L_ret + L_align) or 'independent'
    (L_ret + level losses on the author's own main-area labels, no alignment)."""
    torch.manual_seed(seed)
    Xt = torch.tensor(XB).cuda()
    tr = np.flatnonzero(a_split == "train")
    Wc = W.tocsr()
    works = [Wc.indices[Wc.indptr[a]:Wc.indptr[a + 1]] for a in range(W.shape[0])]
    ref = {l: torch.tensor(oa._normed(paper_views[l])).cuda() for l in LEVELS}           # frozen Papers prefixes
    C = {l: torch.tensor(mains[l]).long().cuda() for l in LEVELS}
    net = Projector(XB.shape[1], 768).cuda()
    opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
    g = np.random.default_rng(seed)
    for ep in range(epochs):
        perm = g.permutation(tr)
        for b in range(0, len(perm) - bs + 1, bs):
            idx = perm[b:b + bs]
            ii = torch.tensor(idx).cuda()
            x = Xt[ii]; e = net(x)
            loss = F.mse_loss(cos_matrix(e), x @ x.T)
            if mode == "aligned":
                p = torch.tensor([g.choice(works[a]) for a in idx]).cuda()                 # one known association each
                for l in LEVELS:
                    loss = loss + ALIGN_W * (1 - (F.normalize(e[:, :PREFIX[l]], dim=-1) * ref[l][p]).sum(1)).mean()
            else:
                for l in LEVELS:
                    z = e[:, :PREFIX[l]]
                    loss = loss + 0.5 * supcon(z, C[l][ii])
            opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        E = net(Xt).cpu().numpy()
    return {l: E[:, :PREFIX[l]] for l in LEVELS}


def b1_authors(XB, mains, a_split, seed):
    """Predict each author's main area from the profile vector (classifier trained on training authors)."""
    torch.manual_seed(seed)
    tr = np.flatnonzero(a_split == "train")
    Xt = torch.tensor(XB).cuda()
    pred = {}
    for l in LEVELS:
        vocab = np.unique(mains[l][tr]); remap = {v: i for i, v in enumerate(vocab)}
        y = torch.tensor([remap[v] for v in mains[l][tr]]).cuda()
        lin = torch.nn.Linear(XB.shape[1], len(vocab)).cuda()
        opt = torch.optim.AdamW(lin.parameters(), lr=1e-2, weight_decay=1e-4)
        it = torch.tensor(tr).cuda()
        for _ in range(300):
            loss = F.cross_entropy(lin(Xt[it]), y); opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            pred[l] = vocab[lin(Xt).argmax(1).cpu().numpy()]
    return pred


def p_at_10(S, R, rng):
    S = S + 1e-6 * rng.random(S.shape)                         # random tie-break (matters for label joins)
    top = np.argsort(-S, axis=1)[:, :10]
    return float(np.take_along_axis(R, top, 1).mean()), top


def joinkeys(seed, nq=1000):
    _gpu()
    rng = np.random.default_rng(seed)
    df, X, codes, W, P, mains, a_split, n_cat = author_tables()
    XB = author_profile_emb()
    Zp = np.load(CACHE / f"treesc_s{seed}.npz")
    paper_q = {l: oa._normed(Zp[l]) for l in LEVELS}                                    # Papers relation (S)
    paper_aw = {l: Zp[f"aw_{l}"] for l in LEVELS}                                       # S applied to authors' papers
    te = np.flatnonzero(a_split == "test")
    REL = {k: np.load(CACHE / "related.npz")[k] for k in ("text", "coact")} if (CACHE / "related.npz").exists() else {}
    Psub = P["subfield"][te].toarray()

    views = {}
    for mode in ("aligned", "independent"):
        V = train_author_sse(XB, W, mains, a_split, paper_aw, mode, seed)
        views[f"SSE {mode}"] = {l: (paper_q[l], oa._normed(V[l][te])) for l in LEVELS}
        note("openalex-E9", f"author SSE {mode} trained (seed {seed})")
    pred_p = oa.b1_labels(X, df, codes, seed)
    pred_a = b1_authors(XB, mains, a_split, seed)

    rows = []
    q_by = {s: rng.choice(np.flatnonzero(df.split.values == s), nq, replace=False) for s in ("seen_test", "unseen")}
    for s, q in q_by.items():
        for l in LEVELS:
            R = codes[l][q][:, None] == mains[l][te][None, :]
            sims = {m: v[l][0][q] @ v[l][1].T for m, v in views.items()}
            sims["B1 labels"] = (pred_p[l][q][:, None] == pred_a[l][te][None, :]).astype(np.float32)
            sims["Raw encoders (SPECTER2 vs bge)"] = oa._normed(X[q])[:, :XB.shape[1]] @ XB[te].T  # not joinable: different spaces
            sims["Random"] = rng.random(R.shape).astype(np.float32)
            for m, S in sims.items():
                p, top = p_at_10(S, R, rng)
                r = {"method": m, "split": s, "level": l, "P@10": p}
                if REL and l == "subfield":
                    for k in ("text", "coact"):
                        C = REL[k][codes[l][q]][:, :Psub.shape[1]] @ Psub.T
                        r[f"credit_{k}@10"] = float(np.take_along_axis(C, top, 1).mean())
                rows.append(r)
    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "e9_joinkeys.json").write_text(json.dumps(rows, indent=1))
    cols = ["method", "split", "level", "P@10"] + (["credit_text@10", "credit_coact@10"] if REL else [])
    rows_md = [{c: r.get(c, float("nan")) for c in cols} for r in rows]
    (out / "e9_joinkeys.md").write_text(md_table(rows_md, cols, f"E9 — trained shared join keys: Papers (SPECTER2) VecJOIN Authors (bge), {len(te)} held-out authors"))
    np.savez(CACHE / f"authors_aligned_s{seed}.npz", **{l: views["SSE aligned"][l][1] for l in LEVELS}, te=te)
    print(open(out / "e9_joinkeys.md").read())


def sweep(seed, nq=1000):
    """E10: tau sweep for the aligned join (field and subfield), on held-out authors and seen-topic papers."""
    _gpu()
    rng = np.random.default_rng(seed)
    df, X, codes, W, P, mains, a_split, n_cat = author_tables()
    Zp = np.load(CACHE / f"treesc_s{seed}.npz"); Za = np.load(CACHE / f"authors_aligned_s{seed}.npz")
    te = Za["te"]
    XB = author_profile_emb()
    pred_p = oa.b1_labels(X, df, codes, seed); pred_a = b1_authors(XB, mains, a_split, seed)
    q = rng.choice(np.flatnonzero(df.split.values == "seen_test"), nq, replace=False)
    rows = []
    for l in LEVELS:
        R = codes[l][q][:, None] == mains[l][te][None, :]
        S = oa._normed(Zp[l][q]) @ Za[l].T
        for tau in np.round(np.arange(0.0, 1.0, 0.05), 2):
            hit = S >= tau
            tp = (hit & R).sum()
            rows.append({"method": "SSE aligned", "level": l, "tau": float(tau), "out_per_paper": float(hit.sum(1).mean()),
                         "precision": float(tp / max(1, hit.sum())), "recall": float(tp / max(1, R.sum())),
                         "F1": float(2 * tp / max(1, hit.sum() + R.sum()))})
        hit = pred_p[l][q][:, None] == pred_a[l][te][None, :]
        tp = (hit & R).sum()
        rows.append({"method": "B1 labels (equality)", "level": l, "tau": float("nan"), "out_per_paper": float(hit.sum(1).mean()),
                     "precision": float(tp / max(1, hit.sum())), "recall": float(tp / max(1, R.sum())),
                     "F1": float(2 * tp / max(1, hit.sum() + R.sum()))})
    out = OUT / f"seed{seed}"
    (out / "e10_sweep.json").write_text(json.dumps(rows, indent=1))
    (out / "e10_sweep.md").write_text(md_table(rows, ["method", "level", "tau", "out_per_paper", "precision", "recall", "F1"],
                                                f"E10 — join threshold sweep ({len(te)} held-out authors, {nq} papers)"))
    print(open(out / "e10_sweep.md").read())


# ------------------------------------------------------------------ GROUP BY_k
def kmeans_groups(Z, k, seed=0):
    """GROUP BY_k as defined in the paper: k centers maximising total cosine similarity; each tuple goes to its
    most similar center (spherical k-means, faiss)."""
    import faiss
    Z = np.ascontiguousarray(oa._normed(Z), dtype=np.float32)
    k = int(max(1, min(k, len(Z))))
    if k == 1:
        return np.zeros(len(Z), int)
    km = faiss.Kmeans(Z.shape[1], k, niter=30, nredo=3, spherical=True, seed=seed, verbose=False, min_points_per_centroid=1)
    km.train(Z)
    return km.index.search(Z, 1)[1].ravel()


def nested_k(views, levels, k_total, seed=0):
    """Roll-up / drill-down with GROUP BY_k: level 1 into k_total[0] groups; inside each group, the next level is
    split into a share of k_total[i] proportional to the group's size (at least 1)."""
    n = len(next(iter(views.values())))
    labels = np.zeros(n, int); parts = {}
    for i, l in enumerate(levels):
        new = np.zeros(n, int); nxt = 0
        for g in np.unique(labels):
            m = np.flatnonzero(labels == g)
            k = k_total[i] if i == 0 else max(1, int(round(k_total[i] * len(m) / n)))
            sub = kmeans_groups(views[l][m], k, seed); new[m] = sub + nxt; nxt += sub.max() + 1
        labels = new; parts[l] = labels.copy()
    return parts


def groupk(seed, n_db=20000):
    _gpu()
    from sklearn.metrics import adjusted_rand_score as ARI, normalized_mutual_info_score as NMI
    rng = np.random.default_rng(0)
    df, X, codes = oa.load()
    db = np.sort(rng.choice(np.flatnonzero(df.split.values != "train"), n_db, replace=False))
    methods = {"B6 plain encoder": {l: X for l in LEVELS}}
    for lab, Z in oa.method_files(seed, (("SSE-treeSC", "treesc"),) + oa.BASE_METHODS).items():
        methods[lab] = {l: Z[l] for l in LEVELS}
    pred = oa.b1_labels(X, df, codes, seed)
    n_true = {l: int(len(np.unique(codes[l][db]))) for l in LEVELS}
    rows = []
    # (a) impact of k (flat GROUP BY_k on the level's prefix)
    for l in ("field", "subfield"):
        for f in (0.25, 0.5, 1, 2, 4):
            k = max(2, int(round(f * n_true[l])))
            for m, v in methods.items():
                g = kmeans_groups(v[l][db], k, seed)
                rows.append({"part": "impact of k", "method": m, "level": l, "k": k, "k/true": f,
                             "NMI": float(NMI(codes[l][db], g)), "ARI": float(ARI(codes[l][db], g))})
            rows.append({"part": "impact of k", "method": "B1 labels (fixed groups)", "level": l, "k": int(len(np.unique(pred[l][db]))),
                         "k/true": float("nan"), "NMI": float(NMI(codes[l][db], pred[l][db])), "ARI": float(ARI(codes[l][db], pred[l][db]))})
        note("openalex-E11", f"impact of k {l} done (seed {seed})")
    # (b) roll-up / drill-down: domain -> field -> subfield, k = true number of groups per level
    for m, v in methods.items():
        parts = nested_k({l: v[l][db] for l in LEVELS}, LEVELS, [n_true[l] for l in LEVELS], seed)
        for l in LEVELS:
            rows.append({"part": "roll-up", "method": m, "level": l, "k": n_true[l], "k/true": 1.0,
                         "NMI": float(NMI(codes[l][db], parts[l])), "ARI": float(ARI(codes[l][db], parts[l]))})
    for l in LEVELS:
        rows.append({"part": "roll-up", "method": "B1 labels (fixed groups)", "level": l, "k": int(len(np.unique(pred[l][db]))),
                     "k/true": float("nan"), "NMI": float(NMI(codes[l][db], pred[l][db])), "ARI": float(ARI(codes[l][db], pred[l][db]))})
    # unseen-topic papers only (labels cannot have their topic)
    un = db[df.split.values[db] == "unseen"]
    for m, v in methods.items():
        g = kmeans_groups(v["subfield"][un], int(len(np.unique(codes["subfield"][un]))), seed)
        rows.append({"part": "unseen topics", "method": m, "level": "subfield", "k": int(g.max() + 1), "k/true": 1.0,
                     "NMI": float(NMI(codes["subfield"][un], g)), "ARI": float(ARI(codes["subfield"][un], g))})
    rows.append({"part": "unseen topics", "method": "B1 labels (fixed groups)", "level": "subfield", "k": int(len(np.unique(pred["subfield"][un]))),
                 "k/true": float("nan"), "NMI": float(NMI(codes["subfield"][un], pred["subfield"][un])),
                 "ARI": float(ARI(codes["subfield"][un], pred["subfield"][un]))})
    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "e11_groupk.json").write_text(json.dumps(rows, indent=1))
    (out / "e11_groupk.md").write_text(md_table(rows, ["part", "method", "level", "k", "k/true", "NMI", "ARI"],
                                                 f"E11 — GROUP BY_k (spherical k-means), {n_db} test papers"))
    print(open(out / "e11_groupk.md").read())


def summary():
    """3-seed mean ± half-range for E9-E11 -> results/openalex/extra_tables.md"""
    out = []
    for name, keys in (("e9_joinkeys", ["method", "split", "level"]), ("e10_sweep", ["method", "level", "tau"]),
                       ("e11_groupk", ["part", "method", "level", "k/true"])):
        fr = [pd.DataFrame(json.loads((OUT / f"seed{s}/{name}.json").read_text())) for s in range(3) if (OUT / f"seed{s}/{name}.json").exists()]
        if not fr:
            continue
        d = pd.concat(fr)
        num = [c for c in d.columns if c not in keys and pd.api.types.is_numeric_dtype(d[c])]
        g = d.groupby(keys, dropna=False, sort=False)[num]
        mean, half = g.mean(), (g.max() - g.min()) / 2
        t = mean.copy().astype(object)
        for c in num:
            t[c] = [f"{a:.3f} ±{b:.3f}" if np.isfinite(a) else "nan" for a, b in zip(mean[c], half[c])]
        out.append(f"### {name} ({len(fr)} seeds)\n\n" + t.reset_index().to_markdown(index=False) + "\n")
    (OUT / "extra_tables.md").write_text("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["joinkeys", "sweep", "groupk", "summary", "profile"])
    p.add_argument("--seed", type=int, default=0)
    a = p.parse_args()
    if a.cmd == "summary":
        summary()
    elif a.cmd == "profile":
        author_profile_emb()
    else:
        {"joinkeys": joinkeys, "sweep": sweep, "groupk": groupk}[a.cmd](a.seed)
