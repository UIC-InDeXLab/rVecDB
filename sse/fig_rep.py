"""Paper figure for query Q4: SELECT REP(g,5), COUNT(*) FROM Animals GROUP BY_k E_habitat  (AwA2 test images, SSE seed 0).

Top: PCA of the habitat block, coloured by GROUP BY_k group (the clusters the query found); the 5 REP medoids of
each group are ringed. Bottom: one row per group: name (true top habitat properties of its members, for reference),
COUNT(*), and REP(g,5) = medoid image of each subgroup with the number of tuples it represents.

Usage: .venv/bin/python -m sse.fig_rep [--fonts cache/fonts] [--out results/awa2/x_rep/rep_figure]
Writes <out>.pdf, <out>.png and <out>.jpg (the paper includes figs/rep_habitat.jpg).
"""
import argparse
import io
import zipfile
from pathlib import Path

import numpy as np

from .awa2 import ZIP_PATH, ROOT
from .awa2_extra import methods_for, _db, kmeans_groups
from .e6_grouping import normed
from .taxonomy_awa2 import HABITAT_PREDICATES

# Okabe-Ito (colour-blind safe), assigned by meaning so that colours read naturally
COL = {"water": "#0072B2", "forest": "#009E73", "plains": "#E69F00", "jungle": "#D55E00", "other": "#CC79A7"}


def colour_for(words):
    w = set(words)
    if w & {"water", "ocean", "coastal", "arctic"}:
        return COL["water"]
    if w & {"jungle", "bush"}:
        return COL["jungle"]
    if w & {"forest", "tree"}:
        return COL["forest"]
    if w & {"plains", "fields", "ground", "desert"}:
        return COL["plains"]
    return COL["other"]


def square(img, size=320):
    w, h = img.size
    s = min(w, h)
    img = img.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
    return img.resize((size, size))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", default=str(ROOT / "cache/fonts"))
    ap.add_argument("--out", default=str(ROOT / "results/awa2/x_rep/rep_figure"))
    ap.add_argument("--h", type=int, default=5)
    a = ap.parse_args()

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    from matplotlib.patches import FancyBboxPatch
    from PIL import Image
    from sklearn.decomposition import PCA

    fam = "DejaVu Sans"
    for f in Path(a.fonts).glob("*.otf"):
        font_manager.fontManager.addfont(str(f))
        fam = "Linux Biolinum O"
    plt.rcParams.update({"font.family": fam, "font.size": 7, "axes.linewidth": 0.6,
                         "pdf.fonttype": 42, "savefig.dpi": 400})

    img_df, cls_df, X, M = methods_for(0)
    v = M["SSE"]
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    db = _db(img_df)
    H = normed(v["habitat"][db])
    g, _ = kmeans_groups(H, 4, 0, return_centers=True)
    Hs = np.stack(cls_df.habitat.values)

    groups = []
    for gi in np.argsort(-np.bincount(g, minlength=4)):
        idx = np.flatnonzero(g == gi)
        mem = db[idx]
        sub, sc = kmeans_groups(v["full"][mem], min(a.h, len(mem)), 0, return_centers=True)
        Zf = normed(v["full"][mem])
        reps = []
        for si in np.argsort(-np.bincount(sub, minlength=sc.shape[0])):
            s_idx = np.flatnonzero(sub == si)
            if len(s_idx):
                med = s_idx[np.argmax(Zf[s_idx] @ normed(sc[si:si + 1]).ravel())]
                reps.append({"pos": int(idx[med]), "img": int(mem[med]), "cls": cls_df.cls[c[mem[med]]], "count": int(len(s_idx))})
        top = [HABITAT_PREDICATES[t] for t in Hs[c[mem]].mean(0).argsort()[::-1][:3]]
        groups.append({"idx": idx, "size": len(idx), "words": top, "reps": reps, "colour": colour_for(top[:2])})

    # PCA, not t-SNE: t-SNE (perplexity 50) breaks every species into its own blob and scatters them, which hides the
    # groups (2-D silhouette 0.29, species-distance Spearman 0.67 vs 0.51 / 0.93 for PCA; see sse.rep_proj)
    Y = PCA(n_components=2, random_state=0).fit_transform(H)

    zf = zipfile.ZipFile(ZIP_PATH)
    thumbs = {r["img"]: square(Image.open(io.BytesIO(zf.read(img_df.path.values[r["img"]]))).convert("RGB"))
              for G in groups for r in G["reps"]}

    # ---------------- layout (ACM single column: 3.33 in) ----------------
    W, n = 3.33, len(groups)
    lab_w, gap = 0.80, 0.035
    th = (W - lab_w - 0.04 - (a.h - 1) * gap) / a.h           # thumbnail side (in)
    row_h = th + 0.19
    map_h = 1.75
    Ht = map_h + 0.12 + n * row_h + 0.02
    fig = plt.figure(figsize=(W, Ht))

    # t-SNE map
    ax = fig.add_axes([0.0, 1 - map_h / Ht, 1.0, (map_h - 0.13) / Ht])
    for k, G in enumerate(groups):
        p = Y[G["idx"]]
        ax.scatter(p[:, 0], p[:, 1], s=1.4, c=G["colour"], alpha=0.45, linewidths=0, rasterized=True)
    placed = []
    for k, G in enumerate(groups):
        P = Y[[r["pos"] for r in G["reps"]]]
        ax.scatter(P[:, 0], P[:, 1], s=16, facecolors=G["colour"], edgecolors="black", linewidths=0.6, zorder=3)
        # label: a spot near the group's median that keeps clear of every ringed medoid and of other labels
        rng_ = Y.max(0) - Y.min(0); m = np.median(Y[G["idx"]], axis=0)
        allP = np.vstack([Y[[r["pos"] for r in GG["reps"]]] for GG in groups] + ([np.array(placed)] if placed else []))
        best = None
        for ang in np.linspace(0, 2 * np.pi, 24, endpoint=False):
            for rad in (0.08, 0.13, 0.18):
                q = np.clip(m + rad * rng_ * np.array([np.cos(ang), np.sin(ang)]), Y.min(0) + 0.07 * rng_, Y.max(0) - 0.07 * rng_)
                clear = np.min(np.linalg.norm((allP - q) / rng_, axis=1))
                score = clear - 0.3 * rad
                if best is None or score > best[0]:
                    best = (score, q)
        cx, cy = best[1]; placed.append(best[1])
        ax.text(cx, cy, f"G{k + 1}", ha="center", va="center", fontsize=8, fontweight="bold", color=G["colour"], zorder=4,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=G["colour"], lw=0.8, alpha=0.95))
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color("#999999")
    ax.set_title("Habitat block of 6,000 test images (PCA), coloured by group", fontsize=6.8, color="#333333",
                 pad=2.5, loc="left")
    ax.text(0.99, 0.02, "ringed: REP(g,5) medoids", transform=ax.transAxes, ha="right", va="bottom", fontsize=6, color="#555555")

    # REP rows
    y0 = 1 - (map_h + 0.12) / Ht
    for k, G in enumerate(groups):
        top = y0 - k * row_h / Ht
        bot = top - row_h / Ht
        band = fig.add_axes([0.0, bot + 0.07 / Ht, lab_w / W, (th + 0.09) / Ht])
        band.axis("off")
        band.add_patch(FancyBboxPatch((0.02, 0.06), 0.96, 0.88, boxstyle="round,pad=0,rounding_size=0.06",
                                      fc=G["colour"], ec="none", alpha=0.13, transform=band.transAxes))
        band.add_patch(FancyBboxPatch((0.02, 0.06), 0.045, 0.88, boxstyle="square,pad=0", fc=G["colour"], ec="none",
                                      transform=band.transAxes))
        band.text(0.13, 0.86, f"G{k + 1}", fontsize=8.5, fontweight="bold", color=G["colour"], va="top", transform=band.transAxes)
        band.text(0.13, 0.60, "\n".join(G["words"]), fontsize=5.7, color="#222222", va="top", linespacing=1.0,
                  transform=band.transAxes)
        band.text(0.95, 0.86, f"n={G['size']:,}", fontsize=6.0, color="#444444", ha="right", va="top", transform=band.transAxes)
        for j, r in enumerate(G["reps"][:a.h]):
            x = (lab_w + 0.04 + j * (th + gap)) / W
            ia = fig.add_axes([x, bot + 0.15 / Ht, th / W, th / Ht])
            ia.imshow(thumbs[r["img"]]); ia.set_xticks([]); ia.set_yticks([])
            for sp in ia.spines.values():
                sp.set_color(G["colour"]); sp.set_linewidth(1.0)
            name = r["cls"].replace("+", " ")
            fig.text(x + th / W / 2, bot + 0.13 / Ht, name, ha="center", va="top", fontsize=5.6, color="#222222")
            ia.text(0.97, 0.03, f"×{r['count']}", transform=ia.transAxes, ha="right", va="bottom", fontsize=5.4,
                    color="white", fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.15", fc="black", ec="none", alpha=0.55))

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".pdf"))
    fig.savefig(out.with_suffix(".png"))
    Image.open(out.with_suffix(".png")).convert("RGB").save(out.with_suffix(".jpg"), quality=93, optimize=True)
    print("saved", out.with_suffix(".pdf"), out.with_suffix(".jpg"))


if __name__ == "__main__":
    main()
