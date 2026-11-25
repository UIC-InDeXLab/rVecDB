# AwA2 summary.md — mean ± spread over 3 seeds

Spread = standard deviation across seeds. Same test queries in every seed.


### E1 own facet

| method | diet | family | habitat |
|---|---|---|---|
| SSE-treeSC | 0.866 ± 0.002 | 0.662 ± 0.005 | 0.926 ± 0.002 |
| SSE-tree | 0.865 ± 0.002 | 0.681 ± 0.006 | 0.927 ± 0.002 |
| B1 labels | 0.573 ± 0.001 | 0.717 ± 0.000 | 0.499 ± 0.001 |
| B1-soft | 0.760 ± 0.000 | 0.509 ± 0.000 | 0.683 ± 0.001 |
| B2 CLIP+text | 0.169 ± 0.000 | 0.222 ± 0.000 | 0.244 ± 0.000 |
| B6 plain CLIP | 0.281 ± 0.000 | 0.229 ± 0.000 | 0.285 ± 0.000 |
| B3 separate | 0.864 ± 0.002 | 0.690 ± 0.003 | 0.923 ± 0.003 |
| B4 CSN | 0.868 ± 0.002 | 0.701 ± 0.001 | 0.920 ± 0.003 |

### E3 general search

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.891 ± 0.002 | 0.813 ± 0.000 | 0.810 ± 0.001 |
| SSE-tree | 0.891 ± 0.003 | 0.826 ± 0.000 | 0.822 ± 0.000 |

### E4 queries

| method | NDCG@10 [all] | NDCG@10 [x unseen] | P@10_feasible [all] | P@10_feasible [x unseen] | predicate_F1 [all] | predicate_F1 [x unseen] |
|---|---|---|---|---|---|---|
| SSE-treeSC | 0.584 ± 0.001 | 0.545 ± 0.003 | 0.586 ± 0.002 | 0.566 ± 0.007 | 0.760 ± 0.002 | 0.722 ± 0.003 |
| SSE-tree | 0.588 ± 0.005 | 0.544 ± 0.008 | 0.592 ± 0.007 | 0.564 ± 0.011 | 0.761 ± 0.002 | 0.722 ± 0.002 |
| B1 labels | 0.356 ± 0.000 | 0.322 ± 0.001 | 0.322 ± 0.000 | 0.295 ± 0.001 | 0.444 ± 0.000 | 0.425 ± 0.000 |
| B1-soft | 0.452 ± 0.000 | 0.446 ± 0.001 | 0.419 ± 0.001 | 0.440 ± 0.001 | 0.631 ± 0.000 | 0.640 ± 0.000 |
| B2 CLIP+text | 0.405 ± 0.000 | 0.401 ± 0.000 | 0.357 ± 0.000 | 0.364 ± 0.000 | 0.476 ± 0.000 | 0.508 ± 0.000 |
| B6 plain CLIP | 0.382 ± 0.000 | 0.392 ± 0.000 | 0.327 ± 0.000 | 0.343 ± 0.000 | 0.532 ± 0.000 | 0.592 ± 0.000 |
| B3 separate | 0.592 ± 0.002 | 0.555 ± 0.002 | 0.592 ± 0.001 | 0.574 ± 0.006 | 0.763 ± 0.001 | 0.722 ± 0.002 |
| B4 CSN | 0.571 ± 0.001 | 0.543 ± 0.001 | 0.575 ± 0.003 | 0.558 ± 0.004 | 0.757 ± 0.002 | 0.724 ± 0.003 |

### E4 no-mixing error (lower=better)

| method | A same-habitat/diff-order | B same-family/diff-habitat |
|---|---|---|
| SSE-treeSC | 0.141 ± 0.002 | 0.117 ± 0.003 |
| SSE-tree | 0.141 ± 0.001 | 0.117 ± 0.003 |
| B1 labels | 0.344 ± 0.001 | 0.599 ± 0.002 |
| B1-soft | 0.271 ± 0.000 | 0.270 ± 0.001 |
| B2 CLIP+text | 0.382 ± 0.000 | 0.227 ± 0.000 |
| B6 plain CLIP | 0.338 ± 0.000 | 0.235 ± 0.000 |
| B3 separate | 0.146 ± 0.003 | 0.120 ± 0.001 |
| B4 CSN | 0.143 ± 0.000 | 0.110 ± 0.007 |

### E2b prefix keeps levels (pair AUC)

| method | same-family AUC | same-genus AUC | same-order AUC |
|---|---|---|---|
| SSE-treeSC order@8 | 0.946 ± 0.001 | 0.944 ± 0.001 | 0.952 ± 0.001 |
| SSE-treeSC family@32 | 0.998 ± 0.000 | 0.989 ± 0.000 | 0.913 ± 0.004 |
| SSE-treeSC genus@64 | 0.995 ± 0.001 | 0.998 ± 0.000 | 0.870 ± 0.005 |
| SSE-tree order@8 | 0.950 ± 0.001 | 0.945 ± 0.000 | 0.954 ± 0.002 |
| SSE-tree family@32 | 0.997 ± 0.000 | 0.989 ± 0.000 | 0.926 ± 0.004 |
| SSE-tree genus@64 | 0.998 ± 0.000 | 0.997 ± 0.000 | 0.902 ± 0.004 |
| B1 labels family view | 0.984 ± 0.000 | 0.977 ± 0.000 | 0.953 ± 0.000 |
| B1-soft family view | 0.993 ± 0.000 | 0.978 ± 0.000 | 0.808 ± 0.000 |
| B2 CLIP+text family view | 0.794 ± 0.000 | 0.865 ± 0.000 | 0.625 ± 0.000 |
| B6 plain CLIP family view | 0.816 ± 0.000 | 0.925 ± 0.000 | 0.625 ± 0.000 |
| B3 separate order@8 | 0.950 ± 0.001 | 0.945 ± 0.001 | 0.953 ± 0.002 |
| B3 separate family@32 | 0.998 ± 0.000 | 0.988 ± 0.000 | 0.932 ± 0.002 |
| B3 separate genus@64 | 0.999 ± 0.000 | 0.998 ± 0.000 | 0.898 ± 0.008 |
| B4 CSN order@8 | 0.953 ± 0.001 | 0.950 ± 0.001 | 0.954 ± 0.002 |
| B4 CSN family@32 | 0.998 ± 0.000 | 0.989 ± 0.000 | 0.939 ± 0.001 |
| B4 CSN genus@64 | 0.998 ± 0.000 | 0.998 ± 0.000 | 0.915 ± 0.003 |

### E5b in-between

| method | spearman |
|---|---|
| SSE-treeSC | 0.916 ± 0.003 |
| SSE-tree | 0.917 ± 0.003 |
| B1 labels | 0.472 ± 0.001 |
| B1-soft | 0.639 ± 0.001 |
| B2 CLIP+text | 0.200 ± 0.000 |
| B6 plain CLIP | 0.211 ± 0.000 |
| B3 separate | 0.913 ± 0.004 |
| B4 CSN | 0.909 ± 0.003 |

### E5c threshold dial

| method | monotonic |
|---|---|
| SSE-treeSC | 1.000 ± 0.000 |
| SSE-tree | 1.000 ± 0.000 |
| B1 labels | 0.891 ± 0.000 |
| B1-soft | 1.000 ± 0.000 |
| B2 CLIP+text | 0.661 ± 0.000 |
| B6 plain CLIP | 0.842 ± 0.000 |
| B3 separate | 1.000 ± 0.000 |
| B4 CSN | 1.000 ± 0.000 |

### E2 zoom levels [seen_test]

| method | family@32 | genus@64 | order@8 |
|---|---|---|---|
| SSE-treeSC | 0.996 ± 0.000 | 0.996 ± 0.000 | 0.999 ± 0.000 |
| SSE-tree | 0.994 ± 0.000 | 0.991 ± 0.000 | 0.998 ± 0.001 |
| SSE-MRL (genus everywhere) | 0.897 ± 0.000 | 0.995 ± 0.000 | 0.705 ± 0.003 |
| CLIP-PCA | 0.721 ± 0.000 | 0.819 ± 0.000 | 0.551 ± 0.000 |

### E2 zoom levels [unseen]

| method | family@32 | genus@64 | order@8 |
|---|---|---|---|
| SSE-treeSC | 0.992 ± 0.000 | 0.993 ± 0.000 | 0.947 ± 0.007 |
| SSE-tree | 0.989 ± 0.001 | 0.992 ± 0.001 | 0.959 ± 0.007 |
| SSE-MRL (genus everywhere) | 0.925 ± 0.009 | 0.984 ± 0.001 | 0.785 ± 0.013 |
| CLIP-PCA | 0.806 ± 0.000 | 0.903 ± 0.000 | 0.637 ± 0.000 |
