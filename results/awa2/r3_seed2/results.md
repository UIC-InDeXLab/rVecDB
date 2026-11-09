# AwA2 results r3_seed2

args: `{'sse': 'SSE=main_wp0.5_s2,SSE-tree=tree_s2,SSE-treeSC=treesc_s2', 'mrl': 'mrl_s2', 'out': 'r3_seed2', 'no_baselines': False, 'seed': 2}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.902 | 0.418 | 0.310 |
| SSE | diet | 0.454 | 0.868 | 0.432 |
| SSE | family | 0.442 | 0.323 | 0.529 |
| SSE | tax | 0.441 | 0.313 | 0.422 |
| SSE | rest | 0.154 | 0.126 | 0.151 |
| SSE | full | 0.317 | 0.296 | 0.260 |
| SSE-tree | habitat | 0.903 | 0.416 | 0.310 |
| SSE-tree | diet | 0.453 | 0.868 | 0.434 |
| SSE-tree | family | 0.274 | 0.374 | 0.721 |
| SSE-tree | tax | 0.292 | 0.378 | 0.703 |
| SSE-tree | rest | 0.155 | 0.122 | 0.138 |
| SSE-treeSC | habitat | 0.903 | 0.415 | 0.309 |
| SSE-treeSC | diet | 0.453 | 0.867 | 0.433 |
| SSE-treeSC | family | 0.308 | 0.377 | 0.710 |
| SSE-treeSC | tax | 0.318 | 0.378 | 0.678 |
| SSE-treeSC | rest | 0.162 | 0.126 | 0.146 |
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

### E3 — general search preserved

| overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|
| 0.841 | 0.819 | 0.823 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 1000 | 0.752 | 0.838 | 0.562 | 0.547 |
| SSE | x unseen | 556 | 0.723 | 0.818 | 0.551 | 0.520 |
| SSE | x seen | 444 | 0.789 | 0.863 | 0.575 | 0.586 |
| SSE | q unseen | 570 | 0.743 | 0.828 | 0.545 | 0.528 |
| SSE-tree | all | 1000 | 0.753 | 0.839 | 0.566 | 0.571 |
| SSE-tree | x unseen | 556 | 0.723 | 0.819 | 0.548 | 0.531 |
| SSE-tree | x seen | 444 | 0.790 | 0.863 | 0.588 | 0.625 |
| SSE-tree | q unseen | 570 | 0.743 | 0.829 | 0.554 | 0.549 |
| SSE-treeSC | all | 1000 | 0.753 | 0.839 | 0.570 | 0.574 |
| SSE-treeSC | x unseen | 556 | 0.724 | 0.820 | 0.556 | 0.538 |
| SSE-treeSC | x seen | 444 | 0.790 | 0.863 | 0.588 | 0.623 |
| SSE-treeSC | q unseen | 570 | 0.744 | 0.829 | 0.560 | 0.554 |
| B1 labels | all | 1000 | 0.483 | 0.521 | 0.356 | 0.384 |
| B1 labels | x unseen | 556 | 0.472 | 0.483 | 0.326 | 0.351 |
| B1 labels | x seen | 444 | 0.498 | 0.567 | 0.393 | 0.429 |
| B1 labels | q unseen | 570 | 0.471 | 0.509 | 0.353 | 0.386 |
| B1-soft | all | 1000 | 0.665 | 0.744 | 0.436 | 0.462 |
| B1-soft | x unseen | 556 | 0.680 | 0.764 | 0.465 | 0.457 |
| B1-soft | x seen | 444 | 0.646 | 0.718 | 0.401 | 0.468 |
| B1-soft | q unseen | 570 | 0.653 | 0.729 | 0.415 | 0.450 |
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
| A same-habitat/diff-order | SSE | 144 | 0.624 | 0.151 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.624 | 0.151 |
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.624 | 0.151 |
| A same-habitat/diff-order | B1 labels | 144 | 0.624 | 0.341 |
| A same-habitat/diff-order | B1-soft | 144 | 0.624 | 0.252 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.624 | 0.379 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.624 | 0.323 |
| B same-family/diff-habitat | SSE | 24 | 0.165 | 0.145 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.165 | 0.145 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.165 | 0.145 |
| B same-family/diff-habitat | B1 labels | 24 | 0.165 | 0.548 |
| B same-family/diff-habitat | B1-soft | 24 | 0.165 | 0.299 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.165 | 0.192 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE | order@8 | 0.962 | 0.924 | 0.912 |
| SSE | family@32 | 0.820 | 0.995 | 0.982 |
| SSE | genus@64 | 0.746 | 0.970 | 0.994 |
| SSE-tree | order@8 | 0.959 | 0.942 | 0.932 |
| SSE-tree | family@32 | 0.954 | 0.996 | 0.985 |
| SSE-tree | genus@64 | 0.941 | 0.997 | 0.995 |
| SSE-treeSC | order@8 | 0.961 | 0.934 | 0.925 |
| SSE-treeSC | family@32 | 0.946 | 0.997 | 0.986 |
| SSE-treeSC | genus@64 | 0.924 | 0.992 | 0.996 |
| B1 labels | family view | 0.959 | 0.985 | 0.978 |
| B1-soft | family view | 0.821 | 0.993 | 0.979 |
| B2 CLIP+text | family view | 0.635 | 0.796 | 0.854 |
| B6 plain CLIP | family view | 0.628 | 0.839 | 0.934 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.888 |
| SSE-tree | 0.889 |
| SSE-treeSC | 0.889 |
| B1 labels | 0.592 |
| B1-soft | 0.723 |
| B2 CLIP+text | 0.212 |
| B6 plain CLIP | 0.234 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.092 | 0.920 |
| SSE-tree | 1.000 | 0.096 | 0.914 |
| SSE-treeSC | 1.000 | 0.116 | 0.899 |
| B1 labels | 0.903 | 0.361 | 0.776 |
| B1-soft | 1.000 | 0.155 | 0.887 |
| B2 CLIP+text | 0.988 | 0.445 | 0.778 |
| B6 plain CLIP | 0.915 | 0.444 | 0.840 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.988 |
| seen_test | SSE | 4 | family | 0.527 |
| seen_test | SSE | 4 | genus | 0.393 |
| seen_test | SSE | 8 | order | 0.995 |
| seen_test | SSE | 8 | family | 0.538 |
| seen_test | SSE | 8 | genus | 0.403 |
| seen_test | SSE | 16 | order | 0.939 |
| seen_test | SSE | 16 | family | 0.978 |
| seen_test | SSE | 16 | genus | 0.737 |
| seen_test | SSE | 32 | order | 0.831 |
| seen_test | SSE | 32 | family | 0.985 |
| seen_test | SSE | 32 | genus | 0.753 |
| seen_test | SSE | 64 | order | 0.759 |
| seen_test | SSE | 64 | family | 0.903 |
| seen_test | SSE | 64 | genus | 0.985 |
| seen_test | SSE-tree | 4 | order | 0.978 |
| seen_test | SSE-tree | 4 | family | 0.531 |
| seen_test | SSE-tree | 4 | genus | 0.394 |
| seen_test | SSE-tree | 8 | order | 0.992 |
| seen_test | SSE-tree | 8 | family | 0.549 |
| seen_test | SSE-tree | 8 | genus | 0.412 |
| seen_test | SSE-tree | 16 | order | 0.989 |
| seen_test | SSE-tree | 16 | family | 0.952 |
| seen_test | SSE-tree | 16 | genus | 0.740 |
| seen_test | SSE-tree | 32 | order | 0.987 |
| seen_test | SSE-tree | 32 | family | 0.974 |
| seen_test | SSE-tree | 32 | genus | 0.771 |
| seen_test | SSE-tree | 64 | order | 0.981 |
| seen_test | SSE-tree | 64 | family | 0.974 |
| seen_test | SSE-tree | 64 | genus | 0.970 |
| seen_test | SSE-treeSC | 4 | order | 0.983 |
| seen_test | SSE-treeSC | 4 | family | 0.527 |
| seen_test | SSE-treeSC | 4 | genus | 0.391 |
| seen_test | SSE-treeSC | 8 | order | 0.994 |
| seen_test | SSE-treeSC | 8 | family | 0.543 |
| seen_test | SSE-treeSC | 8 | genus | 0.406 |
| seen_test | SSE-treeSC | 16 | order | 0.989 |
| seen_test | SSE-treeSC | 16 | family | 0.972 |
| seen_test | SSE-treeSC | 16 | genus | 0.737 |
| seen_test | SSE-treeSC | 32 | order | 0.982 |
| seen_test | SSE-treeSC | 32 | family | 0.984 |
| seen_test | SSE-treeSC | 32 | genus | 0.755 |
| seen_test | SSE-treeSC | 64 | order | 0.974 |
| seen_test | SSE-treeSC | 64 | family | 0.962 |
| seen_test | SSE-treeSC | 64 | genus | 0.984 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.579 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.707 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.808 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.696 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.848 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.981 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.740 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.870 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.983 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.748 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.884 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.984 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.744 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.886 |
| seen_test | SSE-MRL (genus everywhere) | 64 | genus | 0.984 |
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
| unseen | SSE | 4 | order | 0.869 |
| unseen | SSE | 4 | family | 0.655 |
| unseen | SSE | 4 | genus | 0.630 |
| unseen | SSE | 8 | order | 0.893 |
| unseen | SSE | 8 | family | 0.756 |
| unseen | SSE | 8 | genus | 0.752 |
| unseen | SSE | 16 | order | 0.883 |
| unseen | SSE | 16 | family | 0.948 |
| unseen | SSE | 16 | genus | 0.923 |
| unseen | SSE | 32 | order | 0.838 |
| unseen | SSE | 32 | family | 0.960 |
| unseen | SSE | 32 | genus | 0.942 |
| unseen | SSE | 64 | order | 0.808 |
| unseen | SSE | 64 | family | 0.966 |
| unseen | SSE | 64 | genus | 0.977 |
| unseen | SSE-tree | 4 | order | 0.888 |
| unseen | SSE-tree | 4 | family | 0.736 |
| unseen | SSE-tree | 4 | genus | 0.718 |
| unseen | SSE-tree | 8 | order | 0.941 |
| unseen | SSE-tree | 8 | family | 0.865 |
| unseen | SSE-tree | 8 | genus | 0.857 |
| unseen | SSE-tree | 16 | order | 0.935 |
| unseen | SSE-tree | 16 | family | 0.972 |
| unseen | SSE-tree | 16 | genus | 0.942 |
| unseen | SSE-tree | 32 | order | 0.935 |
| unseen | SSE-tree | 32 | family | 0.986 |
| unseen | SSE-tree | 32 | genus | 0.971 |
| unseen | SSE-tree | 64 | order | 0.930 |
| unseen | SSE-tree | 64 | family | 0.988 |
| unseen | SSE-tree | 64 | genus | 0.986 |
| unseen | SSE-treeSC | 4 | order | 0.904 |
| unseen | SSE-treeSC | 4 | family | 0.650 |
| unseen | SSE-treeSC | 4 | genus | 0.649 |
| unseen | SSE-treeSC | 8 | order | 0.934 |
| unseen | SSE-treeSC | 8 | family | 0.821 |
| unseen | SSE-treeSC | 8 | genus | 0.826 |
| unseen | SSE-treeSC | 16 | order | 0.933 |
| unseen | SSE-treeSC | 16 | family | 0.975 |
| unseen | SSE-treeSC | 16 | genus | 0.956 |
| unseen | SSE-treeSC | 32 | order | 0.909 |
| unseen | SSE-treeSC | 32 | family | 0.984 |
| unseen | SSE-treeSC | 32 | genus | 0.968 |
| unseen | SSE-treeSC | 64 | order | 0.892 |
| unseen | SSE-treeSC | 64 | family | 0.984 |
| unseen | SSE-treeSC | 64 | genus | 0.985 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.687 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.753 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.784 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.774 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.900 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.946 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.783 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.913 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.965 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.791 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.947 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.974 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.795 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.956 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.977 |
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
