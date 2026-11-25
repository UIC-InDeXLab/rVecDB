"""E7 — cost: storage, index build, and query latency of the paper's query Q1 (habitat filter + Family ranking).

Representations (AwA2 models, seed 0), scaled to N objects by jittered copies of the 37k real vectors:
  SSE-768 / SSE-128 : one vector; habitat block (32-d) and Family prefix (32-d) are slices of it
  B3 separate       : 6 vectors per object (habitat 32, diet 16, order 8, family 32, genus 64) + 768 encoder vector
  B4 CSN            : one 768-d vector + one shared 768-d mask per facet; a facet similarity = masked cosine (768-d)
  B1 labels         : 14 habitat bits + predicted Family id (+ the 768 encoder vector for search)
Plans:
  scan  : exact. habitat similarity over all N, keep the top 25% (range), Family similarity over the survivors, top 10.
  hnsw  : 'the 10 most habitat-similar objects' with a faiss HNSW index per facet (M=32): build time, memory, latency.
Single-threaded timings (median over queries).
Usage: .venv/bin/python -m sse.cost --n 1000000
"""
import argparse
import json
import time

import numpy as np

from .awa2 import CACHE, ROOT


def normed(M):
    return (M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-8)).astype(np.float32)


def scale(M, n, rng, noise=0.02):
    idx = rng.integers(0, len(M), n)
    return normed(M[idx] + noise * rng.standard_normal((n, M.shape[1])).astype(np.float32) / np.sqrt(M.shape[1]))


def main():
    import faiss
    faiss.omp_set_num_threads(1)
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1_000_000)
    ap.add_argument("--nq", type=int, default=50)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    rng = np.random.default_rng(0)
    L = json.loads((CACHE / f"emb_treesc_s{a.seed}.json").read_text())["layout"]
    E768 = np.load(CACHE / f"emb_treesc_s{a.seed}.npy")
    E128 = np.load(CACHE / f"emb_treesc128_s{a.seed}.npy")
    B3 = np.load(CACHE / f"b3tree_s{a.seed}.npz"); CS = np.load(CACHE / f"csntree_s{a.seed}.npz")
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    idx = rng.integers(0, len(X), a.n)
    jit = lambda M: normed(M[idx] + 0.02 * rng.standard_normal((a.n, M.shape[1])).astype(np.float32) / np.sqrt(M.shape[1]))
    hab, fam = slice(*L["habitat"]), slice(0, L["prefix"]["family"])

    reps = {}
    # SSE: one row-major vector; facet views are column slices of it (per-block normalised at query time = stored norms)
    for lab, E in (("SSE-768", E768), ("SSE-128", E128)):
        V = E[idx] + 0.02 * rng.standard_normal((a.n, E.shape[1])).astype(np.float32) / np.sqrt(E.shape[1])
        V = V.astype(np.float32)
        nh = np.linalg.norm(V[:, hab], axis=1); nf = np.linalg.norm(V[:, fam], axis=1)
        reps[lab] = {"store_floats": E.shape[1] + 2, "vectors": 1,
                     "hab": lambda q, V=V, nh=nh: (V[:, hab] @ q[hab]) / nh,
                     "fam": lambda q, c, V=V, nf=nf: (V[c][:, fam] @ q[fam]) / nf[c],
                     "q": lambda i, V=V: V[i], "hab_mat": normed(V[:, hab])}
        # same vector, block-columnar physical layout: the fixed layout lets the system store each block (and each
        # prefix segment of the taxonomy block) as its own contiguous column group — no extra space.
        P = L["prefix"]
        segs = [np.ascontiguousarray(V[:, a:b]) for a, b in ((0, P["order"]), (P["order"], P["family"]))]
        Hc = np.ascontiguousarray(V[:, hab])
        reps[lab + " (block-columnar)"] = {
            "store_floats": E.shape[1] + 2, "vectors": 1,
            "hab": lambda q, Hc=Hc, nh=nh: (Hc @ q[hab]) / nh,
            "fam": lambda q, c, segs=segs, nf=nf: (segs[0][c] @ q[:P["order"]] + segs[1][c] @ q[P["order"]:P["family"]]) / nf[c],
            "q": lambda i, V=V: V[i], "hab_mat": None}
    Bh, Bf = jit(B3["habitat"]), jit(B3["family"])
    reps["B3 separate"] = {"store_floats": 32 + 16 + 8 + 32 + 64 + 768, "vectors": 6,
                           "hab": lambda q: Bh @ q[0], "fam": lambda q, c: Bf[c] @ q[1],
                           "q": lambda i: (Bh[i], Bf[i]), "hab_mat": Bh}
    from .train_baselines import DIMS
    m = np.maximum(CS["_mask"], 0); conds = list(DIMS)
    mh, mf = m[conds.index("habitat")], m[conds.index("family")]
    C = jit(CS["full"]) if "full" in CS else jit(X)
    nh = np.linalg.norm(C * mh, axis=1); nf = np.linalg.norm(C * mf, axis=1)
    reps["B4 CSN"] = {"store_floats": 768 + 5, "vectors": 1,
                      "hab": lambda q: (C @ (q * mh * mh)) / nh, "fam": lambda q, c: (C[c] @ (q * mf * mf)) / nf[c],
                      "q": lambda i: C[i], "hab_mat": normed(C * mh)}
    # stronger CSN implementation: one materialised matrix per facet with only that mask's active dimensions
    ah, af = np.flatnonzero(mh > 1e-3), np.flatnonzero(mf > 1e-3)
    Ch, Cf = normed(C[:, ah] * mh[ah]), normed(C[:, af] * mf[af])
    n_active = int(sum((m[i] > 1e-3).sum() for i in range(len(conds))))
    reps["B4 CSN (active dims materialised)"] = {
        "store_floats": 768 + n_active, "vectors": 1 + len(conds),
        "hab": lambda q: Ch @ q[0], "fam": lambda q, c: Cf[c] @ q[1], "q": lambda i: (Ch[i], Cf[i]), "hab_mat": Ch}
    Hb = (rng.random((a.n, 14)) < 0.3); Fid = rng.integers(0, 27, a.n)
    Hp = np.packbits(Hb, axis=1).view(np.uint16).ravel()
    reps["B1 labels"] = {"store_floats": 768 + 1, "vectors": 1,
                         "hab": lambda q: np.bitwise_count(Hp & q[0]) / np.maximum(1, np.bitwise_count(Hp | q[0])),
                         "fam": lambda q, c: (Fid[c] == q[1]).astype(np.float32),
                         "q": lambda i: (Hp[i], Fid[i]), "hab_mat": None}

    qs = rng.integers(0, a.n, a.nq)
    rows = []
    for lab, R in reps.items():
        ts = []
        for i in qs:
            q = R["q"](i)
            t0 = time.perf_counter()
            s = R["hab"](q)
            cand = np.argpartition(-s, a.n // 4)[:a.n // 4]
            f = R["fam"](q, cand)
            top = cand[np.argpartition(-f, 10)[:10]]
            ts.append(time.perf_counter() - t0)
        row = {"method": lab, "N": a.n, "vectors per object": R["vectors"], "floats per object": R["store_floats"],
               "storage GB (float32)": a.n * R["store_floats"] * 4 / 1e9, "Q1 scan ms": 1e3 * float(np.median(ts))}
        H = R["hab_mat"]
        if H is not None:
            t0 = time.perf_counter()
            index = faiss.IndexHNSWFlat(H.shape[1], 32, faiss.METRIC_INNER_PRODUCT)
            faiss.omp_set_num_threads(16); index.add(np.ascontiguousarray(H)); faiss.omp_set_num_threads(1)
            row["habitat HNSW build s (16 thr)"] = time.perf_counter() - t0
            row["habitat index dims"] = int(H.shape[1])
            row["habitat index GB"] = a.n * (H.shape[1] * 4 + 32 * 2 * 4) / 1e9
            tq = []
            for i in qs:
                t0 = time.perf_counter(); index.search(H[i:i + 1], 10); tq.append(time.perf_counter() - t0)
            row["habitat top-10 HNSW ms"] = 1e3 * float(np.median(tq))
            del index
        rows.append(row); print(row, flush=True)
    out = ROOT / "results/awa2/x_cost"; out.mkdir(parents=True, exist_ok=True)
    (out / f"cost_n{a.n}.json").write_text(json.dumps(rows, indent=1))
    from .evaluate import md_table
    cols = ["method", "N", "vectors per object", "floats per object", "storage GB (float32)", "Q1 scan ms",
            "habitat index dims", "habitat index GB", "habitat HNSW build s (16 thr)", "habitat top-10 HNSW ms"]
    rows_md = [{c: r.get(c, float("nan")) for c in cols} for r in rows]
    (out / f"cost_n{a.n}.md").write_text(md_table(rows_md, cols, f"E7 cost at N = {a.n:,} (single-threaded queries, median of {a.nq})"))
    print((out / f"cost_n{a.n}.md").read_text())


if __name__ == "__main__":
    main()
