"""MovieLens (text) version of the AwA2 pipeline.

Objects   : movies with a TMDB plot overview (13,248), text = "Title (year). overview"
Encoder   : BAAI/bge-base-en-v1.5 (768 numbers), frozen
Facets    : tag-genome scores (0-1) grouped by data/movielens/tag_groups.csv into genre / tone / theme / style
            (group "other" — names, awards, quality words, places — is not used)
Truth     : facet similarity of two movies = cosine of their CENTERED genome scores on that facet's tags
            (centered per tag, so the common baseline relevance does not make every pair look similar)
Split     : 75% train / 25% test movies (every test movie is a new object; no hierarchy, so no zoom tests)
SSE layout: [ genre 32 | tone 32 | theme 32 | style 32 | rest 640 ] = 768

Usage:
  .venv/bin/python -m sse.movielens prep                 # build data + bge vectors
  .venv/bin/python -m sse.movielens train --method sse|hard|b3|csn --seed 0
  .venv/bin/python -m sse.movielens eval --seed 0        # E1, E3, E4 (+no-mixing), E5b, E5c
"""
import argparse
import csv
import json
import re
import sys

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

from .awa2 import ROOT
from .evaluate import Scorer, ap, ndcg, note, md_table
from .train_sse import Projector, cos_matrix

D = ROOT / "data/movielens"
CACHE = ROOT / "cache/movielens"
OUT = ROOT / "results/movielens"
FACETS = ("genre", "tone", "theme", "style")
LAYOUT = {"genre": (0, 32), "tone": (32, 64), "theme": (64, 96), "style": (96, 128), "rest": (128, 768)}
ENCODER = "BAAI/bge-base-en-v1.5"


# ------------------------------------------------------------------ data
def prep():
    CACHE.mkdir(parents=True, exist_ok=True)
    gs = pd.read_csv(D / "ml-25m/genome-scores.csv")
    G = gs.pivot(index="movieId", columns="tagId", values="relevance")
    tags = pd.read_csv(D / "ml-25m/genome-tags.csv").set_index("tagId").tag
    movies = pd.read_csv(D / "ml-25m/movies.csv").set_index("movieId")
    links = pd.read_csv(D / "ml-25m/links.csv").set_index("movieId")
    md = pd.read_csv(D / "tmdb/movies_metadata.csv", low_memory=False, usecols=["id", "overview"])
    md["tmdbId"] = pd.to_numeric(md["id"], errors="coerce")
    md = md.dropna(subset=["tmdbId", "overview"]).drop_duplicates("tmdbId").set_index("tmdbId").overview
    df = pd.DataFrame(index=G.index)
    df["title"] = movies.title.reindex(df.index)
    df["overview"] = links.tmdbId.reindex(df.index).map(md)
    df = df[df.overview.notna() & (df.overview.str.len() > 40)]
    df["year"] = df.title.str.extract(r"\((\d{4})\)\s*$")[0].astype(float)
    df["text"] = df.title + ". " + df.overview
    rng = np.random.default_rng(0)
    df["split"] = np.where(rng.random(len(df)) < 0.75, "train", "seen_test")
    G = G.loc[df.index]
    groups = {r["tag"]: r["group"] for r in csv.DictReader(open(D / "tag_groups.csv"))}
    tag_group = np.array([groups[tags[t]] for t in G.columns])
    np.save(CACHE / "genome.npy", G.values.astype(np.float32))
    np.save(CACHE / "tag_group.npy", tag_group)
    df.drop(columns=["overview"]).to_parquet(CACHE / "movies.parquet")

    from sentence_transformers import SentenceTransformer
    enc = SentenceTransformer(ENCODER, device="cuda")
    X = enc.encode(df.text.tolist(), batch_size=256, normalize_embeddings=True, show_progress_bar=True)
    np.save(CACHE / "text_emb.npy", X.astype(np.float32))
    tag_names = [tags[t] for t in G.columns]
    np.save(CACHE / "tag_emb.npy", enc.encode([f"a movie that is {t}" for t in tag_names],
                                              normalize_embeddings=True).astype(np.float32))
    print("movies", len(df), "| split", df.split.value_counts().to_dict(),
          "| tags per facet", {f: int((tag_group == f).sum()) for f in FACETS}, "| X", X.shape)


def load():
    df = pd.read_parquet(CACHE / "movies.parquet")
    G = np.load(CACHE / "genome.npy")
    tg = np.load(CACHE / "tag_group.npy")
    X = np.load(CACHE / "text_emb.npy")
    facet = {}
    for f in FACETS:
        V = G[:, tg == f]
        tr = df.split.values == "train"
        V = V - V[tr].mean(0)                       # center per tag (train statistics)
        facet[f] = V / (np.linalg.norm(V, axis=1, keepdims=True) + 1e-8)
    raw = {f: G[:, tg == f] for f in FACETS}
    return df, X, facet, raw, tg


# ------------------------------------------------------------------ training
def train(method, seed, epochs=60, bs=1024, lr=1e-3):
    torch.manual_seed(seed)
    df, X, facet, raw, tg = load()
    tr = torch.tensor(np.flatnonzero(df.split.values == "train"))
    Xt = torch.tensor(X).cuda()
    if method == "hard":   # yes/no labels only: tag relevance >= 0.5 -> yes; target = Jaccard of yes-sets
        B = {f: torch.tensor((raw[f] >= 0.5).astype(np.float32)).cuda() for f in FACETS}
    Ft = {f: torch.tensor(facet[f]).cuda() for f in FACETS}

    def target(f, idx):
        if method == "hard":
            b = B[f][idx]; inter = b @ b.T
            uni = b.sum(1)[:, None] + b.sum(1)[None, :] - inter
            return torch.where(uni > 0, inter / uni.clamp(min=1), torch.ones_like(inter))
        v = Ft[f][idx]
        return v @ v.T

    out = {}
    if method in ("sse", "hard"):
        net = Projector(768, 768).cuda()
        opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
        for _ in range(epochs):
            perm = tr[torch.randperm(len(tr))]
            for b in range(len(tr) // bs):
                idx = perm[b * bs:(b + 1) * bs].cuda()
                x = Xt[idx]; e = net(x)
                loss = F.mse_loss(cos_matrix(e), x @ x.T)
                for f in FACETS:
                    loss = loss + F.mse_loss(cos_matrix(e[:, slice(*LAYOUT[f])]), target(f, idx))
                opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            E = net(Xt).cpu().numpy()
        out = {f: E[:, slice(*LAYOUT[f])] for f in FACETS}
        out["full"] = E
    elif method == "b3":
        out["full"] = X
        for f in FACETS:
            net = Projector(768, 32, hidden=1024).cuda()
            opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
            for _ in range(epochs):
                perm = tr[torch.randperm(len(tr))]
                for b in range(len(tr) // bs):
                    idx = perm[b * bs:(b + 1) * bs].cuda()
                    loss = F.mse_loss(cos_matrix(net(Xt[idx])), target(f, idx))
                    opt.zero_grad(); loss.backward(); opt.step()
            with torch.no_grad():
                out[f] = net(Xt).cpu().numpy()
    elif method == "csn":
        net = Projector(768, 768).cuda()
        masks = nn.Parameter(torch.randn(len(FACETS), 768, device="cuda") * 0.7 + 0.9)
        opt = torch.optim.AdamW(list(net.parameters()) + [masks], lr=lr, weight_decay=1e-4)
        for _ in range(epochs):
            perm = tr[torch.randperm(len(tr))]
            for b in range(len(tr) // bs):
                idx = perm[b * bs:(b + 1) * bs].cuda()
                x = Xt[idx]; e = net(x); m = F.relu(masks)
                loss = F.mse_loss(cos_matrix(e), x @ x.T) + 5e-4 * m.abs().sum()
                for i, f in enumerate(FACETS):
                    loss = loss + F.mse_loss(cos_matrix(e * m[i]), target(f, idx))
                opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            E = net(Xt); m = F.relu(masks)
            out = {f: (E * m[i]).cpu().numpy() for i, f in enumerate(FACETS)}
            out["full"] = E.cpu().numpy()
    np.savez(CACHE / f"{method}_s{seed}.npz", **out)
    print("saved", method, seed, "final loss", float(loss))


# ------------------------------------------------------------------ baselines without SSE training
def label_baselines(X, df, raw, seed):
    """B1: per facet, a multi-label classifier for 'tag relevance >= 0.5', trained on train movies."""
    torch.manual_seed(seed)
    tr = df.split.values == "train"
    Xt = torch.tensor(X).cuda()
    hard, soft = {"full": (X, "cos")}, {"full": (X, "cos")}
    for f in FACETS:
        Y = torch.tensor((raw[f] >= 0.5).astype(np.float32)).cuda()
        lin = nn.Linear(768, Y.shape[1]).cuda()
        opt = torch.optim.AdamW(lin.parameters(), lr=1e-3, weight_decay=1e-4)
        idx_tr = torch.tensor(np.flatnonzero(tr)).cuda()
        for _ in range(60):
            perm = idx_tr[torch.randperm(len(idx_tr), device="cuda")]
            for i in range(0, len(perm), 1024):
                b = perm[i:i + 1024]
                loss = F.binary_cross_entropy_with_logits(lin(Xt[b]), Y[b])
                opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            P = torch.sigmoid(lin(Xt)).cpu().numpy()
        hard[f] = ((P >= 0.5).astype(np.float32), "jacc")
        soft[f] = (P, "cos")
    return hard, soft


def text_prompt_baseline(X, tg):
    """B2: zero-shot — similarity of the movie text to 'a movie that is <tag>' for every tag of the facet."""
    Tm = np.load(CACHE / "tag_emb.npy")
    out = {"full": (X, "cos")}
    for f in FACETS:
        S = X @ Tm[tg == f].T
        out[f] = (S - S.mean(0), "cos")
    return out


# ------------------------------------------------------------------ evaluation
def evaluate(seed, n_q=1000):
    rng = np.random.default_rng(0)
    df, X, facet, raw, tg = load()
    db = np.flatnonzero(df.split.values == "seen_test")
    truth = {f: facet[f] for f in FACETS}
    methods = {}
    for lab, tag in (("SSE", "sse"), ("SSE-hard", "hard"), ("B3 separate", "b3"), ("B4 CSN", "csn")):
        p = CACHE / f"{tag}_s{seed}.npz"
        if p.exists():
            Z = np.load(p)
            methods[lab] = {f: (Z[f], "cos") for f in (*FACETS, "full")}
    b1, b1s = label_baselines(X, df, raw, seed)
    methods.update({"B1 labels": b1, "B1-soft": b1s, "B2 text prompts": text_prompt_baseline(X, tg),
                    "B6 plain bge": {f: (X, "cos") for f in (*FACETS, "full")}})
    res, md = {}, ["# MovieLens results (seed %d)\n" % seed]

    def tsim(f, a, b):
        return (truth[f][a] * truth[f][b]).sum(1)

    # E1
    note("ml-E1", "started")
    a, b = rng.choice(db, 200_000), rng.choice(db, 200_000); k = a != b; a, b = a[k], b[k]
    from scipy.stats import spearmanr
    gt = {f: tsim(f, a, b) for f in FACETS}
    rows = []
    for m, v in methods.items():
        for view in FACETS:
            s = Scorer(v[view]).pairs(a, b)
            rows.append({"method": m, "view": view, **{f: float(spearmanr(s, gt[f]).statistic) for f in FACETS}})
    res["E1"] = rows
    md.append(md_table(rows, ["method", "view", *FACETS], "E1 — Spearman of each view vs each true facet"))
    note("ml-E1", "done")

    # E3 general search: overlap@10 with plain bge, and agreement of full-vector similarity with bge similarity
    note("ml-E3", "started")
    base = Scorer((X, "cos")); rows = []
    qs = rng.choice(db, 300, replace=False)
    for m in ("SSE", "B4 CSN"):
        if m not in methods:
            continue
        full = Scorer(methods[m]["full"]); ov = []
        for q in qs:
            d = db[db != q]
            ov.append(len(set(d[np.argsort(-base(q, d))[:10]]) & set(d[np.argsort(-full(q, d))[:10]])) / 10)
        rows.append({"method": m, "overlap@10_with_bge": float(np.mean(ov))})
    res["E3"] = rows
    if rows:
        md.append(md_table(rows, ["method", "overlap@10_with_bge"], "E3 — general search preserved"))
    note("ml-E3", "done")

    # E4: filter on facet A (reference x), rank on facet B (reference q); graded truth
    note("ml-E4", "started")
    pairs = [("tone", "theme"), ("genre", "tone"), ("theme", "style"), ("genre", "theme")]
    per = {m: [] for m in methods}
    for _ in range(n_q):
        fa, fb = pairs[rng.integers(len(pairs))]
        x, q = rng.choice(db, 2, replace=False)
        frac = rng.choice([0.1, 0.25])
        ts = truth[fa][db] @ truth[fa][x]
        F_true = ts >= np.quantile(ts, 1 - frac)
        gain = np.clip(truth[fb][db] @ truth[fb][q], 0, None) * F_true
        for m, v in methods.items():
            hs = Scorer(v[fa])(x, db)
            M = np.zeros(len(db), bool); M[np.argsort(-hs, kind="stable")[:F_true.sum()]] = True
            top = np.argsort(-np.where(M, Scorer(v[fb])(q, db), -np.inf), kind="stable")[:10]
            per[m].append({"predicate_F1": float((M & F_true).sum() / F_true.sum()), "predicate_AP": ap(hs, F_true),
                           "P@10_feasible": float(F_true[top].mean()), "NDCG@10": float(ndcg(gain[top], gain[F_true]))})
    rows = [{"method": m, **{k: float(np.nanmean([r[k] for r in rs])) for k in rs[0]}} for m, rs in per.items()]
    res["E4"] = rows
    md.append(md_table(rows, ["method", "predicate_F1", "predicate_AP", "P@10_feasible", "NDCG@10"],
                       "E4 — filter on one facet (ref x), rank on another (ref q); graded truth"))
    note("ml-E4", "done")

    # E5b: in-between — among pairs whose yes/no tag sets differ, does the method follow graded truth?
    note("ml-E5", "started")
    rows = []
    for f in FACETS:
        bb = raw[f] >= 0.5
        diff = ~(bb[a] == bb[b]).all(1)
        for m, v in methods.items():
            s = Scorer(v[f]).pairs(a[diff], b[diff])
            rows.append({"facet": f, "method": m, "spearman": float(spearmanr(s, gt[f][diff]).statistic)})
    res["E5b"] = rows
    piv = pd.DataFrame(rows).pivot(index="method", columns="facet", values="spearman").reset_index()
    md.append(md_table(piv.to_dict("records"), ["method", *FACETS],
                       "E5b — in-between similarity among pairs whose yes/no tags differ"))
    # E5c: threshold dial on tone
    rows = []
    for m, v in methods.items():
        sf = Scorer(v["tone"]); curves = []
        for x in rng.choice(db, 200, replace=False):
            s = sf(x, db); t = truth["tone"][db] @ truth["tone"][x]
            curves.append([t[ch].mean() for ch in np.array_split(np.argsort(s, kind="stable"), 10)])
        cv = np.mean(curves, 0)
        rows.append({"method": m, "monotonic": float(spearmanr(np.arange(10), cv).statistic),
                     "low": float(cv[0]), "high": float(cv[-1])})
    res["E5c"] = rows
    md.append(md_table(rows, ["method", "monotonic", "low", "high"], "E5c — tone threshold as a dial"))
    note("ml-E5", "done")

    out = OUT / f"seed{seed}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(res, indent=1))
    (out / "results.md").write_text("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    ap_ = argparse.ArgumentParser()
    ap_.add_argument("cmd", choices=["prep", "train", "eval"])
    ap_.add_argument("--method", default="sse")
    ap_.add_argument("--seed", type=int, default=0)
    a = ap_.parse_args()
    if a.cmd == "prep":
        prep()
    elif a.cmd == "train":
        train(a.method, a.seed)
    else:
        evaluate(a.seed)
