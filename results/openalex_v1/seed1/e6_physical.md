### E6 — roll-up / drill-down within Physical Sciences (8000 test papers; kappa tuned on training papers by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain encoder | field | 0.920 | 4791 | 1 | 10 | 0.288 | 0.372 | 0.000 | 0.022 |
| connected | B6 plain encoder | subfield | 0.920 | 4791 | 1 | 87 | 0.288 | 0.569 | 0.000 | 0.045 |
| connected | B6 plain encoder | topic | 0.940 | 7470 | 0 | 1150 | 0.000 | 0.836 | nan | 0.048 |
| connected | SSE-treeSC | field | 0.920 | 5428 | 2 | 10 | 0.282 | 0.382 | 0.182 | 0.042 |
| connected | SSE-treeSC | subfield | 0.860 | 5976 | 2 | 87 | 0.220 | 0.591 | 0.111 | 0.039 |
| connected | SSE-treeSC | topic | 0.840 | 6658 | 4 | 1150 | 0.091 | 0.827 | 0.489 | 0.120 |
| connected | SSE-tree | field | 0.900 | 4577 | 1 | 10 | 0.401 | 0.353 | 0.000 | 0.031 |
| connected | SSE-tree | subfield | 0.820 | 6061 | 1 | 87 | 0.199 | 0.598 | 0.000 | 0.048 |
| connected | SSE-tree | topic | 0.720 | 6407 | 1 | 1150 | 0.160 | 0.796 | 0.000 | 0.026 |
| connected | SSE (yes/no levels) | field | 0.940 | 4976 | 2 | 10 | 0.327 | 0.376 | 0.203 | 0.042 |
| connected | SSE (yes/no levels) | subfield | 0.880 | 5913 | 4 | 87 | 0.221 | 0.606 | 0.375 | 0.065 |
| connected | SSE (yes/no levels) | topic | 0.860 | 6873 | 3 | 1150 | 0.062 | 0.830 | 0.401 | 0.110 |
| connected | B3 separate (graded+contrastive) | field | 0.920 | 6072 | 3 | 10 | 0.192 | 0.408 | 0.529 | 0.064 |
| connected | B3 separate (graded+contrastive) | subfield | 0.840 | 6496 | 5 | 87 | 0.148 | 0.622 | 0.532 | 0.074 |
| connected | B3 separate (graded+contrastive) | topic | 0.840 | 7019 | 1 | 1150 | 0.050 | 0.828 | 0.000 | 0.080 |
| connected | B4 CSN (graded+contrastive) | field | 0.860 | 5139 | 2 | 10 | 0.324 | 0.375 | 0.126 | 0.043 |
| connected | B4 CSN (graded+contrastive) | subfield | 0.840 | 5517 | 4 | 87 | 0.276 | 0.594 | 0.333 | 0.058 |
| connected | B4 CSN (graded+contrastive) | topic | 0.840 | 6265 | 5 | 1150 | 0.124 | 0.821 | 0.440 | 0.094 |
| center | B6 plain encoder | field | 0.880 | 1025 | 15 | 10 | 0.504 | 0.339 | 0.279 | 0.044 |
| center | B6 plain encoder | subfield | 0.900 | 4165 | 2 | 87 | 0.063 | 0.597 | 0.241 | 0.046 |
| center | B6 plain encoder | topic | 0.920 | 6843 | 0 | 1150 | 0.000 | 0.834 | nan | 0.062 |
| center | SSE-treeSC | field | 0.780 | 968 | 13 | 10 | 0.630 | 0.439 | 0.538 | 0.235 |
| center | SSE-treeSC | subfield | 0.720 | 2234 | 13 | 87 | 0.362 | 0.589 | 0.594 | 0.173 |
| center | SSE-treeSC | topic | 0.740 | 4549 | 6 | 1150 | 0.075 | 0.812 | 0.568 | 0.173 |
| center | SSE-tree | field | 0.740 | 1065 | 11 | 10 | 0.588 | 0.347 | 0.325 | 0.099 |
| center | SSE-tree | subfield | 0.660 | 3059 | 10 | 87 | 0.272 | 0.559 | 0.392 | 0.084 |
| center | SSE-tree | topic | 0.640 | 5657 | 3 | 1150 | 0.048 | 0.815 | 0.447 | 0.098 |
| center | SSE (yes/no levels) | field | 0.820 | 512 | 15 | 10 | 0.716 | 0.451 | 0.538 | 0.267 |
| center | SSE (yes/no levels) | subfield | 0.720 | 1695 | 12 | 87 | 0.393 | 0.571 | 0.586 | 0.182 |
| center | SSE (yes/no levels) | topic | 0.760 | 4688 | 4 | 1150 | 0.054 | 0.817 | 0.516 | 0.183 |
| center | B3 separate (graded+contrastive) | field | 0.740 | 572 | 12 | 10 | 0.697 | 0.416 | 0.475 | 0.203 |
| center | B3 separate (graded+contrastive) | subfield | 0.700 | 2260 | 16 | 87 | 0.320 | 0.582 | 0.598 | 0.142 |
| center | B3 separate (graded+contrastive) | topic | 0.720 | 4584 | 2 | 1150 | 0.029 | 0.809 | 0.292 | 0.133 |
| center | B4 CSN (graded+contrastive) | field | 0.680 | 706 | 12 | 10 | 0.694 | 0.416 | 0.470 | 0.202 |
| center | B4 CSN (graded+contrastive) | subfield | 0.720 | 2362 | 13 | 87 | 0.281 | 0.590 | 0.617 | 0.144 |
| center | B4 CSN (graded+contrastive) | topic | 0.760 | 4921 | 3 | 1150 | 0.035 | 0.817 | 0.457 | 0.133 |
