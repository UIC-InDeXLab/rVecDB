"""Train a Schema-Structured Embedding (SSE) projection on frozen CLIP features (AwA2).

Variants (--variant):
  main   : habitat/diet blocks trained on graded scores; Order/Family/Genus labels on prefixes 8/32/64
  hard   : habitat/diet blocks trained on yes/no labels only; "same" only if ALL yes/no answers match
  hardj  : yes/no labels only, but credit for each shared yes (Jaccard of the yes-sets)   -> E5(b)
  mrl    : like main, but every taxonomy prefix is trained with Genus labels  -> E2 ablation
  tree   : each prefix follows GRADED family-tree similarity (MSE, like habitat), no yes/no contrastive
             Order prefix:  1 same order, 0 else
             Family prefix: 1 same family, 0.5 same order, 0 else
             Genus prefix:  1 same genus, 0.67 same family, 0.33 same order, 0 else
  treesc : tree + the yes/no contrastive loss of main

Usage: .venv/bin/python -m sse.train_sse --variant main [--dim 768]
Writes cache/awa2/emb_<variant>_<dim>.npy  (all images, L2-normalised per block not applied)
"""
import argparse
import json

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from .awa2 import load_meta, CACHE
from .taxonomy_awa2 import LEVELS


def layout(dim):
    """Block layout. Facet blocks are fixed; the residual ("rest") absorbs the remainder."""
    tax, hab, diet = 64, 32, 16
    return {
        "tax": (0, tax), "habitat": (tax, tax + hab), "diet": (tax + hab, tax + hab + diet),
        "rest": (tax + hab + diet, dim), "prefix": {"order": 8, "family": 32, "genus": 64},
    }


class Projector(nn.Module):
    def __init__(self, d_in=768, d_out=768, hidden=2048):
        super().__init__()
        self.mlp = nn.Sequential(nn.Linear(d_in, hidden), nn.GELU(), nn.Linear(hidden, d_out))
        self.skip = nn.Linear(d_in, d_out, bias=False)

    def forward(self, x):
        return self.mlp(x) + self.skip(x)


def cos_matrix(z):
    z = F.normalize(z, dim=-1)
    return z @ z.T


def supcon(z, labels, t=0.1):
    """Supervised contrastive loss on one view."""
    z = F.normalize(z, dim=-1)
    logits = z @ z.T / t
    n = len(z)
    eye = torch.eye(n, dtype=torch.bool, device=z.device)
    logits = logits.masked_fill(eye, -1e9)
    pos = (labels[:, None] == labels[None, :]) & ~eye
    logp = logits - torch.logsumexp(logits, dim=1, keepdim=True)
    has = pos.any(1)
    return -((logp * pos).sum(1)[has] / pos.sum(1)[has]).mean()


def facet_targets(cls_df, facet, hard, jaccard=False):
    v = np.stack(cls_df[facet].values)
    if jaccard:
        b = (v >= 0.5).astype(np.float32)
        inter = b @ b.T
        union = b.sum(1)[:, None] + b.sum(1)[None, :] - inter
        return np.where(union > 0, inter / np.maximum(union, 1), 1.0).astype(np.float32)
    if hard:
        b = (v >= 0.5).astype(np.float32)
        # categorical label = the exact yes/no pattern: same pattern -> 1, else 0
        return (b[:, None, :] == b[None, :, :]).all(-1).astype(np.float32)
    v = v / (np.linalg.norm(v, axis=1, keepdims=True) + 1e-8)
    return (v @ v.T).astype(np.float32)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="main", choices=["main", "hard", "hardj", "mrl", "tree", "treesc"])
    ap.add_argument("--dim", type=int, default=768)
    ap.add_argument("--epochs", type=int, default=40)
    ap.add_argument("--bs", type=int, default=1024)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--w_ret", type=float, default=1.0)
    ap.add_argument("--w_facet", type=float, default=1.0)
    ap.add_argument("--w_prefix", type=float, default=0.5)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--name", default="", help="output tag (default: <variant>_<dim>)")
    args = ap.parse_args()
    torch.manual_seed(args.seed)
    dev = "cuda"

    img_df, cls_df = load_meta()
    X = torch.tensor(np.load(CACHE / "clip_img.npy"), dtype=torch.float32)
    cls_idx = {c: i for i, c in enumerate(cls_df.cls)}
    y_cls = torch.tensor(img_df.cls.map(cls_idx).values)
    lvl_ids = {l: torch.tensor(cls_df[l].astype("category").cat.codes.values, dtype=torch.long)
               for l in LEVELS}
    S = {f: torch.tensor(facet_targets(cls_df, f, args.variant == "hard", args.variant == "hardj")) for f in ("habitat", "diet")}
    S = {k: v.to(dev) for k, v in S.items()}
    lvl_ids = {k: v.to(dev) for k, v in lvl_ids.items()}
    same = {l: (lvl_ids[l][:, None] == lvl_ids[l][None, :]).float() for l in LEVELS}
    tree_target = {
        "order": same["order"],
        "family": torch.maximum(same["family"], 0.5 * same["order"]),
        "genus": torch.maximum(torch.maximum(same["genus"], 0.67 * same["family"]), 0.33 * same["order"]),
    }

    train = torch.tensor(np.flatnonzero(img_df.split.values == "train"))
    L = layout(args.dim)
    model = Projector(768, args.dim).to(dev)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    steps = args.epochs * (len(train) // args.bs)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=args.lr, total_steps=steps)

    step = 0
    for ep in range(args.epochs):
        perm = train[torch.randperm(len(train))]
        for b in range(len(train) // args.bs):
            idx = perm[b * args.bs:(b + 1) * args.bs]
            x, c = X[idx].to(dev), y_cls[idx].to(dev)
            e = model(x)
            # 1) keep general similarity of CLIP
            l_ret = F.mse_loss(cos_matrix(e), x @ x.T)
            # 2) facet blocks follow facet similarity
            l_facet = sum(F.mse_loss(cos_matrix(e[:, slice(*L[f])]), S[f][c][:, c])
                          for f in ("habitat", "diet"))
            # 3) taxonomy prefixes follow their hierarchy level
            l_prefix = 0
            for lvl, plen in L["prefix"].items():
                if args.variant in ("tree", "treesc"):
                    l_prefix = l_prefix + 10 * F.mse_loss(cos_matrix(e[:, :plen]), tree_target[lvl][c][:, c])
                if args.variant != "tree":
                    target_lvl = "genus" if args.variant == "mrl" else lvl
                    l_prefix = l_prefix + supcon(e[:, :plen], lvl_ids[target_lvl][c])
            loss = args.w_ret * l_ret + args.w_facet * l_facet + args.w_prefix * l_prefix
            opt.zero_grad()
            loss.backward()
            opt.step()
            sched.step()
            step += 1
        if ep % 10 == 0 or ep == args.epochs - 1:
            print(f"ep {ep:3d}  loss {loss.item():.4f}  ret {l_ret.item():.4f}  "
                  f"facet {l_facet.item():.4f}  prefix {l_prefix.item():.4f}")

    model.eval()
    with torch.no_grad():
        E = torch.cat([model(X[i:i + 8192].to(dev)).cpu() for i in range(0, len(X), 8192)])
    name = "emb_" + (args.name or f"{args.variant}_{args.dim}")
    np.save(CACHE / f"{name}.npy", E.numpy().astype(np.float32))
    (CACHE / f"{name}.json").write_text(json.dumps({"args": vars(args), "layout": L}, indent=1))
    print("saved", name, E.shape)


if __name__ == "__main__":
    main()
