### E6 — roll-up / drill-down within Aves (6586 test images; kappa tuned on training images by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain CLIP | order | 0.860 | 2181 | 1 | 32 | 0.645 | 0.311 | 0.000 | 0.060 |
| connected | B6 plain CLIP | family | 0.900 | 5350 | 2 | 147 | 0.104 | 0.640 | 0.263 | 0.038 |
| connected | B6 plain CLIP | genus | 0.900 | 5350 | 2 | 648 | 0.104 | 0.782 | 0.212 | 0.027 |
| connected | SSE (yes/no levels) | order | 0.940 | 1429 | 2 | 32 | 0.755 | 0.346 | 0.090 | 0.152 |
| connected | SSE (yes/no levels) | family | 0.880 | 4215 | 11 | 147 | 0.280 | 0.686 | 0.757 | 0.307 |
| connected | SSE (yes/no levels) | genus | 0.860 | 4815 | 10 | 648 | 0.184 | 0.803 | 0.641 | 0.148 |
| connected | SSE-tree | order | 0.960 | 2324 | 4 | 32 | 0.618 | 0.543 | 0.676 | 0.616 |
| connected | SSE-tree | family | 0.820 | 4622 | 5 | 147 | 0.259 | 0.648 | 0.526 | 0.144 |
| connected | SSE-tree | genus | 0.720 | 5286 | 4 | 648 | 0.140 | 0.790 | 0.443 | 0.068 |
| center | B6 plain CLIP | order | 0.760 | 499 | 9 | 32 | 0.733 | 0.308 | 0.243 | 0.207 |
| center | B6 plain CLIP | family | 0.820 | 2319 | 11 | 147 | 0.306 | 0.551 | 0.298 | 0.041 |
| center | B6 plain CLIP | genus | 0.860 | 4484 | 4 | 648 | 0.076 | 0.767 | 0.269 | 0.029 |
| center | SSE (yes/no levels) | order | 0.800 | 262 | 13 | 32 | 0.835 | 0.552 | 0.608 | 0.664 |
| center | SSE (yes/no levels) | family | 0.760 | 1636 | 16 | 147 | 0.375 | 0.636 | 0.655 | 0.283 |
| center | SSE (yes/no levels) | genus | 0.780 | 3679 | 6 | 648 | 0.081 | 0.787 | 0.621 | 0.136 |
| center | SSE-tree | order | 0.860 | 532 | 8 | 32 | 0.713 | 0.504 | 0.592 | 0.630 |
| center | SSE-tree | family | 0.700 | 2570 | 7 | 147 | 0.266 | 0.613 | 0.449 | 0.154 |
| center | SSE-tree | genus | 0.640 | 4546 | 4 | 648 | 0.059 | 0.786 | 0.490 | 0.065 |
