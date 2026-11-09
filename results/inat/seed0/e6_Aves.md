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
| connected | SSE-treeSC | order | 0.960 | 3271 | 4 | 32 | 0.442 | 0.526 | 0.816 | 0.478 |
| connected | SSE-treeSC | family | 0.860 | 4814 | 4 | 147 | 0.187 | 0.665 | 0.605 | 0.176 |
| connected | SSE-treeSC | genus | 0.840 | 5218 | 4 | 648 | 0.129 | 0.798 | 0.473 | 0.098 |
| connected | B3 separate (graded+contrastive) | order | 0.940 | 1369 | 1 | 32 | 0.771 | 0.319 | 0.000 | 0.124 |
| connected | B3 separate (graded+contrastive) | family | 0.840 | 3713 | 7 | 147 | 0.348 | 0.663 | 0.591 | 0.199 |
| connected | B3 separate (graded+contrastive) | genus | 0.840 | 4649 | 8 | 648 | 0.199 | 0.800 | 0.597 | 0.144 |
| connected | B4 CSN (graded+contrastive) | order | 0.800 | 1802 | 1 | 32 | 0.714 | 0.286 | 0.000 | 0.035 |
| connected | B4 CSN (graded+contrastive) | family | 0.820 | 3574 | 9 | 147 | 0.392 | 0.668 | 0.658 | 0.238 |
| connected | B4 CSN (graded+contrastive) | genus | 0.840 | 4605 | 9 | 648 | 0.196 | 0.801 | 0.618 | 0.153 |
| center | B6 plain CLIP | order | 0.760 | 499 | 9 | 32 | 0.733 | 0.308 | 0.243 | 0.207 |
| center | B6 plain CLIP | family | 0.820 | 2319 | 11 | 147 | 0.306 | 0.551 | 0.298 | 0.041 |
| center | B6 plain CLIP | genus | 0.860 | 4484 | 4 | 648 | 0.076 | 0.767 | 0.269 | 0.029 |
| center | SSE (yes/no levels) | order | 0.800 | 282 | 15 | 32 | 0.840 | 0.550 | 0.612 | 0.681 |
| center | SSE (yes/no levels) | family | 0.760 | 1745 | 13 | 147 | 0.310 | 0.635 | 0.653 | 0.267 |
| center | SSE (yes/no levels) | genus | 0.800 | 4074 | 2 | 648 | 0.031 | 0.794 | 0.354 | 0.119 |
| center | SSE-tree | order | 0.860 | 564 | 5 | 32 | 0.687 | 0.519 | 0.635 | 0.653 |
| center | SSE-tree | family | 0.640 | 1844 | 10 | 147 | 0.435 | 0.584 | 0.458 | 0.111 |
| center | SSE-tree | genus | 0.640 | 4147 | 5 | 648 | 0.083 | 0.777 | 0.503 | 0.078 |
| center | SSE-treeSC | order | 0.800 | 281 | 12 | 32 | 0.805 | 0.545 | 0.632 | 0.684 |
| center | SSE-treeSC | family | 0.740 | 1759 | 14 | 147 | 0.353 | 0.636 | 0.601 | 0.280 |
| center | SSE-treeSC | genus | 0.780 | 4011 | 3 | 648 | 0.048 | 0.793 | 0.466 | 0.122 |
| center | B3 separate (graded+contrastive) | order | 0.820 | 323 | 12 | 32 | 0.777 | 0.559 | 0.654 | 0.689 |
| center | B3 separate (graded+contrastive) | family | 0.720 | 1699 | 14 | 147 | 0.358 | 0.638 | 0.640 | 0.337 |
| center | B3 separate (graded+contrastive) | genus | 0.760 | 3762 | 5 | 648 | 0.081 | 0.789 | 0.578 | 0.138 |
| center | B4 CSN (graded+contrastive) | order | 0.560 | 276 | 13 | 32 | 0.883 | 0.527 | 0.558 | 0.659 |
| center | B4 CSN (graded+contrastive) | family | 0.700 | 1703 | 15 | 147 | 0.351 | 0.636 | 0.631 | 0.223 |
| center | B4 CSN (graded+contrastive) | genus | 0.780 | 4101 | 3 | 648 | 0.038 | 0.796 | 0.509 | 0.124 |
