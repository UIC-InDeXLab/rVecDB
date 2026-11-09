# AwA2 results r3_seed1

args: `{'sse': 'SSE=main_wp0.5_s1,SSE-tree=tree_s1,SSE-treeSC=treesc_s1', 'mrl': 'mrl_s1', 'out': 'r3_seed1', 'no_baselines': False, 'seed': 1}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.902 | 0.420 | 0.307 |
| SSE | diet | 0.456 | 0.869 | 0.429 |
| SSE | family | 0.450 | 0.320 | 0.529 |
| SSE | tax | 0.442 | 0.304 | 0.417 |
| SSE | rest | 0.152 | 0.129 | 0.151 |
| SSE | full | 0.319 | 0.301 | 0.260 |
| SSE-tree | habitat | 0.904 | 0.421 | 0.305 |
| SSE-tree | diet | 0.455 | 0.870 | 0.428 |
| SSE-tree | family | 0.288 | 0.382 | 0.723 |
| SSE-tree | tax | 0.299 | 0.385 | 0.703 |
| SSE-tree | rest | 0.156 | 0.125 | 0.140 |
| SSE-treeSC | habitat | 0.903 | 0.420 | 0.305 |
| SSE-treeSC | diet | 0.456 | 0.869 | 0.426 |
| SSE-treeSC | family | 0.305 | 0.381 | 0.710 |
| SSE-treeSC | tax | 0.314 | 0.380 | 0.675 |
| SSE-treeSC | rest | 0.165 | 0.130 | 0.147 |
| B1 labels | habitat | 0.608 | 0.276 | 0.276 |
| B1 labels | diet | 0.260 | 0.588 | 0.284 |
| B1 labels | family | 0.321 | 0.393 | 0.727 |
| B1-soft | habitat | 0.755 | 0.371 | 0.366 |
| B1-soft | diet | 0.409 | 0.786 | 0.349 |
| B1-soft | family | 0.325 | 0.376 | 0.529 |
| B2 CLIP+text | habitat | 0.255 | 0.180 | 0.122 |
| B2 CLIP+text | diet | 0.209 | 0.169 | 0.093 |
| B2 CLIP+text | family | 0.205 | 0.194 | 0.241 |
| B6 plain CLIP | habitat | 0.308 | 0.281 | 0.237 |
| B6 plain CLIP | diet | 0.308 | 0.281 | 0.237 |
| B6 plain CLIP | family | 0.308 | 0.281 | 0.237 |

### E3 — general search preserved

| overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|
| 0.839 | 0.819 | 0.822 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 1000 | 0.751 | 0.837 | 0.560 | 0.552 |
| SSE | x unseen | 556 | 0.720 | 0.814 | 0.552 | 0.525 |
| SSE | x seen | 444 | 0.790 | 0.865 | 0.570 | 0.589 |
| SSE | q unseen | 570 | 0.742 | 0.827 | 0.543 | 0.533 |
| SSE-tree | all | 1000 | 0.752 | 0.837 | 0.568 | 0.588 |
| SSE-tree | x unseen | 556 | 0.721 | 0.815 | 0.553 | 0.550 |
| SSE-tree | x seen | 444 | 0.790 | 0.864 | 0.586 | 0.641 |
| SSE-tree | q unseen | 570 | 0.742 | 0.827 | 0.561 | 0.581 |
| SSE-treeSC | all | 1000 | 0.751 | 0.837 | 0.561 | 0.574 |
| SSE-treeSC | x unseen | 556 | 0.721 | 0.815 | 0.548 | 0.536 |
| SSE-treeSC | x seen | 444 | 0.790 | 0.864 | 0.577 | 0.626 |
| SSE-treeSC | q unseen | 570 | 0.742 | 0.827 | 0.550 | 0.559 |
| B1 labels | all | 1000 | 0.483 | 0.520 | 0.356 | 0.382 |
| B1 labels | x unseen | 556 | 0.471 | 0.483 | 0.326 | 0.349 |
| B1 labels | x seen | 444 | 0.498 | 0.567 | 0.393 | 0.427 |
| B1 labels | q unseen | 570 | 0.471 | 0.509 | 0.353 | 0.384 |
| B1-soft | all | 1000 | 0.665 | 0.744 | 0.436 | 0.462 |
| B1-soft | x unseen | 556 | 0.680 | 0.764 | 0.465 | 0.458 |
| B1-soft | x seen | 444 | 0.646 | 0.718 | 0.401 | 0.468 |
| B1-soft | q unseen | 570 | 0.653 | 0.729 | 0.415 | 0.451 |
| B2 CLIP+text | all | 1000 | 0.474 | 0.520 | 0.374 | 0.409 |
| B2 CLIP+text | x unseen | 556 | 0.501 | 0.556 | 0.382 | 0.404 |
| B2 CLIP+text | x seen | 444 | 0.439 | 0.475 | 0.365 | 0.415 |
| B2 CLIP+text | q unseen | 570 | 0.458 | 0.501 | 0.385 | 0.438 |
| B6 plain CLIP | all | 1000 | 0.554 | 0.630 | 0.332 | 0.398 |
| B6 plain CLIP | x unseen | 556 | 0.616 | 0.707 | 0.338 | 0.397 |
| B6 plain CLIP | x seen | 444 | 0.477 | 0.534 | 0.326 | 0.399 |
| B6 plain CLIP | q unseen | 570 | 0.542 | 0.616 | 0.341 | 0.418 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE | 144 | 0.624 | 0.144 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.624 | 0.142 |
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.624 | 0.142 |
| A same-habitat/diff-order | B1 labels | 144 | 0.624 | 0.340 |
| A same-habitat/diff-order | B1-soft | 144 | 0.624 | 0.252 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.624 | 0.379 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.624 | 0.323 |
| B same-family/diff-habitat | SSE | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.165 | 0.138 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.165 | 0.139 |
| B same-family/diff-habitat | B1 labels | 24 | 0.165 | 0.548 |
| B same-family/diff-habitat | B1-soft | 24 | 0.165 | 0.299 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.165 | 0.192 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE | order@8 | 0.960 | 0.925 | 0.910 |
| SSE | family@32 | 0.820 | 0.995 | 0.982 |
| SSE | genus@64 | 0.743 | 0.968 | 0.994 |
| SSE-tree | order@8 | 0.958 | 0.943 | 0.934 |
| SSE-tree | family@32 | 0.955 | 0.997 | 0.985 |
| SSE-tree | genus@64 | 0.941 | 0.997 | 0.995 |
| SSE-treeSC | order@8 | 0.960 | 0.935 | 0.924 |
| SSE-treeSC | family@32 | 0.946 | 0.997 | 0.986 |
| SSE-treeSC | genus@64 | 0.922 | 0.992 | 0.996 |
| B1 labels | family view | 0.959 | 0.985 | 0.978 |
| B1-soft | family view | 0.821 | 0.993 | 0.979 |
| B2 CLIP+text | family view | 0.635 | 0.796 | 0.854 |
| B6 plain CLIP | family view | 0.628 | 0.839 | 0.934 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.888 |
| SSE-tree | 0.891 |
| SSE-treeSC | 0.890 |
| B1 labels | 0.590 |
| B1-soft | 0.722 |
| B2 CLIP+text | 0.212 |
| B6 plain CLIP | 0.234 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.093 | 0.920 |
| SSE-tree | 1.000 | 0.097 | 0.915 |
| SSE-treeSC | 1.000 | 0.119 | 0.900 |
| B1 labels | 0.903 | 0.361 | 0.775 |
| B1-soft | 1.000 | 0.156 | 0.887 |
| B2 CLIP+text | 0.988 | 0.445 | 0.778 |
| B6 plain CLIP | 0.915 | 0.444 | 0.840 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.989 |
| seen_test | SSE | 4 | family | 0.527 |
| seen_test | SSE | 4 | genus | 0.388 |
| seen_test | SSE | 8 | order | 0.995 |
| seen_test | SSE | 8 | family | 0.538 |
| seen_test | SSE | 8 | genus | 0.404 |
| seen_test | SSE | 16 | order | 0.921 |
| seen_test | SSE | 16 | family | 0.975 |
| seen_test | SSE | 16 | genus | 0.736 |
| seen_test | SSE | 32 | order | 0.825 |
| seen_test | SSE | 32 | family | 0.985 |
| seen_test | SSE | 32 | genus | 0.753 |
| seen_test | SSE | 64 | order | 0.760 |
| seen_test | SSE | 64 | family | 0.903 |
| seen_test | SSE | 64 | genus | 0.984 |
| seen_test | SSE-tree | 4 | order | 0.976 |
| seen_test | SSE-tree | 4 | family | 0.527 |
| seen_test | SSE-tree | 4 | genus | 0.393 |
| seen_test | SSE-tree | 8 | order | 0.990 |
| seen_test | SSE-tree | 8 | family | 0.547 |
| seen_test | SSE-tree | 8 | genus | 0.414 |
| seen_test | SSE-tree | 16 | order | 0.989 |
| seen_test | SSE-tree | 16 | family | 0.958 |
| seen_test | SSE-tree | 16 | genus | 0.744 |
| seen_test | SSE-tree | 32 | order | 0.987 |
| seen_test | SSE-tree | 32 | family | 0.975 |
| seen_test | SSE-tree | 32 | genus | 0.782 |
| seen_test | SSE-tree | 64 | order | 0.981 |
| seen_test | SSE-tree | 64 | family | 0.973 |
| seen_test | SSE-tree | 64 | genus | 0.967 |
| seen_test | SSE-treeSC | 4 | order | 0.990 |
| seen_test | SSE-treeSC | 4 | family | 0.534 |
| seen_test | SSE-treeSC | 4 | genus | 0.394 |
| seen_test | SSE-treeSC | 8 | order | 0.993 |
| seen_test | SSE-treeSC | 8 | family | 0.545 |
| seen_test | SSE-treeSC | 8 | genus | 0.408 |
| seen_test | SSE-treeSC | 16 | order | 0.989 |
| seen_test | SSE-treeSC | 16 | family | 0.972 |
| seen_test | SSE-treeSC | 16 | genus | 0.731 |
| seen_test | SSE-treeSC | 32 | order | 0.982 |
| seen_test | SSE-treeSC | 32 | family | 0.984 |
| seen_test | SSE-treeSC | 32 | genus | 0.756 |
| seen_test | SSE-treeSC | 64 | order | 0.973 |
| seen_test | SSE-treeSC | 64 | family | 0.962 |
| seen_test | SSE-treeSC | 64 | genus | 0.984 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.619 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.723 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.839 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.685 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.847 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.978 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.686 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.849 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.980 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.743 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.884 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.984 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.745 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.887 |
| seen_test | SSE-MRL (genus everywhere) | 64 | genus | 0.985 |
| seen_test | CLIP-PCA | 4 | order | 0.508 |
| seen_test | CLIP-PCA | 4 | family | 0.485 |
| seen_test | CLIP-PCA | 4 | genus | 0.538 |
| seen_test | CLIP-PCA | 8 | order | 0.593 |
| seen_test | CLIP-PCA | 8 | family | 0.607 |
| seen_test | CLIP-PCA | 8 | genus | 0.671 |
| seen_test | CLIP-PCA | 16 | order | 0.641 |
| seen_test | CLIP-PCA | 16 | family | 0.704 |
| seen_test | CLIP-PCA | 16 | genus | 0.779 |
| seen_test | CLIP-PCA | 32 | order | 0.664 |
| seen_test | CLIP-PCA | 32 | family | 0.743 |
| seen_test | CLIP-PCA | 32 | genus | 0.834 |
| seen_test | CLIP-PCA | 64 | order | 0.660 |
| seen_test | CLIP-PCA | 64 | family | 0.739 |
| seen_test | CLIP-PCA | 64 | genus | 0.835 |
| unseen | SSE | 4 | order | 0.865 |
| unseen | SSE | 4 | family | 0.679 |
| unseen | SSE | 4 | genus | 0.658 |
| unseen | SSE | 8 | order | 0.887 |
| unseen | SSE | 8 | family | 0.756 |
| unseen | SSE | 8 | genus | 0.731 |
| unseen | SSE | 16 | order | 0.889 |
| unseen | SSE | 16 | family | 0.943 |
| unseen | SSE | 16 | genus | 0.922 |
| unseen | SSE | 32 | order | 0.839 |
| unseen | SSE | 32 | family | 0.962 |
| unseen | SSE | 32 | genus | 0.940 |
| unseen | SSE | 64 | order | 0.803 |
| unseen | SSE | 64 | family | 0.964 |
| unseen | SSE | 64 | genus | 0.978 |
| unseen | SSE-tree | 4 | order | 0.879 |
| unseen | SSE-tree | 4 | family | 0.665 |
| unseen | SSE-tree | 4 | genus | 0.634 |
| unseen | SSE-tree | 8 | order | 0.942 |
| unseen | SSE-tree | 8 | family | 0.871 |
| unseen | SSE-tree | 8 | genus | 0.863 |
| unseen | SSE-tree | 16 | order | 0.953 |
| unseen | SSE-tree | 16 | family | 0.970 |
| unseen | SSE-tree | 16 | genus | 0.950 |
| unseen | SSE-tree | 32 | order | 0.950 |
| unseen | SSE-tree | 32 | family | 0.988 |
| unseen | SSE-tree | 32 | genus | 0.973 |
| unseen | SSE-tree | 64 | order | 0.938 |
| unseen | SSE-tree | 64 | family | 0.990 |
| unseen | SSE-tree | 64 | genus | 0.988 |
| unseen | SSE-treeSC | 4 | order | 0.891 |
| unseen | SSE-treeSC | 4 | family | 0.715 |
| unseen | SSE-treeSC | 4 | genus | 0.690 |
| unseen | SSE-treeSC | 8 | order | 0.931 |
| unseen | SSE-treeSC | 8 | family | 0.820 |
| unseen | SSE-treeSC | 8 | genus | 0.814 |
| unseen | SSE-treeSC | 16 | order | 0.943 |
| unseen | SSE-treeSC | 16 | family | 0.974 |
| unseen | SSE-treeSC | 16 | genus | 0.955 |
| unseen | SSE-treeSC | 32 | order | 0.914 |
| unseen | SSE-treeSC | 32 | family | 0.984 |
| unseen | SSE-treeSC | 32 | genus | 0.968 |
| unseen | SSE-treeSC | 64 | order | 0.891 |
| unseen | SSE-treeSC | 64 | family | 0.985 |
| unseen | SSE-treeSC | 64 | genus | 0.986 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.759 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.801 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.785 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.798 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.919 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.932 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.801 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.947 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.958 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.790 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.960 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.975 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.789 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.962 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.976 |
| unseen | CLIP-PCA | 4 | order | 0.594 |
| unseen | CLIP-PCA | 4 | family | 0.619 |
| unseen | CLIP-PCA | 4 | genus | 0.685 |
| unseen | CLIP-PCA | 8 | order | 0.646 |
| unseen | CLIP-PCA | 8 | family | 0.696 |
| unseen | CLIP-PCA | 8 | genus | 0.766 |
| unseen | CLIP-PCA | 16 | order | 0.706 |
| unseen | CLIP-PCA | 16 | family | 0.809 |
| unseen | CLIP-PCA | 16 | genus | 0.862 |
| unseen | CLIP-PCA | 32 | order | 0.740 |
| unseen | CLIP-PCA | 32 | family | 0.864 |
| unseen | CLIP-PCA | 32 | genus | 0.910 |
| unseen | CLIP-PCA | 64 | order | 0.758 |
| unseen | CLIP-PCA | 64 | family | 0.889 |
| unseen | CLIP-PCA | 64 | genus | 0.938 |
