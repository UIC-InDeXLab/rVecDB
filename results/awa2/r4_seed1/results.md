# AwA2 results r4_seed1

args: `{'sse': 'SSE=tree_s1', 'mrl': 'mrl_s1', 'out': 'r4_seed1', 'no_baselines': False, 'extra': 'B3 separate=b3_s1,B4 CSN=csn_s1', 'seed': 1}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE | habitat | 0.904 | 0.421 | 0.305 |
| SSE | diet | 0.455 | 0.870 | 0.428 |
| SSE | family | 0.288 | 0.382 | 0.723 |
| SSE | tax | 0.299 | 0.385 | 0.703 |
| SSE | rest | 0.156 | 0.125 | 0.140 |
| SSE | full | 0.322 | 0.305 | 0.265 |
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
| B3 separate | habitat | 0.904 | 0.421 | 0.305 |
| B3 separate | diet | 0.458 | 0.867 | 0.439 |
| B3 separate | family | 0.491 | 0.291 | 0.463 |
| B4 CSN | habitat | 0.892 | 0.421 | 0.314 |
| B4 CSN | diet | 0.452 | 0.866 | 0.436 |
| B4 CSN | family | 0.492 | 0.333 | 0.489 |

### E3 — general search preserved

| overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|
| 0.856 | 0.819 | 0.822 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 1000 | 0.752 | 0.837 | 0.568 | 0.588 |
| SSE | x unseen | 556 | 0.721 | 0.815 | 0.553 | 0.550 |
| SSE | x seen | 444 | 0.790 | 0.864 | 0.586 | 0.641 |
| SSE | q unseen | 570 | 0.742 | 0.827 | 0.561 | 0.581 |
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
| B3 separate | all | 1000 | 0.755 | 0.840 | 0.565 | 0.545 |
| B3 separate | x unseen | 556 | 0.725 | 0.819 | 0.551 | 0.516 |
| B3 separate | x seen | 444 | 0.792 | 0.866 | 0.584 | 0.584 |
| B3 separate | q unseen | 570 | 0.746 | 0.831 | 0.550 | 0.528 |
| B4 CSN | all | 1000 | 0.746 | 0.831 | 0.552 | 0.545 |
| B4 CSN | x unseen | 556 | 0.714 | 0.809 | 0.536 | 0.513 |
| B4 CSN | x seen | 444 | 0.786 | 0.859 | 0.573 | 0.587 |
| B4 CSN | q unseen | 570 | 0.737 | 0.822 | 0.535 | 0.522 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE | 144 | 0.624 | 0.142 |
| A same-habitat/diff-order | B1 labels | 144 | 0.624 | 0.340 |
| A same-habitat/diff-order | B1-soft | 144 | 0.624 | 0.252 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.624 | 0.379 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.624 | 0.323 |
| A same-habitat/diff-order | B3 separate | 144 | 0.624 | 0.149 |
| A same-habitat/diff-order | B4 CSN | 144 | 0.624 | 0.146 |
| B same-family/diff-habitat | SSE | 24 | 0.165 | 0.138 |
| B same-family/diff-habitat | B1 labels | 24 | 0.165 | 0.548 |
| B same-family/diff-habitat | B1-soft | 24 | 0.165 | 0.299 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.165 | 0.206 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.165 | 0.192 |
| B same-family/diff-habitat | B3 separate | 24 | 0.165 | 0.145 |
| B same-family/diff-habitat | B4 CSN | 24 | 0.165 | 0.139 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE | order@8 | 0.958 | 0.943 | 0.934 |
| SSE | family@32 | 0.955 | 0.997 | 0.985 |
| SSE | genus@64 | 0.941 | 0.997 | 0.995 |
| B1 labels | family view | 0.959 | 0.985 | 0.978 |
| B1-soft | family view | 0.821 | 0.993 | 0.979 |
| B2 CLIP+text | family view | 0.635 | 0.796 | 0.854 |
| B6 plain CLIP | family view | 0.628 | 0.839 | 0.934 |
| B3 separate | order@8 | 0.964 | 0.926 | 0.915 |
| B3 separate | family@32 | 0.773 | 0.993 | 0.978 |
| B3 separate | genus@64 | 0.724 | 0.958 | 0.993 |
| B4 CSN | order@8 | 0.971 | 0.931 | 0.922 |
| B4 CSN | family@32 | 0.792 | 0.993 | 0.980 |
| B4 CSN | genus@64 | 0.736 | 0.950 | 0.993 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE | 0.891 |
| B1 labels | 0.590 |
| B1-soft | 0.722 |
| B2 CLIP+text | 0.212 |
| B6 plain CLIP | 0.234 |
| B3 separate | 0.891 |
| B4 CSN | 0.876 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE | 1.000 | 0.092 | 0.920 |
| B1 labels | 0.903 | 0.355 | 0.789 |
| B1-soft | 1.000 | 0.168 | 0.870 |
| B2 CLIP+text | 1.000 | 0.446 | 0.772 |
| B6 plain CLIP | 0.915 | 0.440 | 0.843 |
| B3 separate | 1.000 | 0.088 | 0.920 |
| B4 CSN | 1.000 | 0.102 | 0.914 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE | 4 | order | 0.976 |
| seen_test | SSE | 4 | family | 0.527 |
| seen_test | SSE | 4 | genus | 0.393 |
| seen_test | SSE | 8 | order | 0.990 |
| seen_test | SSE | 8 | family | 0.547 |
| seen_test | SSE | 8 | genus | 0.414 |
| seen_test | SSE | 16 | order | 0.989 |
| seen_test | SSE | 16 | family | 0.958 |
| seen_test | SSE | 16 | genus | 0.744 |
| seen_test | SSE | 32 | order | 0.987 |
| seen_test | SSE | 32 | family | 0.975 |
| seen_test | SSE | 32 | genus | 0.782 |
| seen_test | SSE | 64 | order | 0.981 |
| seen_test | SSE | 64 | family | 0.973 |
| seen_test | SSE | 64 | genus | 0.967 |
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
| unseen | SSE | 4 | order | 0.879 |
| unseen | SSE | 4 | family | 0.665 |
| unseen | SSE | 4 | genus | 0.634 |
| unseen | SSE | 8 | order | 0.942 |
| unseen | SSE | 8 | family | 0.871 |
| unseen | SSE | 8 | genus | 0.863 |
| unseen | SSE | 16 | order | 0.953 |
| unseen | SSE | 16 | family | 0.970 |
| unseen | SSE | 16 | genus | 0.950 |
| unseen | SSE | 32 | order | 0.950 |
| unseen | SSE | 32 | family | 0.988 |
| unseen | SSE | 32 | genus | 0.973 |
| unseen | SSE | 64 | order | 0.938 |
| unseen | SSE | 64 | family | 0.990 |
| unseen | SSE | 64 | genus | 0.988 |
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
