### E6 — roll-up / drill-down within Insecta (11281 test images; kappa tuned on training images by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain CLIP | order | 0.880 | 3372 | 2 | 17 | 0.682 | 0.268 | 0.017 | 0.130 |
| connected | B6 plain CLIP | family | 0.900 | 6138 | 5 | 190 | 0.429 | 0.574 | 0.401 | 0.107 |
| connected | B6 plain CLIP | genus | 0.920 | 9176 | 3 | 1472 | 0.137 | 0.811 | 0.326 | 0.026 |
| connected | SSE (yes/no levels) | order | 0.960 | 2536 | 3 | 17 | 0.767 | 0.470 | 0.656 | 0.543 |
| connected | SSE (yes/no levels) | family | 0.880 | 4478 | 4 | 190 | 0.588 | 0.570 | 0.444 | 0.124 |
| connected | SSE (yes/no levels) | genus | 0.860 | 7308 | 6 | 1472 | 0.265 | 0.789 | 0.433 | 0.042 |
| connected | SSE-tree | order | 0.940 | 1515 | 1 | 17 | 0.862 | 0.223 | 0.000 | 0.119 |
| connected | SSE-tree | family | 0.840 | 4783 | 4 | 190 | 0.564 | 0.579 | 0.447 | 0.134 |
| connected | SSE-tree | genus | 0.800 | 9223 | 3 | 1472 | 0.114 | 0.817 | 0.311 | 0.030 |
| connected | SSE-treeSC | order | 0.960 | 3026 | 4 | 17 | 0.721 | 0.537 | 0.892 | 0.745 |
| connected | SSE-treeSC | family | 0.860 | 4440 | 4 | 190 | 0.592 | 0.575 | 0.422 | 0.126 |
| connected | SSE-treeSC | genus | 0.860 | 8344 | 7 | 1472 | 0.142 | 0.822 | 0.523 | 0.081 |
| connected | B3 separate (graded+contrastive) | order | 0.960 | 2847 | 4 | 17 | 0.740 | 0.549 | 0.886 | 0.765 |
| connected | B3 separate (graded+contrastive) | family | 0.880 | 6532 | 5 | 190 | 0.373 | 0.600 | 0.444 | 0.122 |
| connected | B3 separate (graded+contrastive) | genus | 0.840 | 8157 | 6 | 1472 | 0.196 | 0.806 | 0.443 | 0.045 |
| connected | B4 CSN (graded+contrastive) | order | 0.820 | 2279 | 2 | 17 | 0.795 | 0.403 | 0.466 | 0.402 |
| connected | B4 CSN (graded+contrastive) | family | 0.840 | 5303 | 5 | 190 | 0.505 | 0.586 | 0.480 | 0.127 |
| connected | B4 CSN (graded+contrastive) | genus | 0.840 | 7937 | 6 | 1472 | 0.191 | 0.810 | 0.461 | 0.056 |
| center | B6 plain CLIP | order | 0.760 | 354 | 8 | 17 | 0.828 | 0.269 | 0.262 | 0.278 |
| center | B6 plain CLIP | family | 0.820 | 2133 | 11 | 190 | 0.481 | 0.514 | 0.463 | 0.160 |
| center | B6 plain CLIP | genus | 0.880 | 6653 | 4 | 1472 | 0.099 | 0.775 | 0.358 | 0.031 |
| center | SSE (yes/no levels) | order | 0.780 | 218 | 5 | 17 | 0.908 | 0.639 | 0.764 | 0.838 |
| center | SSE (yes/no levels) | family | 0.800 | 2406 | 20 | 190 | 0.536 | 0.631 | 0.677 | 0.324 |
| center | SSE (yes/no levels) | genus | 0.820 | 6808 | 3 | 1472 | 0.053 | 0.815 | 0.401 | 0.100 |
| center | SSE-tree | order | 0.740 | 328 | 5 | 17 | 0.896 | 0.595 | 0.733 | 0.826 |
| center | SSE-tree | family | 0.740 | 3178 | 7 | 190 | 0.489 | 0.596 | 0.562 | 0.241 |
| center | SSE-tree | genus | 0.720 | 7272 | 4 | 1472 | 0.080 | 0.798 | 0.375 | 0.051 |
| center | SSE-treeSC | order | 0.740 | 235 | 7 | 17 | 0.916 | 0.634 | 0.755 | 0.843 |
| center | SSE-treeSC | family | 0.760 | 2244 | 15 | 190 | 0.539 | 0.628 | 0.656 | 0.335 |
| center | SSE-treeSC | genus | 0.800 | 6496 | 3 | 1472 | 0.044 | 0.810 | 0.418 | 0.097 |
| center | B3 separate (graded+contrastive) | order | 0.760 | 288 | 5 | 17 | 0.905 | 0.655 | 0.804 | 0.857 |
| center | B3 separate (graded+contrastive) | family | 0.760 | 2375 | 19 | 190 | 0.580 | 0.634 | 0.650 | 0.330 |
| center | B3 separate (graded+contrastive) | genus | 0.780 | 6258 | 3 | 1472 | 0.046 | 0.806 | 0.415 | 0.104 |
| center | B4 CSN (graded+contrastive) | order | 0.600 | 601 | 5 | 17 | 0.884 | 0.647 | 0.811 | 0.853 |
| center | B4 CSN (graded+contrastive) | family | 0.740 | 2709 | 17 | 190 | 0.504 | 0.634 | 0.671 | 0.314 |
| center | B4 CSN (graded+contrastive) | genus | 0.780 | 6667 | 3 | 1472 | 0.048 | 0.813 | 0.410 | 0.095 |
