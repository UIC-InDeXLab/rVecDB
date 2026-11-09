# AwA2 results r3_seed0

args: `{'sse': 'SSE=main_wp0.5_s0,SSE-tree=tree_s0,SSE-treeSC=treesc_s0', 'mrl': 'mrl_s0', 'out': 'r3_seed0', 'no_baselines': False, 'seed': 0}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.901 | 0.421 | 0.307 |
| SSE | diet | 0.454 | 0.865 | 0.431 |
| SSE | family | 0.455 | 0.314 | 0.527 |
| SSE | tax | 0.443 | 0.311 | 0.421 |
| SSE | rest | 0.151 | 0.132 | 0.151 |
| SSE | full | 0.318 | 0.300 | 0.259 |
| SSE-tree | habitat | 0.903 | 0.422 | 0.308 |
| SSE-tree | diet | 0.453 | 0.866 | 0.432 |
| SSE-tree | family | 0.295 | 0.378 | 0.723 |
| SSE-tree | tax | 0.293 | 0.389 | 0.704 |
| SSE-tree | rest | 0.157 | 0.129 | 0.136 |
| SSE-treeSC | habitat | 0.902 | 0.421 | 0.307 |
| SSE-treeSC | diet | 0.454 | 0.866 | 0.430 |
| SSE-treeSC | family | 0.311 | 0.378 | 0.709 |
| SSE-treeSC | tax | 0.324 | 0.386 | 0.678 |
| SSE-treeSC | rest | 0.164 | 0.133 | 0.143 |
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

### E3 — general search preserved

| overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|
| 0.838 | 0.819 | 0.821 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 1000 | 0.753 | 0.838 | 0.560 | 0.548 |
| SSE | x unseen | 556 | 0.722 | 0.815 | 0.546 | 0.522 |
| SSE | x seen | 444 | 0.792 | 0.867 | 0.579 | 0.584 |
| SSE | q unseen | 570 | 0.745 | 0.829 | 0.537 | 0.526 |
| SSE-tree | all | 1000 | 0.754 | 0.839 | 0.557 | 0.579 |
| SSE-tree | x unseen | 556 | 0.725 | 0.818 | 0.539 | 0.546 |
| SSE-tree | x seen | 444 | 0.792 | 0.867 | 0.579 | 0.625 |
| SSE-tree | q unseen | 570 | 0.746 | 0.830 | 0.543 | 0.562 |
| SSE-treeSC | all | 1000 | 0.754 | 0.839 | 0.562 | 0.576 |
| SSE-treeSC | x unseen | 556 | 0.724 | 0.817 | 0.540 | 0.540 |
| SSE-treeSC | x seen | 444 | 0.792 | 0.867 | 0.589 | 0.625 |
| SSE-treeSC | q unseen | 570 | 0.745 | 0.830 | 0.551 | 0.554 |
| B1 labels | all | 1000 | 0.485 | 0.522 | 0.357 | 0.386 |
| B1 labels | x unseen | 556 | 0.473 | 0.484 | 0.327 | 0.352 |
| B1 labels | x seen | 444 | 0.500 | 0.570 | 0.396 | 0.433 |
| B1 labels | q unseen | 570 | 0.472 | 0.510 | 0.352 | 0.386 |
| B1-soft | all | 1000 | 0.665 | 0.744 | 0.437 | 0.462 |
| B1-soft | x unseen | 556 | 0.679 | 0.764 | 0.466 | 0.458 |
| B1-soft | x seen | 444 | 0.646 | 0.719 | 0.401 | 0.468 |
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
| A same-habitat/diff-order | SSE | 144 | 0.624 | 0.147 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.624 | 0.147 |
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.624 | 0.147 |
| A same-habitat/diff-order | B1 labels | 144 | 0.624 | 0.338 |
| A same-habitat/diff-order | B1-soft | 144 | 0.624 | 0.252 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.624 | 0.379 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.624 | 0.323 |
| B same-family/diff-habitat | SSE | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.165 | 0.139 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.165 | 0.140 |
| B same-family/diff-habitat | B1 labels | 24 | 0.165 | 0.548 |
| B same-family/diff-habitat | B1-soft | 24 | 0.165 | 0.300 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.165 | 0.192 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE | order@8 | 0.961 | 0.925 | 0.909 |
| SSE | family@32 | 0.818 | 0.995 | 0.982 |
| SSE | genus@64 | 0.745 | 0.968 | 0.994 |
| SSE-tree | order@8 | 0.958 | 0.943 | 0.935 |
| SSE-tree | family@32 | 0.955 | 0.996 | 0.985 |
| SSE-tree | genus@64 | 0.941 | 0.997 | 0.996 |
| SSE-treeSC | order@8 | 0.959 | 0.937 | 0.927 |
| SSE-treeSC | family@32 | 0.946 | 0.997 | 0.986 |
| SSE-treeSC | genus@64 | 0.923 | 0.992 | 0.996 |
| B1 labels | family view | 0.960 | 0.985 | 0.978 |
| B1-soft | family view | 0.821 | 0.993 | 0.979 |
| B2 CLIP+text | family view | 0.635 | 0.796 | 0.854 |
| B6 plain CLIP | family view | 0.628 | 0.839 | 0.934 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.888 |
| SSE-tree | 0.890 |
| SSE-treeSC | 0.888 |
| B1 labels | 0.592 |
| B1-soft | 0.723 |
| B2 CLIP+text | 0.212 |
| B6 plain CLIP | 0.234 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.092 | 0.920 |
| SSE-tree | 1.000 | 0.096 | 0.915 |
| SSE-treeSC | 1.000 | 0.117 | 0.898 |
| B1 labels | 0.903 | 0.361 | 0.776 |
| B1-soft | 1.000 | 0.156 | 0.887 |
| B2 CLIP+text | 0.988 | 0.445 | 0.778 |
| B6 plain CLIP | 0.915 | 0.444 | 0.840 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.950 |
| seen_test | SSE | 4 | family | 0.511 |
| seen_test | SSE | 4 | genus | 0.382 |
| seen_test | SSE | 8 | order | 0.995 |
| seen_test | SSE | 8 | family | 0.539 |
| seen_test | SSE | 8 | genus | 0.407 |
| seen_test | SSE | 16 | order | 0.916 |
| seen_test | SSE | 16 | family | 0.970 |
| seen_test | SSE | 16 | genus | 0.735 |
| seen_test | SSE | 32 | order | 0.828 |
| seen_test | SSE | 32 | family | 0.984 |
| seen_test | SSE | 32 | genus | 0.754 |
| seen_test | SSE | 64 | order | 0.761 |
| seen_test | SSE | 64 | family | 0.902 |
| seen_test | SSE | 64 | genus | 0.985 |
| seen_test | SSE-tree | 4 | order | 0.969 |
| seen_test | SSE-tree | 4 | family | 0.529 |
| seen_test | SSE-tree | 4 | genus | 0.396 |
| seen_test | SSE-tree | 8 | order | 0.989 |
| seen_test | SSE-tree | 8 | family | 0.545 |
| seen_test | SSE-tree | 8 | genus | 0.408 |
| seen_test | SSE-tree | 16 | order | 0.989 |
| seen_test | SSE-tree | 16 | family | 0.938 |
| seen_test | SSE-tree | 16 | genus | 0.730 |
| seen_test | SSE-tree | 32 | order | 0.986 |
| seen_test | SSE-tree | 32 | family | 0.974 |
| seen_test | SSE-tree | 32 | genus | 0.766 |
| seen_test | SSE-tree | 64 | order | 0.981 |
| seen_test | SSE-tree | 64 | family | 0.977 |
| seen_test | SSE-tree | 64 | genus | 0.972 |
| seen_test | SSE-treeSC | 4 | order | 0.951 |
| seen_test | SSE-treeSC | 4 | family | 0.519 |
| seen_test | SSE-treeSC | 4 | genus | 0.387 |
| seen_test | SSE-treeSC | 8 | order | 0.994 |
| seen_test | SSE-treeSC | 8 | family | 0.543 |
| seen_test | SSE-treeSC | 8 | genus | 0.407 |
| seen_test | SSE-treeSC | 16 | order | 0.988 |
| seen_test | SSE-treeSC | 16 | family | 0.955 |
| seen_test | SSE-treeSC | 16 | genus | 0.727 |
| seen_test | SSE-treeSC | 32 | order | 0.982 |
| seen_test | SSE-treeSC | 32 | family | 0.984 |
| seen_test | SSE-treeSC | 32 | genus | 0.757 |
| seen_test | SSE-treeSC | 64 | order | 0.974 |
| seen_test | SSE-treeSC | 64 | family | 0.962 |
| seen_test | SSE-treeSC | 64 | genus | 0.984 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.562 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.681 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.836 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.691 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.854 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.978 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.695 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.857 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.979 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.741 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.882 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.983 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.747 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.887 |
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
| unseen | SSE | 4 | order | 0.759 |
| unseen | SSE | 4 | family | 0.531 |
| unseen | SSE | 4 | genus | 0.498 |
| unseen | SSE | 8 | order | 0.890 |
| unseen | SSE | 8 | family | 0.745 |
| unseen | SSE | 8 | genus | 0.715 |
| unseen | SSE | 16 | order | 0.885 |
| unseen | SSE | 16 | family | 0.904 |
| unseen | SSE | 16 | genus | 0.890 |
| unseen | SSE | 32 | order | 0.836 |
| unseen | SSE | 32 | family | 0.959 |
| unseen | SSE | 32 | genus | 0.940 |
| unseen | SSE | 64 | order | 0.804 |
| unseen | SSE | 64 | family | 0.961 |
| unseen | SSE | 64 | genus | 0.976 |
| unseen | SSE-tree | 4 | order | 0.806 |
| unseen | SSE-tree | 4 | family | 0.594 |
| unseen | SSE-tree | 4 | genus | 0.585 |
| unseen | SSE-tree | 8 | order | 0.942 |
| unseen | SSE-tree | 8 | family | 0.876 |
| unseen | SSE-tree | 8 | genus | 0.866 |
| unseen | SSE-tree | 16 | order | 0.944 |
| unseen | SSE-tree | 16 | family | 0.950 |
| unseen | SSE-tree | 16 | genus | 0.946 |
| unseen | SSE-tree | 32 | order | 0.956 |
| unseen | SSE-tree | 32 | family | 0.986 |
| unseen | SSE-tree | 32 | genus | 0.973 |
| unseen | SSE-tree | 64 | order | 0.942 |
| unseen | SSE-tree | 64 | family | 0.990 |
| unseen | SSE-tree | 64 | genus | 0.986 |
| unseen | SSE-treeSC | 4 | order | 0.816 |
| unseen | SSE-treeSC | 4 | family | 0.601 |
| unseen | SSE-treeSC | 4 | genus | 0.598 |
| unseen | SSE-treeSC | 8 | order | 0.935 |
| unseen | SSE-treeSC | 8 | family | 0.839 |
| unseen | SSE-treeSC | 8 | genus | 0.842 |
| unseen | SSE-treeSC | 16 | order | 0.940 |
| unseen | SSE-treeSC | 16 | family | 0.947 |
| unseen | SSE-treeSC | 16 | genus | 0.943 |
| unseen | SSE-treeSC | 32 | order | 0.915 |
| unseen | SSE-treeSC | 32 | family | 0.985 |
| unseen | SSE-treeSC | 32 | genus | 0.969 |
| unseen | SSE-treeSC | 64 | order | 0.891 |
| unseen | SSE-treeSC | 64 | family | 0.984 |
| unseen | SSE-treeSC | 64 | genus | 0.985 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.668 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.632 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.683 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.776 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.909 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.921 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.786 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.941 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.954 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.788 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.957 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.972 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.791 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.959 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.975 |
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
