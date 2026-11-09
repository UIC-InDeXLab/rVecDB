"""Q2-style queries from the paper (Section 4, Q2), on AwA2:

    SELECT * FROM Animals t
    WHERE  E_tax^(1)(t) ~ c_<Order>                         -- Order filter via a named-concept PROTOTYPE
      AND  lo <= sim(E_habitat(t), E_habitat(x)) <= hi       -- habitat BAND (not just ">= threshold")
    ORDER BY sim(E(t), E(q))                                 -- general similarity
    LIMIT 10

(No year condition: AwA2 has no dates.)

Truth: Order filter = true order; band = items whose TRUE habitat similarity to x falls in the [lo, hi]
quantile band; both must hold. Each method uses its own scores with the same quantile band and the
same number of Order members (size-matched, like E4).
Prototype c_<Order> = mean of the Order view over TRAINING images of that order (B1: the order label).

Metrics: F1 of the Order filter, F1 of the band, F1 of the combined feasible set,
P@10 = share of the returned top-10 that truly satisfy both conditions.

Usage: .venv/bin/python -m sse.q2 --sse tree_s0 --extra "B3 separate=b3tree_s0,B4 CSN=csntree_s0" --out r5_seed0 --seed 0
"""
import argparse
import json

import numpy as np
import torch

from .awa2 import load_meta, CACHE, ROOT
from .baselines import b1_labels
from .evaluate import Scorer, truth

BANDS = [(0.5, 0.8), (0.3, 0.6), (0.6, 0.9), (0.2, 0.5)]


def f1(a, b):
    tp = (a & b).sum()
    return float(2 * tp / max(1, a.sum() + b.sum()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sse", default="tree_s0")
    ap.add_argument("--extra", default="")
    ap.add_argument("--out", default="r5_seed0")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--n", type=int, default=1000)
    args = ap.parse_args()
    torch.manual_seed(args.seed)
    rng = np.random.default_rng(0)                      # same queries for every seed

    img_df, cls_df = load_meta()
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    db = np.flatnonzero(np.isin(img_df.split.values, ["seen_test", "unseen"]))
    tr = img_df.split.values == "train"
    T = truth(cls_df)
    order_name = cls_df.order.values[c]
    train_orders = sorted(set(cls_df.order[~cls_df.unseen]))

    def proto_views(order_view):
        """Order view + prototypes (mean over training images of each order)."""
        return order_view, {o: order_view[tr & (order_name == o)].mean(0) for o in train_orders}

    E = np.load(CACHE / f"emb_{args.sse}.npy")
    L = json.loads((CACHE / f"emb_{args.sse}.json").read_text())["layout"]
    methods = {"SSE": {"order": proto_views(E[:, :8]), "habitat": (E[:, slice(*L["habitat"])], "cos"),
                       "full": (E, "cos")},
               "B6 plain CLIP": {"order": proto_views(X), "habitat": (X, "cos"), "full": (X, "cos")}}
    for kv in filter(None, args.extra.split(",")):
        lab, tag = kv.split("=")
        Z = np.load(CACHE / f"{tag}.npz")
        methods[lab] = {"order": proto_views(Z["order"]), "habitat": (Z["habitat"], "cos"), "full": (Z["full"], "cos")}
    b1, b1s, ocodes, oprobs = b1_labels(X, img_df, cls_df, return_order=True)
    onehot = np.eye(len(train_orders), dtype=np.float32)
    methods["B1 labels"] = {"order": (onehot[ocodes], {o: onehot[i] for i, o in enumerate(train_orders)}),
                            "habitat": b1["habitat"], "full": (X, "cos")}
    methods["B1-soft"] = {"order": (oprobs, {o: onehot[i] for i, o in enumerate(train_orders)}),
                          "habitat": b1s["habitat"], "full": (X, "cos")}

    # queries: target order with >= 2 species in the database
    db_orders = [o for o in train_orders if len(set(c[db][order_name[db] == o])) >= 2]
    queries = [(rng.choice(db_orders), int(rng.choice(db)), int(rng.choice(db)), BANDS[rng.integers(len(BANDS))])
               for _ in range(args.n)]
    print("orders used:", db_orders, flush=True)

    def band_mask(scores, lo, hi):
        r = np.empty(len(scores)); r[np.argsort(scores, kind="stable")] = np.arange(len(scores)) / len(scores)
        return (r >= lo) & (r < hi)

    res = {m: [] for m in methods}
    for o, x, q, (lo, hi) in queries:
        t_order = order_name[db] == o
        t_band = band_mask(T["habitat"][c[x], c[db]] + 1e-6 * rng.random(len(db)), lo, hi)
        t_feas = t_order & t_band
        for m, v in methods.items():
            ov, protos = v["order"]
            pv = ov[db] / (np.linalg.norm(ov[db], axis=1, keepdims=True) + 1e-8)
            p = protos[o] / (np.linalg.norm(protos[o]) + 1e-8)
            so = pv @ p
            m_order = np.zeros(len(db), bool); m_order[np.argsort(-so, kind="stable")[:t_order.sum()]] = True
            m_band = band_mask(Scorer(v["habitat"])(x, db), lo, hi)
            m_feas = m_order & m_band
            rank = np.where(m_feas, Scorer(v["full"])(q, db), -np.inf)
            top = np.argsort(-rank, kind="stable")[:10]
            top = top[np.isfinite(rank[top])]
            res[m].append({"order_F1": f1(m_order, t_order), "band_F1": f1(m_band, t_band),
                           "feasible_F1": f1(m_feas, t_feas),
                           "P@10": float(t_feas[top].mean()) if len(top) else 0.0})

    out = ROOT / "results/awa2" / args.out
    out.mkdir(parents=True, exist_ok=True)
    summ = {m: {k: float(np.mean([r[k] for r in rs])) for k in rs[0]} for m, rs in res.items()}
    (out / "q2.json").write_text(json.dumps(summ, indent=1))
    md = ["### Q2 — Order prototype filter + habitat BAND + general ranking", "",
          "| method | order_F1 | band_F1 | feasible_F1 | P@10 |", "|---|---|---|---|---|"]
    md += [f"| {m} | {d['order_F1']:.3f} | {d['band_F1']:.3f} | {d['feasible_F1']:.3f} | {d['P@10']:.3f} |"
           for m, d in summ.items()]
    (out / "q2.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
