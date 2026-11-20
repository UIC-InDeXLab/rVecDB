### E6 — roll-up / drill-down within Physical Sciences (8000 test papers; kappa tuned on training papers by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain encoder | field | 0.920 | 4791 | 1 | 10 | 0.288 | 0.372 | 0.000 | 0.022 |
| connected | B6 plain encoder | subfield | 0.920 | 4791 | 1 | 87 | 0.288 | 0.569 | 0.000 | 0.045 |
| connected | SSE-treeSC | field | 0.880 | 5754 | 4 | 10 | 0.243 | 0.412 | 0.545 | 0.088 |
| connected | SSE-treeSC | subfield | 0.820 | 5979 | 5 | 87 | 0.217 | 0.615 | 0.509 | 0.092 |
| connected | SSE-tree | field | 0.840 | 4523 | 1 | 10 | 0.416 | 0.352 | 0.000 | 0.031 |
| connected | SSE-tree | subfield | 0.780 | 6073 | 2 | 87 | 0.184 | 0.607 | 0.132 | 0.056 |
| connected | SSE (yes/no levels) | field | 0.920 | 3772 | 1 | 10 | 0.500 | 0.325 | 0.000 | 0.013 |
| connected | SSE (yes/no levels) | subfield | 0.860 | 5273 | 6 | 87 | 0.291 | 0.611 | 0.518 | 0.110 |
| connected | B3 separate (graded+contrastive) | field | 0.860 | 5016 | 2 | 10 | 0.341 | 0.373 | 0.131 | 0.044 |
| connected | B3 separate (graded+contrastive) | subfield | 0.840 | 5861 | 6 | 87 | 0.228 | 0.617 | 0.524 | 0.091 |
| connected | B4 CSN (graded+contrastive) | field | 0.840 | 4668 | 1 | 10 | 0.386 | 0.354 | 0.000 | 0.028 |
| connected | B4 CSN (graded+contrastive) | subfield | 0.840 | 5409 | 5 | 87 | 0.276 | 0.598 | 0.365 | 0.063 |
| center | B6 plain encoder | field | 0.880 | 1025 | 15 | 10 | 0.504 | 0.339 | 0.279 | 0.044 |
| center | B6 plain encoder | subfield | 0.900 | 4165 | 2 | 87 | 0.063 | 0.597 | 0.241 | 0.046 |
| center | SSE-treeSC | field | 0.680 | 623 | 13 | 10 | 0.753 | 0.427 | 0.471 | 0.225 |
| center | SSE-treeSC | subfield | 0.700 | 2385 | 14 | 87 | 0.301 | 0.590 | 0.621 | 0.151 |
| center | SSE-tree | field | 0.700 | 1807 | 12 | 10 | 0.530 | 0.357 | 0.307 | 0.081 |
| center | SSE-tree | subfield | 0.660 | 4168 | 7 | 87 | 0.169 | 0.594 | 0.468 | 0.077 |
| center | SSE (yes/no levels) | field | 0.780 | 332 | 13 | 10 | 0.779 | 0.457 | 0.538 | 0.310 |
| center | SSE (yes/no levels) | subfield | 0.680 | 1377 | 16 | 87 | 0.455 | 0.560 | 0.587 | 0.179 |
| center | B3 separate (graded+contrastive) | field | 0.700 | 865 | 13 | 10 | 0.693 | 0.430 | 0.503 | 0.235 |
| center | B3 separate (graded+contrastive) | subfield | 0.660 | 1934 | 15 | 87 | 0.388 | 0.570 | 0.566 | 0.152 |
| center | B4 CSN (graded+contrastive) | field | 0.660 | 701 | 10 | 10 | 0.696 | 0.425 | 0.489 | 0.233 |
| center | B4 CSN (graded+contrastive) | subfield | 0.720 | 2482 | 16 | 87 | 0.301 | 0.599 | 0.633 | 0.151 |
