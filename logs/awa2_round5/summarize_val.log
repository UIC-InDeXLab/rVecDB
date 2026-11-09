# AwA2 round5_val_summary.md — mean ± spread over 3 seeds

Spread = standard deviation across seeds. Same test queries in every seed.


### E1 own facet

| method | diet | family | habitat |
|---|---|---|---|
| SSE | 0.835 ± 0.003 | 0.554 ± 0.005 | 0.666 ± 0.001 |
| SSE-tree | 0.837 ± 0.002 | 0.718 ± 0.001 | 0.673 ± 0.001 |
| SSE-treeSC | 0.836 ± 0.003 | 0.709 ± 0.000 | 0.673 ± 0.001 |

### E3 general search

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE | 0.856 ± 0.001 | 0.801 ± 0.000 | 0.820 ± 0.000 |
| SSE-tree | 0.863 ± 0.001 | 0.790 ± 0.000 | 0.813 ± 0.001 |
| SSE-treeSC | 0.866 ± 0.001 | 0.793 ± 0.000 | 0.819 ± 0.001 |

### E4 queries

| method | NDCG@10 [all] | NDCG@10 [x unseen] | P@10_feasible [all] | P@10_feasible [x unseen] | predicate_F1 [all] | predicate_F1 [x unseen] |
|---|---|---|---|---|---|---|
| SSE | 0.571 ± 0.001 | 0.549 ± 0.003 | 0.543 ± 0.002 | 0.517 ± 0.005 | 0.707 ± 0.001 | 0.693 ± 0.003 |
| SSE-tree | 0.608 ± 0.000 | 0.574 ± 0.008 | 0.535 ± 0.003 | 0.506 ± 0.005 | 0.709 ± 0.001 | 0.693 ± 0.005 |
| SSE-treeSC | 0.605 ± 0.002 | 0.570 ± 0.006 | 0.540 ± 0.002 | 0.515 ± 0.002 | 0.709 ± 0.001 | 0.694 ± 0.005 |

### E4 no-mixing error (lower=better)

| method | A same-habitat/diff-order | B same-family/diff-habitat |
|---|---|---|
| SSE | 0.236 ± 0.005 | 0.159 ± 0.002 |
| SSE-tree | 0.234 ± 0.006 | 0.159 ± 0.001 |
| SSE-treeSC | 0.235 ± 0.005 | 0.158 ± 0.002 |

### E2b prefix keeps levels (pair AUC)

| method | same-family AUC | same-genus AUC | same-order AUC |
|---|---|---|---|
| SSE order@8 | 0.919 ± 0.001 | 0.898 ± 0.001 | 0.949 ± 0.004 |
| SSE family@32 | 0.920 ± 0.003 | 0.978 ± 0.000 | 0.843 ± 0.004 |
| SSE genus@64 | 0.886 ± 0.001 | 0.991 ± 0.000 | 0.804 ± 0.001 |
| SSE-tree order@8 | 0.930 ± 0.001 | 0.914 ± 0.001 | 0.970 ± 0.001 |
| SSE-tree family@32 | 0.965 ± 0.002 | 0.981 ± 0.000 | 0.961 ± 0.001 |
| SSE-tree genus@64 | 0.959 ± 0.001 | 0.992 ± 0.000 | 0.953 ± 0.001 |
| SSE-treeSC order@8 | 0.926 ± 0.001 | 0.910 ± 0.002 | 0.966 ± 0.001 |
| SSE-treeSC family@32 | 0.964 ± 0.001 | 0.981 ± 0.000 | 0.953 ± 0.000 |
| SSE-treeSC genus@64 | 0.952 ± 0.001 | 0.992 ± 0.000 | 0.945 ± 0.000 |

### E5b in-between

| method | spearman |
|---|---|
| SSE | 0.565 ± 0.000 |
| SSE-tree | 0.574 ± 0.001 |
| SSE-treeSC | 0.574 ± 0.001 |

### E5c threshold dial

| method | monotonic |
|---|---|
| SSE | 1.000 ± 0.000 |
| SSE-tree | 1.000 ± 0.000 |
| SSE-treeSC | 1.000 ± 0.000 |

### E2 zoom levels [seen_test]

| method | family@32 | genus@64 | order@8 |
|---|---|---|---|
| SSE | 0.992 ± 0.000 | 0.992 ± 0.000 | 1.000 ± 0.000 |
| SSE-tree | 0.991 ± 0.000 | 0.987 ± 0.001 | 1.000 ± 0.000 |
| SSE-treeSC | 0.993 ± 0.000 | 0.993 ± 0.000 | 1.000 ± 0.000 |
| CLIP-PCA | 0.786 ± 0.000 | 0.839 ± 0.000 | 0.597 ± 0.000 |

### E2 zoom levels [unseen]

| method | family@32 | genus@64 | order@8 |
|---|---|---|---|
| SSE | 0.914 ± 0.002 | 0.922 ± 0.000 | 0.858 ± 0.004 |
| SSE-tree | 0.919 ± 0.004 | 0.922 ± 0.002 | 0.879 ± 0.004 |
| SSE-treeSC | 0.919 ± 0.002 | 0.921 ± 0.002 | 0.876 ± 0.002 |
| CLIP-PCA | 0.869 ± 0.000 | 0.885 ± 0.000 | 0.881 ± 0.000 |
