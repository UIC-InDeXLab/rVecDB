# AwA2 results seed0

args: `{'sse': 'SSE-treeSC=treesc_s0,SSE-tree=tree_s0', 'mrl': 'mrl_s0', 'out': 'seed0', 'no_baselines': False, 'extra': 'B3 separate=b3tree_s0,B4 CSN=csntree_s0', 'seed': 0}`

### E1 — Spearman of each view vs. each true facet (higher on own facet = good)

| method | view | habitat | diet | taxonomy |
|---|---|---|---|---|
| SSE-treeSC | habitat | 0.923 | 0.419 | 0.290 |
| SSE-treeSC | diet | 0.476 | 0.864 | 0.399 |
| SSE-treeSC | family | 0.314 | 0.390 | 0.669 |
| SSE-treeSC | tax | 0.328 | 0.372 | 0.608 |
| SSE-treeSC | rest | 0.178 | 0.163 | 0.161 |
| SSE-tree | habitat | 0.925 | 0.419 | 0.290 |
| SSE-tree | diet | 0.478 | 0.863 | 0.400 |
| SSE-tree | family | 0.282 | 0.409 | 0.690 |
| SSE-tree | tax | 0.289 | 0.403 | 0.648 |
| SSE-tree | rest | 0.182 | 0.166 | 0.157 |
| B1 labels | habitat | 0.498 | 0.202 | 0.285 |
| B1 labels | diet | 0.208 | 0.572 | 0.204 |
| B1 labels | family | 0.313 | 0.396 | 0.717 |
| B1-soft | habitat | 0.683 | 0.327 | 0.386 |
| B1-soft | diet | 0.371 | 0.760 | 0.326 |
| B1-soft | family | 0.293 | 0.364 | 0.509 |
| B2 CLIP+text | habitat | 0.244 | 0.161 | 0.098 |
| B2 CLIP+text | diet | 0.203 | 0.169 | 0.061 |
| B2 CLIP+text | family | 0.216 | 0.207 | 0.222 |
| B6 plain CLIP | habitat | 0.285 | 0.281 | 0.229 |
| B6 plain CLIP | diet | 0.285 | 0.281 | 0.229 |
| B6 plain CLIP | family | 0.285 | 0.281 | 0.229 |
| B3 separate | habitat | 0.919 | 0.423 | 0.284 |
| B3 separate | diet | 0.469 | 0.865 | 0.413 |
| B3 separate | family | 0.313 | 0.444 | 0.687 |
| B4 CSN | habitat | 0.917 | 0.424 | 0.305 |
| B4 CSN | diet | 0.487 | 0.870 | 0.419 |
| B4 CSN | family | 0.274 | 0.381 | 0.700 |

### E3 — general search preserved

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.890 | 0.813 | 0.812 |
| SSE-tree | 0.892 | 0.826 | 0.822 |

### E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE-treeSC | all | 1000 | 0.758 | 0.850 | 0.589 | 0.583 |
| SSE-treeSC | x unseen | 555 | 0.719 | 0.823 | 0.575 | 0.546 |
| SSE-treeSC | x seen | 445 | 0.806 | 0.884 | 0.607 | 0.633 |
| SSE-treeSC | q unseen | 572 | 0.753 | 0.844 | 0.588 | 0.571 |
| SSE-tree | all | 1000 | 0.759 | 0.852 | 0.595 | 0.588 |
| SSE-tree | x unseen | 555 | 0.721 | 0.825 | 0.576 | 0.545 |
| SSE-tree | x seen | 445 | 0.807 | 0.885 | 0.619 | 0.646 |
| SSE-tree | q unseen | 572 | 0.754 | 0.846 | 0.589 | 0.570 |
| B1 labels | all | 1000 | 0.444 | 0.478 | 0.322 | 0.357 |
| B1 labels | x unseen | 555 | 0.425 | 0.435 | 0.295 | 0.323 |
| B1 labels | x seen | 445 | 0.467 | 0.531 | 0.355 | 0.403 |
| B1 labels | q unseen | 572 | 0.430 | 0.466 | 0.311 | 0.339 |
| B1-soft | all | 1000 | 0.631 | 0.710 | 0.418 | 0.451 |
| B1-soft | x unseen | 555 | 0.640 | 0.721 | 0.439 | 0.445 |
| B1-soft | x seen | 445 | 0.620 | 0.697 | 0.392 | 0.460 |
| B1-soft | q unseen | 572 | 0.621 | 0.699 | 0.396 | 0.440 |
| B2 CLIP+text | all | 1000 | 0.476 | 0.519 | 0.357 | 0.405 |
| B2 CLIP+text | x unseen | 555 | 0.508 | 0.561 | 0.364 | 0.401 |
| B2 CLIP+text | x seen | 445 | 0.435 | 0.467 | 0.350 | 0.409 |
| B2 CLIP+text | q unseen | 572 | 0.463 | 0.504 | 0.361 | 0.418 |
| B6 plain CLIP | all | 1000 | 0.532 | 0.606 | 0.327 | 0.382 |
| B6 plain CLIP | x unseen | 555 | 0.592 | 0.683 | 0.343 | 0.392 |
| B6 plain CLIP | x seen | 445 | 0.458 | 0.511 | 0.305 | 0.368 |
| B6 plain CLIP | q unseen | 572 | 0.522 | 0.595 | 0.334 | 0.398 |
| B3 separate | all | 1000 | 0.762 | 0.852 | 0.591 | 0.595 |
| B3 separate | x unseen | 555 | 0.719 | 0.822 | 0.565 | 0.554 |
| B3 separate | x seen | 445 | 0.815 | 0.890 | 0.623 | 0.650 |
| B3 separate | q unseen | 572 | 0.756 | 0.846 | 0.576 | 0.571 |
| B4 CSN | all | 1000 | 0.756 | 0.850 | 0.576 | 0.573 |
| B4 CSN | x unseen | 555 | 0.722 | 0.827 | 0.557 | 0.543 |
| B4 CSN | x seen | 445 | 0.799 | 0.878 | 0.600 | 0.613 |
| B4 CSN | q unseen | 572 | 0.753 | 0.846 | 0.563 | 0.544 |

### E4 — no-mixing test (lower error = better)

| pair_type | method | n_class_pairs | true_jaccard | abs_error |
|---|---|---|---|---|
| A same-habitat/diff-order | SSE-treeSC | 144 | 0.626 | 0.143 |
| A same-habitat/diff-order | SSE-tree | 144 | 0.626 | 0.142 |
| A same-habitat/diff-order | B1 labels | 144 | 0.626 | 0.345 |
| A same-habitat/diff-order | B1-soft | 144 | 0.626 | 0.271 |
| A same-habitat/diff-order | B2 CLIP+text | 144 | 0.626 | 0.382 |
| A same-habitat/diff-order | B6 plain CLIP | 144 | 0.626 | 0.338 |
| A same-habitat/diff-order | B3 separate | 144 | 0.626 | 0.142 |
| A same-habitat/diff-order | B4 CSN | 144 | 0.626 | 0.144 |
| B same-family/diff-habitat | SSE-treeSC | 24 | 0.151 | 0.113 |
| B same-family/diff-habitat | SSE-tree | 24 | 0.151 | 0.112 |
| B same-family/diff-habitat | B1 labels | 24 | 0.151 | 0.602 |
| B same-family/diff-habitat | B1-soft | 24 | 0.151 | 0.269 |
| B same-family/diff-habitat | B2 CLIP+text | 24 | 0.151 | 0.227 |
| B same-family/diff-habitat | B6 plain CLIP | 24 | 0.151 | 0.235 |
| B same-family/diff-habitat | B3 separate | 24 | 0.151 | 0.119 |
| B same-family/diff-habitat | B4 CSN | 24 | 0.151 | 0.118 |

### E2b — does each prefix keep its own AND coarser levels? (pair AUC)

| method | prefix | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE-treeSC | order@8 | 0.950 | 0.945 | 0.943 |
| SSE-treeSC | family@32 | 0.917 | 0.998 | 0.989 |
| SSE-treeSC | genus@64 | 0.874 | 0.995 | 0.998 |
| SSE-tree | order@8 | 0.951 | 0.950 | 0.946 |
| SSE-tree | family@32 | 0.932 | 0.997 | 0.989 |
| SSE-tree | genus@64 | 0.903 | 0.998 | 0.997 |
| B1 labels | family view | 0.954 | 0.984 | 0.977 |
| B1-soft | family view | 0.808 | 0.993 | 0.978 |
| B2 CLIP+text | family view | 0.625 | 0.794 | 0.865 |
| B6 plain CLIP | family view | 0.625 | 0.816 | 0.925 |
| B3 separate | order@8 | 0.956 | 0.950 | 0.945 |
| B3 separate | family@32 | 0.930 | 0.998 | 0.988 |
| B3 separate | genus@64 | 0.888 | 0.999 | 0.998 |
| B4 CSN | order@8 | 0.952 | 0.952 | 0.949 |
| B4 CSN | family@32 | 0.939 | 0.998 | 0.989 |
| B4 CSN | genus@64 | 0.911 | 0.999 | 0.998 |

### E5b — in-between similarity among pairs labels call 'different'

| method | spearman_on_label-different_pairs |
|---|---|
| SSE-treeSC | 0.912 |
| SSE-tree | 0.914 |
| B1 labels | 0.471 |
| B1-soft | 0.639 |
| B2 CLIP+text | 0.200 |
| B6 plain CLIP | 0.211 |
| B3 separate | 0.908 |
| B4 CSN | 0.905 |

### E5c — stricter threshold -> closer matches?

| method | monotonic_spearman | low_bin_true_sim | high_bin_true_sim |
|---|---|---|---|
| SSE-treeSC | 1.000 | 0.084 | 0.912 |
| SSE-tree | 1.000 | 0.071 | 0.922 |
| B1 labels | 0.891 | 0.398 | 0.666 |
| B1-soft | 1.000 | 0.147 | 0.878 |
| B2 CLIP+text | 0.661 | 0.456 | 0.788 |
| B6 plain CLIP | 0.842 | 0.483 | 0.811 |
| B3 separate | 1.000 | 0.083 | 0.925 |
| B4 CSN | 1.000 | 0.077 | 0.918 |

### E2 — taxonomy prefix length vs. level

| split | method | prefix_len | level | mAP |
|---|---|---|---|---|
| seen_test | SSE-treeSC | 4 | order | 0.997 |
| seen_test | SSE-treeSC | 4 | family | 0.518 |
| seen_test | SSE-treeSC | 4 | genus | 0.405 |
| seen_test | SSE-treeSC | 8 | order | 0.999 |
| seen_test | SSE-treeSC | 8 | family | 0.525 |
| seen_test | SSE-treeSC | 8 | genus | 0.410 |
| seen_test | SSE-treeSC | 16 | order | 0.999 |
| seen_test | SSE-treeSC | 16 | family | 0.992 |
| seen_test | SSE-treeSC | 16 | genus | 0.786 |
| seen_test | SSE-treeSC | 32 | order | 0.994 |
| seen_test | SSE-treeSC | 32 | family | 0.996 |
| seen_test | SSE-treeSC | 32 | genus | 0.809 |
| seen_test | SSE-treeSC | 64 | order | 0.990 |
| seen_test | SSE-treeSC | 64 | family | 0.981 |
| seen_test | SSE-treeSC | 64 | genus | 0.996 |
| seen_test | SSE-tree | 4 | order | 0.995 |
| seen_test | SSE-tree | 4 | family | 0.520 |
| seen_test | SSE-tree | 4 | genus | 0.409 |
| seen_test | SSE-tree | 8 | order | 0.998 |
| seen_test | SSE-tree | 8 | family | 0.529 |
| seen_test | SSE-tree | 8 | genus | 0.418 |
| seen_test | SSE-tree | 16 | order | 0.999 |
| seen_test | SSE-tree | 16 | family | 0.990 |
| seen_test | SSE-tree | 16 | genus | 0.802 |
| seen_test | SSE-tree | 32 | order | 0.998 |
| seen_test | SSE-tree | 32 | family | 0.994 |
| seen_test | SSE-tree | 32 | genus | 0.857 |
| seen_test | SSE-tree | 64 | order | 0.994 |
| seen_test | SSE-tree | 64 | family | 0.993 |
| seen_test | SSE-tree | 64 | genus | 0.991 |
| seen_test | SSE-MRL (genus everywhere) | 4 | order | 0.679 |
| seen_test | SSE-MRL (genus everywhere) | 4 | family | 0.775 |
| seen_test | SSE-MRL (genus everywhere) | 4 | genus | 0.927 |
| seen_test | SSE-MRL (genus everywhere) | 8 | order | 0.708 |
| seen_test | SSE-MRL (genus everywhere) | 8 | family | 0.869 |
| seen_test | SSE-MRL (genus everywhere) | 8 | genus | 0.994 |
| seen_test | SSE-MRL (genus everywhere) | 16 | order | 0.701 |
| seen_test | SSE-MRL (genus everywhere) | 16 | family | 0.887 |
| seen_test | SSE-MRL (genus everywhere) | 16 | genus | 0.994 |
| seen_test | SSE-MRL (genus everywhere) | 32 | order | 0.731 |
| seen_test | SSE-MRL (genus everywhere) | 32 | family | 0.897 |
| seen_test | SSE-MRL (genus everywhere) | 32 | genus | 0.995 |
| seen_test | SSE-MRL (genus everywhere) | 64 | order | 0.730 |
| seen_test | SSE-MRL (genus everywhere) | 64 | family | 0.899 |
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
| unseen | SSE-treeSC | 4 | order | 0.932 |
| unseen | SSE-treeSC | 4 | family | 0.725 |
| unseen | SSE-treeSC | 4 | genus | 0.739 |
| unseen | SSE-treeSC | 8 | order | 0.945 |
| unseen | SSE-treeSC | 8 | family | 0.882 |
| unseen | SSE-treeSC | 8 | genus | 0.891 |
| unseen | SSE-treeSC | 16 | order | 0.908 |
| unseen | SSE-treeSC | 16 | family | 0.982 |
| unseen | SSE-treeSC | 16 | genus | 0.972 |
| unseen | SSE-treeSC | 32 | order | 0.929 |
| unseen | SSE-treeSC | 32 | family | 0.992 |
| unseen | SSE-treeSC | 32 | genus | 0.986 |
| unseen | SSE-treeSC | 64 | order | 0.902 |
| unseen | SSE-treeSC | 64 | family | 0.990 |
| unseen | SSE-treeSC | 64 | genus | 0.993 |
| unseen | SSE-tree | 4 | order | 0.881 |
| unseen | SSE-tree | 4 | family | 0.779 |
| unseen | SSE-tree | 4 | genus | 0.781 |
| unseen | SSE-tree | 8 | order | 0.950 |
| unseen | SSE-tree | 8 | family | 0.914 |
| unseen | SSE-tree | 8 | genus | 0.902 |
| unseen | SSE-tree | 16 | order | 0.933 |
| unseen | SSE-tree | 16 | family | 0.965 |
| unseen | SSE-tree | 16 | genus | 0.954 |
| unseen | SSE-tree | 32 | order | 0.939 |
| unseen | SSE-tree | 32 | family | 0.987 |
| unseen | SSE-tree | 32 | genus | 0.984 |
| unseen | SSE-tree | 64 | order | 0.919 |
| unseen | SSE-tree | 64 | family | 0.992 |
| unseen | SSE-tree | 64 | genus | 0.992 |
| unseen | SSE-MRL (genus everywhere) | 4 | order | 0.747 |
| unseen | SSE-MRL (genus everywhere) | 4 | family | 0.849 |
| unseen | SSE-MRL (genus everywhere) | 4 | genus | 0.927 |
| unseen | SSE-MRL (genus everywhere) | 8 | order | 0.784 |
| unseen | SSE-MRL (genus everywhere) | 8 | family | 0.901 |
| unseen | SSE-MRL (genus everywhere) | 8 | genus | 0.983 |
| unseen | SSE-MRL (genus everywhere) | 16 | order | 0.791 |
| unseen | SSE-MRL (genus everywhere) | 16 | family | 0.907 |
| unseen | SSE-MRL (genus everywhere) | 16 | genus | 0.983 |
| unseen | SSE-MRL (genus everywhere) | 32 | order | 0.810 |
| unseen | SSE-MRL (genus everywhere) | 32 | family | 0.912 |
| unseen | SSE-MRL (genus everywhere) | 32 | genus | 0.983 |
| unseen | SSE-MRL (genus everywhere) | 64 | order | 0.814 |
| unseen | SSE-MRL (genus everywhere) | 64 | family | 0.922 |
| unseen | SSE-MRL (genus everywhere) | 64 | genus | 0.982 |
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
