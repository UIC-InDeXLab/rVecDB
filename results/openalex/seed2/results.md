# OpenAlex results (seed 2)

### E2 — topic prefix length vs level (mAP)

**seen_test**

|                                                   |     8 |    16 |    32 |    64 |   128 |
|:--------------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                         | 0.544 | 0.525 | 0.515 | 0.506 | 0.502 |
| ('Encoder-PCA', 'field')                          | 0.218 | 0.237 | 0.244 | 0.242 | 0.239 |
| ('Encoder-PCA', 'subfield')                       | 0.122 | 0.158 | 0.187 | 0.197 | 0.2   |
| ('SSE (yes/no levels)', 'domain')                 | 0.698 | 0.75  | 0.632 | 0.596 | 0.565 |
| ('SSE (yes/no levels)', 'field')                  | 0.136 | 0.155 | 0.367 | 0.441 | 0.375 |
| ('SSE (yes/no levels)', 'subfield')               | 0.048 | 0.058 | 0.155 | 0.193 | 0.307 |
| ('SSE-MRL (finest level everywhere)', 'domain')   | 0.492 | 0.564 | 0.556 | 0.563 | 0.562 |
| ('SSE-MRL (finest level everywhere)', 'field')    | 0.24  | 0.349 | 0.355 | 0.366 | 0.366 |
| ('SSE-MRL (finest level everywhere)', 'subfield') | 0.157 | 0.255 | 0.277 | 0.305 | 0.307 |
| ('SSE-tree', 'domain')                            | 0.657 | 0.751 | 0.739 | 0.717 | 0.69  |
| ('SSE-tree', 'field')                             | 0.149 | 0.182 | 0.234 | 0.301 | 0.289 |
| ('SSE-tree', 'subfield')                          | 0.067 | 0.093 | 0.137 | 0.19  | 0.203 |
| ('SSE-treeSC', 'domain')                          | 0.63  | 0.754 | 0.706 | 0.648 | 0.604 |
| ('SSE-treeSC', 'field')                           | 0.128 | 0.161 | 0.329 | 0.43  | 0.372 |
| ('SSE-treeSC', 'subfield')                        | 0.049 | 0.069 | 0.158 | 0.209 | 0.305 |

**unseen**

|                                                   |     8 |    16 |    32 |    64 |   128 |
|:--------------------------------------------------|------:|------:|------:|------:|------:|
| ('Encoder-PCA', 'domain')                         | 0.542 | 0.532 | 0.525 | 0.519 | 0.516 |
| ('Encoder-PCA', 'field')                          | 0.289 | 0.33  | 0.348 | 0.356 | 0.355 |
| ('Encoder-PCA', 'subfield')                       | 0.227 | 0.3   | 0.343 | 0.368 | 0.379 |
| ('SSE (yes/no levels)', 'domain')                 | 0.706 | 0.75  | 0.648 | 0.599 | 0.58  |
| ('SSE (yes/no levels)', 'field')                  | 0.169 | 0.191 | 0.393 | 0.459 | 0.445 |
| ('SSE (yes/no levels)', 'subfield')               | 0.085 | 0.104 | 0.254 | 0.304 | 0.391 |
| ('SSE-MRL (finest level everywhere)', 'domain')   | 0.514 | 0.578 | 0.576 | 0.577 | 0.577 |
| ('SSE-MRL (finest level everywhere)', 'field')    | 0.299 | 0.42  | 0.428 | 0.438 | 0.439 |
| ('SSE-MRL (finest level everywhere)', 'subfield') | 0.226 | 0.337 | 0.364 | 0.388 | 0.391 |
| ('SSE-tree', 'domain')                            | 0.681 | 0.765 | 0.756 | 0.735 | 0.712 |
| ('SSE-tree', 'field')                             | 0.197 | 0.242 | 0.309 | 0.389 | 0.386 |
| ('SSE-tree', 'subfield')                          | 0.128 | 0.179 | 0.247 | 0.327 | 0.356 |
| ('SSE-treeSC', 'domain')                          | 0.654 | 0.758 | 0.716 | 0.656 | 0.622 |
| ('SSE-treeSC', 'field')                           | 0.157 | 0.208 | 0.374 | 0.462 | 0.449 |
| ('SSE-treeSC', 'subfield')                        | 0.084 | 0.13  | 0.265 | 0.332 | 0.401 |

### E2b — does each level's view keep its own and coarser levels? (pair AUC)

| method | view | same-domain AUC | same-field AUC | same-subfield AUC |
|---|---|---|---|---|
| SSE-treeSC | domain | 0.912 | 0.828 | 0.838 |
| SSE-treeSC | field | 0.834 | 0.913 | 0.930 |
| SSE-treeSC | subfield | 0.796 | 0.894 | 0.944 |
| SSE-tree | domain | 0.909 | 0.826 | 0.840 |
| SSE-tree | field | 0.889 | 0.860 | 0.885 |
| SSE-tree | subfield | 0.871 | 0.856 | 0.890 |
| SSE (yes/no levels) | domain | 0.906 | 0.832 | 0.843 |
| SSE (yes/no levels) | field | 0.769 | 0.923 | 0.935 |
| SSE (yes/no levels) | subfield | 0.742 | 0.896 | 0.947 |
| B3 separate (graded+contrastive) | domain | 0.912 | 0.824 | 0.834 |
| B3 separate (graded+contrastive) | field | 0.837 | 0.913 | 0.929 |
| B3 separate (graded+contrastive) | subfield | 0.784 | 0.891 | 0.945 |
| B4 CSN (graded+contrastive) | domain | 0.913 | 0.821 | 0.832 |
| B4 CSN (graded+contrastive) | field | 0.840 | 0.912 | 0.927 |
| B4 CSN (graded+contrastive) | subfield | 0.798 | 0.893 | 0.943 |
| B1 labels | all levels | 0.799 | 0.844 | 0.896 |
| B6 plain encoder | full | 0.627 | 0.784 | 0.866 |

### E2s (coarse levels)

| split | level | method | P@10 | tree_credit@10 |
|---|---|---|---|---|
| seen_test | domain | SSE-treeSC | 0.809 | 0.809 |
| seen_test | domain | SSE-tree | 0.824 | 0.824 |
| seen_test | domain | SSE (yes/no levels) | 0.801 | 0.801 |
| seen_test | domain | SSE-MRL (finest level everywhere) | 0.833 | 0.833 |
| seen_test | domain | B3 separate (graded+contrastive) | 0.817 | 0.817 |
| seen_test | domain | B4 CSN (graded+contrastive) | 0.846 | 0.846 |
| seen_test | domain | Encoder-PCA | 0.794 | 0.794 |
| seen_test | domain | B6 plain encoder | 0.815 | 0.815 |
| seen_test | domain | B1 labels | 0.820 | 0.820 |
| seen_test | domain | Random | 0.274 | 0.274 |
| seen_test | field | SSE-treeSC | 0.641 | 0.749 |
| seen_test | field | SSE-tree | 0.602 | 0.732 |
| seen_test | field | SSE (yes/no levels) | 0.623 | 0.736 |
| seen_test | field | SSE-MRL (finest level everywhere) | 0.659 | 0.760 |
| seen_test | field | B3 separate (graded+contrastive) | 0.636 | 0.748 |
| seen_test | field | B4 CSN (graded+contrastive) | 0.652 | 0.757 |
| seen_test | field | Encoder-PCA | 0.600 | 0.717 |
| seen_test | field | B6 plain encoder | 0.582 | 0.698 |
| seen_test | field | B1 labels | 0.583 | 0.705 |
| seen_test | field | Random | 0.039 | 0.156 |
| unseen | domain | SSE-treeSC | 0.812 | 0.812 |
| unseen | domain | SSE-tree | 0.845 | 0.845 |
| unseen | domain | SSE (yes/no levels) | 0.799 | 0.799 |
| unseen | domain | SSE-MRL (finest level everywhere) | 0.873 | 0.873 |
| unseen | domain | B3 separate (graded+contrastive) | 0.825 | 0.825 |
| unseen | domain | B4 CSN (graded+contrastive) | 0.896 | 0.896 |
| unseen | domain | Encoder-PCA | 0.854 | 0.854 |
| unseen | domain | B6 plain encoder | 0.909 | 0.909 |
| unseen | domain | B1 labels | 0.899 | 0.899 |
| unseen | domain | Random | 0.263 | 0.263 |
| unseen | field | SSE-treeSC | 0.758 | 0.825 |
| unseen | field | SSE-tree | 0.774 | 0.842 |
| unseen | field | SSE (yes/no levels) | 0.709 | 0.789 |
| unseen | field | SSE-MRL (finest level everywhere) | 0.778 | 0.841 |
| unseen | field | B3 separate (graded+contrastive) | 0.772 | 0.839 |
| unseen | field | B4 CSN (graded+contrastive) | 0.780 | 0.844 |
| unseen | field | Encoder-PCA | 0.807 | 0.863 |
| unseen | field | B6 plain encoder | 0.803 | 0.856 |
| unseen | field | B1 labels | 0.752 | 0.817 |
| unseen | field | Random | 0.043 | 0.153 |

### E2s — paper -> 10 nearest papers at the level's own view: exact label (P@10) and tree credit (1 same label, partial credit for sharing a coarser level)

| split | level | method | P@10 | tree_credit@10 | credit_text@10 | credit_coact@10 |
|---|---|---|---|---|---|---|
| seen_test | subfield | SSE-treeSC | 0.512 | 0.682 | 0.623 | 0.548 |
| seen_test | subfield | SSE-tree | 0.450 | 0.642 | 0.570 | 0.489 |
| seen_test | subfield | SSE (yes/no levels) | 0.502 | 0.676 | 0.617 | 0.541 |
| seen_test | subfield | SSE-MRL (finest level everywhere) | 0.501 | 0.675 | 0.617 | 0.540 |
| seen_test | subfield | B3 separate (graded+contrastive) | 0.512 | 0.682 | 0.624 | 0.548 |
| seen_test | subfield | B4 CSN (graded+contrastive) | 0.501 | 0.672 | 0.616 | 0.539 |
| seen_test | subfield | Encoder-PCA | 0.463 | 0.635 | 0.576 | 0.500 |
| seen_test | subfield | B6 plain encoder | 0.451 | 0.616 | 0.563 | 0.486 |
| seen_test | subfield | B1 labels | 0.396 | 0.589 | 0.521 | 0.436 |
| seen_test | subfield | Random | 0.010 | 0.108 | 0.072 | 0.022 |
| unseen | subfield | SSE-treeSC | 0.711 | 0.808 | 0.776 | 0.735 |
| unseen | subfield | SSE-tree | 0.722 | 0.819 | 0.781 | 0.744 |
| unseen | subfield | SSE (yes/no levels) | 0.686 | 0.792 | 0.756 | 0.711 |
| unseen | subfield | SSE-MRL (finest level everywhere) | 0.688 | 0.793 | 0.759 | 0.714 |
| unseen | subfield | B3 separate (graded+contrastive) | 0.698 | 0.798 | 0.766 | 0.723 |
| unseen | subfield | B4 CSN (graded+contrastive) | 0.711 | 0.810 | 0.777 | 0.735 |
| unseen | subfield | Encoder-PCA | 0.745 | 0.831 | 0.801 | 0.765 |
| unseen | subfield | B6 plain encoder | 0.730 | 0.814 | 0.786 | 0.750 |
| unseen | subfield | B1 labels | 0.624 | 0.737 | 0.700 | 0.650 |
| unseen | subfield | Random | 0.018 | 0.108 | 0.078 | 0.029 |

### E3 — general search preserved

| method | overlap@10_with_encoder | topic_mAP_encoder | topic_mAP_SSE |
|---|---|---|---|
| SSE-treeSC | 0.841 | 0.413 | 0.427 |
| SSE-tree | 0.877 | 0.413 | 0.419 |
| SSE (yes/no levels) | 0.770 | 0.413 | 0.430 |
| SSE-MRL (finest level everywhere) | 0.808 | 0.413 | 0.427 |
