# AwA2 results x_eval_seed2

args: `{'sse': 'SSE-treeSC=treesc_s2,SSE-tree=tree_s2,SSE-treeSC-256=treesc256_s2,SSE-treeSC-128=treesc128_s2', 'mrl': 'mrl_s2', 'out': 'x_eval_seed2', 'no_baselines': False, 'extra': 'B3 separate=b3tree_s2,B4 CSN=csntree_s2', 'seed': 2}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE-treeSC | habitat | 0.903 | 0.415 | 0.309 |
| SSE-treeSC | diet | 0.453 | 0.867 | 0.433 |
| SSE-treeSC | family | 0.308 | 0.377 | 0.710 |
| SSE-treeSC | tax | 0.318 | 0.378 | 0.678 |
| SSE-treeSC | rest | 0.162 | 0.126 | 0.146 |
| SSE-tree | habitat | 0.903 | 0.416 | 0.310 |
| SSE-tree | diet | 0.453 | 0.868 | 0.434 |
| SSE-tree | family | 0.274 | 0.374 | 0.721 |
| SSE-tree | tax | 0.292 | 0.378 | 0.703 |
| SSE-tree | rest | 0.155 | 0.122 | 0.138 |
| SSE-treeSC-256 | habitat | 0.904 | 0.413 | 0.304 |
| SSE-treeSC-256 | diet | 0.456 | 0.866 | 0.423 |
| SSE-treeSC-256 | family | 0.304 | 0.371 | 0.708 |
| SSE-treeSC-256 | tax | 0.313 | 0.375 | 0.678 |
| SSE-treeSC-256 | rest | 0.122 | 0.113 | 0.138 |
| SSE-treeSC-128 | habitat | 0.903 | 0.412 | 0.306 |
| SSE-treeSC-128 | diet | 0.451 | 0.864 | 0.436 |
| SSE-treeSC-128 | family | 0.305 | 0.382 | 0.712 |
| SSE-treeSC-128 | tax | 0.306 | 0.378 | 0.678 |
| SSE-treeSC-128 | rest | 0.032 | 0.063 | 0.107 |
| B1 labels | habitat | 0.609 | 0.277 | 0.276 |
| B1 labels | diet | 0.259 | 0.587 | 0.284 |
| B1 labels | family | 0.321 | 0.393 | 0.727 |
| B1-soft | habitat | 0.756 | 0.372 | 0.365 |
| B1-soft | diet | 0.408 | 0.787 | 0.350 |
| B1-soft | family | 0.325 | 0.376 | 0.529 |
| B2 CLIP+text | habitat | 0.255 | 0.180 | 0.122 |
| B2 CLIP+text | diet | 0.209 | 0.169 | 0.093 |
| B2 CLIP+text | family | 0.205 | 0.194 | 0.241 |
| B6 plain CLIP | habitat | 0.308 | 0.281 | 0.237 |
| B6 plain CLIP | diet | 0.308 | 0.281 | 0.237 |
| B6 plain CLIP | family | 0.308 | 0.281 | 0.237 |
| B3 separate | habitat | 0.905 | 0.424 | 0.310 |
| B3 separate | diet | 0.448 | 0.865 | 0.448 |
| B3 separate | family | 0.276 | 0.362 | 0.725 |
| B4 CSN | habitat | 0.902 | 0.424 | 0.310 |
| B4 CSN | diet | 0.453 | 0.869 | 0.440 |
| B4 CSN | family | 0.266 | 0.361 | 0.731 |

### E3 — general search preserved

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.850 | 0.819 | 0.823 |
| SSE-tree | 0.857 | 0.836 | 0.840 |
| SSE-treeSC-256 | 0.705 | 0.831 | 0.828 |
| SSE-treeSC-128 | 0.452 | 0.801 | 0.796 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE-treeSC | all | 1000 | 0.752 | 0.838 | 0.573 | 0.561 |
| SSE-treeSC | x unseen | 552 | 0.727 | 0.822 | 0.549 | 0.515 |
| SSE-treeSC | x seen | 448 | 0.783 | 0.857 | 0.603 | 0.621 |
| SSE-treeSC | q unseen | 573 | 0.747 | 0.831 | 0.565 | 0.530 |
| SSE-tree | all | 1000 | 0.752 | 0.837 | 0.562 | 0.563 |
| SSE-tree | x unseen | 552 | 0.726 | 0.822 | 0.535 | 0.514 |
| SSE-tree | x seen | 448 | 0.783 | 0.857 | 0.596 | 0.627 |
| SSE-tree | q unseen | 573 | 0.746 | 0.831 | 0.551 | 0.530 |
| SSE-treeSC-256 | all | 1000 | 0.753 | 0.837 | 0.570 | 0.565 |
| SSE-treeSC-256 | x unseen | 552 | 0.727 | 0.819 | 0.543 | 0.519 |
| SSE-treeSC-256 | x seen | 448 | 0.786 | 0.859 | 0.603 | 0.627 |
| SSE-treeSC-256 | q unseen | 573 | 0.746 | 0.829 | 0.555 | 0.538 |
| SSE-treeSC-128 | all | 1000 | 0.746 | 0.830 | 0.558 | 0.559 |
| SSE-treeSC-128 | x unseen | 552 | 0.718 | 0.812 | 0.525 | 0.509 |
| SSE-treeSC-128 | x seen | 448 | 0.780 | 0.853 | 0.598 | 0.624 |
| SSE-treeSC-128 | q unseen | 573 | 0.740 | 0.823 | 0.547 | 0.533 |
| B1 labels | all | 1000 | 0.476 | 0.513 | 0.348 | 0.375 |
| B1 labels | x unseen | 552 | 0.466 | 0.478 | 0.319 | 0.344 |
| B1 labels | x seen | 448 | 0.487 | 0.556 | 0.383 | 0.415 |
| B1 labels | q unseen | 573 | 0.467 | 0.502 | 0.328 | 0.349 |
| B1-soft | all | 1000 | 0.657 | 0.736 | 0.429 | 0.457 |
| B1-soft | x unseen | 552 | 0.678 | 0.762 | 0.444 | 0.434 |
| B1-soft | x seen | 448 | 0.631 | 0.703 | 0.410 | 0.486 |
| B1-soft | q unseen | 573 | 0.649 | 0.725 | 0.411 | 0.431 |
| B2 CLIP+text | all | 1000 | 0.465 | 0.508 | 0.361 | 0.405 |
| B2 CLIP+text | x unseen | 552 | 0.494 | 0.545 | 0.364 | 0.389 |
| B2 CLIP+text | x seen | 448 | 0.430 | 0.463 | 0.358 | 0.425 |
| B2 CLIP+text | q unseen | 573 | 0.457 | 0.497 | 0.356 | 0.404 |
| B6 plain CLIP | all | 1000 | 0.548 | 0.622 | 0.316 | 0.387 |
| B6 plain CLIP | x unseen | 552 | 0.614 | 0.704 | 0.312 | 0.381 |
| B6 plain CLIP | x seen | 448 | 0.467 | 0.521 | 0.321 | 0.394 |
| B6 plain CLIP | q unseen | 573 | 0.540 | 0.611 | 0.312 | 0.387 |
| B3 separate | all | 1000 | 0.756 | 0.839 | 0.560 | 0.575 |
| B3 separate | x unseen | 552 | 0.728 | 0.822 | 0.529 | 0.523 |
| B3 separate | x seen | 448 | 0.790 | 0.861 | 0.598 | 0.642 |
| B3 separate | q unseen | 573 | 0.750 | 0.833 | 0.554 | 0.559 |
| B4 CSN | all | 1000 | 0.752 | 0.837 | 0.556 | 0.571 |
| B4 CSN | x unseen | 552 | 0.727 | 0.823 | 0.527 | 0.527 |
| B4 CSN | x seen | 448 | 0.782 | 0.855 | 0.592 | 0.627 |
| B4 CSN | q unseen | 573 | 0.747 | 0.832 | 0.546 | 0.549 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.652 | 0.152 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.652 | 0.152 |
| A same-habitat/diff-order | SSE-treeSC-256 | 144 | 0.652 | 0.147 |
| A same-habitat/diff-order | SSE-treeSC-128 | 144 | 0.652 | 0.156 |
| A same-habitat/diff-order | B1 labels | 144 | 0.652 | 0.347 |
| A same-habitat/diff-order | B1-soft | 144 | 0.652 | 0.269 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.652 | 0.396 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.652 | 0.347 |
| A same-habitat/diff-order | B3 separate | 144 | 0.652 | 0.148 |
| A same-habitat/diff-order | B4 CSN | 144 | 0.652 | 0.152 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.145 | 0.130 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.145 | 0.129 |
| B same-family/diff-habitat | SSE-treeSC-256 | 24 | 0.145 | 0.125 |
| B same-family/diff-habitat | SSE-treeSC-128 | 24 | 0.145 | 0.130 |
| B same-family/diff-habitat | B1 labels | 24 | 0.145 | 0.539 |
| B same-family/diff-habitat | B1-soft | 24 | 0.145 | 0.297 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.145 | 0.191 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.145 | 0.204 |
| B same-family/diff-habitat | B3 separate | 24 | 0.145 | 0.130 |
| B same-family/diff-habitat | B4 CSN | 24 | 0.145 | 0.124 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE-treeSC | order@8 | 0.961 | 0.934 | 0.925 |
| SSE-treeSC | family@32 | 0.946 | 0.997 | 0.986 |
| SSE-treeSC | genus@64 | 0.923 | 0.992 | 0.996 |
| SSE-tree | order@8 | 0.959 | 0.942 | 0.932 |
| SSE-tree | family@32 | 0.954 | 0.996 | 0.985 |
| SSE-tree | genus@64 | 0.941 | 0.997 | 0.995 |
| SSE-treeSC-256 | order@8 | 0.961 | 0.934 | 0.922 |
| SSE-treeSC-256 | family@32 | 0.944 | 0.997 | 0.986 |
| SSE-treeSC-256 | genus@64 | 0.923 | 0.992 | 0.996 |
| SSE-treeSC-128 | order@8 | 0.962 | 0.936 | 0.924 |
| SSE-treeSC-128 | family@32 | 0.947 | 0.997 | 0.985 |
| SSE-treeSC-128 | genus@64 | 0.923 | 0.993 | 0.996 |
| B1 labels | family view | 0.959 | 0.985 | 0.978 |
| B1-soft | family view | 0.821 | 0.993 | 0.979 |
| B2 CLIP+text | family view | 0.635 | 0.796 | 0.854 |
| B6 plain CLIP | family view | 0.628 | 0.839 | 0.935 |
| B3 separate | order@8 | 0.961 | 0.941 | 0.931 |
| B3 separate | family@32 | 0.956 | 0.997 | 0.986 |
| B3 separate | genus@64 | 0.943 | 0.997 | 0.996 |
| B4 CSN | order@8 | 0.961 | 0.943 | 0.932 |
| B4 CSN | family@32 | 0.960 | 0.996 | 0.985 |
| B4 CSN | genus@64 | 0.947 | 0.997 | 0.995 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE-treeSC | 0.889 |
| SSE-tree | 0.889 |
| SSE-treeSC-256 | 0.890 |
| SSE-treeSC-128 | 0.888 |
| B1 labels | 0.592 |
| B1-soft | 0.723 |
| B2 CLIP+text | 0.211 |
| B6 plain CLIP | 0.234 |
| B3 separate | 0.892 |
| B4 CSN | 0.888 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE-treeSC | 1.000 | 0.088 | 0.919 |
| SSE-tree | 1.000 | 0.095 | 0.920 |
| SSE-treeSC-256 | 1.000 | 0.100 | 0.916 |
| SSE-treeSC-128 | 1.000 | 0.099 | 0.909 |
| B1 labels | 0.903 | 0.381 | 0.762 |
| B1-soft | 1.000 | 0.155 | 0.881 |
| B2 CLIP+text | 1.000 | 0.443 | 0.775 |
| B6 plain CLIP | 0.927 | 0.428 | 0.838 |
| B3 separate | 1.000 | 0.087 | 0.926 |
| B4 CSN | 1.000 | 0.090 | 0.917 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE-treeSC | 4 | order | 0.984 |
| seen_test | SSE-treeSC | 4 | family | 0.511 |
| seen_test | SSE-treeSC | 4 | genus | 0.370 |
| seen_test | SSE-treeSC | 8 | order | 0.995 |
| seen_test | SSE-treeSC | 8 | family | 0.526 |
| seen_test | SSE-treeSC | 8 | genus | 0.381 |
| seen_test | SSE-treeSC | 16 | order | 0.994 |
| seen_test | SSE-treeSC | 16 | family | 0.978 |
| seen_test | SSE-treeSC | 16 | genus | 0.716 |
| seen_test | SSE-treeSC | 32 | order | 0.989 |
| seen_test | SSE-treeSC | 32 | family | 0.989 |
| seen_test | SSE-treeSC | 32 | genus | 0.734 |
| seen_test | SSE-treeSC | 64 | order | 0.982 |
| seen_test | SSE-treeSC | 64 | family | 0.967 |
| seen_test | SSE-treeSC | 64 | genus | 0.987 |
| seen_test | SSE-tree | 4 | order | 0.986 |
| seen_test | SSE-tree | 4 | family | 0.520 |
| seen_test | SSE-tree | 4 | genus | 0.375 |
| seen_test | SSE-tree | 8 | order | 0.995 |
| seen_test | SSE-tree | 8 | family | 0.532 |
| seen_test | SSE-tree | 8 | genus | 0.386 |
| seen_test | SSE-tree | 16 | order | 0.994 |
| seen_test | SSE-tree | 16 | family | 0.963 |
| seen_test | SSE-tree | 16 | genus | 0.715 |
| seen_test | SSE-tree | 32 | order | 0.992 |
| seen_test | SSE-tree | 32 | family | 0.982 |
| seen_test | SSE-tree | 32 | genus | 0.743 |
| seen_test | SSE-tree | 64 | order | 0.988 |
| seen_test | SSE-tree | 64 | family | 0.982 |
| seen_test | SSE-tree | 64 | genus | 0.977 |
| seen_test | SSE-treeSC-256 | 4 | order | 0.988 |
| seen_test | SSE-treeSC-256 | 4 | family | 0.516 |
| seen_test | SSE-treeSC-256 | 4 | genus | 0.371 |
| seen_test | SSE-treeSC-256 | 8 | order | 0.995 |
| seen_test | SSE-treeSC-256 | 8 | family | 0.527 |
| seen_test | SSE-treeSC-256 | 8 | genus | 0.381 |
| seen_test | SSE-treeSC-256 | 16 | order | 0.994 |
| seen_test | SSE-treeSC-256 | 16 | family | 0.970 |
| seen_test | SSE-treeSC-256 | 16 | genus | 0.719 |
| seen_test | SSE-treeSC-256 | 32 | order | 0.989 |
| seen_test | SSE-treeSC-256 | 32 | family | 0.989 |
| seen_test | SSE-treeSC-256 | 32 | genus | 0.738 |
| seen_test | SSE-treeSC-256 | 64 | order | 0.981 |
| seen_test | SSE-treeSC-256 | 64 | family | 0.967 |
| seen_test | SSE-treeSC-256 | 64 | genus | 0.987 |
| seen_test | SSE-treeSC-128 | 4 | order | 0.966 |
| seen_test | SSE-treeSC-128 | 4 | family | 0.513 |
| seen_test | SSE-treeSC-128 | 4 | genus | 0.370 |
| seen_test | SSE-treeSC-128 | 8 | order | 0.995 |
| seen_test | SSE-treeSC-128 | 8 | family | 0.528 |
| seen_test | SSE-treeSC-128 | 8 | genus | 0.382 |
| seen_test | SSE-treeSC-128 | 16 | order | 0.994 |
| seen_test | SSE-treeSC-128 | 16 | family | 0.966 |
| seen_test | SSE-treeSC-128 | 16 | genus | 0.702 |
| seen_test | SSE-treeSC-128 | 32 | order | 0.989 |
| seen_test | SSE-treeSC-128 | 32 | family | 0.989 |
| seen_test | SSE-treeSC-128 | 32 | genus | 0.735 |
| seen_test | SSE-treeSC-128 | 64 | order | 0.981 |
| seen_test | SSE-treeSC-128 | 64 | family | 0.968 |
| seen_test | SSE-treeSC-128 | 64 | genus | 0.987 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.581 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.714 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.827 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.695 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.839 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.984 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.735 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.859 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.987 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.743 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.875 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.988 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.740 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.877 |
| seen_test | SSE-MRL (genus everywhere) | 64 | genus | 0.988 |
| seen_test | CLIP-PCA | 4 | order | 0.524 |
| seen_test | CLIP-PCA | 4 | family | 0.503 |
| seen_test | CLIP-PCA | 4 | genus | 0.582 |
| seen_test | CLIP-PCA | 8 | order | 0.590 |
| seen_test | CLIP-PCA | 8 | family | 0.608 |
| seen_test | CLIP-PCA | 8 | genus | 0.687 |
| seen_test | CLIP-PCA | 16 | order | 0.638 |
| seen_test | CLIP-PCA | 16 | family | 0.699 |
| seen_test | CLIP-PCA | 16 | genus | 0.797 |
| seen_test | CLIP-PCA | 32 | order | 0.658 |
| seen_test | CLIP-PCA | 32 | family | 0.736 |
| seen_test | CLIP-PCA | 32 | genus | 0.848 |
| seen_test | CLIP-PCA | 64 | order | 0.654 |
| seen_test | CLIP-PCA | 64 | family | 0.733 |
| seen_test | CLIP-PCA | 64 | genus | 0.851 |
| unseen | SSE-treeSC | 4 | order | 0.905 |
| unseen | SSE-treeSC | 4 | family | 0.604 |
| unseen | SSE-treeSC | 4 | genus | 0.601 |
| unseen | SSE-treeSC | 8 | order | 0.932 |
| unseen | SSE-treeSC | 8 | family | 0.774 |
| unseen | SSE-treeSC | 8 | genus | 0.779 |
| unseen | SSE-treeSC | 16 | order | 0.934 |
| unseen | SSE-treeSC | 16 | family | 0.960 |
| unseen | SSE-treeSC | 16 | genus | 0.944 |
| unseen | SSE-treeSC | 32 | order | 0.911 |
| unseen | SSE-treeSC | 32 | family | 0.976 |
| unseen | SSE-treeSC | 32 | genus | 0.964 |
| unseen | SSE-treeSC | 64 | order | 0.892 |
| unseen | SSE-treeSC | 64 | family | 0.981 |
| unseen | SSE-treeSC | 64 | genus | 0.983 |
| unseen | SSE-tree | 4 | order | 0.897 |
| unseen | SSE-tree | 4 | family | 0.698 |
| unseen | SSE-tree | 4 | genus | 0.685 |
| unseen | SSE-tree | 8 | order | 0.940 |
| unseen | SSE-tree | 8 | family | 0.826 |
| unseen | SSE-tree | 8 | genus | 0.823 |
| unseen | SSE-tree | 16 | order | 0.937 |
| unseen | SSE-tree | 16 | family | 0.959 |
| unseen | SSE-tree | 16 | genus | 0.937 |
| unseen | SSE-tree | 32 | order | 0.941 |
| unseen | SSE-tree | 32 | family | 0.977 |
| unseen | SSE-tree | 32 | genus | 0.969 |
| unseen | SSE-tree | 64 | order | 0.936 |
| unseen | SSE-tree | 64 | family | 0.986 |
| unseen | SSE-tree | 64 | genus | 0.985 |
| unseen | SSE-treeSC-256 | 4 | order | 0.856 |
| unseen | SSE-treeSC-256 | 4 | family | 0.673 |
| unseen | SSE-treeSC-256 | 4 | genus | 0.626 |
| unseen | SSE-treeSC-256 | 8 | order | 0.932 |
| unseen | SSE-treeSC-256 | 8 | family | 0.766 |
| unseen | SSE-treeSC-256 | 8 | genus | 0.749 |
| unseen | SSE-treeSC-256 | 16 | order | 0.943 |
| unseen | SSE-treeSC-256 | 16 | family | 0.940 |
| unseen | SSE-treeSC-256 | 16 | genus | 0.920 |
| unseen | SSE-treeSC-256 | 32 | order | 0.909 |
| unseen | SSE-treeSC-256 | 32 | family | 0.978 |
| unseen | SSE-treeSC-256 | 32 | genus | 0.964 |
| unseen | SSE-treeSC-256 | 64 | order | 0.888 |
| unseen | SSE-treeSC-256 | 64 | family | 0.983 |
| unseen | SSE-treeSC-256 | 64 | genus | 0.984 |
| unseen | SSE-treeSC-128 | 4 | order | 0.723 |
| unseen | SSE-treeSC-128 | 4 | family | 0.614 |
| unseen | SSE-treeSC-128 | 4 | genus | 0.586 |
| unseen | SSE-treeSC-128 | 8 | order | 0.933 |
| unseen | SSE-treeSC-128 | 8 | family | 0.783 |
| unseen | SSE-treeSC-128 | 8 | genus | 0.765 |
| unseen | SSE-treeSC-128 | 16 | order | 0.939 |
| unseen | SSE-treeSC-128 | 16 | family | 0.958 |
| unseen | SSE-treeSC-128 | 16 | genus | 0.939 |
| unseen | SSE-treeSC-128 | 32 | order | 0.913 |
| unseen | SSE-treeSC-128 | 32 | family | 0.977 |
| unseen | SSE-treeSC-128 | 32 | genus | 0.964 |
| unseen | SSE-treeSC-128 | 64 | order | 0.889 |
| unseen | SSE-treeSC-128 | 64 | family | 0.983 |
| unseen | SSE-treeSC-128 | 64 | genus | 0.984 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.674 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.751 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.779 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.763 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.901 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.944 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.768 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.910 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.959 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.774 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.940 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.965 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.777 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.948 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.967 |
| unseen | CLIP-PCA | 4 | order | 0.604 |
| unseen | CLIP-PCA | 4 | family | 0.628 |
| unseen | CLIP-PCA | 4 | genus | 0.691 |
| unseen | CLIP-PCA | 8 | order | 0.633 |
| unseen | CLIP-PCA | 8 | family | 0.689 |
| unseen | CLIP-PCA | 8 | genus | 0.756 |
| unseen | CLIP-PCA | 16 | order | 0.687 |
| unseen | CLIP-PCA | 16 | family | 0.797 |
| unseen | CLIP-PCA | 16 | genus | 0.851 |
| unseen | CLIP-PCA | 32 | order | 0.721 |
| unseen | CLIP-PCA | 32 | family | 0.854 |
| unseen | CLIP-PCA | 32 | genus | 0.902 |
| unseen | CLIP-PCA | 64 | order | 0.740 |
| unseen | CLIP-PCA | 64 | family | 0.882 |
| unseen | CLIP-PCA | 64 | genus | 0.932 |
