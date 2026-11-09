### E6 — roll-up / drill-down within Insecta (11281 test images; kappa tuned on training images by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain CLIP | order | 0.880 | 3372 | 2 | 17 | 0.682 | 0.268 | 0.017 | 0.130 |
| connected | B6 plain CLIP | family | 0.900 | 6138 | 5 | 190 | 0.429 | 0.574 | 0.401 | 0.107 |
| connected | B6 plain CLIP | genus | 0.920 | 9176 | 3 | 1472 | 0.137 | 0.811 | 0.326 | 0.026 |
| connected | SSE (yes/no levels) | order | 0.960 | 2746 | 3 | 17 | 0.748 | 0.459 | 0.649 | 0.538 |
| connected | SSE (yes/no levels) | family | 0.880 | 4718 | 4 | 190 | 0.568 | 0.573 | 0.437 | 0.123 |
| connected | SSE (yes/no levels) | genus | 0.880 | 8915 | 5 | 1472 | 0.096 | 0.831 | 0.485 | 0.087 |
| connected | SSE-tree | order | 0.940 | 1458 | 1 | 17 | 0.867 | 0.212 | 0.000 | 0.112 |
| connected | SSE-tree | family | 0.820 | 3989 | 4 | 190 | 0.633 | 0.572 | 0.445 | 0.133 |
| connected | SSE-tree | genus | 0.800 | 9172 | 3 | 1472 | 0.116 | 0.816 | 0.304 | 0.030 |
| connected | SSE-treeSC | order | 0.960 | 3151 | 4 | 17 | 0.707 | 0.535 | 0.902 | 0.744 |
| connected | SSE-treeSC | family | 0.880 | 5833 | 5 | 190 | 0.456 | 0.591 | 0.440 | 0.126 |
| connected | SSE-treeSC | genus | 0.860 | 8369 | 8 | 1472 | 0.164 | 0.820 | 0.540 | 0.076 |
| connected | B3 separate (graded+contrastive) | order | 0.960 | 2779 | 4 | 17 | 0.742 | 0.552 | 0.893 | 0.767 |
| connected | B3 separate (graded+contrastive) | family | 0.860 | 5386 | 5 | 190 | 0.497 | 0.590 | 0.457 | 0.132 |
| connected | B3 separate (graded+contrastive) | genus | 0.840 | 7697 | 7 | 1472 | 0.227 | 0.803 | 0.473 | 0.053 |
| connected | B4 CSN (graded+contrastive) | order | 0.820 | 2417 | 3 | 17 | 0.782 | 0.470 | 0.650 | 0.531 |
| connected | B4 CSN (graded+contrastive) | family | 0.840 | 5488 | 6 | 190 | 0.489 | 0.590 | 0.497 | 0.129 |
| connected | B4 CSN (graded+contrastive) | genus | 0.840 | 7910 | 6 | 1472 | 0.188 | 0.811 | 0.470 | 0.061 |
| center | B6 plain CLIP | order | 0.760 | 354 | 8 | 17 | 0.828 | 0.269 | 0.262 | 0.278 |
| center | B6 plain CLIP | family | 0.820 | 2133 | 11 | 190 | 0.481 | 0.514 | 0.463 | 0.160 |
| center | B6 plain CLIP | genus | 0.880 | 6653 | 4 | 1472 | 0.099 | 0.775 | 0.358 | 0.031 |
| center | SSE (yes/no levels) | order | 0.780 | 247 | 5 | 17 | 0.900 | 0.643 | 0.778 | 0.849 |
| center | SSE (yes/no levels) | family | 0.780 | 2125 | 18 | 190 | 0.562 | 0.631 | 0.658 | 0.328 |
| center | SSE (yes/no levels) | genus | 0.820 | 6808 | 3 | 1472 | 0.046 | 0.816 | 0.416 | 0.109 |
| center | SSE-tree | order | 0.800 | 498 | 5 | 17 | 0.872 | 0.609 | 0.784 | 0.828 |
| center | SSE-tree | family | 0.740 | 3290 | 9 | 190 | 0.498 | 0.590 | 0.563 | 0.211 |
| center | SSE-tree | genus | 0.720 | 7319 | 4 | 1472 | 0.083 | 0.798 | 0.329 | 0.045 |
| center | SSE-treeSC | order | 0.760 | 298 | 6 | 17 | 0.901 | 0.651 | 0.797 | 0.854 |
| center | SSE-treeSC | family | 0.780 | 2649 | 16 | 190 | 0.491 | 0.634 | 0.677 | 0.320 |
| center | SSE-treeSC | genus | 0.800 | 6502 | 3 | 1472 | 0.045 | 0.808 | 0.413 | 0.096 |
| center | B3 separate (graded+contrastive) | order | 0.780 | 341 | 5 | 17 | 0.889 | 0.648 | 0.812 | 0.855 |
| center | B3 separate (graded+contrastive) | family | 0.740 | 2259 | 16 | 190 | 0.550 | 0.624 | 0.632 | 0.311 |
| center | B3 separate (graded+contrastive) | genus | 0.800 | 7102 | 2 | 1472 | 0.035 | 0.819 | 0.306 | 0.103 |
| center | B4 CSN (graded+contrastive) | order | 0.620 | 699 | 7 | 17 | 0.886 | 0.653 | 0.815 | 0.848 |
| center | B4 CSN (graded+contrastive) | family | 0.720 | 2411 | 17 | 190 | 0.547 | 0.634 | 0.675 | 0.338 |
| center | B4 CSN (graded+contrastive) | genus | 0.780 | 6506 | 3 | 1472 | 0.051 | 0.810 | 0.413 | 0.109 |
