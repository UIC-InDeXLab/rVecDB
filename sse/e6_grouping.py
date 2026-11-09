"""E6 — semantic GROUP BY and roll-up / drill-down, as defined in the paper (range-connected clustering).

GROUP BY_kappa on a view: connect two items if similarity >= kappa; groups = connected components.
Roll-up / drill-down: group by the Order prefix; inside each Order group, group by the Family prefix;
inside each Family group, group by the Genus prefix (so every small group has exactly one parent).

kappa is chosen on TRAINING images (no peeking at test), then applied to the test database.
Agreement with the true groups: NMI and ARI (0 = random, 1 = perfect).
  habitat truth  = groups of species with similar habitat SCORE VECTORS (average-linkage clustering of the
                   50 species' 14 habitat scores; number of groups picked by silhouette, 4..12)
  taxonomy truth = true Order / Family / Genus

Usage: .venv/bin/python -m sse.e6_grouping --sse tree_s0 --extra "B3 separate=b3_s0,B4 CSN=csn_s0" --out r4_seed0
"""
import argparse
import json

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from sklearn.metrics import adjusted_rand_score as ARI, normalized_mutual_info_score as NMI

from .awa2 import load_meta, CACHE, ROOT
from .baselines import sse_views, b6_clip
from .taxonomy_awa2 import LEVELS, HABITAT_PREDICATES

KAPPAS = np.round(np.arange(0.30, 0.995, 0.02), 2)


def normed(M):
    M = np.asarray(M, np.float32)
    return M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-8)


def cc_groups(Z, kappa, chunk=4096):
    """Range-connected clustering: connected components of the graph sim >= kappa."""
    n = len(Z)
    rows, cols = [], []
    for i in range(0, n, chunk):
        S = Z[i:i + chunk] @ Z.T
        r, c = np.nonzero(S >= kappa)
        rows.append(r + i); cols.append(c)
    r, c = np.concatenate(rows), np.concatenate(cols)
    g = csr_matrix((np.ones(len(r), np.int8), (r, c)), shape=(n, n))
    return connected_components(g, directed=False)[1]


def center_groups(Z, kappa, chunk=4096):
    """Center-based ranges (no chaining): repeatedly take the unassigned item with the most neighbours
    (sim >= kappa); its range among the still-unassigned items becomes one group."""
    n = len(Z)
    A = (Z @ Z.T) >= kappa                      # n <= ~6000 here, so the full matrix fits easily
    deg = A.sum(1)
    lab = np.full(n, -1)
    g = 0
    for ctr in np.argsort(-deg, kind="stable"):
        if lab[ctr] >= 0:
            continue
        members = np.flatnonzero(A[ctr] & (lab < 0))
        lab[members] = g
        lab[ctr] = g
        g += 1
    return lab


POLICY = {"connected": cc_groups, "center": center_groups}


def best_kappa(Z, truth, idx, policy="connected"):
    scores = [(NMI(truth[idx], POLICY[policy](Z[idx], k)), k) for k in KAPPAS]
    return max(scores)[1]


def nested(views, idx, kappas, policy="connected"):
    """Recursive refinement: Order groups -> Family groups inside them -> Genus groups inside those."""
    parts, labels = {}, np.zeros(len(idx), int)
    for lvl in LEVELS:
        Z = views[lvl][idx]
        new = np.zeros(len(idx), int)
        nxt = 0
        for g in np.unique(labels):
            m = np.flatnonzero(labels == g)
            sub = POLICY[policy](Z[m], kappas[lvl])
            new[m] = sub + nxt
            nxt += sub.max() + 1
        labels = new
        parts[lvl] = labels.copy()
    return parts


def habitat_truth(cls_df):
    """Cluster the species' habitat score vectors -> 'true' habitat groups (printed for checking)."""
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.metrics import silhouette_score
    V = normed(np.stack(cls_df.habitat.values))
    best = None
    for k in range(4, 13):
        lab = AgglomerativeClustering(n_clusters=k, metric="cosine", linkage="average").fit_predict(V)
        sc = silhouette_score(V, lab, metric="cosine")
        if best is None or sc > best[0]:
            best = (sc, k, lab)
    sc, k, lab = best
    print(f"habitat truth: {k} groups (silhouette {sc:.2f})", flush=True)
    for g in range(k):
        members = list(cls_df.cls[lab == g])
        top = np.stack(cls_df.habitat.values)[lab == g].mean(0).argsort()[::-1][:3]
        print(f"  group {g}: [{', '.join(HABITAT_PREDICATES[t] for t in top)}] {members}", flush=True)
    return lab


def describe(truth, g, min_share=0.01):
    """Main groups = groups holding >= 1% of the items. Coverage = share of items in main groups."""
    sizes = np.bincount(g)
    main = sizes >= max(2, min_share * len(g))
    in_main = main[g]
    return {"n_groups": int(len(sizes)), "n_main_groups": int(main.sum()), "coverage": float(in_main.mean()),
            "NMI": float(NMI(truth, g)), "ARI": float(ARI(truth, g)),
            "NMI_main": float(NMI(truth[in_main], g[in_main])) if in_main.any() else float("nan")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sse", default="tree_s0")
    ap.add_argument("--extra", default="")
    ap.add_argument("--out", default="r4_seed0")
    ap.add_argument("--n_tune", type=int, default=4000)
    ap.add_argument("--n_test", type=int, default=6000)
    args = ap.parse_args()
    rng = np.random.default_rng(0)

    img_df, cls_df = load_meta()
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    hab_main = habitat_truth(cls_df)[c]
    tax = {l: cls_df[l].astype("category").cat.codes.values[c] for l in LEVELS}
    db = np.flatnonzero(img_df.split.values != "train")
    db = np.sort(rng.choice(db, min(args.n_test, len(db)), replace=False))   # keep the graph small
    tune = rng.choice(np.flatnonzero(img_df.split.values == "train"), args.n_tune, replace=False)

    L = json.loads((CACHE / f"emb_{args.sse}.json").read_text())["layout"]
    E = np.load(CACHE / f"emb_{args.sse}.npy")
    sv = sse_views(E, L)
    methods = {"SSE": {"habitat": sv["habitat"][0], "order": E[:, :8], "family": E[:, :32], "genus": E[:, :64]},
               "B6 plain CLIP": {k: X for k in ("habitat", *LEVELS)}}
    for kv in filter(None, args.extra.split(",")):
        lab, tag = kv.split("=")
        Z = np.load(CACHE / f"{tag}.npz")
        methods[lab] = {k: Z[k] for k in ("habitat", *LEVELS)}
    methods = {m: {k: normed(v) for k, v in vs.items()} for m, vs in methods.items()}

    rows = []
    for policy in ("connected", "center"):
        for m, vs in methods.items():
            # habitat GROUP BY
            k = best_kappa(vs["habitat"], hab_main, tune, policy)
            g = POLICY[policy](vs["habitat"][db], k)
            rows.append({"policy": policy, "method": m, "grouping": "habitat", "kappa": float(k),
                         "n_true": int(len(np.unique(hab_main[db]))), **describe(hab_main[db], g)})
            # roll-up / drill-down (kappa per level tuned on train)
            kap = {lvl: best_kappa(vs[lvl], tax[lvl], tune, policy) for lvl in LEVELS}
            parts = nested(vs, db, kap, policy)
            for lvl in LEVELS:
                g = parts[lvl]
                rows.append({"policy": policy, "method": m, "grouping": f"nested {lvl}", "kappa": float(kap[lvl]),
                             "n_true": int(len(np.unique(tax[lvl][db]))), **describe(tax[lvl][db], g)})
            print(policy, m, "done", flush=True)

    out = ROOT / "results/awa2" / args.out
    out.mkdir(parents=True, exist_ok=True)
    (out / "e6.json").write_text(json.dumps(rows, indent=1))
    md = ["### E6 — GROUP BY and roll-up/drill-down (kappa tuned on training images)", "",
          "Main groups = groups holding >= 1% of items; coverage = share of items in main groups.", "",
          "Policy 'connected' = paper's range-connected components; 'center' = center-based ranges (no chaining).", "",
          "| policy | method | grouping | kappa | groups found | main groups | true groups | coverage | NMI | NMI (main) | ARI |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    md += [f"| {r['policy']} | {r['method']} | {r['grouping']} | {r['kappa']:.2f} | {r['n_groups']} | {r['n_main_groups']} | "
           f"{r['n_true']} | {r['coverage']:.2f} | {r['NMI']:.3f} | {r['NMI_main']:.3f} | {r['ARI']:.3f} |" for r in rows]
    (out / "e6.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
