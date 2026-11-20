# OpenAlex results (seed 0)

### E2 — topic prefix length vs level (mAP)

**seen_test**

|                                            |     8 |    16 |    32 |    64 |   128 |
|:-------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                  | 0.544 | 0.525 | 0.515 | 0.506 | 0.502 |
| ('Encoder-PCA', 'field')                   | 0.218 | 0.237 | 0.244 | 0.242 | 0.239 |
| ('Encoder-PCA', 'subfield')                | 0.122 | 0.158 | 0.187 | 0.197 | 0.2   |
| ('Encoder-PCA', 'topic')                   | 0.083 | 0.142 | 0.203 | 0.234 | 0.251 |
| ('SSE (yes/no levels)', 'domain')          | 0.749 | 0.617 | 0.589 | 0.557 | 0.475 |
| ('SSE (yes/no levels)', 'field')           | 0.141 | 0.333 | 0.441 | 0.373 | 0.3   |
| ('SSE (yes/no levels)', 'subfield')        | 0.049 | 0.136 | 0.192 | 0.305 | 0.267 |
| ('SSE (yes/no levels)', 'topic')           | 0.019 | 0.076 | 0.13  | 0.233 | 0.309 |
| ('SSE-MRL (topic everywhere)', 'domain')   | 0.52  | 0.508 | 0.484 | 0.479 | 0.481 |
| ('SSE-MRL (topic everywhere)', 'field')    | 0.271 | 0.279 | 0.288 | 0.292 | 0.293 |
| ('SSE-MRL (topic everywhere)', 'subfield') | 0.178 | 0.214 | 0.25  | 0.258 | 0.259 |
| ('SSE-MRL (topic everywhere)', 'topic')    | 0.146 | 0.21  | 0.28  | 0.305 | 0.308 |
| ('SSE-tree', 'domain')                     | 0.748 | 0.73  | 0.7   | 0.67  | 0.642 |
| ('SSE-tree', 'field')                      | 0.164 | 0.22  | 0.308 | 0.291 | 0.273 |
| ('SSE-tree', 'subfield')                   | 0.07  | 0.119 | 0.185 | 0.201 | 0.203 |
| ('SSE-tree', 'topic')                      | 0.04  | 0.096 | 0.161 | 0.211 | 0.24  |
| ('SSE-treeSC', 'domain')                   | 0.755 | 0.708 | 0.644 | 0.596 | 0.53  |
| ('SSE-treeSC', 'field')                    | 0.151 | 0.306 | 0.429 | 0.37  | 0.308 |
| ('SSE-treeSC', 'subfield')                 | 0.058 | 0.138 | 0.203 | 0.302 | 0.269 |
| ('SSE-treeSC', 'topic')                    | 0.029 | 0.09  | 0.151 | 0.249 | 0.311 |

**unseen**

|                                            |     8 |    16 |    32 |    64 |   128 |
|:-------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                  | 0.542 | 0.532 | 0.525 | 0.519 | 0.516 |
| ('Encoder-PCA', 'field')                   | 0.289 | 0.33  | 0.348 | 0.356 | 0.355 |
| ('Encoder-PCA', 'subfield')                | 0.227 | 0.3   | 0.343 | 0.368 | 0.379 |
| ('Encoder-PCA', 'topic')                   | 0.198 | 0.3   | 0.38  | 0.431 | 0.455 |
| ('SSE (yes/no levels)', 'domain')          | 0.74  | 0.62  | 0.584 | 0.569 | 0.499 |
| ('SSE (yes/no levels)', 'field')           | 0.173 | 0.349 | 0.448 | 0.439 | 0.413 |
| ('SSE (yes/no levels)', 'subfield')        | 0.088 | 0.211 | 0.298 | 0.383 | 0.413 |
| ('SSE (yes/no levels)', 'topic')           | 0.057 | 0.163 | 0.257 | 0.377 | 0.46  |
| ('SSE-MRL (topic everywhere)', 'domain')   | 0.531 | 0.534 | 0.511 | 0.507 | 0.507 |
| ('SSE-MRL (topic everywhere)', 'field')    | 0.362 | 0.376 | 0.4   | 0.407 | 0.408 |
| ('SSE-MRL (topic everywhere)', 'subfield') | 0.297 | 0.342 | 0.391 | 0.409 | 0.411 |
| ('SSE-MRL (topic everywhere)', 'topic')    | 0.258 | 0.343 | 0.428 | 0.459 | 0.462 |
| ('SSE-tree', 'domain')                     | 0.756 | 0.742 | 0.716 | 0.69  | 0.664 |
| ('SSE-tree', 'field')                      | 0.216 | 0.293 | 0.398 | 0.385 | 0.374 |
| ('SSE-tree', 'subfield')                   | 0.135 | 0.215 | 0.318 | 0.345 | 0.362 |
| ('SSE-tree', 'topic')                      | 0.103 | 0.196 | 0.313 | 0.375 | 0.416 |
| ('SSE-treeSC', 'domain')                   | 0.747 | 0.709 | 0.646 | 0.614 | 0.556 |
| ('SSE-treeSC', 'field')                    | 0.194 | 0.342 | 0.45  | 0.443 | 0.421 |
| ('SSE-treeSC', 'subfield')                 | 0.11  | 0.22  | 0.319 | 0.396 | 0.419 |
| ('SSE-treeSC', 'topic')                    | 0.076 | 0.184 | 0.288 | 0.403 | 0.471 |

### E2b — does each level's view keep its own and coarser levels? (pair AUC)

| method | view | same-domain AUC | same-field AUC | same-subfield AUC | same-topic AUC |
|---|---|---|---|---|---|
| SSE-treeSC | domain | 0.910 | 0.826 | 0.836 | 0.880 |
| SSE-treeSC | field | 0.830 | 0.913 | 0.927 | 0.965 |
| SSE-treeSC | subfield | 0.791 | 0.892 | 0.941 | 0.982 |
| SSE-treeSC | topic | 0.727 | 0.856 | 0.918 | 0.989 |
| SSE-tree | domain | 0.905 | 0.826 | 0.838 | 0.886 |
| SSE-tree | field | 0.873 | 0.868 | 0.896 | 0.958 |
| SSE-tree | subfield | 0.852 | 0.857 | 0.894 | 0.966 |
| SSE-tree | topic | 0.832 | 0.844 | 0.888 | 0.972 |
| SSE (yes/no levels) | domain | 0.903 | 0.828 | 0.838 | 0.881 |
| SSE (yes/no levels) | field | 0.756 | 0.920 | 0.932 | 0.966 |
| SSE (yes/no levels) | subfield | 0.729 | 0.894 | 0.945 | 0.982 |
| SSE (yes/no levels) | topic | 0.648 | 0.845 | 0.915 | 0.989 |
| B3 separate (graded+contrastive) | domain | 0.913 | 0.825 | 0.835 | 0.880 |
| B3 separate (graded+contrastive) | field | 0.822 | 0.915 | 0.929 | 0.967 |
| B3 separate (graded+contrastive) | subfield | 0.790 | 0.891 | 0.943 | 0.982 |
| B3 separate (graded+contrastive) | topic | 0.731 | 0.851 | 0.917 | 0.988 |
| B4 CSN (graded+contrastive) | domain | 0.912 | 0.820 | 0.829 | 0.883 |
| B4 CSN (graded+contrastive) | field | 0.832 | 0.913 | 0.927 | 0.967 |
| B4 CSN (graded+contrastive) | subfield | 0.788 | 0.893 | 0.942 | 0.982 |
| B4 CSN (graded+contrastive) | topic | 0.723 | 0.853 | 0.917 | 0.989 |
| B1 labels | all levels | 0.767 | 0.834 | 0.889 | 0.950 |
| B6 plain encoder | full | 0.627 | 0.784 | 0.866 | 0.971 |

### E3 — general search preserved

| method | overlap@10_with_encoder | topic_mAP_encoder | topic_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.815 | 0.237 | 0.253 |
| SSE-tree | 0.840 | 0.237 | 0.238 |
| SSE (yes/no levels) | 0.704 | 0.237 | 0.261 |
| SSE-MRL (topic everywhere) | 0.756 | 0.237 | 0.258 |
