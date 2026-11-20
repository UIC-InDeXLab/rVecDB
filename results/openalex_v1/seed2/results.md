# OpenAlex results (seed 2)

### E2 — topic prefix length vs level (mAP)

**seen_test**

|                                            |     8 |    16 |    32 |    64 |   128 |
|:-------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                  | 0.544 | 0.525 | 0.515 | 0.506 | 0.502 |
| ('Encoder-PCA', 'field')                   | 0.218 | 0.237 | 0.244 | 0.242 | 0.239 |
| ('Encoder-PCA', 'subfield')                | 0.122 | 0.158 | 0.187 | 0.197 | 0.2   |
| ('Encoder-PCA', 'topic')                   | 0.083 | 0.142 | 0.203 | 0.234 | 0.251 |
| ('SSE (yes/no levels)', 'domain')          | 0.747 | 0.637 | 0.599 | 0.568 | 0.481 |
| ('SSE (yes/no levels)', 'field')           | 0.143 | 0.327 | 0.44  | 0.371 | 0.298 |
| ('SSE (yes/no levels)', 'subfield')        | 0.05  | 0.129 | 0.19  | 0.304 | 0.264 |
| ('SSE (yes/no levels)', 'topic')           | 0.02  | 0.068 | 0.13  | 0.234 | 0.305 |
| ('SSE-MRL (topic everywhere)', 'domain')   | 0.522 | 0.502 | 0.478 | 0.474 | 0.475 |
| ('SSE-MRL (topic everywhere)', 'field')    | 0.271 | 0.269 | 0.285 | 0.291 | 0.291 |
| ('SSE-MRL (topic everywhere)', 'subfield') | 0.179 | 0.21  | 0.247 | 0.257 | 0.258 |
| ('SSE-MRL (topic everywhere)', 'topic')    | 0.147 | 0.209 | 0.275 | 0.303 | 0.304 |
| ('SSE-tree', 'domain')                     | 0.747 | 0.73  | 0.698 | 0.67  | 0.644 |
| ('SSE-tree', 'field')                      | 0.168 | 0.239 | 0.313 | 0.297 | 0.274 |
| ('SSE-tree', 'subfield')                   | 0.071 | 0.117 | 0.183 | 0.201 | 0.202 |
| ('SSE-tree', 'topic')                      | 0.041 | 0.093 | 0.167 | 0.206 | 0.239 |
| ('SSE-treeSC', 'domain')                   | 0.757 | 0.712 | 0.647 | 0.601 | 0.534 |
| ('SSE-treeSC', 'field')                    | 0.153 | 0.303 | 0.43  | 0.368 | 0.307 |
| ('SSE-treeSC', 'subfield')                 | 0.058 | 0.129 | 0.202 | 0.301 | 0.269 |
| ('SSE-treeSC', 'topic')                    | 0.031 | 0.086 | 0.15  | 0.252 | 0.31  |

**unseen**

|                                            |     8 |    16 |    32 |    64 |   128 |
|:-------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                  | 0.542 | 0.532 | 0.525 | 0.519 | 0.516 |
| ('Encoder-PCA', 'field')                   | 0.289 | 0.33  | 0.348 | 0.356 | 0.355 |
| ('Encoder-PCA', 'subfield')                | 0.227 | 0.3   | 0.343 | 0.368 | 0.379 |
| ('Encoder-PCA', 'topic')                   | 0.198 | 0.3   | 0.38  | 0.431 | 0.455 |
| ('SSE (yes/no levels)', 'domain')          | 0.747 | 0.637 | 0.601 | 0.585 | 0.511 |
| ('SSE (yes/no levels)', 'field')           | 0.176 | 0.359 | 0.454 | 0.442 | 0.415 |
| ('SSE (yes/no levels)', 'subfield')        | 0.09  | 0.219 | 0.299 | 0.383 | 0.413 |
| ('SSE (yes/no levels)', 'topic')           | 0.059 | 0.161 | 0.254 | 0.375 | 0.459 |
| ('SSE-MRL (topic everywhere)', 'domain')   | 0.538 | 0.523 | 0.511 | 0.503 | 0.505 |
| ('SSE-MRL (topic everywhere)', 'field')    | 0.366 | 0.386 | 0.401 | 0.408 | 0.409 |
| ('SSE-MRL (topic everywhere)', 'subfield') | 0.296 | 0.343 | 0.391 | 0.409 | 0.411 |
| ('SSE-MRL (topic everywhere)', 'topic')    | 0.259 | 0.341 | 0.421 | 0.453 | 0.458 |
| ('SSE-tree', 'domain')                     | 0.757 | 0.743 | 0.717 | 0.693 | 0.67  |
| ('SSE-tree', 'field')                      | 0.214 | 0.312 | 0.398 | 0.39  | 0.376 |
| ('SSE-tree', 'subfield')                   | 0.135 | 0.219 | 0.31  | 0.343 | 0.359 |
| ('SSE-tree', 'topic')                      | 0.105 | 0.194 | 0.308 | 0.373 | 0.413 |
| ('SSE-treeSC', 'domain')                   | 0.757 | 0.714 | 0.653 | 0.62  | 0.564 |
| ('SSE-treeSC', 'field')                    | 0.196 | 0.35  | 0.455 | 0.446 | 0.424 |
| ('SSE-treeSC', 'subfield')                 | 0.11  | 0.227 | 0.316 | 0.395 | 0.42  |
| ('SSE-treeSC', 'topic')                    | 0.078 | 0.183 | 0.282 | 0.398 | 0.471 |

### E2b — does each level's view keep its own and coarser levels? (pair AUC)

| method | view | same-domain AUC | same-field AUC | same-subfield AUC | same-topic AUC |
|---|---|---|---|---|---|
| SSE-treeSC | domain | 0.912 | 0.828 | 0.839 | 0.881 |
| SSE-treeSC | field | 0.832 | 0.913 | 0.929 | 0.967 |
| SSE-treeSC | subfield | 0.793 | 0.892 | 0.942 | 0.982 |
| SSE-treeSC | topic | 0.733 | 0.858 | 0.922 | 0.989 |
| SSE-tree | domain | 0.906 | 0.825 | 0.837 | 0.886 |
| SSE-tree | field | 0.875 | 0.869 | 0.895 | 0.955 |
| SSE-tree | subfield | 0.855 | 0.857 | 0.893 | 0.965 |
| SSE-tree | topic | 0.838 | 0.844 | 0.887 | 0.969 |
| SSE (yes/no levels) | domain | 0.905 | 0.828 | 0.840 | 0.884 |
| SSE (yes/no levels) | field | 0.774 | 0.922 | 0.935 | 0.969 |
| SSE (yes/no levels) | subfield | 0.753 | 0.895 | 0.947 | 0.982 |
| SSE (yes/no levels) | topic | 0.668 | 0.847 | 0.919 | 0.990 |
| B3 separate (graded+contrastive) | domain | 0.914 | 0.827 | 0.838 | 0.882 |
| B3 separate (graded+contrastive) | field | 0.826 | 0.916 | 0.932 | 0.967 |
| B3 separate (graded+contrastive) | subfield | 0.797 | 0.891 | 0.943 | 0.983 |
| B3 separate (graded+contrastive) | topic | 0.732 | 0.852 | 0.915 | 0.989 |
| B4 CSN (graded+contrastive) | domain | 0.913 | 0.822 | 0.832 | 0.888 |
| B4 CSN (graded+contrastive) | field | 0.838 | 0.911 | 0.926 | 0.968 |
| B4 CSN (graded+contrastive) | subfield | 0.798 | 0.892 | 0.942 | 0.983 |
| B4 CSN (graded+contrastive) | topic | 0.734 | 0.855 | 0.919 | 0.989 |
| B1 labels | all levels | 0.768 | 0.834 | 0.889 | 0.949 |
| B6 plain encoder | full | 0.627 | 0.784 | 0.866 | 0.971 |

### E3 — general search preserved

| method | overlap@10_with_encoder | topic_mAP_encoder | topic_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.807 | 0.237 | 0.253 |
| SSE-tree | 0.869 | 0.237 | 0.237 |
| SSE (yes/no levels) | 0.701 | 0.237 | 0.263 |
| SSE-MRL (topic everywhere) | 0.765 | 0.237 | 0.257 |
