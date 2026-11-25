### E6 — roll-up / drill-down within Aves (6586 test images; kappa tuned on training images by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain CLIP | order | 0.860 | 2181 | 1 | 32 | 0.645 | 0.311 | 0.000 | 0.060 |
| connected | B6 plain CLIP | family | 0.900 | 5350 | 2 | 147 | 0.104 | 0.640 | 0.263 | 0.038 |
| connected | B6 plain CLIP | genus | 0.900 | 5350 | 2 | 648 | 0.104 | 0.782 | 0.212 | 0.027 |
| connected | SSE (yes/no levels) | order | 0.960 | 3424 | 5 | 32 | 0.412 | 0.521 | 0.866 | 0.435 |
| connected | SSE (yes/no levels) | family | 0.880 | 5053 | 5 | 147 | 0.147 | 0.671 | 0.696 | 0.171 |
| connected | SSE (yes/no levels) | genus | 0.860 | 5376 | 5 | 648 | 0.101 | 0.804 | 0.542 | 0.103 |
| connected | SSE-tree | order | 0.960 | 2374 | 3 | 32 | 0.600 | 0.544 | 0.659 | 0.629 |
| connected | SSE-tree | family | 0.820 | 4614 | 4 | 147 | 0.249 | 0.641 | 0.465 | 0.110 |
| connected | SSE-tree | genus | 0.720 | 5173 | 4 | 648 | 0.157 | 0.785 | 0.403 | 0.054 |
| center | B6 plain CLIP | order | 0.760 | 499 | 9 | 32 | 0.733 | 0.308 | 0.243 | 0.207 |
| center | B6 plain CLIP | family | 0.820 | 2319 | 11 | 147 | 0.306 | 0.551 | 0.298 | 0.041 |
| center | B6 plain CLIP | genus | 0.860 | 4484 | 4 | 648 | 0.076 | 0.767 | 0.269 | 0.029 |
| center | SSE (yes/no levels) | order | 0.800 | 282 | 15 | 32 | 0.840 | 0.550 | 0.612 | 0.681 |
| center | SSE (yes/no levels) | family | 0.760 | 1745 | 13 | 147 | 0.310 | 0.635 | 0.653 | 0.267 |
| center | SSE (yes/no levels) | genus | 0.800 | 4074 | 2 | 648 | 0.031 | 0.794 | 0.354 | 0.119 |
| center | SSE-tree | order | 0.860 | 564 | 5 | 32 | 0.687 | 0.519 | 0.635 | 0.653 |
| center | SSE-tree | family | 0.640 | 1844 | 10 | 147 | 0.435 | 0.584 | 0.458 | 0.111 |
| center | SSE-tree | genus | 0.640 | 4147 | 5 | 648 | 0.083 | 0.777 | 0.503 | 0.078 |
