# AwA2 results r4b_seed2

args: `{'sse': 'SSE=tree_s2', 'mrl': 'mrl_s2', 'out': 'r4b_seed2', 'no_baselines': False, 'extra': 'B3 separate=b3tree_s2,B4 CSN=csntree_s2', 'seed': 2}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.903 | 0.416 | 0.310 |
| SSE | diet | 0.453 | 0.868 | 0.434 |
| SSE | family | 0.274 | 0.374 | 0.721 |
| SSE | tax | 0.292 | 0.378 | 0.703 |
| SSE | rest | 0.155 | 0.122 | 0.138 |
| SSE | full | 0.318 | 0.299 | 0.265 |
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

| overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|
| 0.855 | 0.819 | 0.824 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 1000 | 0.753 | 0.839 | 0.566 | 0.571 |
| SSE | x unseen | 556 | 0.723 | 0.819 | 0.548 | 0.531 |
| SSE | x seen | 444 | 0.790 | 0.863 | 0.588 | 0.625 |
| SSE | q unseen | 570 | 0.743 | 0.829 | 0.554 | 0.549 |
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
| B3 separate | all | 1000 | 0.756 | 0.840 | 0.557 | 0.582 |
| B3 separate | x unseen | 556 | 0.725 | 0.820 | 0.540 | 0.540 |
| B3 separate | x seen | 444 | 0.793 | 0.866 | 0.579 | 0.639 |
| B3 separate | q unseen | 570 | 0.747 | 0.831 | 0.544 | 0.572 |
| B4 CSN | all | 1000 | 0.753 | 0.839 | 0.559 | 0.580 |
| B4 CSN | x unseen | 556 | 0.725 | 0.821 | 0.542 | 0.543 |
| B4 CSN | x seen | 444 | 0.787 | 0.862 | 0.579 | 0.630 |
| B4 CSN | q unseen | 570 | 0.743 | 0.830 | 0.545 | 0.569 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE | 144 | 0.624 | 0.151 |
| A same-habitat/diff-order | B1 labels | 144 | 0.624 | 0.341 |
| A same-habitat/diff-order | B1-soft | 144 | 0.624 | 0.252 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.624 | 0.379 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.624 | 0.323 |
| A same-habitat/diff-order | B3 separate | 144 | 0.624 | 0.148 |
| A same-habitat/diff-order | B4 CSN | 144 | 0.624 | 0.150 |
| B same-family/diff-habitat | SSE | 24 | 0.165 | 0.145 |
| B same-family/diff-habitat | B1 labels | 24 | 0.165 | 0.548 |
| B same-family/diff-habitat | B1-soft | 24 | 0.165 | 0.299 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.165 | 0.192 |
| B same-family/diff-habitat | B3 separate | 24 | 0.165 | 0.147 |
| B same-family/diff-habitat | B4 CSN | 24 | 0.165 | 0.140 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE | order@8 | 0.959 | 0.942 | 0.932 |
| SSE | family@32 | 0.954 | 0.996 | 0.985 |
| SSE | genus@64 | 0.941 | 0.997 | 0.995 |
| B1 labels | family view | 0.959 | 0.985 | 0.978 |
| B1-soft | family view | 0.821 | 0.993 | 0.979 |
| B2 CLIP+text | family view | 0.635 | 0.796 | 0.854 |
| B6 plain CLIP | family view | 0.628 | 0.839 | 0.934 |
| B3 separate | order@8 | 0.961 | 0.941 | 0.931 |
| B3 separate | family@32 | 0.956 | 0.997 | 0.986 |
| B3 separate | genus@64 | 0.943 | 0.997 | 0.996 |
| B4 CSN | order@8 | 0.961 | 0.943 | 0.932 |
| B4 CSN | family@32 | 0.960 | 0.996 | 0.985 |
| B4 CSN | genus@64 | 0.947 | 0.997 | 0.995 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.889 |
| B1 labels | 0.592 |
| B1-soft | 0.723 |
| B2 CLIP+text | 0.212 |
| B6 plain CLIP | 0.234 |
| B3 separate | 0.892 |
| B4 CSN | 0.888 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.091 | 0.920 |
| B1 labels | 0.903 | 0.355 | 0.790 |
| B1-soft | 1.000 | 0.167 | 0.869 |
| B2 CLIP+text | 1.000 | 0.446 | 0.772 |
| B6 plain CLIP | 0.915 | 0.440 | 0.843 |
| B3 separate | 1.000 | 0.086 | 0.920 |
| B4 CSN | 1.000 | 0.093 | 0.916 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.978 |
| seen_test | SSE | 4 | family | 0.531 |
| seen_test | SSE | 4 | genus | 0.394 |
| seen_test | SSE | 8 | order | 0.992 |
| seen_test | SSE | 8 | family | 0.549 |
| seen_test | SSE | 8 | genus | 0.412 |
| seen_test | SSE | 16 | order | 0.989 |
| seen_test | SSE | 16 | family | 0.952 |
| seen_test | SSE | 16 | genus | 0.740 |
| seen_test | SSE | 32 | order | 0.987 |
| seen_test | SSE | 32 | family | 0.974 |
| seen_test | SSE | 32 | genus | 0.771 |
| seen_test | SSE | 64 | order | 0.981 |
| seen_test | SSE | 64 | family | 0.974 |
| seen_test | SSE | 64 | genus | 0.970 |
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
| unseen | SSE | 4 | order | 0.888 |
| unseen | SSE | 4 | family | 0.736 |
| unseen | SSE | 4 | genus | 0.718 |
| unseen | SSE | 8 | order | 0.941 |
| unseen | SSE | 8 | family | 0.865 |
| unseen | SSE | 8 | genus | 0.857 |
| unseen | SSE | 16 | order | 0.935 |
| unseen | SSE | 16 | family | 0.972 |
| unseen | SSE | 16 | genus | 0.942 |
| unseen | SSE | 32 | order | 0.935 |
| unseen | SSE | 32 | family | 0.986 |
| unseen | SSE | 32 | genus | 0.971 |
| unseen | SSE | 64 | order | 0.930 |
| unseen | SSE | 64 | family | 0.988 |
| unseen | SSE | 64 | genus | 0.986 |
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
