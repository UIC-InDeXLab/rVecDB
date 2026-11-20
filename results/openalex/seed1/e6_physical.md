### E6 — roll-up / drill-down within Physical Sciences (8000 test papers; kappa tuned on training papers by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain encoder | field | 0.920 | 4791 | 1 | 10 | 0.288 | 0.372 | 0.000 | 0.022 |
| connected | B6 plain encoder | subfield | 0.920 | 4791 | 1 | 87 | 0.288 | 0.569 | 0.000 | 0.045 |
| connected | SSE-treeSC | field | 0.880 | 5429 | 2 | 10 | 0.286 | 0.379 | 0.134 | 0.042 |
| connected | SSE-treeSC | subfield | 0.840 | 5996 | 5 | 87 | 0.211 | 0.613 | 0.451 | 0.076 |
| connected | SSE-tree | field | 0.840 | 4394 | 1 | 10 | 0.435 | 0.347 | 0.000 | 0.029 |
| connected | SSE-tree | subfield | 0.780 | 6109 | 1 | 87 | 0.185 | 0.601 | 0.000 | 0.048 |
| connected | SSE (yes/no levels) | field | 0.940 | 5545 | 4 | 10 | 0.244 | 0.410 | 0.530 | 0.082 |
| connected | SSE (yes/no levels) | subfield | 0.860 | 6041 | 5 | 87 | 0.203 | 0.613 | 0.478 | 0.073 |
| connected | B3 separate (graded+contrastive) | field | 0.860 | 5255 | 2 | 10 | 0.311 | 0.378 | 0.126 | 0.052 |
| connected | B3 separate (graded+contrastive) | subfield | 0.840 | 5958 | 2 | 87 | 0.215 | 0.593 | 0.106 | 0.042 |
| connected | B4 CSN (graded+contrastive) | field | 0.860 | 4811 | 1 | 10 | 0.362 | 0.360 | 0.000 | 0.033 |
| connected | B4 CSN (graded+contrastive) | subfield | 0.840 | 5371 | 1 | 87 | 0.292 | 0.564 | 0.000 | 0.026 |
| center | B6 plain encoder | field | 0.880 | 1025 | 15 | 10 | 0.504 | 0.339 | 0.279 | 0.044 |
| center | B6 plain encoder | subfield | 0.900 | 4165 | 2 | 87 | 0.063 | 0.597 | 0.241 | 0.046 |
| center | SSE-treeSC | field | 0.720 | 959 | 16 | 10 | 0.707 | 0.426 | 0.485 | 0.203 |
| center | SSE-treeSC | subfield | 0.680 | 2161 | 14 | 87 | 0.360 | 0.579 | 0.594 | 0.167 |
| center | SSE-tree | field | 0.680 | 1441 | 8 | 10 | 0.560 | 0.343 | 0.269 | 0.072 |
| center | SSE-tree | subfield | 0.620 | 3301 | 8 | 87 | 0.246 | 0.567 | 0.360 | 0.087 |
| center | SSE (yes/no levels) | field | 0.820 | 499 | 12 | 10 | 0.693 | 0.455 | 0.560 | 0.286 |
| center | SSE (yes/no levels) | subfield | 0.740 | 2107 | 13 | 87 | 0.326 | 0.590 | 0.631 | 0.171 |
| center | B3 separate (graded+contrastive) | field | 0.720 | 1217 | 13 | 10 | 0.620 | 0.442 | 0.551 | 0.267 |
| center | B3 separate (graded+contrastive) | subfield | 0.700 | 2596 | 13 | 87 | 0.316 | 0.596 | 0.631 | 0.158 |
| center | B4 CSN (graded+contrastive) | field | 0.720 | 1021 | 13 | 10 | 0.653 | 0.431 | 0.511 | 0.219 |
| center | B4 CSN (graded+contrastive) | subfield | 0.720 | 2474 | 11 | 87 | 0.279 | 0.595 | 0.638 | 0.151 |
