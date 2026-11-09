# AwA2 results val_seed1

args: `{'sse': 'SSE=val_main_s1,SSE-tree=val_tree_s1,SSE-treeSC=val_treesc_s1', 'mrl': '', 'out': 'val_seed1', 'no_baselines': True, 'extra': '', 'seed': 1}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.665 | 0.353 | 0.314 |
| SSE | diet | 0.480 | 0.834 | 0.502 |
| SSE | family | 0.355 | 0.278 | 0.548 |
| SSE | tax | 0.382 | 0.320 | 0.495 |
| SSE | rest | 0.134 | 0.159 | 0.195 |
| SSE | full | 0.257 | 0.311 | 0.334 |
| SSE-tree | habitat | 0.674 | 0.358 | 0.314 |
| SSE-tree | diet | 0.482 | 0.835 | 0.502 |
| SSE-tree | family | 0.276 | 0.366 | 0.719 |
| SSE-tree | tax | 0.295 | 0.378 | 0.709 |
| SSE-tree | rest | 0.135 | 0.161 | 0.187 |
| SSE-treeSC | habitat | 0.673 | 0.358 | 0.314 |
| SSE-treeSC | diet | 0.481 | 0.835 | 0.501 |
| SSE-treeSC | family | 0.272 | 0.359 | 0.708 |
| SSE-treeSC | tax | 0.292 | 0.376 | 0.697 |
| SSE-treeSC | rest | 0.143 | 0.162 | 0.190 |

### E3 — general search preserved

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE | 0.857 | 0.801 | 0.821 |
| SSE-tree | 0.861 | 0.790 | 0.814 |
| SSE-treeSC | 0.866 | 0.793 | 0.820 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 1000 | 0.706 | 0.785 | 0.542 | 0.569 |
| SSE | x unseen | 344 | 0.692 | 0.777 | 0.514 | 0.546 |
| SSE | x seen | 656 | 0.712 | 0.790 | 0.556 | 0.580 |
| SSE | q unseen | 355 | 0.705 | 0.783 | 0.463 | 0.517 |
| SSE-tree | all | 1000 | 0.708 | 0.788 | 0.537 | 0.608 |
| SSE-tree | x unseen | 344 | 0.695 | 0.780 | 0.513 | 0.574 |
| SSE-tree | x seen | 656 | 0.715 | 0.792 | 0.550 | 0.624 |
| SSE-tree | q unseen | 355 | 0.707 | 0.785 | 0.456 | 0.535 |
| SSE-treeSC | all | 1000 | 0.708 | 0.787 | 0.542 | 0.607 |
| SSE-treeSC | x unseen | 344 | 0.695 | 0.780 | 0.516 | 0.569 |
| SSE-treeSC | x seen | 656 | 0.714 | 0.791 | 0.555 | 0.624 |
| SSE-treeSC | q unseen | 355 | 0.707 | 0.785 | 0.462 | 0.534 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE | 144 | 0.572 | 0.235 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.572 | 0.233 |
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.572 | 0.233 |
| B same-family/diff-habitat | SSE | 24 | 0.160 | 0.157 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.160 | 0.158 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.160 | 0.158 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE | order@8 | 0.955 | 0.918 | 0.897 |
| SSE | family@32 | 0.839 | 0.917 | 0.979 |
| SSE | genus@64 | 0.804 | 0.886 | 0.991 |
| SSE-tree | order@8 | 0.970 | 0.930 | 0.915 |
| SSE-tree | family@32 | 0.961 | 0.967 | 0.981 |
| SSE-tree | genus@64 | 0.954 | 0.960 | 0.991 |
| SSE-treeSC | order@8 | 0.967 | 0.926 | 0.910 |
| SSE-treeSC | family@32 | 0.953 | 0.964 | 0.981 |
| SSE-treeSC | genus@64 | 0.945 | 0.953 | 0.992 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.566 |
| SSE-tree | 0.576 |
| SSE-treeSC | 0.576 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.238 | 0.881 |
| SSE-tree | 1.000 | 0.237 | 0.879 |
| SSE-treeSC | 1.000 | 0.238 | 0.874 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.997 |
| seen_test | SSE | 4 | family | 0.518 |
| seen_test | SSE | 4 | genus | 0.419 |
| seen_test | SSE | 8 | order | 1.000 |
| seen_test | SSE | 8 | family | 0.531 |
| seen_test | SSE | 8 | genus | 0.430 |
| seen_test | SSE | 16 | order | 0.966 |
| seen_test | SSE | 16 | family | 0.990 |
| seen_test | SSE | 16 | genus | 0.801 |
| seen_test | SSE | 32 | order | 0.823 |
| seen_test | SSE | 32 | family | 0.992 |
| seen_test | SSE | 32 | genus | 0.810 |
| seen_test | SSE | 64 | order | 0.774 |
| seen_test | SSE | 64 | family | 0.946 |
| seen_test | SSE | 64 | genus | 0.992 |
| seen_test | SSE-tree | 4 | order | 0.946 |
| seen_test | SSE-tree | 4 | family | 0.494 |
| seen_test | SSE-tree | 4 | genus | 0.394 |
| seen_test | SSE-tree | 8 | order | 1.000 |
| seen_test | SSE-tree | 8 | family | 0.539 |
| seen_test | SSE-tree | 8 | genus | 0.437 |
| seen_test | SSE-tree | 16 | order | 0.999 |
| seen_test | SSE-tree | 16 | family | 0.985 |
| seen_test | SSE-tree | 16 | genus | 0.819 |
| seen_test | SSE-tree | 32 | order | 0.998 |
| seen_test | SSE-tree | 32 | family | 0.991 |
| seen_test | SSE-tree | 32 | genus | 0.850 |
| seen_test | SSE-tree | 64 | order | 0.993 |
| seen_test | SSE-tree | 64 | family | 0.991 |
| seen_test | SSE-tree | 64 | genus | 0.985 |
| seen_test | SSE-treeSC | 4 | order | 0.998 |
| seen_test | SSE-treeSC | 4 | family | 0.527 |
| seen_test | SSE-treeSC | 4 | genus | 0.423 |
| seen_test | SSE-treeSC | 8 | order | 1.000 |
| seen_test | SSE-treeSC | 8 | family | 0.536 |
| seen_test | SSE-treeSC | 8 | genus | 0.431 |
| seen_test | SSE-treeSC | 16 | order | 0.999 |
| seen_test | SSE-treeSC | 16 | family | 0.988 |
| seen_test | SSE-treeSC | 16 | genus | 0.799 |
| seen_test | SSE-treeSC | 32 | order | 0.995 |
| seen_test | SSE-treeSC | 32 | family | 0.992 |
| seen_test | SSE-treeSC | 32 | genus | 0.814 |
| seen_test | SSE-treeSC | 64 | order | 0.989 |
| seen_test | SSE-treeSC | 64 | family | 0.987 |
| seen_test | SSE-treeSC | 64 | genus | 0.992 |
| seen_test | CLIP-PCA | 4 | order | 0.537 |
| seen_test | CLIP-PCA | 4 | family | 0.535 |
| seen_test | CLIP-PCA | 4 | genus | 0.567 |
| seen_test | CLIP-PCA | 8 | order | 0.597 |
| seen_test | CLIP-PCA | 8 | family | 0.656 |
| seen_test | CLIP-PCA | 8 | genus | 0.681 |
| seen_test | CLIP-PCA | 16 | order | 0.654 |
| seen_test | CLIP-PCA | 16 | family | 0.763 |
| seen_test | CLIP-PCA | 16 | genus | 0.809 |
| seen_test | CLIP-PCA | 32 | order | 0.663 |
| seen_test | CLIP-PCA | 32 | family | 0.786 |
| seen_test | CLIP-PCA | 32 | genus | 0.841 |
| seen_test | CLIP-PCA | 64 | order | 0.656 |
| seen_test | CLIP-PCA | 64 | family | 0.781 |
| seen_test | CLIP-PCA | 64 | genus | 0.839 |
| unseen | SSE | 4 | order | 0.833 |
| unseen | SSE | 4 | family | 0.834 |
| unseen | SSE | 4 | genus | 0.834 |
| unseen | SSE | 8 | order | 0.860 |
| unseen | SSE | 8 | family | 0.890 |
| unseen | SSE | 8 | genus | 0.890 |
| unseen | SSE | 16 | order | 0.885 |
| unseen | SSE | 16 | family | 0.913 |
| unseen | SSE | 16 | genus | 0.913 |
| unseen | SSE | 32 | order | 0.894 |
| unseen | SSE | 32 | family | 0.915 |
| unseen | SSE | 32 | genus | 0.915 |
| unseen | SSE | 64 | order | 0.915 |
| unseen | SSE | 64 | family | 0.921 |
| unseen | SSE | 64 | genus | 0.921 |
| unseen | SSE-tree | 4 | order | 0.867 |
| unseen | SSE-tree | 4 | family | 0.866 |
| unseen | SSE-tree | 4 | genus | 0.866 |
| unseen | SSE-tree | 8 | order | 0.880 |
| unseen | SSE-tree | 8 | family | 0.893 |
| unseen | SSE-tree | 8 | genus | 0.893 |
| unseen | SSE-tree | 16 | order | 0.899 |
| unseen | SSE-tree | 16 | family | 0.915 |
| unseen | SSE-tree | 16 | genus | 0.915 |
| unseen | SSE-tree | 32 | order | 0.909 |
| unseen | SSE-tree | 32 | family | 0.925 |
| unseen | SSE-tree | 32 | genus | 0.925 |
| unseen | SSE-tree | 64 | order | 0.916 |
| unseen | SSE-tree | 64 | family | 0.925 |
| unseen | SSE-tree | 64 | genus | 0.925 |
| unseen | SSE-treeSC | 4 | order | 0.863 |
| unseen | SSE-treeSC | 4 | family | 0.850 |
| unseen | SSE-treeSC | 4 | genus | 0.850 |
| unseen | SSE-treeSC | 8 | order | 0.877 |
| unseen | SSE-treeSC | 8 | family | 0.894 |
| unseen | SSE-treeSC | 8 | genus | 0.894 |
| unseen | SSE-treeSC | 16 | order | 0.906 |
| unseen | SSE-treeSC | 16 | family | 0.917 |
| unseen | SSE-treeSC | 16 | genus | 0.917 |
| unseen | SSE-treeSC | 32 | order | 0.909 |
| unseen | SSE-treeSC | 32 | family | 0.921 |
| unseen | SSE-treeSC | 32 | genus | 0.921 |
| unseen | SSE-treeSC | 64 | order | 0.918 |
| unseen | SSE-treeSC | 64 | family | 0.922 |
| unseen | SSE-treeSC | 64 | genus | 0.922 |
| unseen | CLIP-PCA | 4 | order | 0.797 |
| unseen | CLIP-PCA | 4 | family | 0.802 |
| unseen | CLIP-PCA | 4 | genus | 0.802 |
| unseen | CLIP-PCA | 8 | order | 0.881 |
| unseen | CLIP-PCA | 8 | family | 0.861 |
| unseen | CLIP-PCA | 8 | genus | 0.861 |
| unseen | CLIP-PCA | 16 | order | 0.876 |
| unseen | CLIP-PCA | 16 | family | 0.853 |
| unseen | CLIP-PCA | 16 | genus | 0.853 |
| unseen | CLIP-PCA | 32 | order | 0.889 |
| unseen | CLIP-PCA | 32 | family | 0.869 |
| unseen | CLIP-PCA | 32 | genus | 0.869 |
| unseen | CLIP-PCA | 64 | order | 0.898 |
| unseen | CLIP-PCA | 64 | family | 0.885 |
| unseen | CLIP-PCA | 64 | genus | 0.885 |
