"""Do the GROUP BY_4 habitat groups of the Q4 figure make sense? (AwA2 test images, SSE seed 0)

1. Species split: how many species are spread over >1 group (each species has ONE true habitat profile).
2. Agreement with the true habitat groups (species habitat-score clustering, as in E6): NMI / ARI.
3. Quality inside the embedding: cosine silhouette and the k-means objective.
4. Alternatives on the same block: k-means with many restarts, average-linkage, species-level k-means, other k.
Usage: .venv/bin/python -m sse.rep_check
"""
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import adjusted_rand_score as ARI, normalized_mutual_info_score as NMI, silhouette_score

from .awa2_extra import methods_for, _db, kmeans_groups
from .e6_grouping import habitat_truth, normed
from .taxonomy_awa2 import HABITAT_PREDICATES


def km(Z, k, seed=0, nredo=3):
    import faiss
    Z = np.ascontiguousarray(normed(Z), dtype=np.float32)
    m = faiss.Kmeans(Z.shape[1], k, niter=50, nredo=nredo, spherical=True, seed=seed, verbose=False, min_points_per_centroid=1)
    m.train(Z)
    lab = m.index.search(Z, 1)[1].ravel()
    C = normed(m.centroids)
    return lab, float((Z * C[lab]).sum(1).mean())          # mean cosine to own center (objective)


def report(name, lab, Z, truth, sp, rng):
    s = rng.choice(len(Z), 3000, replace=False)
    split = sum(len(np.unique(lab[sp == x])) > 1 and np.bincount(lab[sp == x]).max() < 0.9 * (sp == x).sum() for x in np.unique(sp))
    C = normed(np.stack([Z[lab == g].mean(0) for g in np.unique(lab)]))
    obj = float((Z * C[np.searchsorted(np.unique(lab), lab)]).sum(1).mean())
    print(f"{name:42s} k={len(np.unique(lab)):2d}  NMI {NMI(truth, lab):.3f}  ARI {ARI(truth, lab):.3f}  "
          f"silhouette {silhouette_score(Z[s], lab[s], metric='cosine'):.3f}  objective {obj:.4f}  "
          f"species split (>10% elsewhere) {split}", flush=True)


def main():
    rng = np.random.default_rng(0)
    img_df, cls_df, X, M = methods_for(0)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    db = _db(img_df)
    truth_all = habitat_truth(cls_df)
    truth = truth_all[c[db]]
    sp = c[db]
    Z = normed(M["SSE"]["habitat"][db])
    print(f"\n{len(db)} test images, {len(np.unique(sp))} species, true habitat groups: {len(np.unique(truth))}\n")

    lab_fig = kmeans_groups(Z, 4, 0)                        # what the figure used (nredo=3)
    report("figure: k-means k=4 (nredo 3)", lab_fig, Z, truth, sp, rng)
    report("truth: species habitat-score groups", truth, Z, truth, sp, rng)
    best = None
    for seed in range(10):
        lab, obj = km(Z, 4, seed, nredo=10)
        if best is None or obj > best[1]:
            best = (lab, obj, seed)
    report(f"k-means k=4, best of 10x10 restarts (seed {best[2]})", best[0], Z, truth, sp, rng)
    for link in ("average", "complete"):
        lab = AgglomerativeClustering(n_clusters=4, metric="cosine", linkage=link).fit_predict(Z)
        report(f"agglomerative {link}, k=4", lab, Z, truth, sp, rng)
    # species-level: cluster the 40-50 species centroids (each species stays whole)
    S = np.unique(sp)
    Cs = normed(np.stack([Z[sp == x].mean(0) for x in S]))
    for k in (3, 4, 5, 6):
        ls, _ = km(Cs, k, 0, nredo=20)
        lab = ls[np.searchsorted(S, sp)]
        report(f"k-means on species centroids, k={k}", lab, Z, truth, sp, rng)
    for k in (3, 5, 6):
        lab, _ = km(Z, k, 0, nredo=10)
        report(f"k-means images, k={k}", lab, Z, truth, sp, rng)

    print("\nSpecies spread over >1 group in the figure's grouping (share in the main group):")
    for x in S:
        b = np.bincount(lab_fig[sp == x], minlength=4)
        if b.max() < 0.9 * b.sum():
            print(f"  {cls_df.cls[x]:20s} {b.tolist()}  true group {truth_all[x]}")
    print("\nTrue habitat groups (species):")
    for g in np.unique(truth_all):
        mem = cls_df.cls[truth_all == g].tolist()
        print(f"  {g}: {mem}")
    print("\nFigure groups (species with >=10% of their images):")
    for g in range(4):
        b = np.bincount(sp[lab_fig == g], minlength=len(cls_df))
        print(f"  G{g}: " + ", ".join(f"{cls_df.cls[x]}({b[x]})" for x in b.argsort()[::-1] if b[x] >= 0.1 * (sp == x).sum()))


if __name__ == "__main__":
    main()
