### E6 — roll-up / drill-down within Physical Sciences (8000 test papers; kappa tuned on training papers by ARI)

| policy | method | level | kappa | n_groups | n_main_groups | n_true | coverage | NMI | NMI_main | ARI |
|---|---|---|---|---|---|---|---|---|---|---|
| connected | B6 plain encoder | field | 0.920 | 4791 | 1 | 10 | 0.288 | 0.372 | 0.000 | 0.022 |
| connected | B6 plain encoder | subfield | 0.920 | 4791 | 1 | 87 | 0.288 | 0.569 | 0.000 | 0.045 |
| connected | B6 plain encoder | topic | 0.940 | 7470 | 0 | 1150 | 0.000 | 0.836 | nan | 0.048 |
| connected | SSE-treeSC | field | 0.920 | 5644 | 4 | 10 | 0.251 | 0.412 | 0.581 | 0.077 |
| connected | SSE-treeSC | subfield | 0.860 | 6198 | 5 | 87 | 0.182 | 0.620 | 0.528 | 0.085 |
| connected | SSE-treeSC | topic | 0.840 | 6790 | 3 | 1150 | 0.066 | 0.829 | 0.437 | 0.114 |
| connected | SSE-tree | field | 0.900 | 4417 | 1 | 10 | 0.429 | 0.347 | 0.000 | 0.025 |
| connected | SSE-tree | subfield | 0.820 | 5907 | 2 | 87 | 0.222 | 0.596 | 0.109 | 0.049 |
| connected | SSE-tree | topic | 0.740 | 6605 | 3 | 1150 | 0.123 | 0.816 | 0.314 | 0.063 |
| connected | SSE (yes/no levels) | field | 0.940 | 5030 | 4 | 10 | 0.315 | 0.404 | 0.480 | 0.087 |
| connected | SSE (yes/no levels) | subfield | 0.880 | 5879 | 5 | 87 | 0.215 | 0.609 | 0.432 | 0.068 |
| connected | SSE (yes/no levels) | topic | 0.860 | 6887 | 2 | 1150 | 0.047 | 0.832 | 0.340 | 0.108 |
| connected | B3 separate (graded+contrastive) | field | 0.900 | 4621 | 2 | 10 | 0.383 | 0.370 | 0.183 | 0.049 |
| connected | B3 separate (graded+contrastive) | subfield | 0.840 | 5568 | 5 | 87 | 0.265 | 0.608 | 0.452 | 0.084 |
| connected | B3 separate (graded+contrastive) | topic | 0.840 | 6662 | 3 | 1150 | 0.065 | 0.832 | 0.390 | 0.130 |
| connected | B4 CSN (graded+contrastive) | field | 0.840 | 5122 | 2 | 10 | 0.327 | 0.376 | 0.122 | 0.047 |
| connected | B4 CSN (graded+contrastive) | subfield | 0.820 | 5427 | 2 | 87 | 0.286 | 0.573 | 0.092 | 0.032 |
| connected | B4 CSN (graded+contrastive) | topic | 0.840 | 6567 | 3 | 1150 | 0.065 | 0.831 | 0.399 | 0.130 |
| center | B6 plain encoder | field | 0.880 | 1025 | 15 | 10 | 0.504 | 0.339 | 0.279 | 0.044 |
| center | B6 plain encoder | subfield | 0.900 | 4165 | 2 | 87 | 0.063 | 0.597 | 0.241 | 0.046 |
| center | B6 plain encoder | topic | 0.920 | 6843 | 0 | 1150 | 0.000 | 0.834 | nan | 0.062 |
| center | SSE-treeSC | field | 0.760 | 785 | 16 | 10 | 0.703 | 0.437 | 0.505 | 0.235 |
| center | SSE-treeSC | subfield | 0.700 | 1942 | 10 | 87 | 0.337 | 0.574 | 0.575 | 0.159 |
| center | SSE-treeSC | topic | 0.740 | 4620 | 5 | 1150 | 0.067 | 0.814 | 0.544 | 0.164 |
| center | SSE-tree | field | 0.760 | 1222 | 11 | 10 | 0.569 | 0.363 | 0.352 | 0.115 |
| center | SSE-tree | subfield | 0.700 | 3717 | 8 | 87 | 0.199 | 0.585 | 0.431 | 0.083 |
| center | SSE-tree | topic | 0.660 | 5897 | 1 | 1150 | 0.018 | 0.820 | 0.000 | 0.089 |
| center | SSE (yes/no levels) | field | 0.800 | 363 | 13 | 10 | 0.779 | 0.450 | 0.519 | 0.272 |
| center | SSE (yes/no levels) | subfield | 0.760 | 2036 | 14 | 87 | 0.327 | 0.584 | 0.628 | 0.165 |
| center | SSE (yes/no levels) | topic | 0.760 | 4781 | 4 | 1150 | 0.052 | 0.818 | 0.519 | 0.168 |
| center | B3 separate (graded+contrastive) | field | 0.760 | 845 | 15 | 10 | 0.671 | 0.440 | 0.524 | 0.251 |
| center | B3 separate (graded+contrastive) | subfield | 0.700 | 2386 | 12 | 87 | 0.323 | 0.591 | 0.632 | 0.172 |
| center | B3 separate (graded+contrastive) | topic | 0.740 | 4880 | 5 | 1150 | 0.067 | 0.818 | 0.576 | 0.174 |
| center | B4 CSN (graded+contrastive) | field | 0.680 | 1020 | 12 | 10 | 0.682 | 0.437 | 0.528 | 0.246 |
| center | B4 CSN (graded+contrastive) | subfield | 0.680 | 2121 | 16 | 87 | 0.376 | 0.583 | 0.592 | 0.158 |
| center | B4 CSN (graded+contrastive) | topic | 0.740 | 4759 | 2 | 1150 | 0.023 | 0.818 | 0.314 | 0.176 |
