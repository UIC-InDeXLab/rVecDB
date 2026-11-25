# AwA2 results x_eval_seed0

args: `{'sse': 'SSE-treeSC=treesc_s0,SSE-tree=tree_s0,SSE-treeSC-256=treesc256_s0,SSE-treeSC-128=treesc128_s0', 'mrl': 'mrl_s0', 'out': 'x_eval_seed0', 'no_baselines': False, 'extra': 'B3 separate=b3tree_s0,B4 CSN=csntree_s0', 'seed': 0}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE-treeSC | habitat | 0.902 | 0.421 | 0.307 |
| SSE-treeSC | diet | 0.454 | 0.866 | 0.430 |
| SSE-treeSC | family | 0.311 | 0.378 | 0.709 |
| SSE-treeSC | tax | 0.324 | 0.386 | 0.678 |
| SSE-treeSC | rest | 0.164 | 0.133 | 0.143 |
| SSE-tree | habitat | 0.903 | 0.422 | 0.308 |
| SSE-tree | diet | 0.453 | 0.866 | 0.432 |
| SSE-tree | family | 0.295 | 0.378 | 0.723 |
| SSE-tree | tax | 0.293 | 0.389 | 0.704 |
| SSE-tree | rest | 0.157 | 0.129 | 0.136 |
| SSE-treeSC-256 | habitat | 0.903 | 0.416 | 0.301 |
| SSE-treeSC-256 | diet | 0.453 | 0.870 | 0.434 |
| SSE-treeSC-256 | family | 0.294 | 0.374 | 0.710 |
| SSE-treeSC-256 | tax | 0.307 | 0.375 | 0.677 |
| SSE-treeSC-256 | rest | 0.132 | 0.106 | 0.140 |
| SSE-treeSC-128 | habitat | 0.902 | 0.409 | 0.299 |
| SSE-treeSC-128 | diet | 0.454 | 0.866 | 0.432 |
| SSE-treeSC-128 | family | 0.305 | 0.379 | 0.713 |
| SSE-treeSC-128 | tax | 0.308 | 0.381 | 0.675 |
| SSE-treeSC-128 | rest | 0.047 | 0.078 | 0.093 |
| B1 labels | habitat | 0.608 | 0.277 | 0.276 |
| B1 labels | diet | 0.260 | 0.587 | 0.285 |
| B1 labels | family | 0.321 | 0.393 | 0.728 |
| B1-soft | habitat | 0.756 | 0.372 | 0.365 |
| B1-soft | diet | 0.409 | 0.786 | 0.347 |
| B1-soft | family | 0.325 | 0.376 | 0.529 |
| B2 CLIP+text | habitat | 0.255 | 0.180 | 0.122 |
| B2 CLIP+text | diet | 0.209 | 0.169 | 0.093 |
| B2 CLIP+text | family | 0.205 | 0.194 | 0.241 |
| B6 plain CLIP | habitat | 0.308 | 0.281 | 0.237 |
| B6 plain CLIP | diet | 0.308 | 0.281 | 0.237 |
| B6 plain CLIP | family | 0.308 | 0.281 | 0.237 |
| B3 separate | habitat | 0.906 | 0.420 | 0.310 |
| B3 separate | diet | 0.475 | 0.865 | 0.433 |
| B3 separate | family | 0.286 | 0.383 | 0.724 |
| B4 CSN | habitat | 0.900 | 0.423 | 0.318 |
| B4 CSN | diet | 0.454 | 0.870 | 0.445 |
| B4 CSN | family | 0.287 | 0.373 | 0.730 |

### E3 — general search preserved

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.848 | 0.819 | 0.822 |
| SSE-tree | 0.852 | 0.836 | 0.839 |
| SSE-treeSC-256 | 0.706 | 0.831 | 0.831 |
| SSE-treeSC-128 | 0.448 | 0.801 | 0.784 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE-treeSC | all | 1000 | 0.752 | 0.836 | 0.562 | 0.560 |
| SSE-treeSC | x unseen | 552 | 0.725 | 0.817 | 0.529 | 0.513 |
| SSE-treeSC | x seen | 448 | 0.786 | 0.860 | 0.602 | 0.620 |
| SSE-treeSC | q unseen | 573 | 0.747 | 0.830 | 0.549 | 0.527 |
| SSE-tree | all | 1000 | 0.753 | 0.837 | 0.552 | 0.569 |
| SSE-tree | x unseen | 552 | 0.725 | 0.818 | 0.521 | 0.522 |
| SSE-tree | x seen | 448 | 0.786 | 0.860 | 0.592 | 0.630 |
| SSE-tree | q unseen | 573 | 0.747 | 0.831 | 0.536 | 0.544 |
| SSE-treeSC-256 | all | 1000 | 0.752 | 0.835 | 0.572 | 0.567 |
| SSE-treeSC-256 | x unseen | 552 | 0.723 | 0.816 | 0.550 | 0.523 |
| SSE-treeSC-256 | x seen | 448 | 0.787 | 0.859 | 0.600 | 0.626 |
| SSE-treeSC-256 | q unseen | 573 | 0.746 | 0.828 | 0.564 | 0.540 |
| SSE-treeSC-128 | all | 1000 | 0.749 | 0.833 | 0.570 | 0.569 |
| SSE-treeSC-128 | x unseen | 552 | 0.721 | 0.814 | 0.544 | 0.519 |
| SSE-treeSC-128 | x seen | 448 | 0.784 | 0.856 | 0.602 | 0.634 |
| SSE-treeSC-128 | q unseen | 573 | 0.743 | 0.825 | 0.555 | 0.538 |
| B1 labels | all | 1000 | 0.477 | 0.515 | 0.350 | 0.379 |
| B1 labels | x unseen | 552 | 0.467 | 0.479 | 0.318 | 0.345 |
| B1 labels | x seen | 448 | 0.490 | 0.558 | 0.388 | 0.423 |
| B1 labels | q unseen | 573 | 0.467 | 0.502 | 0.328 | 0.352 |
| B1-soft | all | 1000 | 0.657 | 0.736 | 0.429 | 0.456 |
| B1-soft | x unseen | 552 | 0.677 | 0.762 | 0.445 | 0.434 |
| B1-soft | x seen | 448 | 0.632 | 0.704 | 0.410 | 0.486 |
| B1-soft | q unseen | 573 | 0.648 | 0.725 | 0.410 | 0.431 |
| B2 CLIP+text | all | 1000 | 0.465 | 0.508 | 0.361 | 0.405 |
| B2 CLIP+text | x unseen | 552 | 0.494 | 0.545 | 0.364 | 0.389 |
| B2 CLIP+text | x seen | 448 | 0.430 | 0.463 | 0.358 | 0.425 |
| B2 CLIP+text | q unseen | 573 | 0.457 | 0.497 | 0.356 | 0.404 |
| B6 plain CLIP | all | 1000 | 0.548 | 0.622 | 0.316 | 0.387 |
| B6 plain CLIP | x unseen | 552 | 0.614 | 0.704 | 0.312 | 0.381 |
| B6 plain CLIP | x seen | 448 | 0.467 | 0.521 | 0.321 | 0.394 |
| B6 plain CLIP | q unseen | 573 | 0.540 | 0.611 | 0.312 | 0.387 |
| B3 separate | all | 1000 | 0.757 | 0.841 | 0.565 | 0.569 |
| B3 separate | x unseen | 552 | 0.731 | 0.825 | 0.536 | 0.520 |
| B3 separate | x seen | 448 | 0.789 | 0.861 | 0.602 | 0.634 |
| B3 separate | q unseen | 573 | 0.751 | 0.834 | 0.558 | 0.545 |
| B4 CSN | all | 1000 | 0.752 | 0.837 | 0.555 | 0.574 |
| B4 CSN | x unseen | 552 | 0.725 | 0.819 | 0.524 | 0.531 |
| B4 CSN | x seen | 448 | 0.786 | 0.859 | 0.593 | 0.631 |
| B4 CSN | q unseen | 573 | 0.747 | 0.831 | 0.543 | 0.547 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.652 | 0.151 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.652 | 0.150 |
| A same-habitat/diff-order | SSE-treeSC-256 | 144 | 0.652 | 0.145 |
| A same-habitat/diff-order | SSE-treeSC-128 | 144 | 0.652 | 0.151 |
| A same-habitat/diff-order | B1 labels | 144 | 0.652 | 0.348 |
| A same-habitat/diff-order | B1-soft | 144 | 0.652 | 0.269 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.652 | 0.396 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.652 | 0.347 |
| A same-habitat/diff-order | B3 separate | 144 | 0.652 | 0.147 |
| A same-habitat/diff-order | B4 CSN | 144 | 0.652 | 0.157 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.145 | 0.120 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.145 | 0.121 |
| B same-family/diff-habitat | SSE-treeSC-256 | 24 | 0.145 | 0.122 |
| B same-family/diff-habitat | SSE-treeSC-128 | 24 | 0.145 | 0.125 |
| B same-family/diff-habitat | B1 labels | 24 | 0.145 | 0.539 |
| B same-family/diff-habitat | B1-soft | 24 | 0.145 | 0.297 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.145 | 0.191 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.145 | 0.204 |
| B same-family/diff-habitat | B3 separate | 24 | 0.145 | 0.127 |
| B same-family/diff-habitat | B4 CSN | 24 | 0.145 | 0.135 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE-treeSC | order@8 | 0.959 | 0.937 | 0.927 |
| SSE-treeSC | family@32 | 0.945 | 0.997 | 0.986 |
| SSE-treeSC | genus@64 | 0.923 | 0.992 | 0.996 |
| SSE-tree | order@8 | 0.958 | 0.943 | 0.934 |
| SSE-tree | family@32 | 0.955 | 0.996 | 0.985 |
| SSE-tree | genus@64 | 0.941 | 0.997 | 0.996 |
| SSE-treeSC-256 | order@8 | 0.962 | 0.934 | 0.925 |
| SSE-treeSC-256 | family@32 | 0.945 | 0.997 | 0.985 |
| SSE-treeSC-256 | genus@64 | 0.923 | 0.992 | 0.996 |
| SSE-treeSC-128 | order@8 | 0.961 | 0.936 | 0.929 |
| SSE-treeSC-128 | family@32 | 0.948 | 0.997 | 0.986 |
| SSE-treeSC-128 | genus@64 | 0.921 | 0.992 | 0.996 |
| B1 labels | family view | 0.960 | 0.985 | 0.978 |
| B1-soft | family view | 0.821 | 0.993 | 0.979 |
| B2 CLIP+text | family view | 0.635 | 0.796 | 0.854 |
| B6 plain CLIP | family view | 0.628 | 0.839 | 0.935 |
| B3 separate | order@8 | 0.960 | 0.942 | 0.932 |
| B3 separate | family@32 | 0.956 | 0.997 | 0.985 |
| B3 separate | genus@64 | 0.941 | 0.997 | 0.996 |
| B4 CSN | order@8 | 0.962 | 0.943 | 0.934 |
| B4 CSN | family@32 | 0.960 | 0.997 | 0.985 |
| B4 CSN | genus@64 | 0.946 | 0.997 | 0.996 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE-treeSC | 0.888 |
| SSE-tree | 0.890 |
| SSE-treeSC-256 | 0.891 |
| SSE-treeSC-128 | 0.888 |
| B1 labels | 0.592 |
| B1-soft | 0.723 |
| B2 CLIP+text | 0.211 |
| B6 plain CLIP | 0.234 |
| B3 separate | 0.893 |
| B4 CSN | 0.887 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE-treeSC | 1.000 | 0.089 | 0.918 |
| SSE-tree | 1.000 | 0.094 | 0.919 |
| SSE-treeSC-256 | 1.000 | 0.101 | 0.915 |
| SSE-treeSC-128 | 1.000 | 0.100 | 0.911 |
| B1 labels | 0.903 | 0.381 | 0.763 |
| B1-soft | 1.000 | 0.155 | 0.881 |
| B2 CLIP+text | 1.000 | 0.443 | 0.775 |
| B6 plain CLIP | 0.927 | 0.428 | 0.838 |
| B3 separate | 1.000 | 0.088 | 0.925 |
| B4 CSN | 1.000 | 0.089 | 0.917 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE-treeSC | 4 | order | 0.964 |
| seen_test | SSE-treeSC | 4 | family | 0.505 |
| seen_test | SSE-treeSC | 4 | genus | 0.363 |
| seen_test | SSE-treeSC | 8 | order | 0.995 |
| seen_test | SSE-treeSC | 8 | family | 0.526 |
| seen_test | SSE-treeSC | 8 | genus | 0.381 |
| seen_test | SSE-treeSC | 16 | order | 0.994 |
| seen_test | SSE-treeSC | 16 | family | 0.961 |
| seen_test | SSE-treeSC | 16 | genus | 0.705 |
| seen_test | SSE-treeSC | 32 | order | 0.989 |
| seen_test | SSE-treeSC | 32 | family | 0.989 |
| seen_test | SSE-treeSC | 32 | genus | 0.736 |
| seen_test | SSE-treeSC | 64 | order | 0.982 |
| seen_test | SSE-treeSC | 64 | family | 0.967 |
| seen_test | SSE-treeSC | 64 | genus | 0.987 |
| seen_test | SSE-tree | 4 | order | 0.985 |
| seen_test | SSE-tree | 4 | family | 0.519 |
| seen_test | SSE-tree | 4 | genus | 0.376 |
| seen_test | SSE-tree | 8 | order | 0.995 |
| seen_test | SSE-tree | 8 | family | 0.532 |
| seen_test | SSE-tree | 8 | genus | 0.385 |
| seen_test | SSE-tree | 16 | order | 0.994 |
| seen_test | SSE-tree | 16 | family | 0.948 |
| seen_test | SSE-tree | 16 | genus | 0.707 |
| seen_test | SSE-tree | 32 | order | 0.992 |
| seen_test | SSE-tree | 32 | family | 0.983 |
| seen_test | SSE-tree | 32 | genus | 0.743 |
| seen_test | SSE-tree | 64 | order | 0.988 |
| seen_test | SSE-tree | 64 | family | 0.983 |
| seen_test | SSE-tree | 64 | genus | 0.978 |
| seen_test | SSE-treeSC-256 | 4 | order | 0.944 |
| seen_test | SSE-treeSC-256 | 4 | family | 0.498 |
| seen_test | SSE-treeSC-256 | 4 | genus | 0.366 |
| seen_test | SSE-treeSC-256 | 8 | order | 0.995 |
| seen_test | SSE-treeSC-256 | 8 | family | 0.525 |
| seen_test | SSE-treeSC-256 | 8 | genus | 0.381 |
| seen_test | SSE-treeSC-256 | 16 | order | 0.993 |
| seen_test | SSE-treeSC-256 | 16 | family | 0.975 |
| seen_test | SSE-treeSC-256 | 16 | genus | 0.716 |
| seen_test | SSE-treeSC-256 | 32 | order | 0.989 |
| seen_test | SSE-treeSC-256 | 32 | family | 0.989 |
| seen_test | SSE-treeSC-256 | 32 | genus | 0.735 |
| seen_test | SSE-treeSC-256 | 64 | order | 0.982 |
| seen_test | SSE-treeSC-256 | 64 | family | 0.967 |
| seen_test | SSE-treeSC-256 | 64 | genus | 0.987 |
| seen_test | SSE-treeSC-128 | 4 | order | 0.985 |
| seen_test | SSE-treeSC-128 | 4 | family | 0.512 |
| seen_test | SSE-treeSC-128 | 4 | genus | 0.367 |
| seen_test | SSE-treeSC-128 | 8 | order | 0.995 |
| seen_test | SSE-treeSC-128 | 8 | family | 0.527 |
| seen_test | SSE-treeSC-128 | 8 | genus | 0.382 |
| seen_test | SSE-treeSC-128 | 16 | order | 0.993 |
| seen_test | SSE-treeSC-128 | 16 | family | 0.980 |
| seen_test | SSE-treeSC-128 | 16 | genus | 0.713 |
| seen_test | SSE-treeSC-128 | 32 | order | 0.989 |
| seen_test | SSE-treeSC-128 | 32 | family | 0.989 |
| seen_test | SSE-treeSC-128 | 32 | genus | 0.735 |
| seen_test | SSE-treeSC-128 | 64 | order | 0.982 |
| seen_test | SSE-treeSC-128 | 64 | family | 0.967 |
| seen_test | SSE-treeSC-128 | 64 | genus | 0.987 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.567 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.674 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.840 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.692 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.850 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.984 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.697 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.857 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.986 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.738 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.876 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.987 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.743 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.880 |
| seen_test | SSE-MRL (genus everywhere) | 64 | genus | 0.987 |
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
| unseen | SSE-treeSC | 4 | order | 0.826 |
| unseen | SSE-treeSC | 4 | family | 0.571 |
| unseen | SSE-treeSC | 4 | genus | 0.567 |
| unseen | SSE-treeSC | 8 | order | 0.933 |
| unseen | SSE-treeSC | 8 | family | 0.801 |
| unseen | SSE-treeSC | 8 | genus | 0.806 |
| unseen | SSE-treeSC | 16 | order | 0.944 |
| unseen | SSE-treeSC | 16 | family | 0.929 |
| unseen | SSE-treeSC | 16 | genus | 0.925 |
| unseen | SSE-treeSC | 32 | order | 0.916 |
| unseen | SSE-treeSC | 32 | family | 0.978 |
| unseen | SSE-treeSC | 32 | genus | 0.966 |
| unseen | SSE-treeSC | 64 | order | 0.890 |
| unseen | SSE-treeSC | 64 | family | 0.981 |
| unseen | SSE-treeSC | 64 | genus | 0.983 |
| unseen | SSE-tree | 4 | order | 0.820 |
| unseen | SSE-tree | 4 | family | 0.569 |
| unseen | SSE-tree | 4 | genus | 0.563 |
| unseen | SSE-tree | 8 | order | 0.942 |
| unseen | SSE-tree | 8 | family | 0.836 |
| unseen | SSE-tree | 8 | genus | 0.832 |
| unseen | SSE-tree | 16 | order | 0.947 |
| unseen | SSE-tree | 16 | family | 0.932 |
| unseen | SSE-tree | 16 | genus | 0.930 |
| unseen | SSE-tree | 32 | order | 0.961 |
| unseen | SSE-tree | 32 | family | 0.981 |
| unseen | SSE-tree | 32 | genus | 0.973 |
| unseen | SSE-tree | 64 | order | 0.947 |
| unseen | SSE-tree | 64 | family | 0.989 |
| unseen | SSE-tree | 64 | genus | 0.988 |
| unseen | SSE-treeSC-256 | 4 | order | 0.911 |
| unseen | SSE-treeSC-256 | 4 | family | 0.664 |
| unseen | SSE-treeSC-256 | 4 | genus | 0.639 |
| unseen | SSE-treeSC-256 | 8 | order | 0.938 |
| unseen | SSE-treeSC-256 | 8 | family | 0.781 |
| unseen | SSE-treeSC-256 | 8 | genus | 0.791 |
| unseen | SSE-treeSC-256 | 16 | order | 0.920 |
| unseen | SSE-treeSC-256 | 16 | family | 0.959 |
| unseen | SSE-treeSC-256 | 16 | genus | 0.946 |
| unseen | SSE-treeSC-256 | 32 | order | 0.913 |
| unseen | SSE-treeSC-256 | 32 | family | 0.977 |
| unseen | SSE-treeSC-256 | 32 | genus | 0.964 |
| unseen | SSE-treeSC-256 | 64 | order | 0.889 |
| unseen | SSE-treeSC-256 | 64 | family | 0.983 |
| unseen | SSE-treeSC-256 | 64 | genus | 0.984 |
| unseen | SSE-treeSC-128 | 4 | order | 0.892 |
| unseen | SSE-treeSC-128 | 4 | family | 0.644 |
| unseen | SSE-treeSC-128 | 4 | genus | 0.627 |
| unseen | SSE-treeSC-128 | 8 | order | 0.935 |
| unseen | SSE-treeSC-128 | 8 | family | 0.800 |
| unseen | SSE-treeSC-128 | 8 | genus | 0.812 |
| unseen | SSE-treeSC-128 | 16 | order | 0.910 |
| unseen | SSE-treeSC-128 | 16 | family | 0.951 |
| unseen | SSE-treeSC-128 | 16 | genus | 0.932 |
| unseen | SSE-treeSC-128 | 32 | order | 0.920 |
| unseen | SSE-treeSC-128 | 32 | family | 0.977 |
| unseen | SSE-treeSC-128 | 32 | genus | 0.966 |
| unseen | SSE-treeSC-128 | 64 | order | 0.890 |
| unseen | SSE-treeSC-128 | 64 | family | 0.984 |
| unseen | SSE-treeSC-128 | 64 | genus | 0.985 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.672 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.622 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.670 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.766 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.894 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.903 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.770 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.928 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.939 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.770 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.947 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.960 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.774 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.950 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.964 |
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
