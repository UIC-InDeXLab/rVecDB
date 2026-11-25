"""iNat GROUP BY_k (paper definition: k centers, spherical k-means) — replaces the threshold rules of E6.

Within one class (birds = Aves, insects = Insecta): roll-up / drill-down Order > Family > Genus with k = number of
true groups at each level; impact of k at the Family level; unseen species only.
Usage: .venv/bin/python -m sse.inat_extra groupk --seed 0
"""
import argparse
import json

import numpy as np
from sklearn.metrics import adjusted_rand_score as ARI, normalized_mutual_info_score as NMI

from . import inat
from .inat import CACHE, OUT, LEVELS
from .awa2_extra import kmeans_groups, nested_k


def groupk(seed):
    inat._gpu() if hasattr(inat, "_gpu") else None
    from .evaluate import md_table
    df, X, codes = inat.load()
    import torch  # noqa: F401  (b1_labels needs the module globals set by inat)
    pred = inat.b1_labels(X, df, codes, seed)
    methods = {"B6 plain CLIP": {l: X for l in LEVELS}}
    for lab, tag in (("SSE-treeSC", "treesc"), ("SSE-tree", "tree"), ("B3 separate", "b3sc"), ("B4 CSN", "csnsc")):
        if (CACHE / f"{tag}_s{seed}.npz").exists():
            Z = np.load(CACHE / f"{tag}_s{seed}.npz"); methods[lab] = {l: Z[l] for l in LEVELS}
    rows = []
    for cls in ("Aves", "Insecta"):
        db = np.flatnonzero((df["class"].values == cls) & (df.split.values != "train"))
        n_true = [int(len(np.unique(codes[l][db]))) for l in LEVELS]
        for m, v in methods.items():
            parts = nested_k({l: v[l][db] for l in LEVELS}, LEVELS, n_true, seed)
            for l, kt in zip(LEVELS, n_true):
                rows.append({"class": cls, "part": "roll-up / drill-down", "method": m, "level": l, "k": kt,
                             "NMI": float(NMI(codes[l][db], parts[l])), "ARI": float(ARI(codes[l][db], parts[l]))})
        for l, kt in zip(LEVELS, n_true):
            rows.append({"class": cls, "part": "roll-up / drill-down", "method": "B1 labels (predicted)", "level": l,
                         "k": int(len(np.unique(pred[l][db]))), "NMI": float(NMI(codes[l][db], pred[l][db])),
                         "ARI": float(ARI(codes[l][db], pred[l][db]))})
        kt = n_true[0]
        for f in (0.5, 1, 2, 4):
            k = max(2, int(round(f * kt)))
            for m, v in methods.items():
                g = kmeans_groups(v["order"][db], k, seed)
                rows.append({"class": cls, "part": f"Order, impact of k (x{f})", "method": m, "level": "order", "k": k,
                             "NMI": float(NMI(codes["order"][db], g)), "ARI": float(ARI(codes["order"][db], g))})
        un = db[df.split.values[db] == "unseen"]
        for l in ("family", "genus"):
            kt = int(len(np.unique(codes[l][un])))
            for m, v in methods.items():
                g = kmeans_groups(v[l][un], kt, seed)
                rows.append({"class": cls, "part": "unseen species", "method": m, "level": l, "k": kt,
                             "NMI": float(NMI(codes[l][un], g)), "ARI": float(ARI(codes[l][un], g))})
            rows.append({"class": cls, "part": "unseen species", "method": "B1 labels (predicted)", "level": l,
                         "k": int(len(np.unique(pred[l][un]))), "NMI": float(NMI(codes[l][un], pred[l][un])),
                         "ARI": float(ARI(codes[l][un], pred[l][un]))})
        inat.note("inat-groupk", f"{cls} done (seed {seed})")
    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "groupk.json").write_text(json.dumps(rows, indent=1))
    (out / "groupk.md").write_text(md_table(rows, ["class", "part", "method", "level", "k", "NMI", "ARI"], "iNat GROUP BY_k"))
    print((out / "groupk.md").read_text())


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["groupk"])
    p.add_argument("--seed", type=int, default=0)
    a = p.parse_args()
    groupk(a.seed)
