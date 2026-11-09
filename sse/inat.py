"""iNaturalist 2021 (validation set) — deep family tree (G2, G6) and scale.

Data   : 100k images, 10,000 species, 10 images each, full taxonomy per image, location + date.
Split  : 20% of species fully held out ("unseen"); for the rest, 7 images train / 3 test ("seen_test").
Levels : Order / Family / Genus (same as AwA2).  SSE layout: [ taxonomy 128 | rest 640 ],
         prefixes 16 / 64 / 128 = Order / Family / Genus.  No habitat facet on iNat.
Truth  : tree similarity (same genus > same family > same order > unrelated).

Usage:
  .venv/bin/python -m sse.inat prep                        # metadata + CLIP vectors (reads the tar.gz directly)
  .venv/bin/python -m sse.inat train --method tree|main|mrl|b3|csn --seed 0
  .venv/bin/python -m sse.inat eval --seed 0               # E2, E2b, E3 (+ B1 labels, CLIP, CLIP-PCA)
  .venv/bin/python -m sse.inat e6 --seed 0                 # roll-up / drill-down
"""
import argparse
import io
import json
import queue
import tarfile
import threading

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

from .awa2 import ROOT
from .evaluate import Scorer, ap, note, md_table
from .train_sse import Projector, cos_matrix, supcon

D = ROOT / "data/inat"
CACHE = ROOT / "cache/inat"
OUT = ROOT / "results/inat"
LEVELS = ("order", "family", "genus")
PREFIX = {"order": 16, "family": 64, "genus": 128}
TAX_DIM = 128


# ------------------------------------------------------------------ data
def prep():
    import open_clip
    from PIL import Image
    CACHE.mkdir(parents=True, exist_ok=True)
    with tarfile.open(D / "val.json.tar.gz") as t:
        meta = json.load(t.extractfile([m for m in t.getmembers() if m.name.endswith(".json")][0]))
    cats = pd.DataFrame(meta["categories"]).set_index("id")
    imgs = pd.DataFrame(meta["images"]).set_index("id")
    ann = pd.DataFrame(meta["annotations"]).set_index("image_id").category_id
    imgs["cat"] = ann.reindex(imgs.index).values
    for lvl in ("kingdom", "phylum", "class", *LEVELS):
        imgs[lvl] = cats[lvl].reindex(imgs.cat).values
    imgs["species"] = imgs.cat
    imgs["year"] = pd.to_datetime(imgs.date, errors="coerce").dt.year
    rng = np.random.default_rng(0)
    species = imgs.species.unique()
    unseen = set(rng.choice(species, int(0.2 * len(species)), replace=False))
    split = np.where(imgs.species.isin(unseen), "unseen", "train").astype(object)
    rank = pd.Series(rng.random(len(imgs)), index=imgs.index).groupby(imgs.species.values).rank(method="first")
    split[(split == "train") & (rank.values > 7)] = "seen_test"      # 7 train / 3 test images per seen species
    imgs["split"] = split
    imgs = imgs.reset_index(drop=True)
    keep = ["file_name", "species", "kingdom", "phylum", "class", *LEVELS, "latitude", "longitude", "year", "split"]
    imgs[[k for k in keep if k in imgs]].to_parquet(CACHE / "images.parquet")
    print("images", len(imgs), imgs.split.value_counts().to_dict(),
          {l: imgs[l].nunique() for l in ("kingdom", "class", *LEVELS)}, flush=True)

    # CLIP vectors: stream the archive once, decode in threads, encode on the GPU
    pos = {fn: i for i, fn in enumerate(imgs.file_name)}
    model, _, preprocess = open_clip.create_model_and_transforms("ViT-L-14", pretrained="openai")
    model = model.cuda().eval().half()
    X = np.zeros((len(imgs), 768), np.float16)
    q = queue.Queue(maxsize=4096)

    def reader():
        with tarfile.open(D / "val.tar.gz", "r|gz") as t:
            for m in t:
                if m.isfile() and m.name in pos:
                    q.put((pos[m.name], t.extractfile(m).read()))
        q.put(None)
    threading.Thread(target=reader, daemon=True).start()
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(24)
    done, batch, ids = 0, [], []

    def dec(b):
        return preprocess(Image.open(io.BytesIO(b)).convert("RGB"))

    def flush(ids, futs):
        x = torch.stack([f.result() for f in futs]).cuda().half()
        with torch.no_grad():
            f = F.normalize(model.encode_image(x).float(), dim=-1)
        X[ids] = f.cpu().numpy().astype(np.float16)
    while True:
        item = q.get()
        if item is None:
            break
        ids.append(item[0]); batch.append(pool.submit(dec, item[1]))
        if len(ids) == 256:
            flush(ids, batch); done += 256; ids, batch = [], []
            if done % 10240 == 0:
                note("inat-clip", f"{done}/{len(imgs)} images")
    if ids:
        flush(ids, batch); done += len(ids)
    np.save(CACHE / "clip_img.npy", X)
    note("inat-clip", f"done {done}/{len(imgs)} images")


def load():
    df = pd.read_parquet(CACHE / "images.parquet")
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    codes = {l: df[l].astype("category").cat.codes.values for l in (*LEVELS, "species")}
    return df, X, codes


def tree_targets(codes_t):
    same = {l: (codes_t[l][:, None] == codes_t[l][None, :]).float() for l in LEVELS}
    return {"order": same["order"],
            "family": torch.maximum(same["family"], 0.5 * same["order"]),
            "genus": torch.maximum(torch.maximum(same["genus"], 0.67 * same["family"]), 0.33 * same["order"])}


# ------------------------------------------------------------------ training
def train(method, seed, epochs=30, bs=2048, lr=1e-3):
    torch.manual_seed(seed)
    df, X, codes = load()
    tr = torch.tensor(np.flatnonzero(df.split.values == "train"))
    Xt = torch.tensor(X).cuda()
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
            T = tree_targets({l: C[l][idx] for l in LEVELS})[lvl]
            loss = loss + 10 * F.mse_loss(cos_matrix(z), T)
        if contrast:
            target = "genus" if method == "mrl" else lvl
            loss = loss + supcon(z, C[target][idx])
        return loss

    if method in ("tree", "main", "mrl", "treesc"):
        net = Projector(768, 768).cuda()
        opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
        for idx in batches():
            x = Xt[idx]; e = net(x)
            loss = F.mse_loss(cos_matrix(e), x @ x.T)
            for lvl in LEVELS:
                loss = loss + 0.5 * level_loss(e[:, :PREFIX[lvl]], lvl, idx)
            opt.zero_grad(); loss.backward(); opt.step()
        with torch.no_grad():
            E = net(Xt).cpu().numpy()
        out = {"full": E, **{l: E[:, :PREFIX[l]] for l in LEVELS}}
    elif method in ("b3", "b3sc"):
        out = {"full": X}
        for lvl in LEVELS:
            net = Projector(768, PREFIX[lvl], hidden=1024).cuda()
            opt = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=1e-4)
            for idx in batches():
                loss = level_loss(net(Xt[idx]), lvl, idx)
                opt.zero_grad(); loss.backward(); opt.step()
            with torch.no_grad():
                out[lvl] = net(Xt).cpu().numpy()
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
        with torch.no_grad():
            E = net(Xt); m = F.relu(masks)
            out = {"full": E.cpu().numpy(), **{l: (E * m[i]).cpu().numpy() for i, l in enumerate(LEVELS)}}
    np.savez(CACHE / f"{method}_s{seed}.npz", **out)
    print("saved", method, seed, "final loss", float(loss), flush=True)


# ------------------------------------------------------------------ evaluation
def b1_labels(X, df, codes, seed):
    """Classifiers for Order / Family / Genus on train images; vocabulary = labels seen in training."""
    torch.manual_seed(seed)
    tr = np.flatnonzero(df.split.values == "train")
    Xt = torch.tensor(X).cuda()
    pred = {}
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
    return pred


def evaluate(seed, nq=400):
    rng = np.random.default_rng(0)
    df, X, codes = load()
    res, md = {}, [f"# iNat results (seed {seed})\n"]
    embs = {}
    for lab, tag in (("SSE-tree", "tree"), ("SSE (yes/no levels)", "main"), ("SSE-treeSC", "treesc"),
                     ("SSE-MRL (genus everywhere)", "mrl")):
        if (CACHE / f"{tag}_s{seed}.npz").exists():
            embs[lab] = np.load(CACHE / f"{tag}_s{seed}.npz")["full"]
    tr = df.split.values == "train"
    mu = X[tr].mean(0); _, _, Vt = np.linalg.svd(X[tr][::4] - mu, full_matrices=False)
    embs["CLIP-PCA"] = (X - mu) @ Vt[:TAX_DIM].T

    # E2: prefix length sweep
    note("inat-E2", "started")
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
    md.append("### E2 — taxonomy prefix length vs level (mAP)\n")
    for split in ("seen_test", "unseen"):
        t = piv[piv.split == split].pivot_table(index=["method", "level"], columns="prefix_len", values="mAP").round(3)
        md.append(f"**{split}**\n\n" + t.to_markdown() + "\n")
    note("inat-E2", "done")

    # E2b: does each level's view keep coarser levels? (pair AUC), incl. B3 / CSN / B1 labels
    note("inat-E2b", "started")
    from sklearn.metrics import roc_auc_score
    db = np.flatnonzero(df.split.values != "train")
    a, b = rng.choice(db, 400_000), rng.choice(db, 400_000); k = a != b; a, b = a[k], b[k]
    tax = sum((codes[l][a] == codes[l][b]).astype(int) for l in LEVELS)
    views = {}
    for lab, tag in (("SSE-tree", "tree"), ("SSE (yes/no levels)", "main"), ("SSE-treeSC", "treesc"),
                     ("B3 separate (graded)", "b3"), ("B4 CSN (graded)", "csn"),
                     ("B3 separate (graded+contrastive)", "b3sc"), ("B4 CSN (graded+contrastive)", "csnsc")):
        p = CACHE / f"{tag}_s{seed}.npz"
        if p.exists():
            Z = np.load(p); views[lab] = {l: Z[l] for l in LEVELS}
    pred = b1_labels(X, df, codes, seed)
    rows = []
    for m, v in views.items():
        for lvl in LEVELS:
            s = Scorer((v[lvl], "cos")).pairs(a, b)
            rows.append({"method": m, "view": lvl, **{f"same-{l} AUC": float(roc_auc_score(tax >= t, s))
                                                      for t, l in ((1, "order"), (2, "family"), (3, "genus"))}})
    # B1 labels: graded agreement of predicted labels
    s = sum((pred[l][a] == pred[l][b]).astype(float) for l in LEVELS) + 1e-3 * (X[a] * X[b]).sum(1)
    rows.append({"method": "B1 labels", "view": "all levels", **{f"same-{l} AUC": float(roc_auc_score(tax >= t, s))
                                                                 for t, l in ((1, "order"), (2, "family"), (3, "genus"))}})
    s = (X[a] * X[b]).sum(1)
    rows.append({"method": "B6 plain CLIP", "view": "full", **{f"same-{l} AUC": float(roc_auc_score(tax >= t, s))
                                                               for t, l in ((1, "order"), (2, "family"), (3, "genus"))}})
    res["E2b"] = rows
    md.append(md_table(rows, ["method", "view", "same-order AUC", "same-family AUC", "same-genus AUC"],
                       "E2b — does each level's view keep its own and coarser levels? (pair AUC)"))
    # unseen-species slice for B1 vs SSE at family level
    note("inat-E2b", "done")

    # E3: general search — same-species mAP and overlap with CLIP
    note("inat-E3", "started")
    db = np.flatnonzero(df.split.values != "train")
    qs = rng.choice(db, 400, replace=False)
    base = Scorer((X, "cos")); rows = []
    for m in [k for k in embs if k.startswith("SSE")]:
        full = Scorer((embs[m], "cos")); ov, a1, a2 = [], [], []
        for q in qs:
            d = db[db != q]; s1, s2 = base(q, d), full(q, d); rel = codes["species"][d] == codes["species"][q]
            ov.append(len(set(d[np.argsort(-s1)[:10]]) & set(d[np.argsort(-s2)[:10]])) / 10)
            a1.append(ap(s1, rel)); a2.append(ap(s2, rel))
        rows.append({"method": m, "overlap@10_with_CLIP": float(np.mean(ov)),
                     "species_mAP_CLIP": float(np.nanmean(a1)), "species_mAP_SSE": float(np.nanmean(a2))})
    res["E3"] = rows
    md.append(md_table(rows, list(rows[0]), "E3 — general search preserved"))
    note("inat-E3", "done")

    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(res, indent=1))
    (out / "results.md").write_text("\n".join(md))
    print("\n".join(md))


def e6(seed, cls="Aves", n_tune=4000):
    """Roll-up / drill-down within ONE class (enough images per family/genus), both grouping rules.
    kappa tuned on TRAINING images of that class with ARI (NMI rewards all-singleton groupings)."""
    from sklearn.metrics import normalized_mutual_info_score as NMI, adjusted_rand_score as ARI
    from .e6_grouping import POLICY, KAPPAS, normed, describe
    rng = np.random.default_rng(0)
    df, X, codes = load()
    in_cls = df["class"].values == cls
    db = np.flatnonzero(in_cls & (df.split.values != "train"))
    tr_c = np.flatnonzero(in_cls & (df.split.values == "train"))
    tune = rng.choice(tr_c, min(n_tune, len(tr_c)), replace=False)
    methods = {"B6 plain CLIP": {l: X for l in LEVELS}}
    for lab, tag in (("SSE (yes/no levels)", "main"), ("SSE-tree", "tree"), ("SSE-treeSC", "treesc"),
                     ("B3 separate (graded+contrastive)", "b3sc"), ("B4 CSN (graded+contrastive)", "csnsc")):
        if (CACHE / f"{tag}_s{seed}.npz").exists():
            Z = np.load(CACHE / f"{tag}_s{seed}.npz"); methods[lab] = {l: Z[l] for l in LEVELS}
    methods = {m: {l: normed(v[l]) for l in LEVELS} for m, v in methods.items()}
    rows = []
    for policy in ("connected", "center"):
        for m, vs in methods.items():
            kap = {l: max((ARI(codes[l][tune], POLICY[policy](vs[l][tune], k)), k) for k in KAPPAS)[1] for l in LEVELS}
            labels = np.zeros(len(db), int)
            for l in LEVELS:
                new = np.zeros(len(db), int); nxt = 0
                for g in np.unique(labels):
                    idx = np.flatnonzero(labels == g)
                    sub = POLICY[policy](vs[l][db[idx]], kap[l]); new[idx] = sub + nxt; nxt += sub.max() + 1
                labels = new
                rows.append({"policy": policy, "method": m, "level": l, "kappa": float(kap[l]),
                             "n_true": int(len(np.unique(codes[l][db]))), **describe(codes[l][db], labels)})
            note("inat-E6", f"{cls} {policy} {m} done")
    out = OUT / f"seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / f"e6_{cls}.json").write_text(json.dumps(rows, indent=1))
    (out / f"e6_{cls}.md").write_text(md_table(rows, ["policy", "method", "level", "kappa", "n_groups", "n_main_groups",
                                               "n_true", "coverage", "NMI", "NMI_main", "ARI"],
                                        f"E6 — roll-up / drill-down within {cls} ({len(db)} test images; kappa tuned on training images by ARI)"))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["prep", "train", "eval", "e6"])
    p.add_argument("--method", default="tree")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--cls", default="Aves")
    a = p.parse_args()
    if a.cmd == "prep":
        prep()
    elif a.cmd == "train":
        train(a.method, a.seed)
    elif a.cmd == "eval":
        evaluate(a.seed)
    else:
        e6(a.seed, a.cls)
