# AwA2 results seed0

args: `{'sse': 'SSE=main_wp0.5_s0,SSE-wp1=main_wp1_s0,SSE-wp2=main_wp2_s0,SSE-hard=hard_s0,SSE-hardJ=hardj_s0', 'mrl': 'mrl_s0', 'out': 'seed0', 'no_baselines': False, 'seed': 0}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.901 | 0.421 | 0.307 |
| SSE | diet | 0.454 | 0.865 | 0.431 |
| SSE | family | 0.455 | 0.314 | 0.527 |
| SSE | tax | 0.443 | 0.311 | 0.421 |
| SSE | rest | 0.151 | 0.132 | 0.151 |
| SSE | full | 0.318 | 0.300 | 0.259 |
| SSE-wp1 | habitat | 0.901 | 0.421 | 0.307 |
| SSE-wp1 | diet | 0.455 | 0.865 | 0.430 |
| SSE-wp1 | family | 0.455 | 0.314 | 0.526 |
| SSE-wp1 | tax | 0.443 | 0.311 | 0.420 |
| SSE-wp1 | rest | 0.153 | 0.134 | 0.151 |
| SSE-wp2 | habitat | 0.901 | 0.422 | 0.307 |
| SSE-wp2 | diet | 0.455 | 0.865 | 0.428 |
| SSE-wp2 | family | 0.455 | 0.314 | 0.526 |
| SSE-wp2 | tax | 0.444 | 0.311 | 0.420 |
| SSE-wp2 | rest | 0.154 | 0.135 | 0.150 |
| SSE-hard | habitat | 0.347 | 0.255 | 0.196 |
| SSE-hard | diet | 0.396 | 0.709 | 0.259 |
| SSE-hard | family | 0.455 | 0.314 | 0.529 |
| SSE-hard | tax | 0.446 | 0.311 | 0.420 |
| SSE-hard | rest | 0.222 | 0.178 | 0.164 |
| SSE-hardJ | habitat | 0.672 | 0.372 | 0.243 |
| SSE-hardJ | diet | 0.402 | 0.730 | 0.332 |
| SSE-hardJ | family | 0.455 | 0.314 | 0.528 |
| SSE-hardJ | tax | 0.446 | 0.311 | 0.421 |
| SSE-hardJ | rest | 0.194 | 0.164 | 0.158 |
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
| SSE-wp1 | all | 1000 | 0.753 | 0.838 | 0.560 | 0.549 |
| SSE-wp1 | x unseen | 556 | 0.722 | 0.814 | 0.545 | 0.524 |
| SSE-wp1 | x seen | 444 | 0.792 | 0.867 | 0.578 | 0.585 |
| SSE-wp1 | q unseen | 570 | 0.744 | 0.828 | 0.535 | 0.526 |
| SSE-wp2 | all | 1000 | 0.752 | 0.837 | 0.559 | 0.549 |
| SSE-wp2 | x unseen | 556 | 0.721 | 0.814 | 0.544 | 0.523 |
| SSE-wp2 | x seen | 444 | 0.791 | 0.866 | 0.578 | 0.585 |
| SSE-wp2 | q unseen | 570 | 0.743 | 0.828 | 0.535 | 0.526 |
| SSE-hard | all | 1000 | 0.550 | 0.632 | 0.372 | 0.435 |
| SSE-hard | x unseen | 556 | 0.594 | 0.697 | 0.409 | 0.450 |
| SSE-hard | x seen | 444 | 0.495 | 0.550 | 0.327 | 0.414 |
| SSE-hard | q unseen | 570 | 0.541 | 0.618 | 0.362 | 0.437 |
| SSE-hardJ | all | 1000 | 0.643 | 0.719 | 0.441 | 0.468 |
| SSE-hardJ | x unseen | 556 | 0.653 | 0.745 | 0.467 | 0.477 |
| SSE-hardJ | x seen | 444 | 0.630 | 0.688 | 0.409 | 0.454 |
| SSE-hardJ | q unseen | 570 | 0.627 | 0.702 | 0.425 | 0.468 |
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
| A same-habitat/diff-order | SSE-wp1 | 144 | 0.624 | 0.147 |
| A same-habitat/diff-order | SSE-wp2 | 144 | 0.624 | 0.148 |
| A same-habitat/diff-order | SSE-hard | 144 | 0.624 | 0.339 |
| A same-habitat/diff-order | SSE-hardJ | 144 | 0.624 | 0.257 |
| A same-habitat/diff-order | B1 labels | 144 | 0.624 | 0.338 |
| A same-habitat/diff-order | B1-soft | 144 | 0.624 | 0.252 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.624 | 0.379 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.624 | 0.323 |
| B same-family/diff-habitat | SSE | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-wp1 | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-wp2 | 24 | 0.165 | 0.141 |
| B same-family/diff-habitat | SSE-hard | 24 | 0.165 | 0.202 |
| B same-family/diff-habitat | SSE-hardJ | 24 | 0.165 | 0.265 |
| B same-family/diff-habitat | B1 labels | 24 | 0.165 | 0.548 |
| B same-family/diff-habitat | B1-soft | 24 | 0.165 | 0.300 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.165 | 0.192 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.888 |
| SSE-wp1 | 0.888 |
| SSE-wp2 | 0.888 |
| SSE-hard | 0.201 |
| SSE-hardJ | 0.614 |
| B1 labels | 0.590 |
| B1-soft | 0.726 |
| B2 CLIP+text | 0.212 |
| B6 plain CLIP | 0.229 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.100 | 0.919 |
| SSE-wp1 | 1.000 | 0.088 | 0.924 |
| SSE-wp2 | 1.000 | 0.095 | 0.917 |
| SSE-hard | 0.745 | 0.483 | 0.855 |
| SSE-hardJ | 1.000 | 0.281 | 0.873 |
| B1 labels | 0.903 | 0.341 | 0.787 |
| B1-soft | 1.000 | 0.148 | 0.887 |
| B2 CLIP+text | 1.000 | 0.447 | 0.773 |
| B6 plain CLIP | 0.927 | 0.425 | 0.840 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.949 |
| seen_test | SSE | 4 | family | 0.502 |
| seen_test | SSE | 4 | genus | 0.370 |
| seen_test | SSE | 8 | order | 0.998 |
| seen_test | SSE | 8 | family | 0.532 |
| seen_test | SSE | 8 | genus | 0.400 |
| seen_test | SSE | 16 | order | 0.925 |
| seen_test | SSE | 16 | family | 0.987 |
| seen_test | SSE | 16 | genus | 0.749 |
| seen_test | SSE | 32 | order | 0.844 |
| seen_test | SSE | 32 | family | 0.995 |
| seen_test | SSE | 32 | genus | 0.762 |
| seen_test | SSE | 64 | order | 0.768 |
| seen_test | SSE | 64 | family | 0.912 |
| seen_test | SSE | 64 | genus | 0.993 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.576 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.708 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.863 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.696 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.866 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.988 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.700 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.871 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.991 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.745 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.892 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.993 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.751 |
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
| unseen | SSE | 4 | order | 0.768 |
| unseen | SSE | 4 | family | 0.500 |
| unseen | SSE | 4 | genus | 0.461 |
| unseen | SSE | 8 | order | 0.904 |
| unseen | SSE | 8 | family | 0.718 |
| unseen | SSE | 8 | genus | 0.679 |
| unseen | SSE | 16 | order | 0.896 |
| unseen | SSE | 16 | family | 0.901 |
| unseen | SSE | 16 | genus | 0.883 |
| unseen | SSE | 32 | order | 0.838 |
| unseen | SSE | 32 | family | 0.962 |
| unseen | SSE | 32 | genus | 0.941 |
| unseen | SSE | 64 | order | 0.799 |
| unseen | SSE | 64 | family | 0.962 |
| unseen | SSE | 64 | genus | 0.978 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.679 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.629 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.682 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.774 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.911 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.922 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.779 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.938 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.951 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.781 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.956 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.972 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.785 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.959 |
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
