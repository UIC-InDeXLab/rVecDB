# AwA2 round3_summary.md — mean ± spread over 3 seeds

Spread = standard deviation across seeds. Same test queries in every seed.


### E1 own facet

| method | diet | family | habitat |
|---|---|---|---|
| SSE | 0.867 ± 0.001 | 0.528 ± 0.001 | 0.902 ± 0.000 |
| SSE-tree | 0.868 ± 0.002 | 0.722 ± 0.001 | 0.903 ± 0.000 |
| SSE-treeSC | 0.867 ± 0.002 | 0.710 ± 0.000 | 0.903 ± 0.001 |
| B1 labels | 0.587 ± 0.000 | 0.727 ± 0.000 | 0.608 ± 0.001 |
| B1-soft | 0.786 ± 0.000 | 0.529 ± 0.000 | 0.755 ± 0.000 |
| B2 CLIP+text | 0.169 ± 0.000 | 0.241 ± 0.000 | 0.255 ± 0.000 |
| B6 plain CLIP | 0.281 ± 0.000 | 0.237 ± 0.000 | 0.308 ± 0.000 |

### E3 general search

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE | 0.839 ± 0.002 | 0.819 ± 0.000 | 0.822 ± 0.001 |

### E4 queries

| method | NDCG@10 [all] | NDCG@10 [x unseen] | P@10_feasible [all] | P@10_feasible [x unseen] | predicate_F1 [all] | predicate_F1 [x unseen] |
|---|---|---|---|---|---|---|
| SSE | 0.549 ± 0.002 | 0.522 ± 0.002 | 0.561 ± 0.001 | 0.550 ± 0.003 | 0.752 ± 0.001 | 0.722 ± 0.001 |
| SSE-tree | 0.580 ± 0.007 | 0.542 ± 0.008 | 0.564 ± 0.005 | 0.547 ± 0.006 | 0.753 ± 0.001 | 0.723 ± 0.001 |
| SSE-treeSC | 0.574 ± 0.001 | 0.538 ± 0.002 | 0.564 ± 0.004 | 0.548 ± 0.007 | 0.753 ± 0.001 | 0.723 ± 0.002 |
| B1 labels | 0.384 ± 0.002 | 0.351 ± 0.001 | 0.356 ± 0.001 | 0.326 ± 0.000 | 0.484 ± 0.001 | 0.472 ± 0.001 |
| B1-soft | 0.462 ± 0.000 | 0.458 ± 0.000 | 0.437 ± 0.000 | 0.465 ± 0.001 | 0.665 ± 0.000 | 0.680 ± 0.000 |
| B2 CLIP+text | 0.409 ± 0.000 | 0.404 ± 0.000 | 0.374 ± 0.000 | 0.382 ± 0.000 | 0.474 ± 0.000 | 0.501 ± 0.000 |
| B6 plain CLIP | 0.398 ± 0.000 | 0.397 ± 0.000 | 0.332 ± 0.000 | 0.338 ± 0.000 | 0.554 ± 0.000 | 0.616 ± 0.000 |

### E4 no-mixing error (lower=better)

| method | A same-habitat/diff-order | B same-family/diff-habitat |
|---|---|---|
| SSE | 0.147 ± 0.003 | 0.142 ± 0.002 |
| SSE-tree | 0.147 ± 0.004 | 0.141 ± 0.003 |
| SSE-treeSC | 0.147 ± 0.003 | 0.141 ± 0.003 |
| B1 labels | 0.340 ± 0.001 | 0.548 ± 0.000 |
| B1-soft | 0.252 ± 0.000 | 0.299 ± 0.001 |
| B2 CLIP+text | 0.379 ± 0.000 | 0.206 ± 0.000 |
| B6 plain CLIP | 0.323 ± 0.000 | 0.192 ± 0.000 |

### E2b prefix keeps levels (pair AUC)

| method | same-family AUC | same-genus AUC | same-order AUC |
|---|---|---|---|
| SSE order@8 | 0.924 ± 0.000 | 0.911 ± 0.001 | 0.961 ± 0.001 |
| SSE family@32 | 0.995 ± 0.000 | 0.982 ± 0.000 | 0.819 ± 0.001 |
| SSE genus@64 | 0.969 ± 0.001 | 0.994 ± 0.000 | 0.745 ± 0.001 |
| SSE-tree order@8 | 0.943 ± 0.001 | 0.933 ± 0.001 | 0.959 ± 0.000 |
| SSE-tree family@32 | 0.996 ± 0.000 | 0.985 ± 0.000 | 0.955 ± 0.001 |
| SSE-tree genus@64 | 0.997 ± 0.000 | 0.995 ± 0.000 | 0.941 ± 0.000 |
| SSE-treeSC order@8 | 0.935 ± 0.001 | 0.926 ± 0.001 | 0.960 ± 0.001 |
| SSE-treeSC family@32 | 0.997 ± 0.000 | 0.986 ± 0.000 | 0.946 ± 0.000 |
| SSE-treeSC genus@64 | 0.992 ± 0.000 | 0.996 ± 0.000 | 0.923 ± 0.001 |
| B1 labels family view | 0.985 ± 0.000 | 0.978 ± 0.000 | 0.959 ± 0.000 |
| B1-soft family view | 0.993 ± 0.000 | 0.979 ± 0.000 | 0.821 ± 0.000 |
| B2 CLIP+text family view | 0.796 ± 0.000 | 0.854 ± 0.000 | 0.635 ± 0.000 |
| B6 plain CLIP family view | 0.839 ± 0.000 | 0.934 ± 0.000 | 0.628 ± 0.000 |

### E5b in-between

| method | spearman |
|---|---|
| SSE | 0.888 ± 0.000 |
| SSE-tree | 0.890 ± 0.001 |
| SSE-treeSC | 0.889 ± 0.001 |
| B1 labels | 0.591 ± 0.001 |
| B1-soft | 0.722 ± 0.001 |
| B2 CLIP+text | 0.212 ± 0.000 |
| B6 plain CLIP | 0.234 ± 0.000 |

### E5c threshold dial

| method | monotonic |
|---|---|
| SSE | 1.000 ± 0.000 |
| SSE-tree | 1.000 ± 0.000 |
| SSE-treeSC | 1.000 ± 0.000 |
| B1 labels | 0.903 ± 0.000 |
| B1-soft | 1.000 ± 0.000 |
| B2 CLIP+text | 0.988 ± 0.000 |
| B6 plain CLIP | 0.915 ± 0.000 |

### E2 zoom levels [seen_test]

| method | family@32 | genus@64 | order@8 |
|---|---|---|---|
| SSE | 0.985 ± 0.000 | 0.985 ± 0.000 | 0.995 ± 0.000 |
| SSE-tree | 0.974 ± 0.000 | 0.970 ± 0.002 | 0.990 ± 0.001 |
| SSE-treeSC | 0.984 ± 0.000 | 0.984 ± 0.000 | 0.994 ± 0.000 |
| SSE-MRL (genus everywhere) | 0.883 ± 0.001 | 0.984 ± 0.000 | 0.691 ± 0.005 |
| CLIP-PCA | 0.743 ± 0.000 | 0.835 ± 0.000 | 0.593 ± 0.000 |

### E2 zoom levels [unseen]

| method | family@32 | genus@64 | order@8 |
|---|---|---|---|
| SSE | 0.960 ± 0.001 | 0.977 ± 0.001 | 0.890 ± 0.002 |
| SSE-tree | 0.987 ± 0.001 | 0.986 ± 0.001 | 0.941 ± 0.000 |
| SSE-treeSC | 0.984 ± 0.000 | 0.986 ± 0.000 | 0.933 ± 0.002 |
| SSE-MRL (genus everywhere) | 0.955 ± 0.006 | 0.976 ± 0.001 | 0.783 ± 0.011 |
| CLIP-PCA | 0.864 ± 0.000 | 0.938 ± 0.000 | 0.646 ± 0.000 |
