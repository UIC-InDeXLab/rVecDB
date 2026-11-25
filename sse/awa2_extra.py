"""AwA2 extra experiments for the paper (2026-11-25).

groupk     GROUP BY_k (paper definition: k centers, each tuple joins its most similar center = spherical k-means)
           (a) habitat grouping, impact of k; (b) roll-up / drill-down Order > Family > Genus with k = true counts.
rep        Query Q4 of the paper: SELECT REP(g,5), COUNT(*) FROM Animals GROUP BY_k E_habitat  -> table + image grid.
agg        Query Q5 generalised: AVG / MAX of habitat similarity to a reference animal, per Order
           (Order membership from the Order prefix). Score: Spearman of the per-Order aggregates vs the truth.
blockeval  Block-size allocation: validation quality of a habitat / diet block of size d (models trained by
           scripts/run_awa2_extra.sh with SSE_VAL=1).  blocksummary picks d* with exponential vs dense candidates.
textq      Text references: "animals that live where a <species name> lives" — the reference is CLIP's TEXT
           embedding of the name, sent through the same SSE projector (after a mean modality-gap shift).

Usage: .venv/bin/python -m sse.awa2_extra groupk --seed 0  (rep | agg | textq | blockeval --tag ... | blocksummary)
"""
import argparse
import io
import json
import os
import zipfile

import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import adjusted_rand_score as ARI, normalized_mutual_info_score as NMI

from .awa2 import load_meta, CACHE, ROOT, ZIP_PATH
from .baselines import _train_probe, _predict
from .evaluate import truth, md_table, ap
from .taxonomy_awa2 import LEVELS, HABITAT_PREDICATES
from .e6_grouping import habitat_truth, normed

OUT = ROOT / os.environ.get("SSE_OUT_REL", "results/awa2")


def kmeans_groups(Z, k, seed=0, return_centers=False):
    import faiss
    Z = np.ascontiguousarray(normed(Z), dtype=np.float32)
    k = int(max(1, min(k, len(Z))))
    if k == 1:
        lab = np.zeros(len(Z), int)
        return (lab, Z.mean(0, keepdims=True)) if return_centers else lab
    km = faiss.Kmeans(Z.shape[1], k, niter=30, nredo=3, spherical=True, seed=seed, verbose=False, min_points_per_centroid=1)
    km.train(Z)
    lab = km.index.search(Z, 1)[1].ravel()
    return (lab, km.centroids) if return_centers else lab


def nested_k(views, levels, k_total, seed=0):
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


def methods_for(seed, with_b1=True):
    """Views per method: habitat, diet, order, family, genus, full."""
    img_df, cls_df = load_meta()
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    M = {}
    for lab, tag in (("SSE", f"tree_s{seed}"), ("SSE-treeSC", f"treesc_s{seed}")):
        if (CACHE / f"emb_{tag}.npy").exists():
            E = np.load(CACHE / f"emb_{tag}.npy"); L = json.loads((CACHE / f"emb_{tag}.json").read_text())["layout"]
            M[lab] = {"habitat": E[:, slice(*L["habitat"])], "diet": E[:, slice(*L["diet"])],
                      **{l: E[:, :L["prefix"][l]] for l in LEVELS}, "full": E}
    for lab, tag in (("B3 separate", f"b3tree_s{seed}"), ("B4 CSN", f"csntree_s{seed}")):
        if (CACHE / f"{tag}.npz").exists():
            Z = np.load(CACHE / f"{tag}.npz")
            M[lab] = {k: Z[k] for k in ("habitat", *LEVELS)} | {"diet": Z["diet"] if "diet" in Z else X, "full": X}
    M["B6 plain CLIP"] = {k: X for k in ("habitat", "diet", *LEVELS, "full")}
    return img_df, cls_df, X, M


def b1_predictions(X, img_df, cls_df, seed):
    """Predicted habitat yes/no pattern and predicted Order / Family / Genus (training vocabulary)."""
    import torch
    torch.manual_seed(seed)
    tr = img_df.split.values == "train"
    ci = img_df.cls.map({c: i for i, c in enumerate(cls_df.cls)}).values
    hab = np.stack(cls_df.habitat.values)[ci] >= 0.5
    p_hab = _predict(_train_probe(X[tr], hab[tr], True), X, True) >= 0.5
    pred = {"habitat": p_hab}
    for lvl in LEVELS:
        vocab = sorted(cls_df.loc[~cls_df.unseen, lvl].unique())
        y = img_df.cls.map(dict(zip(cls_df.cls, cls_df[lvl]))).values
        y_tr = np.array([vocab.index(v) for v in y[tr]])
        pred[lvl] = _predict(_train_probe(X[tr], y_tr, False), X, False).argmax(1)
    return pred


def _db(img_df, n=6000):
    rng = np.random.default_rng(0)
    db = np.flatnonzero(img_df.split.values != "train")
    return np.sort(rng.choice(db, min(n, len(db)), replace=False))


def _codes(labels):
    return np.unique(labels, axis=0, return_inverse=True)[1].ravel()


# ------------------------------------------------------------------ GROUP BY_k
def groupk(seed):
    img_df, cls_df, X, M = methods_for(seed)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    hab_true = habitat_truth(cls_df)[c]
    tax = {l: cls_df[l].astype("category").cat.codes.values[c] for l in LEVELS}
    db = _db(img_df)
    pred = b1_predictions(X, img_df, cls_df, seed)
    k_true = int(len(np.unique(hab_true[db])))
    rows = []
    for k in sorted({2, 3, 4, 6, 8, 12, 16, k_true}):
        for m, v in M.items():
            g = kmeans_groups(v["habitat"][db], k, seed)
            rows.append({"part": "habitat, impact of k", "method": m, "level": "habitat", "k": k, "k_true": k_true,
                         "NMI": float(NMI(hab_true[db], g)), "ARI": float(ARI(hab_true[db], g))})
    g = _codes(pred["habitat"][db])
    rows.append({"part": "habitat, impact of k", "method": "B1 labels (predicted yes/no pattern)", "level": "habitat",
                 "k": int(g.max() + 1), "k_true": k_true, "NMI": float(NMI(hab_true[db], g)), "ARI": float(ARI(hab_true[db], g))})
    n_true = [int(len(np.unique(tax[l][db]))) for l in LEVELS]
    for m, v in M.items():
        parts = nested_k({l: v[l][db] for l in LEVELS}, LEVELS, n_true, seed)
        for l, kt in zip(LEVELS, n_true):
            rows.append({"part": "roll-up / drill-down", "method": m, "level": l, "k": kt, "k_true": kt,
                         "NMI": float(NMI(tax[l][db], parts[l])), "ARI": float(ARI(tax[l][db], parts[l]))})
    for l, kt in zip(LEVELS, n_true):
        g = pred[l][db]
        rows.append({"part": "roll-up / drill-down", "method": "B1 labels (predicted)", "level": l, "k": int(len(np.unique(g))),
                     "k_true": kt, "NMI": float(NMI(tax[l][db], g)), "ARI": float(ARI(tax[l][db], g))})
    # unseen species only: labels cannot name them
    un = db[img_df.split.values[db] == "unseen"]
    for l in ("family", "genus"):
        kt = int(len(np.unique(tax[l][un])))
        for m, v in M.items():
            g = kmeans_groups(v[l][un], kt, seed)
            rows.append({"part": "unseen species", "method": m, "level": l, "k": kt, "k_true": kt,
                         "NMI": float(NMI(tax[l][un], g)), "ARI": float(ARI(tax[l][un], g))})
        g = pred[l][un]
        rows.append({"part": "unseen species", "method": "B1 labels (predicted)", "level": l, "k": int(len(np.unique(g))),
                     "k_true": kt, "NMI": float(NMI(tax[l][un], g)), "ARI": float(ARI(tax[l][un], g))})
    out = OUT / f"x_seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "groupk.json").write_text(json.dumps(rows, indent=1))
    (out / "groupk.md").write_text(md_table(rows, ["part", "method", "level", "k", "k_true", "NMI", "ARI"],
                                            f"GROUP BY_k on AwA2 ({len(db)} test images)"))
    print((out / "groupk.md").read_text())


# ------------------------------------------------------------------ Q4: REP(g, h)
def rep(seed=0, h=5, k=None):
    img_df, cls_df, X, M = methods_for(seed)
    v = M["SSE"]
    c = img_df.cls.map({kk: i for i, kk in enumerate(cls_df.cls)}).values
    hab_true = habitat_truth(cls_df)[c]
    db = _db(img_df)
    k = k or int(len(np.unique(hab_true[db])))
    g, centers = kmeans_groups(v["habitat"][db], k, seed, return_centers=True)
    H = np.stack(cls_df.habitat.values)
    groups = []
    for gi in np.argsort(-np.bincount(g, minlength=k)):
        mem = db[g == gi]
        sub, sc = kmeans_groups(v["full"][mem], min(h, len(mem)), seed, return_centers=True)
        reps = []
        Zf = normed(v["full"][mem])
        for si in np.argsort(-np.bincount(sub, minlength=sc.shape[0])):
            idx = np.flatnonzero(sub == si)
            if not len(idx):
                continue
            med = idx[np.argmax(Zf[idx] @ normed(sc[si:si + 1]).ravel())]
            reps.append({"img": int(mem[med]), "cls": cls_df.cls[c[mem[med]]], "count": int(len(idx))})
        top = H[c[mem]].mean(0).argsort()[::-1][:3]
        species = np.bincount(c[mem], minlength=len(cls_df))
        groups.append({"group": int(gi), "size": int(len(mem)), "habitat (true avg, top 3)": ", ".join(HABITAT_PREDICATES[t] for t in top),
                       "top species": ", ".join(f"{cls_df.cls[s]} ({species[s]})" for s in species.argsort()[::-1][:4] if species[s]),
                       "unseen species share": float(img_df.split.values[mem].__eq__("unseen").mean()),
                       "REP": reps})
    out = OUT / "x_rep"; out.mkdir(parents=True, exist_ok=True)
    (out / "rep.json").write_text(json.dumps(groups, indent=1))
    md = [f"### Q4: SELECT REP(g,{h}), COUNT(*) FROM Animals GROUP BY_{k} E_habitat  (SSE, seed {seed}, {len(db)} test images)", "",
          "| group | COUNT(*) | true habitat (avg, top 3) | REP(g,5): medoid species (count) | top species in group |", "|---|---|---|---|---|"]
    for G in groups:
        md.append(f"| {G['group']} | {G['size']} | {G['habitat (true avg, top 3)']} | "
                  + "; ".join(f"{r['cls']} ({r['count']})" for r in G["REP"]) + f" | {G['top species']} |")
    (out / "rep.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    try:
        _rep_figure(groups, img_df, out / "rep.png", h)
    except Exception as e:                                  # figure is a nice-to-have
        print("figure failed:", e)


def _rep_figure(groups, img_df, path, h, tile=160):
    from PIL import Image, ImageDraw
    zf = zipfile.ZipFile(ZIP_PATH)
    W, Hh = 220 + h * tile, len(groups) * (tile + 24)
    canvas = Image.new("RGB", (W, Hh), "white"); d = ImageDraw.Draw(canvas)
    for r, G in enumerate(groups):
        y = r * (tile + 24)
        d.text((6, y + 6), f"group {G['group']}  n={G['size']}", fill="black")
        for i, w in enumerate(G["habitat (true avg, top 3)"].split(", ")):
            d.text((6, y + 26 + 16 * i), w, fill=(60, 60, 160))
        for j, R in enumerate(G["REP"][:h]):
            im = Image.open(io.BytesIO(zf.read(img_df.path.values[R["img"]]))).convert("RGB")
            im.thumbnail((tile - 8, tile - 8))
            canvas.paste(im, (220 + j * tile, y + 4))
            d.text((220 + j * tile, y + tile - 2), f"{R['cls'].replace('+', ' ')} ({R['count']})", fill="black")
    canvas.save(path)
    print("saved", path)


# ------------------------------------------------------------------ Q5: aggregates
def agg(seed, n_ref=300):
    """For a reference image r and each training Order o: AVG and MAX over {t : Order prefix of t is closest to the
    prototype of o} of sim_habitat(t, r). Truth uses true Orders and true habitat similarity. Score per reference =
    Spearman over Orders (does the method rank the Orders by 'how much they live like r' correctly?)."""
    img_df, cls_df, X, M = methods_for(seed)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    T = truth(cls_df)
    db = _db(img_df)
    tr = img_df.split.values == "train"
    orders = sorted(cls_df.order[~cls_df.unseen].unique())
    o_img = cls_df.order.values[c]
    o_true = np.array([orders.index(o) if o in orders else -1 for o in o_img[db]])
    keep = [i for i in range(len(orders)) if (o_true == i).sum() >= 20]
    pred = b1_predictions(X, img_df, cls_df, seed)
    vocab_o = sorted(cls_df.loc[~cls_df.unseen, "order"].unique())
    rng = np.random.default_rng(0)
    refs = rng.choice(db, n_ref, replace=False)
    res = {}
    for m, v in list(M.items()) + [("B1 labels", None)]:
        if v is None:
            memb = np.array([orders.index(vocab_o[p]) for p in pred["order"][db]])
            Hb = pred["habitat"].astype(np.float32)
            def hs(r):
                inter = Hb[db] @ Hb[r]; union = Hb[db].sum(1) + Hb[r].sum() - inter
                return np.where(union > 0, inter / np.maximum(union, 1e-8), 1.0)
        else:
            Zo = normed(v["order"]); P = normed(np.stack([Zo[tr & (o_img == o)].mean(0) for o in orders]))
            memb = (Zo[db] @ P.T).argmax(1)
            Zh = normed(v["habitat"])
            hs = lambda r, Zh=Zh: Zh[db] @ Zh[r]
        sp_avg, sp_max, top1 = [], [], []
        for r in refs:
            s_true = T["habitat"][c[r], c[db]]; s = hs(r)
            ta = [s_true[o_true == i].mean() for i in keep]; tm = [s_true[o_true == i].max() for i in keep]
            ea = [s[memb == i].mean() if (memb == i).any() else -1 for i in keep]
            em = [s[memb == i].max() if (memb == i).any() else -1 for i in keep]
            sp_avg.append(spearmanr(ta, ea).correlation); sp_max.append(spearmanr(tm, em).correlation)
            top1.append(int(np.argmax(ta) == np.argmax(ea)))
        res[m] = {"method": m, "Spearman AVG": float(np.nanmean(sp_avg)), "Spearman MAX": float(np.nanmean(sp_max)),
                  "top Order correct (AVG)": float(np.mean(top1)),
                  "Order membership acc": float((memb == o_true)[o_true >= 0].mean())}
    rows = list(res.values())
    out = OUT / f"x_seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "agg.json").write_text(json.dumps(rows, indent=1))
    (out / "agg.md").write_text(md_table(rows, ["method", "Spearman AVG", "Spearman MAX", "top Order correct (AVG)", "Order membership acc"],
                                         f"Q5 aggregates per Order: AVG/MAX habitat similarity to a reference ({n_ref} references, {len(keep)} Orders)"))
    print((out / "agg.md").read_text())


# ------------------------------------------------------------------ block-size allocation
def blockeval(tag, n_pairs=200_000, nq=300):
    """Validation quality (SSE_VAL=1) of the habitat and diet blocks of model emb_<tag>:
    Spearman with the true facet similarity over random pairs, and the habitat filter F1 (as in Q4)."""
    assert os.environ.get("SSE_VAL") == "1", "run with SSE_VAL=1"
    img_df, cls_df = load_meta()
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    T = truth(cls_df)
    db = np.flatnonzero(np.isin(img_df.split.values, ["seen_test", "unseen"]))
    E = np.load(CACHE / f"emb_{tag}.npy"); L = json.loads((CACHE / f"emb_{tag}.json").read_text())["layout"]
    rng = np.random.default_rng(0)
    a, b = rng.choice(db, n_pairs), rng.choice(db, n_pairs)
    r = {"tag": tag, "hab_dim": L["habitat"][1] - L["habitat"][0], "diet_dim": L["diet"][1] - L["diet"][0]}
    for f in ("habitat", "diet"):
        Z = normed(E[:, slice(*L[f])])
        r[f"{f}_spearman"] = float(spearmanr((Z[a] * Z[b]).sum(1), T[f][c[a], c[b]]).correlation)
    Zh = normed(E[:, slice(*L["habitat"])])
    f1 = []
    for x in rng.choice(db, nq, replace=False):
        ts = T["habitat"][c[x], c[db]]; F_true = ts >= np.quantile(ts, 0.75); n = int(F_true.sum())
        s = Zh[db] @ Zh[x]; Mk = np.zeros(len(db), bool); Mk[np.argsort(-s, kind="stable")[:n]] = True
        f1.append((Mk & F_true).sum() / n)
    r["habitat_filter_F1"] = float(np.mean(f1))
    out = ROOT / "results/awa2/x_blocksize"; out.mkdir(parents=True, exist_ok=True)
    (out / f"{tag}.json").write_text(json.dumps(r))
    print(r)


def blocksummary(eps=0.01):
    import pandas as pd
    d = pd.DataFrame([json.loads(p.read_text()) for p in (ROOT / "results/awa2/x_blocksize").glob("*.json")])
    d["seed"] = d.tag.str.extract(r"_s(\d)$").astype(int)
    d["facet"] = np.where(d.tag.str.startswith("bs_hab"), "habitat", "diet")
    md = ["# Block-size allocation (validation split; 3 seeds)", "",
          f"d* = smallest candidate whose quality is within eps = {eps} of the best candidate. "
          "Exponential candidates: powers of two; dense: every size trained.", ""]
    for facet, metric in (("habitat", "habitat_spearman"), ("habitat", "habitat_filter_F1"), ("diet", "diet_spearman")):
        s = d[d.facet == facet]
        dimcol = "hab_dim" if facet == "habitat" else "diet_dim"
        g = s.groupby(dimcol)[metric].agg(["mean", "min", "max"]).reset_index()
        md += [f"## {facet} — {metric}", "", "| d | mean | spread |", "|---|---|---|"]
        md += [f"| {int(r[dimcol])} | {r['mean']:.3f} | ±{(r['max'] - r['min']) / 2:.3f} |" for _, r in g.iterrows()]
        best = g["mean"].max()
        dense = g[g["mean"] >= best - eps][dimcol].min()
        pw = g[g[dimcol].isin([2 ** i for i in range(10)])]
        expo = pw[pw["mean"] >= pw["mean"].max() - eps][dimcol].min()
        q = dict(zip(g[dimcol], g["mean"]))
        md += ["", f"- dense search: d* = {int(dense)} (quality {q[dense]:.3f}); exponential search: d* = {int(expo)} "
               f"(quality {q[expo]:.3f}); best overall {best:.3f}; trainings: dense {len(g)}, exponential {len(pw)}", ""]
    (ROOT / "results/awa2/x_blocksize.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


# ------------------------------------------------------------------ text references
def textq(seed, frac=0.25):
    """Habitat filter with a TEXT reference (species name) vs an IMAGE reference, for every species.
    Truth (as in Q4): images whose true habitat similarity to the reference species is in the top `frac`."""
    import torch
    from .train_sse import Projector
    img_df, cls_df = load_meta()
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    T = truth(cls_df)
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    TX = np.load(CACHE / "clip_text.npz")["species"].astype(np.float32)
    tr = img_df.split.values == "train"
    db = _db(img_df)
    tag = f"tree_s{seed}"
    L = json.loads((CACHE / f"emb_{tag}.json").read_text())["layout"]
    E = np.load(CACHE / f"emb_{tag}.npy")
    net = Projector(768, E.shape[1]); net.load_state_dict(torch.load(CACHE / f"emb_{tag}.pt", map_location="cpu")); net.eval()
    # modality gap: shift text features so their mean matches the mean training image feature, then re-normalise
    TXs = normed(TX - TX.mean(0) + X[tr].mean(0))
    with torch.no_grad():
        Et = net(torch.tensor(TXs)).numpy()
    hab = slice(*L["habitat"])
    Zi, Zt = normed(E[:, hab]), normed(Et[:, hab])
    Xn = normed(X)
    rng = np.random.default_rng(seed)
    rows = []
    for s in range(len(cls_df)):
        ts = T["habitat"][s, c[db]]; F_true = ts >= np.quantile(ts, 1 - frac); n = int(F_true.sum())
        ref_img = rng.choice(np.flatnonzero(c == s))
        scores = {"SSE, text reference": Zi[db] @ Zt[s], "SSE, image reference": Zi[db] @ Zi[ref_img],
                  "CLIP, text reference": Xn[db] @ normed(TX[s:s + 1]).ravel(), "CLIP, image reference": Xn[db] @ Xn[ref_img]}
        for m, sc in scores.items():
            Mk = np.zeros(len(db), bool); Mk[np.argsort(-sc, kind="stable")[:n]] = True
            rows.append({"method": m, "species": cls_df.cls[s], "unseen": bool(cls_df.unseen[s]),
                         "F1": float((Mk & F_true).sum() / n), "AP": ap(sc, F_true)})
    import pandas as pd
    d = pd.DataFrame(rows)
    summ = []
    for m in d.method.unique():
        for sl, f in (("all species", lambda x: x), ("unseen species", lambda x: x[x.unseen]), ("seen species", lambda x: x[~x.unseen])):
            x = f(d[d.method == m]); summ.append({"method": m, "slice": sl, "n": len(x), "F1": float(x.F1.mean()), "AP": float(x.AP.mean())})
    out = OUT / f"x_seed{seed}"; out.mkdir(parents=True, exist_ok=True)
    (out / "textq.json").write_text(json.dumps(summ, indent=1))
    (out / "textq.md").write_text(md_table(summ, ["method", "slice", "n", "F1", "AP"],
                                           f"Habitat filter with a text vs image reference ({len(db)} test images, top {frac:.0%} = true)"))
    print((out / "textq.md").read_text())


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["groupk", "rep", "agg", "blockeval", "blocksummary", "textq"])
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--tag", default="")
    a = p.parse_args()
    if a.cmd == "blockeval":
        blockeval(a.tag)
    elif a.cmd == "blocksummary":
        blocksummary()
    elif a.cmd == "rep":
        rep(a.seed)
    else:
        {"groupk": groupk, "agg": agg, "textq": textq}[a.cmd](a.seed)
