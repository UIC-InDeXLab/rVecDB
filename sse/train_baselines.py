"""Trained baselines on the same frozen CLIP features and the same labels as SSE.

B3  "separate vectors" (what pgvector / Milvus multi-vector users do):
    one small network PER attribute/level, each trained only on its own loss:
      habitat (32) · diet (16) · order (8) · family (32) · genus (64)   + the plain CLIP vector (768)
    -> 920 numbers stored per item (SSE stores 768).

B4  CSN, Conditional Similarity Networks (Veit et al., CVPR 2017), adapted:
    ONE shared 768-d embedding + one LEARNED mask per condition
    (habitat, diet, order, family, genus). Similarity under a condition = cosine of (embedding * mask).
    Masks are non-negative (ReLU) with an L1 penalty, as in the paper. To keep the comparison about
    STRUCTURE (fixed blocks vs. learned masks), CSN uses the same per-condition losses as SSE
    (graded MSE for habitat/diet, contrastive for levels) plus the same "keep CLIP" loss.

Usage: .venv/bin/python -m sse.train_baselines --method b3|csn --seed 0
Writes cache/awa2/<method>_s<seed>.npz with one matrix per view.
"""
import argparse

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from .awa2 import load_meta, CACHE
from .taxonomy_awa2 import LEVELS
from .train_sse import Projector, cos_matrix, supcon, facet_targets

DIMS = {"habitat": 32, "diet": 16, "order": 8, "family": 32, "genus": 64}


def setup(seed):
    torch.manual_seed(seed)
    img_df, cls_df = load_meta()
    X = torch.tensor(np.load(CACHE / "clip_img.npy"), dtype=torch.float32)
    y_cls = torch.tensor(img_df.cls.map({c: i for i, c in enumerate(cls_df.cls)}).values)
    lvl = {l: torch.tensor(cls_df[l].astype("category").cat.codes.values, dtype=torch.long).cuda()
           for l in LEVELS}
    S = {f: torch.tensor(facet_targets(cls_df, f, False)).cuda() for f in ("habitat", "diet")}
    train = torch.tensor(np.flatnonzero(img_df.split.values == "train"))
    return X, y_cls, lvl, S, train


TREE = None   # set in main() when --tree: graded family-tree targets per level (same as SSE-tree)


def cond_loss(name, z, c, lvl, S):
    if name in S:
        return F.mse_loss(cos_matrix(z), S[name][c][:, c])
    if TREE is not None:
        return 0.5 * 10 * F.mse_loss(cos_matrix(z), TREE[name][c][:, c])
    return 0.5 * supcon(z, lvl[name][c])


def batches(train, bs, epochs):
    for _ in range(epochs):
        perm = train[torch.randperm(len(train))]
        for b in range(len(train) // bs):
            yield perm[b * bs:(b + 1) * bs]


def train_b3(X, y_cls, lvl, S, train, epochs=40, bs=1024, lr=1e-3):
    out = {"full": X.numpy()}
    for name, d in DIMS.items():
        net = Projector(768, d, hidden=1024).cuda()
        opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
        for idx in batches(train, bs, epochs):
            x, c = X[idx].cuda(), y_cls[idx].cuda()
            loss = cond_loss(name, net(x), c, lvl, S)
            opt.zero_grad(); loss.backward(); opt.step()
        print(f"B3 {name:8s} d={d:3d} final loss {loss.item():.4f}", flush=True)
        with torch.no_grad():
            out[name] = torch.cat([net(X[i:i + 8192].cuda()).cpu() for i in range(0, len(X), 8192)]).numpy()
    return out


def train_csn(X, y_cls, lvl, S, train, epochs=40, bs=1024, lr=1e-3, l1=5e-4):
    net = Projector(768, 768).cuda()
    conds = list(DIMS)
    # paper init: masks ~ N(0.9, 0.7), passed through ReLU
    masks = nn.Parameter(torch.randn(len(conds), 768, device="cuda") * 0.7 + 0.9)
    opt = torch.optim.AdamW(list(net.parameters()) + [masks], lr=lr, weight_decay=1e-4)
    for idx in batches(train, bs, epochs):
        x, c = X[idx].cuda(), y_cls[idx].cuda()
        e = net(x)
        m = F.relu(masks)
        loss = F.mse_loss(cos_matrix(e), x @ x.T)
        for i, name in enumerate(conds):
            loss = loss + cond_loss(name, e * m[i], c, lvl, S)
        loss = loss + l1 * m.abs().sum()   # L1 norm (sum), as in the CSN paper
        opt.zero_grad(); loss.backward(); opt.step()
    print(f"CSN final loss {loss.item():.4f}", flush=True)
    with torch.no_grad():
        E = torch.cat([net(X[i:i + 8192].cuda()).cpu() for i in range(0, len(X), 8192)])
        m = F.relu(masks).cpu()
    out = {"full": E.numpy()}
    for i, name in enumerate(conds):
        out[name] = (E * m[i]).numpy()
    # how much do the learned masks overlap? (SSE blocks overlap 0 by design)
    act = (m > 1e-3).float()
    print("CSN active dims per mask:", {n: int(act[i].sum()) for i, n in enumerate(conds)}, flush=True)
    ov = {f"{a}/{b}": float((act[i] * act[j]).sum() / max(1, min(act[i].sum(), act[j].sum())))
          for i, a in enumerate(conds) for j, b in enumerate(conds) if i < j}
    print("CSN mask overlap (share of the smaller mask):", {k: round(v, 2) for k, v in ov.items()}, flush=True)
    out["_mask"] = m.numpy()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--method", choices=["b3", "csn"], required=True)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--tree", action="store_true", help="graded family-tree loss for the levels (as SSE-tree)")
    args = ap.parse_args()
    X, y_cls, lvl, S, train = setup(args.seed)
    if args.tree:
        global TREE
        same = {l: (lvl[l][:, None] == lvl[l][None, :]).float() for l in LEVELS}
        TREE = {"order": same["order"],
                "family": torch.maximum(same["family"], 0.5 * same["order"]),
                "genus": torch.maximum(torch.maximum(same["genus"], 0.67 * same["family"]), 0.33 * same["order"])}
    out = (train_b3 if args.method == "b3" else train_csn)(X, y_cls, lvl, S, train)
    path = CACHE / f"{args.method}{'tree' if args.tree else ''}_s{args.seed}.npz"
    np.savez(path, **out)
    print("saved", path)


if __name__ == "__main__":
    main()
