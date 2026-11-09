# AwA2 results val_seed0

args: `{'sse': 'SSE=val_main_s0,SSE-tree=val_tree_s0,SSE-treeSC=val_treesc_s0', 'mrl': '', 'out': 'val_seed0', 'no_baselines': True, 'extra': '', 'seed': 0}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.666 | 0.354 | 0.323 |
| SSE | diet | 0.486 | 0.839 | 0.499 |
| SSE | family | 0.352 | 0.274 | 0.554 |
| SSE | tax | 0.394 | 0.324 | 0.493 |
| SSE | rest | 0.134 | 0.160 | 0.197 |
| SSE | full | 0.256 | 0.308 | 0.332 |
| SSE-tree | habitat | 0.672 | 0.358 | 0.324 |
| SSE-tree | diet | 0.489 | 0.840 | 0.499 |
| SSE-tree | family | 0.263 | 0.355 | 0.717 |
| SSE-tree | tax | 0.272 | 0.364 | 0.707 |
| SSE-tree | rest | 0.133 | 0.160 | 0.186 |
| SSE-treeSC | habitat | 0.673 | 0.360 | 0.324 |
| SSE-treeSC | diet | 0.489 | 0.839 | 0.499 |
| SSE-treeSC | family | 0.265 | 0.352 | 0.708 |
| SSE-treeSC | tax | 0.285 | 0.369 | 0.697 |
| SSE-treeSC | rest | 0.140 | 0.162 | 0.188 |

### E3 — general search preserved

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE | 0.854 | 0.801 | 0.820 |
| SSE-tree | 0.863 | 0.790 | 0.812 |
| SSE-treeSC | 0.867 | 0.793 | 0.819 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 1000 | 0.708 | 0.787 | 0.547 | 0.573 |
| SSE | x unseen | 344 | 0.698 | 0.782 | 0.524 | 0.549 |
| SSE | x seen | 656 | 0.714 | 0.790 | 0.559 | 0.583 |
| SSE | q unseen | 355 | 0.708 | 0.784 | 0.466 | 0.523 |
| SSE-tree | all | 1000 | 0.711 | 0.789 | 0.536 | 0.608 |
| SSE-tree | x unseen | 344 | 0.698 | 0.782 | 0.501 | 0.564 |
| SSE-tree | x seen | 656 | 0.717 | 0.792 | 0.554 | 0.627 |
| SSE-tree | q unseen | 355 | 0.710 | 0.786 | 0.460 | 0.540 |
| SSE-treeSC | all | 1000 | 0.711 | 0.789 | 0.542 | 0.603 |
| SSE-treeSC | x unseen | 344 | 0.700 | 0.784 | 0.517 | 0.562 |
| SSE-treeSC | x seen | 656 | 0.716 | 0.791 | 0.555 | 0.621 |
| SSE-treeSC | q unseen | 355 | 0.710 | 0.786 | 0.461 | 0.535 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE | 144 | 0.572 | 0.231 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.572 | 0.228 |
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.572 | 0.230 |
| B same-family/diff-habitat | SSE | 24 | 0.160 | 0.161 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.160 | 0.160 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.160 | 0.161 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE | order@8 | 0.947 | 0.919 | 0.897 |
| SSE | family@32 | 0.843 | 0.924 | 0.978 |
| SSE | genus@64 | 0.802 | 0.888 | 0.991 |
| SSE-tree | order@8 | 0.969 | 0.929 | 0.913 |
| SSE-tree | family@32 | 0.960 | 0.966 | 0.982 |
| SSE-tree | genus@64 | 0.952 | 0.959 | 0.992 |
| SSE-treeSC | order@8 | 0.965 | 0.925 | 0.909 |
| SSE-treeSC | family@32 | 0.953 | 0.965 | 0.981 |
| SSE-treeSC | genus@64 | 0.946 | 0.952 | 0.993 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.565 |
| SSE-tree | 0.573 |
| SSE-treeSC | 0.575 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.241 | 0.882 |
| SSE-tree | 1.000 | 0.242 | 0.878 |
| SSE-treeSC | 1.000 | 0.242 | 0.873 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.988 |
| seen_test | SSE | 4 | family | 0.517 |
| seen_test | SSE | 4 | genus | 0.415 |
| seen_test | SSE | 8 | order | 1.000 |
| seen_test | SSE | 8 | family | 0.528 |
| seen_test | SSE | 8 | genus | 0.429 |
| seen_test | SSE | 16 | order | 0.939 |
| seen_test | SSE | 16 | family | 0.987 |
| seen_test | SSE | 16 | genus | 0.803 |
| seen_test | SSE | 32 | order | 0.825 |
| seen_test | SSE | 32 | family | 0.992 |
| seen_test | SSE | 32 | genus | 0.812 |
| seen_test | SSE | 64 | order | 0.772 |
| seen_test | SSE | 64 | family | 0.945 |
| seen_test | SSE | 64 | genus | 0.992 |
| seen_test | SSE-tree | 4 | order | 0.984 |
| seen_test | SSE-tree | 4 | family | 0.520 |
| seen_test | SSE-tree | 4 | genus | 0.417 |
| seen_test | SSE-tree | 8 | order | 1.000 |
| seen_test | SSE-tree | 8 | family | 0.538 |
| seen_test | SSE-tree | 8 | genus | 0.433 |
| seen_test | SSE-tree | 16 | order | 1.000 |
| seen_test | SSE-tree | 16 | family | 0.963 |
| seen_test | SSE-tree | 16 | genus | 0.795 |
| seen_test | SSE-tree | 32 | order | 0.997 |
| seen_test | SSE-tree | 32 | family | 0.990 |
| seen_test | SSE-tree | 32 | genus | 0.825 |
| seen_test | SSE-tree | 64 | order | 0.993 |
| seen_test | SSE-tree | 64 | family | 0.992 |
| seen_test | SSE-tree | 64 | genus | 0.988 |
| seen_test | SSE-treeSC | 4 | order | 0.987 |
| seen_test | SSE-treeSC | 4 | family | 0.515 |
| seen_test | SSE-treeSC | 4 | genus | 0.413 |
| seen_test | SSE-treeSC | 8 | order | 1.000 |
| seen_test | SSE-treeSC | 8 | family | 0.534 |
| seen_test | SSE-treeSC | 8 | genus | 0.430 |
| seen_test | SSE-treeSC | 16 | order | 0.999 |
| seen_test | SSE-treeSC | 16 | family | 0.982 |
| seen_test | SSE-treeSC | 16 | genus | 0.795 |
| seen_test | SSE-treeSC | 32 | order | 0.995 |
| seen_test | SSE-treeSC | 32 | family | 0.992 |
| seen_test | SSE-treeSC | 32 | genus | 0.810 |
| seen_test | SSE-treeSC | 64 | order | 0.988 |
| seen_test | SSE-treeSC | 64 | family | 0.987 |
| seen_test | SSE-treeSC | 64 | genus | 0.993 |
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
| unseen | SSE | 4 | order | 0.778 |
| unseen | SSE | 4 | family | 0.822 |
| unseen | SSE | 4 | genus | 0.822 |
| unseen | SSE | 8 | order | 0.852 |
| unseen | SSE | 8 | family | 0.889 |
| unseen | SSE | 8 | genus | 0.889 |
| unseen | SSE | 16 | order | 0.883 |
| unseen | SSE | 16 | family | 0.907 |
| unseen | SSE | 16 | genus | 0.907 |
| unseen | SSE | 32 | order | 0.892 |
| unseen | SSE | 32 | family | 0.912 |
| unseen | SSE | 32 | genus | 0.912 |
| unseen | SSE | 64 | order | 0.915 |
| unseen | SSE | 64 | family | 0.922 |
| unseen | SSE | 64 | genus | 0.922 |
| unseen | SSE-tree | 4 | order | 0.746 |
| unseen | SSE-tree | 4 | family | 0.787 |
| unseen | SSE-tree | 4 | genus | 0.787 |
| unseen | SSE-tree | 8 | order | 0.874 |
| unseen | SSE-tree | 8 | family | 0.891 |
| unseen | SSE-tree | 8 | genus | 0.891 |
| unseen | SSE-tree | 16 | order | 0.902 |
| unseen | SSE-tree | 16 | family | 0.912 |
| unseen | SSE-tree | 16 | genus | 0.912 |
| unseen | SSE-tree | 32 | order | 0.908 |
| unseen | SSE-tree | 32 | family | 0.916 |
| unseen | SSE-tree | 32 | genus | 0.916 |
| unseen | SSE-tree | 64 | order | 0.919 |
| unseen | SSE-tree | 64 | family | 0.921 |
| unseen | SSE-tree | 64 | genus | 0.921 |
| unseen | SSE-treeSC | 4 | order | 0.758 |
| unseen | SSE-treeSC | 4 | family | 0.793 |
| unseen | SSE-treeSC | 4 | genus | 0.793 |
| unseen | SSE-treeSC | 8 | order | 0.872 |
| unseen | SSE-treeSC | 8 | family | 0.893 |
| unseen | SSE-treeSC | 8 | genus | 0.893 |
| unseen | SSE-treeSC | 16 | order | 0.902 |
| unseen | SSE-treeSC | 16 | family | 0.913 |
| unseen | SSE-treeSC | 16 | genus | 0.913 |
| unseen | SSE-treeSC | 32 | order | 0.908 |
| unseen | SSE-treeSC | 32 | family | 0.916 |
| unseen | SSE-treeSC | 32 | genus | 0.916 |
| unseen | SSE-treeSC | 64 | order | 0.922 |
| unseen | SSE-treeSC | 64 | family | 0.921 |
| unseen | SSE-treeSC | 64 | genus | 0.921 |
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
