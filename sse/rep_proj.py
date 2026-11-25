"""Which 2-D projection shows the GROUP BY_4 habitat groups faithfully? Renders candidates side by side and scores
how well each keeps the groups apart in 2-D (silhouette of the group labels in the projection) and how well it keeps
the original between-species distances (Spearman of species-centroid distances, 2-D vs 32-D).
Usage: .venv/bin/python -m sse.rep_proj   -> results/awa2/x_rep/projections.png"""
import numpy as np
from scipy.stats import spearmanr
from scipy.spatial.distance import pdist
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score

from .awa2 import ROOT
from .awa2_extra import methods_for, _db, kmeans_groups
from .e6_grouping import normed


def main():
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    img_df, cls_df, X, M = methods_for(0)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    db = _db(img_df); sp = c[db]
    Z = normed(M["SSE"]["habitat"][db]); g = kmeans_groups(Z, 4, 0)
    S = np.unique(sp); Cz = normed(np.stack([Z[sp == x].mean(0) for x in S]))
    cand = {"PCA": PCA(2, random_state=0).fit_transform(Z),
            "t-SNE perplexity 50 (current)": TSNE(2, perplexity=50, metric="cosine", init="pca", random_state=0).fit_transform(Z),
            "t-SNE perplexity 500": TSNE(2, perplexity=500, metric="cosine", init="pca", random_state=0).fit_transform(Z)}
    try:
        import umap
        cand["UMAP (n_neighbors 200)"] = umap.UMAP(n_neighbors=200, min_dist=0.3, metric="cosine", random_state=0).fit_transform(Z)
    except ImportError:
        pass
    rng = np.random.default_rng(0); s = rng.choice(len(Z), 3000, replace=False)
    fig, axs = plt.subplots(1, len(cand), figsize=(4 * len(cand), 4))
    for ax, (name, Y) in zip(axs, cand.items()):
        C2 = np.stack([Y[sp == x].mean(0) for x in S])
        rho = spearmanr(pdist(C2), pdist(Cz, metric="cosine")).correlation
        sil = silhouette_score(Y[s], g[s])
        print(f"{name:32s} group silhouette in 2-D {sil:.3f}   species-distance Spearman {rho:.3f}", flush=True)
        ax.scatter(Y[:, 0], Y[:, 1], c=g, s=1, cmap="tab10", vmin=0, vmax=9, rasterized=True)
        ax.set_title(f"{name}\nsil {sil:.2f}, global rho {rho:.2f}", fontsize=9); ax.set_xticks([]); ax.set_yticks([])
    fig.savefig(ROOT / "results/awa2/x_rep/projections.png", dpi=110, bbox_inches="tight")


if __name__ == "__main__":
    main()
