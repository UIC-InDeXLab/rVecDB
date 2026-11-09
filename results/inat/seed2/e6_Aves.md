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
| connected | SSE-treeSC | order | 0.960 | 3087 | 5 | 32 | 0.466 | 0.543 | 0.851 | 0.538 |
| connected | SSE-treeSC | family | 0.860 | 4695 | 5 | 147 | 0.215 | 0.664 | 0.602 | 0.172 |
| connected | SSE-treeSC | genus | 0.840 | 5151 | 5 | 648 | 0.139 | 0.798 | 0.514 | 0.100 |
| connected | B3 separate (graded+contrastive) | order | 0.940 | 1199 | 1 | 32 | 0.802 | 0.294 | 0.000 | 0.112 |
| connected | B3 separate (graded+contrastive) | family | 0.860 | 4386 | 8 | 147 | 0.249 | 0.685 | 0.741 | 0.276 |
| connected | B3 separate (graded+contrastive) | genus | 0.840 | 4848 | 8 | 648 | 0.183 | 0.800 | 0.589 | 0.132 |
| connected | B4 CSN (graded+contrastive) | order | 0.800 | 1708 | 1 | 32 | 0.729 | 0.272 | 0.000 | 0.022 |
| connected | B4 CSN (graded+contrastive) | family | 0.840 | 4286 | 11 | 147 | 0.270 | 0.689 | 0.790 | 0.286 |
| connected | B4 CSN (graded+contrastive) | genus | 0.840 | 4837 | 9 | 648 | 0.171 | 0.805 | 0.635 | 0.146 |
| center | B6 plain CLIP | order | 0.760 | 499 | 9 | 32 | 0.733 | 0.308 | 0.243 | 0.207 |
| center | B6 plain CLIP | family | 0.820 | 2319 | 11 | 147 | 0.306 | 0.551 | 0.298 | 0.041 |
| center | B6 plain CLIP | genus | 0.860 | 4484 | 4 | 648 | 0.076 | 0.767 | 0.269 | 0.029 |
| center | SSE (yes/no levels) | order | 0.780 | 215 | 13 | 32 | 0.857 | 0.518 | 0.543 | 0.634 |
| center | SSE (yes/no levels) | family | 0.760 | 1568 | 12 | 147 | 0.316 | 0.625 | 0.598 | 0.220 |
| center | SSE (yes/no levels) | genus | 0.800 | 4029 | 5 | 648 | 0.056 | 0.792 | 0.569 | 0.114 |
| center | SSE-tree | order | 0.860 | 495 | 8 | 32 | 0.714 | 0.522 | 0.639 | 0.653 |
| center | SSE-tree | family | 0.680 | 2286 | 5 | 147 | 0.305 | 0.604 | 0.442 | 0.131 |
| center | SSE-tree | genus | 0.640 | 4341 | 6 | 648 | 0.096 | 0.781 | 0.515 | 0.074 |
| center | SSE-treeSC | order | 0.800 | 257 | 13 | 32 | 0.844 | 0.526 | 0.559 | 0.647 |
| center | SSE-treeSC | family | 0.740 | 1650 | 14 | 147 | 0.354 | 0.627 | 0.574 | 0.238 |
| center | SSE-treeSC | genus | 0.760 | 3513 | 5 | 648 | 0.072 | 0.781 | 0.560 | 0.125 |
| center | B3 separate (graded+contrastive) | order | 0.800 | 237 | 10 | 32 | 0.836 | 0.528 | 0.563 | 0.663 |
| center | B3 separate (graded+contrastive) | family | 0.720 | 1569 | 14 | 147 | 0.367 | 0.625 | 0.597 | 0.256 |
| center | B3 separate (graded+contrastive) | genus | 0.780 | 4126 | 2 | 648 | 0.032 | 0.796 | 0.362 | 0.121 |
| center | B4 CSN (graded+contrastive) | order | 0.620 | 433 | 13 | 32 | 0.802 | 0.555 | 0.623 | 0.663 |
| center | B4 CSN (graded+contrastive) | family | 0.700 | 1696 | 18 | 147 | 0.401 | 0.634 | 0.625 | 0.236 |
| center | B4 CSN (graded+contrastive) | genus | 0.760 | 3782 | 4 | 648 | 0.049 | 0.789 | 0.470 | 0.129 |
