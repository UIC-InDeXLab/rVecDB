# OpenAlex results (seed 0)

### E2 — topic prefix length vs level (mAP)

**seen_test**

|                                                   |     8 |    16 |    32 |    64 |   128 |
|:--------------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                         | 0.544 | 0.525 | 0.515 | 0.506 | 0.502 |
| ('Encoder-PCA', 'field')                          | 0.218 | 0.237 | 0.244 | 0.242 | 0.239 |
| ('Encoder-PCA', 'subfield')                       | 0.122 | 0.158 | 0.187 | 0.197 | 0.2   |
| ('SSE (yes/no levels)', 'domain')                 | 0.677 | 0.752 | 0.633 | 0.59  | 0.561 |
| ('SSE (yes/no levels)', 'field')                  | 0.138 | 0.155 | 0.368 | 0.442 | 0.376 |
| ('SSE (yes/no levels)', 'subfield')               | 0.049 | 0.059 | 0.157 | 0.194 | 0.308 |
| ('SSE-MRL (finest level everywhere)', 'domain')   | 0.453 | 0.565 | 0.56  | 0.558 | 0.557 |
| ('SSE-MRL (finest level everywhere)', 'field')    | 0.217 | 0.351 | 0.356 | 0.366 | 0.366 |
| ('SSE-MRL (finest level everywhere)', 'subfield') | 0.135 | 0.256 | 0.283 | 0.306 | 0.308 |
| ('SSE-tree', 'domain')                            | 0.656 | 0.751 | 0.739 | 0.718 | 0.69  |
| ('SSE-tree', 'field')                             | 0.136 | 0.183 | 0.245 | 0.297 | 0.289 |
| ('SSE-tree', 'subfield')                          | 0.064 | 0.096 | 0.141 | 0.191 | 0.204 |
| ('SSE-treeSC', 'domain')                          | 0.626 | 0.754 | 0.703 | 0.647 | 0.599 |
| ('SSE-treeSC', 'field')                           | 0.121 | 0.16  | 0.348 | 0.43  | 0.373 |
| ('SSE-treeSC', 'subfield')                        | 0.047 | 0.07  | 0.167 | 0.21  | 0.305 |

**unseen**

|                                                   |     8 |    16 |    32 |    64 |   128 |
|:--------------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                         | 0.542 | 0.532 | 0.525 | 0.519 | 0.516 |
| ('Encoder-PCA', 'field')                          | 0.289 | 0.33  | 0.348 | 0.356 | 0.355 |
| ('Encoder-PCA', 'subfield')                       | 0.227 | 0.3   | 0.343 | 0.368 | 0.379 |
| ('SSE (yes/no levels)', 'domain')                 | 0.693 | 0.743 | 0.633 | 0.586 | 0.571 |
| ('SSE (yes/no levels)', 'field')                  | 0.172 | 0.192 | 0.393 | 0.453 | 0.444 |
| ('SSE (yes/no levels)', 'subfield')               | 0.089 | 0.107 | 0.249 | 0.301 | 0.391 |
| ('SSE-MRL (finest level everywhere)', 'domain')   | 0.478 | 0.575 | 0.57  | 0.569 | 0.568 |
| ('SSE-MRL (finest level everywhere)', 'field')    | 0.264 | 0.418 | 0.424 | 0.437 | 0.438 |
| ('SSE-MRL (finest level everywhere)', 'subfield') | 0.192 | 0.334 | 0.357 | 0.387 | 0.391 |
| ('SSE-tree', 'domain')                            | 0.689 | 0.763 | 0.754 | 0.733 | 0.707 |
| ('SSE-tree', 'field')                             | 0.188 | 0.242 | 0.313 | 0.383 | 0.386 |
| ('SSE-tree', 'subfield')                          | 0.119 | 0.174 | 0.247 | 0.326 | 0.356 |
| ('SSE-treeSC', 'domain')                          | 0.65  | 0.75  | 0.705 | 0.651 | 0.615 |
| ('SSE-treeSC', 'field')                           | 0.16  | 0.209 | 0.385 | 0.454 | 0.445 |
| ('SSE-treeSC', 'subfield')                        | 0.083 | 0.128 | 0.262 | 0.328 | 0.401 |

### E2b — does each level's view keep its own and coarser levels? (pair AUC)

| method | view | same-domain AUC | same-field AUC | same-subfield AUC |
|---|---|---|---|---|
| SSE-treeSC | domain | 0.911 | 0.827 | 0.837 |
| SSE-treeSC | field | 0.833 | 0.912 | 0.926 |
| SSE-treeSC | subfield | 0.793 | 0.894 | 0.942 |
| SSE-tree | domain | 0.907 | 0.826 | 0.839 |
| SSE-tree | field | 0.887 | 0.859 | 0.883 |
| SSE-tree | subfield | 0.868 | 0.855 | 0.889 |
| SSE (yes/no levels) | domain | 0.904 | 0.833 | 0.845 |
| SSE (yes/no levels) | field | 0.752 | 0.923 | 0.935 |
| SSE (yes/no levels) | subfield | 0.733 | 0.898 | 0.947 |
| B3 separate (graded+contrastive) | domain | 0.911 | 0.822 | 0.833 |
| B3 separate (graded+contrastive) | field | 0.835 | 0.914 | 0.929 |
| B3 separate (graded+contrastive) | subfield | 0.789 | 0.891 | 0.944 |
| B4 CSN (graded+contrastive) | domain | 0.915 | 0.825 | 0.835 |
| B4 CSN (graded+contrastive) | field | 0.842 | 0.914 | 0.929 |
| B4 CSN (graded+contrastive) | subfield | 0.800 | 0.895 | 0.942 |
| B1 labels | all levels | 0.798 | 0.844 | 0.896 |
| B6 plain encoder | full | 0.627 | 0.784 | 0.866 |

### E2s (coarse levels)

| split | level | method | P@10 | tree_credit@10 |
|---|---|---|---|---|
| seen_test | domain | SSE-treeSC | 0.820 | 0.820 |
| seen_test | domain | SSE-tree | 0.842 | 0.842 |
| seen_test | domain | SSE (yes/no levels) | 0.804 | 0.804 |
| seen_test | domain | SSE-MRL (finest level everywhere) | 0.836 | 0.836 |
| seen_test | domain | B3 separate (graded+contrastive) | 0.825 | 0.825 |
| seen_test | domain | B4 CSN (graded+contrastive) | 0.846 | 0.846 |
| seen_test | domain | Encoder-PCA | 0.794 | 0.794 |
| seen_test | domain | B6 plain encoder | 0.815 | 0.815 |
| seen_test | domain | B1 labels | 0.821 | 0.821 |
| seen_test | domain | Random | 0.274 | 0.274 |
| seen_test | field | SSE-treeSC | 0.637 | 0.748 |
| seen_test | field | SSE-tree | 0.600 | 0.731 |
| seen_test | field | SSE (yes/no levels) | 0.627 | 0.740 |
| seen_test | field | SSE-MRL (finest level everywhere) | 0.656 | 0.756 |
| seen_test | field | B3 separate (graded+contrastive) | 0.632 | 0.745 |
| seen_test | field | B4 CSN (graded+contrastive) | 0.649 | 0.756 |
| seen_test | field | Encoder-PCA | 0.600 | 0.717 |
| seen_test | field | B6 plain encoder | 0.582 | 0.698 |
| seen_test | field | B1 labels | 0.584 | 0.705 |
| seen_test | field | Random | 0.039 | 0.156 |
| unseen | domain | SSE-treeSC | 0.819 | 0.819 |
| unseen | domain | SSE-tree | 0.850 | 0.850 |
| unseen | domain | SSE (yes/no levels) | 0.804 | 0.804 |
| unseen | domain | SSE-MRL (finest level everywhere) | 0.860 | 0.860 |
| unseen | domain | B3 separate (graded+contrastive) | 0.823 | 0.823 |
| unseen | domain | B4 CSN (graded+contrastive) | 0.897 | 0.897 |
| unseen | domain | Encoder-PCA | 0.854 | 0.854 |
| unseen | domain | B6 plain encoder | 0.909 | 0.909 |
| unseen | domain | B1 labels | 0.899 | 0.899 |
| unseen | domain | Random | 0.263 | 0.263 |
| unseen | field | SSE-treeSC | 0.763 | 0.830 |
| unseen | field | SSE-tree | 0.777 | 0.843 |
| unseen | field | SSE (yes/no levels) | 0.711 | 0.792 |
| unseen | field | SSE-MRL (finest level everywhere) | 0.775 | 0.836 |
| unseen | field | B3 separate (graded+contrastive) | 0.768 | 0.835 |
| unseen | field | B4 CSN (graded+contrastive) | 0.777 | 0.843 |
| unseen | field | Encoder-PCA | 0.807 | 0.863 |
| unseen | field | B6 plain encoder | 0.803 | 0.856 |
| unseen | field | B1 labels | 0.754 | 0.820 |
| unseen | field | Random | 0.043 | 0.153 |

### E2s — paper -> 10 nearest papers at the level's own view: exact label (P@10) and tree credit (1 same label, partial credit for sharing a coarser level)

| split | level | method | P@10 | tree_credit@10 | credit_text@10 | credit_coact@10 |
|---|---|---|---|---|---|---|
| seen_test | subfield | SSE-treeSC | 0.506 | 0.681 | 0.621 | 0.544 |
| seen_test | subfield | SSE-tree | 0.454 | 0.642 | 0.572 | 0.492 |
| seen_test | subfield | SSE (yes/no levels) | 0.498 | 0.675 | 0.616 | 0.537 |
| seen_test | subfield | SSE-MRL (finest level everywhere) | 0.496 | 0.672 | 0.614 | 0.535 |
| seen_test | subfield | B3 separate (graded+contrastive) | 0.506 | 0.676 | 0.620 | 0.543 |
| seen_test | subfield | B4 CSN (graded+contrastive) | 0.501 | 0.675 | 0.615 | 0.539 |
| seen_test | subfield | Encoder-PCA | 0.463 | 0.635 | 0.576 | 0.500 |
| seen_test | subfield | B6 plain encoder | 0.451 | 0.616 | 0.563 | 0.486 |
| seen_test | subfield | B1 labels | 0.390 | 0.589 | 0.517 | 0.431 |
| seen_test | subfield | Random | 0.010 | 0.108 | 0.072 | 0.022 |
| unseen | subfield | SSE-treeSC | 0.716 | 0.813 | 0.781 | 0.740 |
| unseen | subfield | SSE-tree | 0.721 | 0.818 | 0.782 | 0.743 |
| unseen | subfield | SSE (yes/no levels) | 0.692 | 0.792 | 0.761 | 0.717 |
| unseen | subfield | SSE-MRL (finest level everywhere) | 0.689 | 0.791 | 0.760 | 0.715 |
| unseen | subfield | B3 separate (graded+contrastive) | 0.716 | 0.813 | 0.781 | 0.740 |
| unseen | subfield | B4 CSN (graded+contrastive) | 0.716 | 0.810 | 0.780 | 0.739 |
| unseen | subfield | Encoder-PCA | 0.745 | 0.831 | 0.801 | 0.765 |
| unseen | subfield | B6 plain encoder | 0.730 | 0.814 | 0.786 | 0.750 |
| unseen | subfield | B1 labels | 0.627 | 0.740 | 0.703 | 0.654 |
| unseen | subfield | Random | 0.018 | 0.108 | 0.078 | 0.029 |

### E3 — general search preserved

| method | overlap@10_with_encoder | topic_mAP_encoder | topic_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.852 | 0.413 | 0.426 |
| SSE-tree | 0.865 | 0.413 | 0.419 |
| SSE (yes/no levels) | 0.777 | 0.413 | 0.431 |
| SSE-MRL (finest level everywhere) | 0.811 | 0.413 | 0.428 |
