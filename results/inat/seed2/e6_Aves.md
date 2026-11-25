### E6 — roll-up / drill-down within Aves (6586 test images; kappa tuned on training images by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain CLIP | order | 0.860 | 2181 | 1 | 32 | 0.645 | 0.311 | 0.000 | 0.060 |
| connected | B6 plain CLIP | family | 0.900 | 5350 | 2 | 147 | 0.104 | 0.640 | 0.263 | 0.038 |
| connected | B6 plain CLIP | genus | 0.900 | 5350 | 2 | 648 | 0.104 | 0.782 | 0.212 | 0.027 |
| connected | SSE (yes/no levels) | order | 0.940 | 1432 | 3 | 32 | 0.762 | 0.471 | 0.475 | 0.420 |
| connected | SSE (yes/no levels) | family | 0.880 | 4196 | 9 | 147 | 0.278 | 0.683 | 0.737 | 0.270 |
| connected | SSE (yes/no levels) | genus | 0.860 | 4761 | 10 | 648 | 0.197 | 0.802 | 0.638 | 0.146 |
| connected | SSE-tree | order | 0.960 | 2317 | 3 | 32 | 0.601 | 0.542 | 0.658 | 0.619 |
| connected | SSE-tree | family | 0.820 | 4582 | 4 | 147 | 0.252 | 0.644 | 0.469 | 0.120 |
| connected | SSE-tree | genus | 0.720 | 5191 | 4 | 648 | 0.158 | 0.786 | 0.414 | 0.063 |
| center | B6 plain CLIP | order | 0.760 | 499 | 9 | 32 | 0.733 | 0.308 | 0.243 | 0.207 |
| center | B6 plain CLIP | family | 0.820 | 2319 | 11 | 147 | 0.306 | 0.551 | 0.298 | 0.041 |
| center | B6 plain CLIP | genus | 0.860 | 4484 | 4 | 648 | 0.076 | 0.767 | 0.269 | 0.029 |
| center | SSE (yes/no levels) | order | 0.780 | 215 | 13 | 32 | 0.857 | 0.518 | 0.543 | 0.634 |
| center | SSE (yes/no levels) | family | 0.760 | 1568 | 12 | 147 | 0.316 | 0.625 | 0.598 | 0.220 |
| center | SSE (yes/no levels) | genus | 0.800 | 4029 | 5 | 648 | 0.056 | 0.792 | 0.569 | 0.114 |
| center | SSE-tree | order | 0.860 | 495 | 8 | 32 | 0.714 | 0.522 | 0.639 | 0.653 |
| center | SSE-tree | family | 0.680 | 2286 | 5 | 147 | 0.305 | 0.604 | 0.442 | 0.131 |
| center | SSE-tree | genus | 0.640 | 4341 | 6 | 648 | 0.096 | 0.781 | 0.515 | 0.074 |
