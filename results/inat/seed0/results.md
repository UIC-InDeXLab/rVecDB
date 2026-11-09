# iNat results (seed 0)

### E2 — taxonomy prefix length vs level (mAP)

**seen_test**

|                                          |     8 |    16 |    32 |    64 |   128 |
|:-----------------------------------------|------:|------:|------:|------:|------:|
| ('CLIP-PCA', 'family')                   | 0.058 | 0.092 | 0.125 | 0.156 | 0.171 |
| ('CLIP-PCA', 'genus')                    | 0.011 | 0.032 | 0.06  | 0.093 | 0.112 |
| ('CLIP-PCA', 'order')                    | 0.215 | 0.264 | 0.3   | 0.323 | 0.331 |
| ('SSE (yes/no levels)', 'family')        | 0.135 | 0.19  | 0.261 | 0.316 | 0.278 |
| ('SSE (yes/no levels)', 'genus')         | 0.045 | 0.073 | 0.123 | 0.169 | 0.216 |
| ('SSE (yes/no levels)', 'order')         | 0.42  | 0.515 | 0.483 | 0.497 | 0.418 |
| ('SSE-MRL (genus everywhere)', 'family') | 0.119 | 0.226 | 0.251 | 0.271 | 0.272 |
| ('SSE-MRL (genus everywhere)', 'genus')  | 0.058 | 0.146 | 0.177 | 0.21  | 0.212 |
| ('SSE-MRL (genus everywhere)', 'order')  | 0.211 | 0.37  | 0.385 | 0.403 | 0.404 |
| ('SSE-tree', 'family')                   | 0.123 | 0.165 | 0.197 | 0.232 | 0.234 |
| ('SSE-tree', 'genus')                    | 0.035 | 0.061 | 0.102 | 0.141 | 0.161 |
| ('SSE-tree', 'order')                    | 0.394 | 0.472 | 0.467 | 0.469 | 0.443 |
| ('SSE-treeSC', 'family')                 | 0.132 | 0.192 | 0.272 | 0.316 | 0.283 |
| ('SSE-treeSC', 'genus')                  | 0.044 | 0.076 | 0.129 | 0.179 | 0.22  |
| ('SSE-treeSC', 'order')                  | 0.401 | 0.517 | 0.508 | 0.504 | 0.442 |

**unseen**

|                                          |     8 |    16 |    32 |    64 |   128 |
|:-----------------------------------------|------:|------:|------:|------:|------:|
| ('CLIP-PCA', 'family')                   | 0.062 | 0.109 | 0.157 | 0.196 | 0.217 |
| ('CLIP-PCA', 'genus')                    | 0.023 | 0.058 | 0.108 | 0.148 | 0.174 |
| ('CLIP-PCA', 'order')                    | 0.212 | 0.272 | 0.322 | 0.349 | 0.36  |
| ('SSE (yes/no levels)', 'family')        | 0.151 | 0.214 | 0.298 | 0.359 | 0.354 |
| ('SSE (yes/no levels)', 'genus')         | 0.068 | 0.12  | 0.191 | 0.258 | 0.324 |
| ('SSE (yes/no levels)', 'order')         | 0.433 | 0.517 | 0.491 | 0.513 | 0.46  |
| ('SSE-MRL (genus everywhere)', 'family') | 0.156 | 0.294 | 0.325 | 0.348 | 0.35  |
| ('SSE-MRL (genus everywhere)', 'genus')  | 0.096 | 0.233 | 0.284 | 0.32  | 0.324 |
| ('SSE-MRL (genus everywhere)', 'order')  | 0.24  | 0.418 | 0.431 | 0.448 | 0.448 |
| ('SSE-tree', 'family')                   | 0.143 | 0.192 | 0.223 | 0.264 | 0.281 |
| ('SSE-tree', 'genus')                    | 0.061 | 0.101 | 0.143 | 0.193 | 0.23  |
| ('SSE-tree', 'order')                    | 0.403 | 0.478 | 0.475 | 0.486 | 0.466 |
| ('SSE-treeSC', 'family')                 | 0.149 | 0.214 | 0.305 | 0.361 | 0.36  |
| ('SSE-treeSC', 'genus')                  | 0.067 | 0.12  | 0.204 | 0.264 | 0.328 |
| ('SSE-treeSC', 'order')                  | 0.414 | 0.515 | 0.515 | 0.522 | 0.482 |

### E2b — does each level's view keep its own and coarser levels? (pair AUC)

| method | view | same-order AUC | same-family AUC | same-genus AUC |
|---|---|---|---|---|
| SSE-tree | order | 0.949 | 0.904 | 0.951 |
| SSE-tree | family | 0.928 | 0.874 | 0.948 |
| SSE-tree | genus | 0.913 | 0.860 | 0.936 |
| SSE (yes/no levels) | order | 0.970 | 0.948 | 0.962 |
| SSE (yes/no levels) | family | 0.934 | 0.960 | 0.980 |
| SSE (yes/no levels) | genus | 0.866 | 0.910 | 0.986 |
| SSE-treeSC | order | 0.971 | 0.939 | 0.961 |
| SSE-treeSC | family | 0.949 | 0.947 | 0.977 |
| SSE-treeSC | genus | 0.898 | 0.901 | 0.984 |
| B3 separate (graded) | order | 0.948 | 0.907 | 0.949 |
| B3 separate (graded) | family | 0.932 | 0.888 | 0.946 |
| B3 separate (graded) | genus | 0.917 | 0.873 | 0.929 |
| B4 CSN (graded) | order | 0.939 | 0.882 | 0.949 |
| B4 CSN (graded) | family | 0.927 | 0.878 | 0.951 |
| B4 CSN (graded) | genus | 0.911 | 0.867 | 0.951 |
| B3 separate (graded+contrastive) | order | 0.971 | 0.938 | 0.963 |
| B3 separate (graded+contrastive) | family | 0.948 | 0.946 | 0.978 |
| B3 separate (graded+contrastive) | genus | 0.873 | 0.899 | 0.985 |
| B4 CSN (graded+contrastive) | order | 0.972 | 0.934 | 0.958 |
| B4 CSN (graded+contrastive) | family | 0.953 | 0.950 | 0.976 |
| B4 CSN (graded+contrastive) | genus | 0.884 | 0.897 | 0.983 |
| B1 labels | all levels | 0.884 | 0.918 | 0.931 |
| B6 plain CLIP | full | 0.822 | 0.877 | 0.909 |

### E3 — general search preserved

| method | overlap@10_with_CLIP | species_mAP_CLIP | species_mAP_SSE |
|---|---|---|---|
| SSE-tree | 0.869 | 0.105 | 0.108 |
| SSE (yes/no levels) | 0.685 | 0.105 | 0.124 |
| SSE-treeSC | 0.776 | 0.105 | 0.119 |
| SSE-MRL (genus everywhere) | 0.692 | 0.105 | 0.124 |
