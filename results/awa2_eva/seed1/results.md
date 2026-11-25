# AwA2 results seed1

args: `{'sse': 'SSE-treeSC=treesc_s1,SSE-tree=tree_s1', 'mrl': 'mrl_s1', 'out': 'seed1', 'no_baselines': False, 'extra': 'B3 separate=b3tree_s1,B4 CSN=csntree_s1', 'seed': 1}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE-treeSC | habitat | 0.929 | 0.427 | 0.288 |
| SSE-treeSC | diet | 0.476 | 0.868 | 0.407 |
| SSE-treeSC | family | 0.326 | 0.394 | 0.662 |
| SSE-treeSC | tax | 0.332 | 0.375 | 0.592 |
| SSE-treeSC | rest | 0.176 | 0.162 | 0.164 |
| SSE-tree | habitat | 0.929 | 0.427 | 0.287 |
| SSE-tree | diet | 0.476 | 0.867 | 0.408 |
| SSE-tree | family | 0.306 | 0.411 | 0.676 |
| SSE-tree | tax | 0.299 | 0.403 | 0.639 |
| SSE-tree | rest | 0.186 | 0.168 | 0.160 |
| B1 labels | habitat | 0.499 | 0.204 | 0.286 |
| B1 labels | diet | 0.210 | 0.573 | 0.201 |
| B1 labels | family | 0.313 | 0.395 | 0.716 |
| B1-soft | habitat | 0.683 | 0.326 | 0.386 |
| B1-soft | diet | 0.371 | 0.760 | 0.325 |
| B1-soft | family | 0.292 | 0.363 | 0.509 |
| B2 CLIP+text | habitat | 0.244 | 0.161 | 0.098 |
| B2 CLIP+text | diet | 0.203 | 0.169 | 0.061 |
| B2 CLIP+text | family | 0.216 | 0.207 | 0.222 |
| B6 plain CLIP | habitat | 0.285 | 0.281 | 0.229 |
| B6 plain CLIP | diet | 0.285 | 0.281 | 0.229 |
| B6 plain CLIP | family | 0.285 | 0.281 | 0.229 |
| B3 separate | habitat | 0.924 | 0.436 | 0.291 |
| B3 separate | diet | 0.476 | 0.864 | 0.408 |
| B3 separate | family | 0.288 | 0.396 | 0.694 |
| B4 CSN | habitat | 0.923 | 0.424 | 0.300 |
| B4 CSN | diet | 0.490 | 0.865 | 0.410 |
| B4 CSN | family | 0.269 | 0.376 | 0.701 |

### E3 — general search preserved

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.894 | 0.813 | 0.810 |
| SSE-tree | 0.887 | 0.826 | 0.822 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE-treeSC | all | 1000 | 0.760 | 0.852 | 0.585 | 0.584 |
| SSE-treeSC | x unseen | 555 | 0.721 | 0.827 | 0.560 | 0.541 |
| SSE-treeSC | x seen | 445 | 0.807 | 0.885 | 0.617 | 0.642 |
| SSE-treeSC | q unseen | 572 | 0.755 | 0.846 | 0.579 | 0.566 |
| SSE-tree | all | 1000 | 0.759 | 0.852 | 0.582 | 0.581 |
| SSE-tree | x unseen | 555 | 0.721 | 0.826 | 0.549 | 0.534 |
| SSE-tree | x seen | 445 | 0.807 | 0.884 | 0.623 | 0.646 |
| SSE-tree | q unseen | 572 | 0.754 | 0.846 | 0.572 | 0.561 |
| B1 labels | all | 1000 | 0.444 | 0.478 | 0.322 | 0.356 |
| B1 labels | x unseen | 555 | 0.425 | 0.434 | 0.295 | 0.321 |
| B1 labels | x seen | 445 | 0.468 | 0.532 | 0.354 | 0.404 |
| B1 labels | q unseen | 572 | 0.431 | 0.467 | 0.312 | 0.337 |
| B1-soft | all | 1000 | 0.631 | 0.710 | 0.419 | 0.452 |
| B1-soft | x unseen | 555 | 0.640 | 0.720 | 0.440 | 0.446 |
| B1-soft | x seen | 445 | 0.620 | 0.697 | 0.394 | 0.460 |
| B1-soft | q unseen | 572 | 0.621 | 0.699 | 0.397 | 0.441 |
| B2 CLIP+text | all | 1000 | 0.476 | 0.519 | 0.357 | 0.405 |
| B2 CLIP+text | x unseen | 555 | 0.508 | 0.561 | 0.364 | 0.401 |
| B2 CLIP+text | x seen | 445 | 0.435 | 0.467 | 0.350 | 0.409 |
| B2 CLIP+text | q unseen | 572 | 0.463 | 0.504 | 0.361 | 0.418 |
| B6 plain CLIP | all | 1000 | 0.532 | 0.606 | 0.327 | 0.382 |
| B6 plain CLIP | x unseen | 555 | 0.592 | 0.683 | 0.343 | 0.392 |
| B6 plain CLIP | x seen | 445 | 0.458 | 0.511 | 0.305 | 0.368 |
| B6 plain CLIP | q unseen | 572 | 0.522 | 0.595 | 0.334 | 0.398 |
| B3 separate | all | 1000 | 0.763 | 0.855 | 0.593 | 0.591 |
| B3 separate | x unseen | 555 | 0.722 | 0.826 | 0.581 | 0.558 |
| B3 separate | x seen | 445 | 0.814 | 0.890 | 0.609 | 0.635 |
| B3 separate | q unseen | 572 | 0.758 | 0.849 | 0.574 | 0.560 |
| B4 CSN | all | 1000 | 0.760 | 0.854 | 0.577 | 0.570 |
| B4 CSN | x unseen | 555 | 0.729 | 0.835 | 0.563 | 0.543 |
| B4 CSN | x seen | 445 | 0.798 | 0.878 | 0.594 | 0.606 |
| B4 CSN | q unseen | 572 | 0.757 | 0.851 | 0.569 | 0.544 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.626 | 0.142 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.626 | 0.142 |
| A same-habitat/diff-order | B1 labels | 144 | 0.626 | 0.343 |
| A same-habitat/diff-order | B1-soft | 144 | 0.626 | 0.270 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.626 | 0.382 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.626 | 0.338 |
| A same-habitat/diff-order | B3 separate | 144 | 0.626 | 0.149 |
| A same-habitat/diff-order | B4 CSN | 144 | 0.626 | 0.143 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.151 | 0.120 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.151 | 0.119 |
| B same-family/diff-habitat | B1 labels | 24 | 0.151 | 0.598 |
| B same-family/diff-habitat | B1-soft | 24 | 0.151 | 0.271 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.151 | 0.227 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.151 | 0.235 |
| B same-family/diff-habitat | B3 separate | 24 | 0.151 | 0.119 |
| B same-family/diff-habitat | B4 CSN | 24 | 0.151 | 0.101 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE-treeSC | order@8 | 0.953 | 0.948 | 0.945 |
| SSE-treeSC | family@32 | 0.912 | 0.998 | 0.989 |
| SSE-treeSC | genus@64 | 0.864 | 0.995 | 0.998 |
| SSE-tree | order@8 | 0.956 | 0.951 | 0.946 |
| SSE-tree | family@32 | 0.922 | 0.997 | 0.989 |
| SSE-tree | genus@64 | 0.896 | 0.998 | 0.997 |
| B1 labels | family view | 0.953 | 0.984 | 0.977 |
| B1-soft | family view | 0.807 | 0.993 | 0.978 |
| B2 CLIP+text | family view | 0.625 | 0.794 | 0.865 |
| B6 plain CLIP | family view | 0.625 | 0.816 | 0.925 |
| B3 separate | order@8 | 0.950 | 0.949 | 0.943 |
| B3 separate | family@32 | 0.935 | 0.998 | 0.989 |
| B3 separate | genus@64 | 0.899 | 0.998 | 0.998 |
| B4 CSN | order@8 | 0.953 | 0.954 | 0.951 |
| B4 CSN | family@32 | 0.940 | 0.998 | 0.989 |
| B4 CSN | genus@64 | 0.916 | 0.998 | 0.997 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE-treeSC | 0.920 |
| SSE-tree | 0.921 |
| B1 labels | 0.472 |
| B1-soft | 0.638 |
| B2 CLIP+text | 0.200 |
| B6 plain CLIP | 0.211 |
| B3 separate | 0.914 |
| B4 CSN | 0.912 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE-treeSC | 1.000 | 0.083 | 0.913 |
| SSE-tree | 1.000 | 0.069 | 0.925 |
| B1 labels | 0.891 | 0.398 | 0.668 |
| B1-soft | 1.000 | 0.148 | 0.878 |
| B2 CLIP+text | 0.661 | 0.456 | 0.788 |
| B6 plain CLIP | 0.842 | 0.483 | 0.811 |
| B3 separate | 1.000 | 0.079 | 0.924 |
| B4 CSN | 1.000 | 0.074 | 0.918 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE-treeSC | 4 | order | 0.994 |
| seen_test | SSE-treeSC | 4 | family | 0.517 |
| seen_test | SSE-treeSC | 4 | genus | 0.404 |
| seen_test | SSE-treeSC | 8 | order | 0.999 |
| seen_test | SSE-treeSC | 8 | family | 0.524 |
| seen_test | SSE-treeSC | 8 | genus | 0.412 |
| seen_test | SSE-treeSC | 16 | order | 0.998 |
| seen_test | SSE-treeSC | 16 | family | 0.993 |
| seen_test | SSE-treeSC | 16 | genus | 0.788 |
| seen_test | SSE-treeSC | 32 | order | 0.995 |
| seen_test | SSE-treeSC | 32 | family | 0.996 |
| seen_test | SSE-treeSC | 32 | genus | 0.808 |
| seen_test | SSE-treeSC | 64 | order | 0.990 |
| seen_test | SSE-treeSC | 64 | family | 0.980 |
| seen_test | SSE-treeSC | 64 | genus | 0.996 |
| seen_test | SSE-tree | 4 | order | 0.992 |
| seen_test | SSE-tree | 4 | family | 0.517 |
| seen_test | SSE-tree | 4 | genus | 0.405 |
| seen_test | SSE-tree | 8 | order | 0.997 |
| seen_test | SSE-tree | 8 | family | 0.530 |
| seen_test | SSE-tree | 8 | genus | 0.421 |
| seen_test | SSE-tree | 16 | order | 0.997 |
| seen_test | SSE-tree | 16 | family | 0.985 |
| seen_test | SSE-tree | 16 | genus | 0.806 |
| seen_test | SSE-tree | 32 | order | 0.998 |
| seen_test | SSE-tree | 32 | family | 0.994 |
| seen_test | SSE-tree | 32 | genus | 0.835 |
| seen_test | SSE-tree | 64 | order | 0.995 |
| seen_test | SSE-tree | 64 | family | 0.993 |
| seen_test | SSE-tree | 64 | genus | 0.991 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.645 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.755 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.927 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.701 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.860 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.994 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.697 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.862 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.994 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.727 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.898 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.995 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.728 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.898 |
| seen_test | SSE-MRL (genus everywhere) | 64 | genus | 0.995 |
| seen_test | CLIP-PCA | 4 | order | 0.477 |
| seen_test | CLIP-PCA | 4 | family | 0.460 |
| seen_test | CLIP-PCA | 4 | genus | 0.493 |
| seen_test | CLIP-PCA | 8 | order | 0.551 |
| seen_test | CLIP-PCA | 8 | family | 0.565 |
| seen_test | CLIP-PCA | 8 | genus | 0.619 |
| seen_test | CLIP-PCA | 16 | order | 0.605 |
| seen_test | CLIP-PCA | 16 | family | 0.677 |
| seen_test | CLIP-PCA | 16 | genus | 0.749 |
| seen_test | CLIP-PCA | 32 | order | 0.628 |
| seen_test | CLIP-PCA | 32 | family | 0.721 |
| seen_test | CLIP-PCA | 32 | genus | 0.810 |
| seen_test | CLIP-PCA | 64 | order | 0.625 |
| seen_test | CLIP-PCA | 64 | family | 0.723 |
| seen_test | CLIP-PCA | 64 | genus | 0.819 |
| unseen | SSE-treeSC | 4 | order | 0.950 |
| unseen | SSE-treeSC | 4 | family | 0.776 |
| unseen | SSE-treeSC | 4 | genus | 0.764 |
| unseen | SSE-treeSC | 8 | order | 0.940 |
| unseen | SSE-treeSC | 8 | family | 0.902 |
| unseen | SSE-treeSC | 8 | genus | 0.901 |
| unseen | SSE-treeSC | 16 | order | 0.928 |
| unseen | SSE-treeSC | 16 | family | 0.976 |
| unseen | SSE-treeSC | 16 | genus | 0.956 |
| unseen | SSE-treeSC | 32 | order | 0.912 |
| unseen | SSE-treeSC | 32 | family | 0.992 |
| unseen | SSE-treeSC | 32 | genus | 0.981 |
| unseen | SSE-treeSC | 64 | order | 0.895 |
| unseen | SSE-treeSC | 64 | family | 0.992 |
| unseen | SSE-treeSC | 64 | genus | 0.994 |
| unseen | SSE-tree | 4 | order | 0.942 |
| unseen | SSE-tree | 4 | family | 0.823 |
| unseen | SSE-tree | 4 | genus | 0.792 |
| unseen | SSE-tree | 8 | order | 0.959 |
| unseen | SSE-tree | 8 | family | 0.924 |
| unseen | SSE-tree | 8 | genus | 0.908 |
| unseen | SSE-tree | 16 | order | 0.953 |
| unseen | SSE-tree | 16 | family | 0.968 |
| unseen | SSE-tree | 16 | genus | 0.952 |
| unseen | SSE-tree | 32 | order | 0.934 |
| unseen | SSE-tree | 32 | family | 0.990 |
| unseen | SSE-tree | 32 | genus | 0.979 |
| unseen | SSE-tree | 64 | order | 0.921 |
| unseen | SSE-tree | 64 | family | 0.991 |
| unseen | SSE-tree | 64 | genus | 0.991 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.701 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.767 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.822 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.801 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.920 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.968 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.798 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.931 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.980 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.805 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.932 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.981 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.806 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.936 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.985 |
| unseen | CLIP-PCA | 4 | order | 0.573 |
| unseen | CLIP-PCA | 4 | family | 0.569 |
| unseen | CLIP-PCA | 4 | genus | 0.623 |
| unseen | CLIP-PCA | 8 | order | 0.637 |
| unseen | CLIP-PCA | 8 | family | 0.664 |
| unseen | CLIP-PCA | 8 | genus | 0.722 |
| unseen | CLIP-PCA | 16 | order | 0.687 |
| unseen | CLIP-PCA | 16 | family | 0.749 |
| unseen | CLIP-PCA | 16 | genus | 0.798 |
| unseen | CLIP-PCA | 32 | order | 0.720 |
| unseen | CLIP-PCA | 32 | family | 0.806 |
| unseen | CLIP-PCA | 32 | genus | 0.850 |
| unseen | CLIP-PCA | 64 | order | 0.751 |
| unseen | CLIP-PCA | 64 | family | 0.858 |
| unseen | CLIP-PCA | 64 | genus | 0.903 |
