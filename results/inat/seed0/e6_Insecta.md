### E6 — roll-up / drill-down within Insecta (11281 test images; kappa tuned on training images by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain CLIP | order | 0.880 | 3372 | 2 | 17 | 0.682 | 0.268 | 0.017 | 0.130 |
| connected | B6 plain CLIP | family | 0.900 | 6138 | 5 | 190 | 0.429 | 0.574 | 0.401 | 0.107 |
| connected | B6 plain CLIP | genus | 0.920 | 9176 | 3 | 1472 | 0.137 | 0.811 | 0.326 | 0.026 |
| connected | SSE (yes/no levels) | order | 0.960 | 2321 | 4 | 17 | 0.785 | 0.569 | 0.862 | 0.772 |
| connected | SSE (yes/no levels) | family | 0.880 | 4021 | 4 | 190 | 0.628 | 0.569 | 0.442 | 0.126 |
| connected | SSE (yes/no levels) | genus | 0.860 | 7160 | 7 | 1472 | 0.292 | 0.785 | 0.451 | 0.042 |
| connected | SSE-tree | order | 0.940 | 1487 | 1 | 17 | 0.864 | 0.219 | 0.000 | 0.119 |
| connected | SSE-tree | family | 0.820 | 3993 | 4 | 190 | 0.632 | 0.572 | 0.445 | 0.133 |
| connected | SSE-tree | genus | 0.800 | 9081 | 3 | 1472 | 0.123 | 0.813 | 0.303 | 0.027 |
| connected | SSE-treeSC | order | 0.940 | 1589 | 2 | 17 | 0.853 | 0.407 | 0.438 | 0.384 |
| connected | SSE-treeSC | family | 0.880 | 5003 | 5 | 190 | 0.519 | 0.592 | 0.454 | 0.130 |
| connected | SSE-treeSC | genus | 0.860 | 7970 | 7 | 1472 | 0.201 | 0.812 | 0.504 | 0.068 |
| connected | B3 separate (graded+contrastive) | order | 0.960 | 2844 | 4 | 17 | 0.739 | 0.547 | 0.885 | 0.759 |
| connected | B3 separate (graded+contrastive) | family | 0.860 | 5073 | 5 | 190 | 0.527 | 0.589 | 0.449 | 0.128 |
| connected | B3 separate (graded+contrastive) | genus | 0.840 | 7837 | 6 | 1472 | 0.227 | 0.799 | 0.434 | 0.042 |
| connected | B4 CSN (graded+contrastive) | order | 0.820 | 2187 | 2 | 17 | 0.803 | 0.410 | 0.466 | 0.416 |
| connected | B4 CSN (graded+contrastive) | family | 0.840 | 4829 | 4 | 190 | 0.550 | 0.579 | 0.443 | 0.127 |
| connected | B4 CSN (graded+contrastive) | genus | 0.840 | 7932 | 5 | 1472 | 0.188 | 0.809 | 0.416 | 0.052 |
| center | B6 plain CLIP | order | 0.760 | 354 | 8 | 17 | 0.828 | 0.269 | 0.262 | 0.278 |
| center | B6 plain CLIP | family | 0.820 | 2133 | 11 | 190 | 0.481 | 0.514 | 0.463 | 0.160 |
| center | B6 plain CLIP | genus | 0.880 | 6653 | 4 | 1472 | 0.099 | 0.775 | 0.358 | 0.031 |
| center | SSE (yes/no levels) | order | 0.820 | 330 | 6 | 17 | 0.899 | 0.630 | 0.773 | 0.834 |
| center | SSE (yes/no levels) | family | 0.800 | 2314 | 17 | 190 | 0.527 | 0.629 | 0.666 | 0.345 |
| center | SSE (yes/no levels) | genus | 0.820 | 6767 | 2 | 1472 | 0.041 | 0.813 | 0.290 | 0.094 |
| center | SSE-tree | order | 0.740 | 307 | 5 | 17 | 0.905 | 0.620 | 0.760 | 0.838 |
| center | SSE-tree | family | 0.700 | 2480 | 7 | 190 | 0.568 | 0.586 | 0.540 | 0.227 |
| center | SSE-tree | genus | 0.720 | 6970 | 5 | 1472 | 0.099 | 0.794 | 0.412 | 0.051 |
| center | SSE-treeSC | order | 0.760 | 273 | 5 | 17 | 0.900 | 0.653 | 0.784 | 0.855 |
| center | SSE-treeSC | family | 0.800 | 2984 | 14 | 190 | 0.436 | 0.638 | 0.683 | 0.327 |
| center | SSE-treeSC | genus | 0.800 | 6494 | 3 | 1472 | 0.051 | 0.808 | 0.406 | 0.097 |
| center | B3 separate (graded+contrastive) | order | 0.780 | 363 | 5 | 17 | 0.887 | 0.648 | 0.820 | 0.850 |
| center | B3 separate (graded+contrastive) | family | 0.760 | 2538 | 18 | 190 | 0.555 | 0.637 | 0.665 | 0.335 |
| center | B3 separate (graded+contrastive) | genus | 0.800 | 7272 | 2 | 1472 | 0.024 | 0.821 | 0.325 | 0.102 |
| center | B4 CSN (graded+contrastive) | order | 0.620 | 615 | 5 | 17 | 0.876 | 0.657 | 0.826 | 0.858 |
| center | B4 CSN (graded+contrastive) | family | 0.740 | 2581 | 18 | 190 | 0.550 | 0.638 | 0.660 | 0.336 |
| center | B4 CSN (graded+contrastive) | genus | 0.780 | 6608 | 3 | 1472 | 0.050 | 0.812 | 0.414 | 0.108 |
