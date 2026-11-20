# OpenAlex results (seed 1)

### E2 — topic prefix length vs level (mAP)

**seen_test**

|                                            |     8 |    16 |    32 |    64 |   128 |
|:-------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                  | 0.544 | 0.525 | 0.515 | 0.506 | 0.502 |
| ('Encoder-PCA', 'field')                   | 0.218 | 0.237 | 0.244 | 0.242 | 0.239 |
| ('Encoder-PCA', 'subfield')                | 0.122 | 0.158 | 0.187 | 0.197 | 0.2   |
| ('Encoder-PCA', 'topic')                   | 0.083 | 0.142 | 0.203 | 0.234 | 0.251 |
| ('SSE (yes/no levels)', 'domain')          | 0.747 | 0.635 | 0.604 | 0.57  | 0.485 |
| ('SSE (yes/no levels)', 'field')           | 0.14  | 0.317 | 0.44  | 0.368 | 0.298 |
| ('SSE (yes/no levels)', 'subfield')        | 0.048 | 0.125 | 0.192 | 0.306 | 0.266 |
| ('SSE (yes/no levels)', 'topic')           | 0.019 | 0.073 | 0.128 | 0.233 | 0.308 |
| ('SSE-MRL (topic everywhere)', 'domain')   | 0.52  | 0.508 | 0.487 | 0.483 | 0.483 |
| ('SSE-MRL (topic everywhere)', 'field')    | 0.265 | 0.265 | 0.282 | 0.289 | 0.289 |
| ('SSE-MRL (topic everywhere)', 'subfield') | 0.18  | 0.209 | 0.248 | 0.259 | 0.26  |
| ('SSE-MRL (topic everywhere)', 'topic')    | 0.147 | 0.214 | 0.282 | 0.304 | 0.31  |
| ('SSE-tree', 'domain')                     | 0.749 | 0.731 | 0.7   | 0.673 | 0.648 |
| ('SSE-tree', 'field')                      | 0.161 | 0.232 | 0.308 | 0.294 | 0.274 |
| ('SSE-tree', 'subfield')                   | 0.07  | 0.121 | 0.182 | 0.201 | 0.203 |
| ('SSE-tree', 'topic')                      | 0.038 | 0.091 | 0.166 | 0.212 | 0.243 |
| ('SSE-treeSC', 'domain')                   | 0.758 | 0.711 | 0.654 | 0.607 | 0.538 |
| ('SSE-treeSC', 'field')                    | 0.149 | 0.301 | 0.43  | 0.37  | 0.307 |
| ('SSE-treeSC', 'subfield')                 | 0.056 | 0.13  | 0.202 | 0.304 | 0.27  |
| ('SSE-treeSC', 'topic')                    | 0.028 | 0.082 | 0.148 | 0.246 | 0.313 |

**unseen**

|                                            |     8 |    16 |    32 |    64 |   128 |
|:-------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                  | 0.542 | 0.532 | 0.525 | 0.519 | 0.516 |
| ('Encoder-PCA', 'field')                   | 0.289 | 0.33  | 0.348 | 0.356 | 0.355 |
| ('Encoder-PCA', 'subfield')                | 0.227 | 0.3   | 0.343 | 0.368 | 0.379 |
| ('Encoder-PCA', 'topic')                   | 0.198 | 0.3   | 0.38  | 0.431 | 0.455 |
| ('SSE (yes/no levels)', 'domain')          | 0.738 | 0.627 | 0.598 | 0.581 | 0.51  |
| ('SSE (yes/no levels)', 'field')           | 0.17  | 0.35  | 0.446 | 0.438 | 0.412 |
| ('SSE (yes/no levels)', 'subfield')        | 0.084 | 0.208 | 0.296 | 0.382 | 0.411 |
| ('SSE (yes/no levels)', 'topic')           | 0.055 | 0.163 | 0.255 | 0.375 | 0.457 |
| ('SSE-MRL (topic everywhere)', 'domain')   | 0.538 | 0.529 | 0.514 | 0.509 | 0.508 |
| ('SSE-MRL (topic everywhere)', 'field')    | 0.365 | 0.38  | 0.398 | 0.406 | 0.407 |
| ('SSE-MRL (topic everywhere)', 'subfield') | 0.298 | 0.343 | 0.389 | 0.406 | 0.408 |
| ('SSE-MRL (topic everywhere)', 'topic')    | 0.261 | 0.332 | 0.418 | 0.452 | 0.456 |
| ('SSE-tree', 'domain')                     | 0.753 | 0.737 | 0.715 | 0.69  | 0.667 |
| ('SSE-tree', 'field')                      | 0.216 | 0.299 | 0.396 | 0.387 | 0.374 |
| ('SSE-tree', 'subfield')                   | 0.134 | 0.213 | 0.31  | 0.345 | 0.36  |
| ('SSE-tree', 'topic')                      | 0.104 | 0.192 | 0.302 | 0.373 | 0.415 |
| ('SSE-treeSC', 'domain')                   | 0.747 | 0.705 | 0.653 | 0.621 | 0.565 |
| ('SSE-treeSC', 'field')                    | 0.194 | 0.345 | 0.448 | 0.441 | 0.42  |
| ('SSE-treeSC', 'subfield')                 | 0.106 | 0.221 | 0.314 | 0.393 | 0.417 |
| ('SSE-treeSC', 'topic')                    | 0.075 | 0.187 | 0.281 | 0.399 | 0.468 |

### E2b — does each level's view keep its own and coarser levels? (pair AUC)

| method | view | same-domain AUC | same-field AUC | same-subfield AUC | same-topic AUC |
|---|---|---|---|---|---|
| SSE-treeSC | domain | 0.911 | 0.827 | 0.835 | 0.872 |
| SSE-treeSC | field | 0.835 | 0.911 | 0.926 | 0.964 |
| SSE-treeSC | subfield | 0.799 | 0.888 | 0.938 | 0.980 |
| SSE-treeSC | topic | 0.739 | 0.853 | 0.917 | 0.988 |
| SSE-tree | domain | 0.904 | 0.825 | 0.838 | 0.882 |
| SSE-tree | field | 0.873 | 0.868 | 0.893 | 0.953 |
| SSE-tree | subfield | 0.852 | 0.856 | 0.893 | 0.963 |
| SSE-tree | topic | 0.835 | 0.843 | 0.887 | 0.969 |
| SSE (yes/no levels) | domain | 0.903 | 0.826 | 0.836 | 0.876 |
| SSE (yes/no levels) | field | 0.777 | 0.919 | 0.933 | 0.966 |
| SSE (yes/no levels) | subfield | 0.753 | 0.891 | 0.943 | 0.981 |
| SSE (yes/no levels) | topic | 0.673 | 0.843 | 0.915 | 0.989 |
| B3 separate (graded+contrastive) | domain | 0.912 | 0.827 | 0.837 | 0.880 |
| B3 separate (graded+contrastive) | field | 0.836 | 0.916 | 0.930 | 0.968 |
| B3 separate (graded+contrastive) | subfield | 0.798 | 0.891 | 0.942 | 0.982 |
| B3 separate (graded+contrastive) | topic | 0.730 | 0.849 | 0.917 | 0.989 |
| B4 CSN (graded+contrastive) | domain | 0.912 | 0.825 | 0.836 | 0.893 |
| B4 CSN (graded+contrastive) | field | 0.845 | 0.911 | 0.927 | 0.969 |
| B4 CSN (graded+contrastive) | subfield | 0.805 | 0.891 | 0.941 | 0.982 |
| B4 CSN (graded+contrastive) | topic | 0.737 | 0.855 | 0.919 | 0.989 |
| B1 labels | all levels | 0.768 | 0.835 | 0.890 | 0.950 |
| B6 plain encoder | full | 0.627 | 0.784 | 0.866 | 0.971 |

### E3 — general search preserved

| method | overlap@10_with_encoder | topic_mAP_encoder | topic_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.802 | 0.237 | 0.252 |
| SSE-tree | 0.864 | 0.237 | 0.238 |
| SSE (yes/no levels) | 0.701 | 0.237 | 0.262 |
| SSE-MRL (topic everywhere) | 0.756 | 0.237 | 0.256 |
