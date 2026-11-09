# AwA2 results seed1

args: `{'sse': 'SSE=main_wp0.5_s1,SSE-wp1=main_wp1_s1,SSE-wp2=main_wp2_s1,SSE-hard=hard_s1,SSE-hardJ=hardj_s1', 'mrl': 'mrl_s1', 'out': 'seed1', 'no_baselines': False, 'seed': 1}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.902 | 0.420 | 0.307 |
| SSE | diet | 0.456 | 0.869 | 0.429 |
| SSE | family | 0.450 | 0.320 | 0.529 |
| SSE | tax | 0.442 | 0.304 | 0.417 |
| SSE | rest | 0.152 | 0.129 | 0.151 |
| SSE | full | 0.319 | 0.301 | 0.260 |
| SSE-wp1 | habitat | 0.901 | 0.420 | 0.306 |
| SSE-wp1 | diet | 0.456 | 0.869 | 0.427 |
| SSE-wp1 | family | 0.450 | 0.320 | 0.529 |
| SSE-wp1 | tax | 0.442 | 0.304 | 0.417 |
| SSE-wp1 | rest | 0.155 | 0.131 | 0.151 |
| SSE-wp2 | habitat | 0.901 | 0.420 | 0.306 |
| SSE-wp2 | diet | 0.455 | 0.869 | 0.427 |
| SSE-wp2 | family | 0.449 | 0.320 | 0.529 |
| SSE-wp2 | tax | 0.442 | 0.303 | 0.417 |
| SSE-wp2 | rest | 0.156 | 0.132 | 0.151 |
| SSE-hard | habitat | 0.347 | 0.244 | 0.206 |
| SSE-hard | diet | 0.398 | 0.707 | 0.249 |
| SSE-hard | family | 0.449 | 0.320 | 0.530 |
| SSE-hard | tax | 0.443 | 0.304 | 0.417 |
| SSE-hard | rest | 0.219 | 0.174 | 0.164 |
| SSE-hardJ | habitat | 0.680 | 0.368 | 0.241 |
| SSE-hardJ | diet | 0.405 | 0.727 | 0.322 |
| SSE-hardJ | family | 0.450 | 0.321 | 0.530 |
| SSE-hardJ | tax | 0.443 | 0.304 | 0.417 |
| SSE-hardJ | rest | 0.193 | 0.159 | 0.158 |
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
| SSE-wp1 | all | 1000 | 0.751 | 0.836 | 0.560 | 0.552 |
| SSE-wp1 | x unseen | 556 | 0.720 | 0.814 | 0.552 | 0.524 |
| SSE-wp1 | x seen | 444 | 0.790 | 0.864 | 0.570 | 0.590 |
| SSE-wp1 | q unseen | 570 | 0.741 | 0.826 | 0.543 | 0.533 |
| SSE-wp2 | all | 1000 | 0.751 | 0.836 | 0.558 | 0.551 |
| SSE-wp2 | x unseen | 556 | 0.720 | 0.813 | 0.550 | 0.523 |
| SSE-wp2 | x seen | 444 | 0.790 | 0.864 | 0.567 | 0.589 |
| SSE-wp2 | q unseen | 570 | 0.741 | 0.826 | 0.541 | 0.533 |
| SSE-hard | all | 1000 | 0.549 | 0.629 | 0.379 | 0.436 |
| SSE-hard | x unseen | 556 | 0.594 | 0.694 | 0.416 | 0.451 |
| SSE-hard | x seen | 444 | 0.493 | 0.546 | 0.332 | 0.415 |
| SSE-hard | q unseen | 570 | 0.540 | 0.615 | 0.366 | 0.436 |
| SSE-hardJ | all | 1000 | 0.643 | 0.719 | 0.436 | 0.465 |
| SSE-hardJ | x unseen | 556 | 0.652 | 0.744 | 0.458 | 0.470 |
| SSE-hardJ | x seen | 444 | 0.631 | 0.687 | 0.410 | 0.459 |
| SSE-hardJ | q unseen | 570 | 0.627 | 0.701 | 0.424 | 0.469 |
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
| A same-habitat/diff-order | SSE-wp1 | 144 | 0.624 | 0.143 |
| A same-habitat/diff-order | SSE-wp2 | 144 | 0.624 | 0.143 |
| A same-habitat/diff-order | SSE-hard | 144 | 0.624 | 0.338 |
| A same-habitat/diff-order | SSE-hardJ | 144 | 0.624 | 0.254 |
| A same-habitat/diff-order | B1 labels | 144 | 0.624 | 0.340 |
| A same-habitat/diff-order | B1-soft | 144 | 0.624 | 0.252 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.624 | 0.379 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.624 | 0.323 |
| B same-family/diff-habitat | SSE | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-wp1 | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-wp2 | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-hard | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | SSE-hardJ | 24 | 0.165 | 0.261 |
| B same-family/diff-habitat | B1 labels | 24 | 0.165 | 0.548 |
| B same-family/diff-habitat | B1-soft | 24 | 0.165 | 0.299 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.165 | 0.192 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.889 |
| SSE-wp1 | 0.889 |
| SSE-wp2 | 0.889 |
| SSE-hard | 0.200 |
| SSE-hardJ | 0.623 |
| B1 labels | 0.589 |
| B1-soft | 0.725 |
| B2 CLIP+text | 0.212 |
| B6 plain CLIP | 0.229 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.102 | 0.920 |
| SSE-wp1 | 1.000 | 0.090 | 0.924 |
| SSE-wp2 | 1.000 | 0.095 | 0.918 |
| SSE-hard | 0.745 | 0.477 | 0.855 |
| SSE-hardJ | 1.000 | 0.274 | 0.871 |
| B1 labels | 0.903 | 0.341 | 0.788 |
| B1-soft | 1.000 | 0.149 | 0.887 |
| B2 CLIP+text | 1.000 | 0.447 | 0.773 |
| B6 plain CLIP | 0.927 | 0.425 | 0.840 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.993 |
| seen_test | SSE | 4 | family | 0.517 |
| seen_test | SSE | 4 | genus | 0.380 |
| seen_test | SSE | 8 | order | 0.998 |
| seen_test | SSE | 8 | family | 0.529 |
| seen_test | SSE | 8 | genus | 0.395 |
| seen_test | SSE | 16 | order | 0.937 |
| seen_test | SSE | 16 | family | 0.988 |
| seen_test | SSE | 16 | genus | 0.742 |
| seen_test | SSE | 32 | order | 0.841 |
| seen_test | SSE | 32 | family | 0.995 |
| seen_test | SSE | 32 | genus | 0.761 |
| seen_test | SSE | 64 | order | 0.766 |
| seen_test | SSE | 64 | family | 0.912 |
| seen_test | SSE | 64 | genus | 0.993 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.635 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.741 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.867 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.695 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.861 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.990 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.693 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.857 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.990 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.748 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.892 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.993 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.749 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.895 |
| seen_test | SSE-MRL (genus everywhere) | 64 | genus | 0.993 |
| seen_test | CLIP-PCA | 4 | order | 0.518 |
| seen_test | CLIP-PCA | 4 | family | 0.499 |
| seen_test | CLIP-PCA | 4 | genus | 0.559 |
| seen_test | CLIP-PCA | 8 | order | 0.597 |
| seen_test | CLIP-PCA | 8 | family | 0.611 |
| seen_test | CLIP-PCA | 8 | genus | 0.668 |
| seen_test | CLIP-PCA | 16 | order | 0.645 |
| seen_test | CLIP-PCA | 16 | family | 0.714 |
| seen_test | CLIP-PCA | 16 | genus | 0.790 |
| seen_test | CLIP-PCA | 32 | order | 0.659 |
| seen_test | CLIP-PCA | 32 | family | 0.743 |
| seen_test | CLIP-PCA | 32 | genus | 0.833 |
| seen_test | CLIP-PCA | 64 | order | 0.652 |
| seen_test | CLIP-PCA | 64 | family | 0.738 |
| seen_test | CLIP-PCA | 64 | genus | 0.833 |
| unseen | SSE | 4 | order | 0.890 |
| unseen | SSE | 4 | family | 0.652 |
| unseen | SSE | 4 | genus | 0.624 |
| unseen | SSE | 8 | order | 0.903 |
| unseen | SSE | 8 | family | 0.731 |
| unseen | SSE | 8 | genus | 0.699 |
| unseen | SSE | 16 | order | 0.899 |
| unseen | SSE | 16 | family | 0.937 |
| unseen | SSE | 16 | genus | 0.914 |
| unseen | SSE | 32 | order | 0.840 |
| unseen | SSE | 32 | family | 0.964 |
| unseen | SSE | 32 | genus | 0.940 |
| unseen | SSE | 64 | order | 0.799 |
| unseen | SSE | 64 | family | 0.965 |
| unseen | SSE | 64 | genus | 0.980 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.764 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.820 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.795 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.802 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.923 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.935 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.800 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.948 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.960 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.784 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.960 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.976 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.782 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.961 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.976 |
| unseen | CLIP-PCA | 4 | order | 0.608 |
| unseen | CLIP-PCA | 4 | family | 0.635 |
| unseen | CLIP-PCA | 4 | genus | 0.706 |
| unseen | CLIP-PCA | 8 | order | 0.636 |
| unseen | CLIP-PCA | 8 | family | 0.692 |
| unseen | CLIP-PCA | 8 | genus | 0.769 |
| unseen | CLIP-PCA | 16 | order | 0.692 |
| unseen | CLIP-PCA | 16 | family | 0.801 |
| unseen | CLIP-PCA | 16 | genus | 0.863 |
| unseen | CLIP-PCA | 32 | order | 0.726 |
| unseen | CLIP-PCA | 32 | family | 0.856 |
| unseen | CLIP-PCA | 32 | genus | 0.914 |
| unseen | CLIP-PCA | 64 | order | 0.744 |
| unseen | CLIP-PCA | 64 | family | 0.880 |
| unseen | CLIP-PCA | 64 | genus | 0.940 |
