### E6 — roll-up / drill-down within Physical Sciences (8000 test papers; kappa tuned on training papers by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain encoder | field | 0.920 | 4791 | 1 | 10 | 0.288 | 0.372 | 0.000 | 0.022 |
| connected | B6 plain encoder | subfield | 0.920 | 4791 | 1 | 87 | 0.288 | 0.569 | 0.000 | 0.045 |
| connected | B6 plain encoder | topic | 0.940 | 7470 | 0 | 1150 | 0.000 | 0.836 | nan | 0.048 |
| connected | SSE-treeSC | field | 0.920 | 5626 | 4 | 10 | 0.253 | 0.401 | 0.445 | 0.060 |
| connected | SSE-treeSC | subfield | 0.860 | 6180 | 6 | 87 | 0.190 | 0.621 | 0.557 | 0.090 |
| connected | SSE-treeSC | topic | 0.840 | 6749 | 2 | 1150 | 0.071 | 0.826 | 0.248 | 0.092 |
| connected | SSE-tree | field | 0.900 | 4877 | 1 | 10 | 0.361 | 0.362 | 0.000 | 0.035 |
| connected | SSE-tree | subfield | 0.820 | 6212 | 2 | 87 | 0.188 | 0.603 | 0.125 | 0.049 |
| connected | SSE-tree | topic | 0.740 | 6717 | 2 | 1150 | 0.100 | 0.820 | 0.240 | 0.069 |
| connected | SSE (yes/no levels) | field | 0.920 | 3404 | 1 | 10 | 0.548 | 0.314 | 0.000 | 0.011 |
| connected | SSE (yes/no levels) | subfield | 0.860 | 4663 | 1 | 87 | 0.380 | 0.535 | 0.000 | 0.020 |
| connected | SSE (yes/no levels) | topic | 0.840 | 6032 | 7 | 1150 | 0.162 | 0.818 | 0.520 | 0.100 |
| connected | B3 separate (graded+contrastive) | field | 0.920 | 6372 | 3 | 10 | 0.141 | 0.418 | 0.617 | 0.062 |
| connected | B3 separate (graded+contrastive) | subfield | 0.840 | 6723 | 3 | 87 | 0.119 | 0.622 | 0.428 | 0.066 |
| connected | B3 separate (graded+contrastive) | topic | 0.840 | 7190 | 3 | 1150 | 0.049 | 0.832 | 0.464 | 0.099 |
| connected | B4 CSN (graded+contrastive) | field | 0.820 | 4367 | 1 | 10 | 0.426 | 0.347 | 0.000 | 0.025 |
| connected | B4 CSN (graded+contrastive) | subfield | 0.820 | 5186 | 2 | 87 | 0.307 | 0.570 | 0.105 | 0.034 |
| connected | B4 CSN (graded+contrastive) | topic | 0.820 | 6117 | 5 | 1150 | 0.126 | 0.822 | 0.456 | 0.107 |
| center | B6 plain encoder | field | 0.880 | 1025 | 15 | 10 | 0.504 | 0.339 | 0.279 | 0.044 |
| center | B6 plain encoder | subfield | 0.900 | 4165 | 2 | 87 | 0.063 | 0.597 | 0.241 | 0.046 |
| center | B6 plain encoder | topic | 0.920 | 6843 | 0 | 1150 | 0.000 | 0.834 | nan | 0.062 |
| center | SSE-treeSC | field | 0.760 | 794 | 13 | 10 | 0.677 | 0.434 | 0.507 | 0.226 |
| center | SSE-treeSC | subfield | 0.720 | 2313 | 11 | 87 | 0.293 | 0.585 | 0.619 | 0.156 |
| center | SSE-treeSC | topic | 0.760 | 5179 | 4 | 1150 | 0.052 | 0.822 | 0.533 | 0.157 |
| center | SSE-tree | field | 0.740 | 1191 | 11 | 10 | 0.568 | 0.355 | 0.334 | 0.108 |
| center | SSE-tree | subfield | 0.680 | 3604 | 9 | 87 | 0.214 | 0.577 | 0.427 | 0.080 |
| center | SSE-tree | topic | 0.640 | 5637 | 3 | 1150 | 0.044 | 0.814 | 0.453 | 0.104 |
| center | SSE (yes/no levels) | field | 0.800 | 493 | 13 | 10 | 0.705 | 0.451 | 0.560 | 0.287 |
| center | SSE (yes/no levels) | subfield | 0.720 | 1819 | 13 | 87 | 0.368 | 0.578 | 0.627 | 0.187 |
| center | SSE (yes/no levels) | topic | 0.760 | 4893 | 4 | 1150 | 0.054 | 0.820 | 0.517 | 0.178 |
| center | B3 separate (graded+contrastive) | field | 0.760 | 849 | 14 | 10 | 0.654 | 0.439 | 0.528 | 0.243 |
| center | B3 separate (graded+contrastive) | subfield | 0.700 | 2441 | 12 | 87 | 0.304 | 0.594 | 0.645 | 0.169 |
| center | B3 separate (graded+contrastive) | topic | 0.740 | 4950 | 4 | 1150 | 0.055 | 0.822 | 0.554 | 0.183 |
| center | B4 CSN (graded+contrastive) | field | 0.660 | 860 | 10 | 10 | 0.664 | 0.437 | 0.519 | 0.255 |
| center | B4 CSN (graded+contrastive) | subfield | 0.660 | 1953 | 14 | 87 | 0.366 | 0.575 | 0.583 | 0.165 |
| center | B4 CSN (graded+contrastive) | topic | 0.740 | 5008 | 3 | 1150 | 0.044 | 0.822 | 0.475 | 0.177 |
