### E6 — roll-up / drill-down within Physical Sciences (8000 test papers; kappa tuned on training papers by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain encoder | field | 0.920 | 4791 | 1 | 10 | 0.288 | 0.372 | 0.000 | 0.022 |
| connected | B6 plain encoder | subfield | 0.920 | 4791 | 1 | 87 | 0.288 | 0.569 | 0.000 | 0.045 |
| connected | SSE-treeSC | field | 0.880 | 5744 | 3 | 10 | 0.241 | 0.399 | 0.392 | 0.056 |
| connected | SSE-treeSC | subfield | 0.820 | 6005 | 3 | 87 | 0.207 | 0.601 | 0.296 | 0.053 |
| connected | SSE-tree | field | 0.840 | 4396 | 1 | 10 | 0.434 | 0.347 | 0.000 | 0.026 |
| connected | SSE-tree | subfield | 0.780 | 6065 | 2 | 87 | 0.180 | 0.606 | 0.140 | 0.054 |
| connected | SSE (yes/no levels) | field | 0.940 | 5538 | 4 | 10 | 0.253 | 0.414 | 0.591 | 0.098 |
| connected | SSE (yes/no levels) | subfield | 0.860 | 6042 | 6 | 87 | 0.205 | 0.617 | 0.561 | 0.086 |
| connected | B3 separate (graded+contrastive) | field | 0.860 | 4710 | 1 | 10 | 0.379 | 0.356 | 0.000 | 0.029 |
| connected | B3 separate (graded+contrastive) | subfield | 0.820 | 5564 | 4 | 87 | 0.267 | 0.592 | 0.287 | 0.055 |
| connected | B4 CSN (graded+contrastive) | field | 0.840 | 4983 | 1 | 10 | 0.347 | 0.361 | 0.000 | 0.029 |
| connected | B4 CSN (graded+contrastive) | subfield | 0.840 | 5712 | 6 | 87 | 0.247 | 0.610 | 0.468 | 0.081 |
| center | B6 plain encoder | field | 0.880 | 1025 | 15 | 10 | 0.504 | 0.339 | 0.279 | 0.044 |
| center | B6 plain encoder | subfield | 0.900 | 4165 | 2 | 87 | 0.063 | 0.597 | 0.241 | 0.046 |
| center | SSE-treeSC | field | 0.720 | 996 | 13 | 10 | 0.659 | 0.434 | 0.508 | 0.232 |
| center | SSE-treeSC | subfield | 0.660 | 1998 | 15 | 87 | 0.389 | 0.574 | 0.561 | 0.156 |
| center | SSE-tree | field | 0.720 | 2040 | 10 | 10 | 0.479 | 0.375 | 0.363 | 0.099 |
| center | SSE-tree | subfield | 0.660 | 4149 | 6 | 87 | 0.153 | 0.594 | 0.390 | 0.074 |
| center | SSE (yes/no levels) | field | 0.800 | 361 | 12 | 10 | 0.746 | 0.449 | 0.520 | 0.287 |
| center | SSE (yes/no levels) | subfield | 0.720 | 1737 | 14 | 87 | 0.373 | 0.576 | 0.601 | 0.171 |
| center | B3 separate (graded+contrastive) | field | 0.700 | 813 | 14 | 10 | 0.705 | 0.427 | 0.496 | 0.223 |
| center | B3 separate (graded+contrastive) | subfield | 0.640 | 1893 | 11 | 87 | 0.362 | 0.574 | 0.589 | 0.170 |
| center | B4 CSN (graded+contrastive) | field | 0.680 | 956 | 12 | 10 | 0.690 | 0.428 | 0.489 | 0.220 |
| center | B4 CSN (graded+contrastive) | subfield | 0.700 | 2298 | 13 | 87 | 0.306 | 0.589 | 0.632 | 0.155 |
