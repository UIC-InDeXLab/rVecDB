# OpenAlex — summary over 3 seeds

### E2 — mAP of each level at its OWN prefix (domain@8, field@32, subfield@64, topic@128)

| split     | method                     | domain       | field        | subfield     | topic        |
|:----------|:---------------------------|:-------------|:-------------|:-------------|:-------------|
| seen_test | SSE-treeSC                 | 0.757 ±0.001 | 0.43 ±0.001  | 0.302 ±0.001 | 0.312 ±0.001 |
| seen_test | SSE-tree                   | 0.748 ±0.001 | 0.31 ±0.002  | 0.201 ±0.0   | 0.241 ±0.002 |
| seen_test | SSE (yes/no levels)        | 0.748 ±0.001 | 0.44 ±0.0    | 0.305 ±0.001 | 0.307 ±0.002 |
| seen_test | SSE-MRL (topic everywhere) | 0.521 ±0.001 | 0.285 ±0.003 | 0.258 ±0.001 | 0.307 ±0.003 |
| seen_test | Encoder-PCA                | 0.544 ±0.0   | 0.244 ±0.0   | 0.197 ±0.0   | 0.251 ±0.0   |
| unseen    | SSE-treeSC                 | 0.75 ±0.005  | 0.451 ±0.003 | 0.395 ±0.002 | 0.47 ±0.001  |
| unseen    | SSE-tree                   | 0.755 ±0.002 | 0.398 ±0.001 | 0.344 ±0.001 | 0.415 ±0.002 |
| unseen    | SSE (yes/no levels)        | 0.742 ±0.004 | 0.45 ±0.004  | 0.382 ±0.001 | 0.459 ±0.002 |
| unseen    | SSE-MRL (topic everywhere) | 0.535 ±0.004 | 0.4 ±0.002   | 0.408 ±0.001 | 0.459 ±0.003 |
| unseen    | Encoder-PCA                | 0.542 ±0.0   | 0.348 ±0.0   | 0.368 ±0.0   | 0.455 ±0.0   |

### E2 — prefix length where each level peaks (should be 8 / 32 / 64 / 128)

| split     | method                     |   domain |   field |   subfield |   topic |
|:----------|:---------------------------|---------:|--------:|-----------:|--------:|
| seen_test | Encoder-PCA                |        8 |      32 |        128 |     128 |
| seen_test | SSE (yes/no levels)        |        8 |      32 |         64 |     128 |
| seen_test | SSE-MRL (topic everywhere) |        8 |     128 |        128 |     128 |
| seen_test | SSE-tree                   |        8 |      32 |        128 |     128 |
| seen_test | SSE-treeSC                 |        8 |      32 |         64 |     128 |
| unseen    | Encoder-PCA                |        8 |      64 |        128 |     128 |
| unseen    | SSE (yes/no levels)        |        8 |      32 |        128 |     128 |
| unseen    | SSE-MRL (topic everywhere) |        8 |     128 |        128 |     128 |
| unseen    | SSE-tree                   |        8 |      32 |        128 |     128 |
| unseen    | SSE-treeSC                 |        8 |      32 |        128 |     128 |

### E2b — pair AUC per view (does a finer view keep coarser levels?)

| method                           | view       | same-domain AUC   | same-field AUC   | same-subfield AUC   | same-topic AUC   |
|:---------------------------------|:-----------|:------------------|:-----------------|:--------------------|:-----------------|
| SSE-treeSC                       | domain     | 0.911 ±0.001      | 0.827 ±0.001     | 0.837 ±0.002        | 0.878 ±0.005     |
| SSE-treeSC                       | field      | 0.832 ±0.003      | 0.912 ±0.001     | 0.927 ±0.002        | 0.965 ±0.002     |
| SSE-treeSC                       | subfield   | 0.794 ±0.004      | 0.891 ±0.002     | 0.94 ±0.002         | 0.982 ±0.001     |
| SSE-treeSC                       | topic      | 0.733 ±0.006      | 0.856 ±0.002     | 0.919 ±0.002        | 0.989 ±0.001     |
| SSE-tree                         | domain     | 0.905 ±0.001      | 0.826 ±0.001     | 0.838 ±0.0          | 0.885 ±0.002     |
| SSE-tree                         | field      | 0.874 ±0.001      | 0.868 ±0.0       | 0.895 ±0.001        | 0.955 ±0.003     |
| SSE-tree                         | subfield   | 0.853 ±0.002      | 0.856 ±0.0       | 0.893 ±0.0          | 0.965 ±0.002     |
| SSE-tree                         | topic      | 0.835 ±0.003      | 0.844 ±0.0       | 0.887 ±0.0          | 0.97 ±0.001      |
| SSE (yes/no levels)              | domain     | 0.904 ±0.001      | 0.828 ±0.001     | 0.838 ±0.002        | 0.88 ±0.004      |
| SSE (yes/no levels)              | field      | 0.769 ±0.01       | 0.92 ±0.001      | 0.933 ±0.001        | 0.967 ±0.001     |
| SSE (yes/no levels)              | subfield   | 0.745 ±0.012      | 0.893 ±0.002     | 0.945 ±0.002        | 0.982 ±0.001     |
| SSE (yes/no levels)              | topic      | 0.663 ±0.012      | 0.845 ±0.002     | 0.916 ±0.002        | 0.989 ±0.0       |
| B3 separate (graded+contrastive) | domain     | 0.913 ±0.001      | 0.827 ±0.001     | 0.837 ±0.001        | 0.881 ±0.001     |
| B3 separate (graded+contrastive) | field      | 0.828 ±0.007      | 0.916 ±0.001     | 0.93 ±0.001         | 0.968 ±0.001     |
| B3 separate (graded+contrastive) | subfield   | 0.795 ±0.004      | 0.891 ±0.0       | 0.943 ±0.001        | 0.982 ±0.001     |
| B3 separate (graded+contrastive) | topic      | 0.731 ±0.001      | 0.851 ±0.002     | 0.916 ±0.001        | 0.989 ±0.0       |
| B4 CSN (graded+contrastive)      | domain     | 0.913 ±0.0        | 0.822 ±0.002     | 0.832 ±0.003        | 0.888 ±0.005     |
| B4 CSN (graded+contrastive)      | field      | 0.838 ±0.007      | 0.912 ±0.001     | 0.927 ±0.001        | 0.968 ±0.001     |
| B4 CSN (graded+contrastive)      | subfield   | 0.797 ±0.009      | 0.892 ±0.001     | 0.941 ±0.001        | 0.982 ±0.0       |
| B4 CSN (graded+contrastive)      | topic      | 0.731 ±0.007      | 0.854 ±0.001     | 0.918 ±0.001        | 0.989 ±0.0       |
| B1 labels                        | all levels | 0.768 ±0.0        | 0.834 ±0.0       | 0.889 ±0.0          | 0.95 ±0.001      |
| B6 plain encoder                 | full       | 0.627 ±0.0        | 0.784 ±0.0       | 0.866 ±0.0          | 0.971 ±0.0       |

### E3 — general search

| method                     | overlap@10_with_encoder   | topic_mAP_encoder   | topic_mAP_SSE   |
|:---------------------------|:--------------------------|:--------------------|:----------------|
| SSE-treeSC                 | 0.808 ±0.006              | 0.237 ±0.0          | 0.253 ±0.0      |
| SSE-tree                   | 0.858 ±0.015              | 0.237 ±0.0          | 0.238 ±0.0      |
| SSE (yes/no levels)        | 0.702 ±0.002              | 0.237 ±0.0          | 0.262 ±0.001    |
| SSE-MRL (topic everywhere) | 0.759 ±0.005              | 0.237 ±0.0          | 0.257 ±0.001    |

### E8a — Papers VecJOIN Authors (truth: share of the author's papers in the paper's area)

| query_split   | level    | method                           | Spearman     | NDCG@10      | join_F1      | authors_per_paper   |
|:--------------|:---------|:---------------------------------|:-------------|:-------------|:-------------|:--------------------|
| seen_test     | domain   | B6 plain encoder                 | 0.298 ±0.0   | 0.712 ±0.0   | 0.427 ±0.0   | 2605.733 ±0.0       |
| unseen        | domain   | B6 plain encoder                 | 0.302 ±0.0   | 0.727 ±0.0   | 0.436 ±0.0   | 2621.824 ±0.0       |
| seen_test     | domain   | SSE-treeSC                       | 0.72 ±0.003  | 0.742 ±0.003 | 0.745 ±0.0   | 1486.167 ±14.659    |
| unseen        | domain   | SSE-treeSC                       | 0.714 ±0.001 | 0.732 ±0.005 | 0.725 ±0.002 | 1525.302 ±7.936     |
| seen_test     | domain   | SSE-tree                         | 0.706 ±0.001 | 0.741 ±0.003 | 0.742 ±0.0   | 1407.24 ±16.563     |
| unseen        | domain   | SSE-tree                         | 0.696 ±0.001 | 0.736 ±0.001 | 0.72 ±0.001  | 1445.282 ±18.518    |
| seen_test     | domain   | SSE (yes/no levels)              | 0.702 ±0.002 | 0.742 ±0.003 | 0.724 ±0.001 | 1597.028 ±33.965    |
| unseen        | domain   | SSE (yes/no levels)              | 0.699 ±0.001 | 0.733 ±0.004 | 0.71 ±0.001  | 1631.859 ±24.681    |
| seen_test     | domain   | SSE-MRL (topic everywhere)       | 0.416 ±0.016 | 0.711 ±0.0   | 0.522 ±0.007 | 2079.519 ±21.952    |
| unseen        | domain   | SSE-MRL (topic everywhere)       | 0.402 ±0.021 | 0.711 ±0.002 | 0.517 ±0.01  | 2096.276 ±36.207    |
| seen_test     | domain   | B3 separate (graded+contrastive) | 0.725 ±0.003 | 0.745 ±0.001 | 0.746 ±0.001 | 1484.391 ±0.866     |
| unseen        | domain   | B3 separate (graded+contrastive) | 0.717 ±0.005 | 0.737 ±0.002 | 0.727 ±0.003 | 1536.172 ±2.24      |
| seen_test     | domain   | B4 CSN (graded+contrastive)      | 0.729 ±0.0   | 0.746 ±0.001 | 0.745 ±0.001 | 1439.614 ±21.798    |
| unseen        | domain   | B4 CSN (graded+contrastive)      | 0.718 ±0.001 | 0.746 ±0.001 | 0.723 ±0.002 | 1496.19 ±27.425     |
| seen_test     | domain   | B1 labels                        | 0.615 ±0.003 | 0.709 ±0.016 | 0.664 ±0.001 | 1398.764 ±26.082    |
| unseen        | domain   | B1 labels                        | 0.572 ±0.002 | 0.675 ±0.014 | 0.632 ±0.0   | 1461.366 ±25.943    |
| seen_test     | field    | B6 plain encoder                 | 0.315 ±0.0   | 0.404 ±0.0   | 0.152 ±0.0   | 298.419 ±0.0        |
| unseen        | field    | B6 plain encoder                 | 0.314 ±0.0   | 0.456 ±0.0   | 0.179 ±0.0   | 305.005 ±0.0        |
| seen_test     | field    | SSE-treeSC                       | 0.432 ±0.002 | 0.467 ±0.002 | 0.328 ±0.003 | 200.186 ±21.888     |
| unseen        | field    | SSE-treeSC                       | 0.418 ±0.003 | 0.483 ±0.001 | 0.343 ±0.002 | 198.312 ±20.572     |
| seen_test     | field    | SSE-tree                         | 0.372 ±0.002 | 0.428 ±0.004 | 0.247 ±0.002 | 202.512 ±21.489     |
| unseen        | field    | SSE-tree                         | 0.367 ±0.002 | 0.473 ±0.002 | 0.281 ±0.004 | 192.555 ±21.966     |
| seen_test     | field    | SSE (yes/no levels)              | 0.451 ±0.001 | 0.471 ±0.002 | 0.34 ±0.002  | 179.761 ±1.172      |
| unseen        | field    | SSE (yes/no levels)              | 0.443 ±0.004 | 0.482 ±0.002 | 0.354 ±0.003 | 175.393 ±1.479      |
| seen_test     | field    | SSE-MRL (topic everywhere)       | 0.342 ±0.005 | 0.445 ±0.001 | 0.255 ±0.002 | 179.5 ±1.897        |
| unseen        | field    | SSE-MRL (topic everywhere)       | 0.337 ±0.007 | 0.485 ±0.001 | 0.286 ±0.001 | 186.992 ±3.299      |
| seen_test     | field    | B3 separate (graded+contrastive) | 0.434 ±0.002 | 0.469 ±0.005 | 0.334 ±0.008 | 176.899 ±3.359      |
| unseen        | field    | B3 separate (graded+contrastive) | 0.427 ±0.001 | 0.483 ±0.001 | 0.348 ±0.006 | 172.296 ±3.2        |
| seen_test     | field    | B4 CSN (graded+contrastive)      | 0.429 ±0.002 | 0.469 ±0.002 | 0.32 ±0.004  | 170.54 ±2.644       |
| unseen        | field    | B4 CSN (graded+contrastive)      | 0.415 ±0.004 | 0.494 ±0.002 | 0.341 ±0.003 | 170.37 ±0.886       |
| seen_test     | field    | B1 labels                        | 0.432 ±0.002 | 0.445 ±0.005 | 0.312 ±0.002 | 143.155 ±0.858      |
| unseen        | field    | B1 labels                        | 0.427 ±0.002 | 0.463 ±0.005 | 0.333 ±0.002 | 143.24 ±0.894       |
| seen_test     | subfield | B6 plain encoder                 | 0.236 ±0.0   | 0.301 ±0.0   | 0.094 ±0.0   | 41.007 ±0.0         |
| unseen        | subfield | B6 plain encoder                 | 0.238 ±0.0   | 0.341 ±0.0   | 0.112 ±0.0   | 47.097 ±0.0         |
| seen_test     | subfield | SSE-treeSC                       | 0.289 ±0.001 | 0.36 ±0.001  | 0.225 ±0.002 | 46.364 ±0.556       |
| unseen        | subfield | SSE-treeSC                       | 0.285 ±0.002 | 0.359 ±0.001 | 0.214 ±0.003 | 51.547 ±0.199       |
| seen_test     | subfield | SSE-tree                         | 0.25 ±0.001  | 0.31 ±0.003  | 0.159 ±0.002 | 44.022 ±1.018       |
| unseen        | subfield | SSE-tree                         | 0.256 ±0.001 | 0.343 ±0.001 | 0.175 ±0.003 | 44.364 ±1.468       |
| seen_test     | subfield | SSE (yes/no levels)              | 0.294 ±0.001 | 0.357 ±0.001 | 0.224 ±0.003 | 48.275 ±0.591       |
| unseen        | subfield | SSE (yes/no levels)              | 0.287 ±0.002 | 0.35 ±0.001  | 0.216 ±0.004 | 52.568 ±0.416       |
| seen_test     | subfield | SSE-MRL (topic everywhere)       | 0.251 ±0.001 | 0.354 ±0.001 | 0.196 ±0.002 | 47.903 ±0.524       |
| unseen        | subfield | SSE-MRL (topic everywhere)       | 0.253 ±0.001 | 0.367 ±0.002 | 0.215 ±0.002 | 53.42 ±1.193        |
| seen_test     | subfield | B3 separate (graded+contrastive) | 0.292 ±0.001 | 0.361 ±0.001 | 0.231 ±0.001 | 47.697 ±0.165       |
| unseen        | subfield | B3 separate (graded+contrastive) | 0.282 ±0.002 | 0.361 ±0.002 | 0.221 ±0.006 | 52.454 ±0.082       |
| seen_test     | subfield | B4 CSN (graded+contrastive)      | 0.289 ±0.002 | 0.361 ±0.003 | 0.23 ±0.004  | 46.955 ±0.453       |
| unseen        | subfield | B4 CSN (graded+contrastive)      | 0.282 ±0.001 | 0.363 ±0.001 | 0.219 ±0.002 | 51.505 ±0.351       |
| seen_test     | subfield | B1 labels                        | 0.259 ±0.001 | 0.207 ±0.007 | 0.126 ±0.001 | 47.658 ±0.565       |
| unseen        | subfield | B1 labels                        | 0.258 ±0.0   | 0.207 ±0.008 | 0.145 ±0.001 | 51.992 ±0.617       |
| seen_test     | topic    | B6 plain encoder                 | 0.114 ±0.0   | 0.322 ±0.0   | 0.113 ±0.0   | 2.847 ±0.0          |
| unseen        | topic    | B6 plain encoder                 | 0.12 ±0.0    | 0.364 ±0.0   | 0.107 ±0.0   | 5.026 ±0.0          |
| seen_test     | topic    | SSE-treeSC                       | 0.122 ±0.001 | 0.375 ±0.0   | 0.212 ±0.001 | 4.827 ±0.042        |
| unseen        | topic    | SSE-treeSC                       | 0.123 ±0.0   | 0.37 ±0.0    | 0.209 ±0.002 | 6.161 ±0.178        |
| seen_test     | topic    | SSE-tree                         | 0.113 ±0.001 | 0.329 ±0.002 | 0.137 ±0.003 | 4.104 ±0.21         |
| unseen        | topic    | SSE-tree                         | 0.12 ±0.001  | 0.365 ±0.001 | 0.152 ±0.004 | 5.141 ±0.127        |
| seen_test     | topic    | SSE (yes/no levels)              | 0.12 ±0.001  | 0.372 ±0.001 | 0.217 ±0.004 | 5.072 ±0.041        |
| unseen        | topic    | SSE (yes/no levels)              | 0.124 ±0.001 | 0.364 ±0.001 | 0.208 ±0.002 | 6.624 ±0.175        |
| seen_test     | topic    | SSE-MRL (topic everywhere)       | 0.121 ±0.001 | 0.372 ±0.0   | 0.217 ±0.002 | 5.091 ±0.044        |
| unseen        | topic    | SSE-MRL (topic everywhere)       | 0.125 ±0.0   | 0.364 ±0.002 | 0.211 ±0.001 | 6.696 ±0.237        |
| seen_test     | topic    | B3 separate (graded+contrastive) | 0.12 ±0.0    | 0.377 ±0.0   | 0.215 ±0.003 | 5.079 ±0.034        |
| unseen        | topic    | B3 separate (graded+contrastive) | 0.121 ±0.001 | 0.369 ±0.002 | 0.211 ±0.004 | 6.419 ±0.201        |
| seen_test     | topic    | B4 CSN (graded+contrastive)      | 0.122 ±0.0   | 0.375 ±0.004 | 0.214 ±0.002 | 4.86 ±0.069         |
| unseen        | topic    | B4 CSN (graded+contrastive)      | 0.125 ±0.0   | 0.369 ±0.004 | 0.21 ±0.001  | 6.23 ±0.057         |
| seen_test     | topic    | B1 labels                        | 0.074 ±0.001 | 0.109 ±0.002 | 0.007 ±0.0   | 84.684 ±2.7         |
| unseen        | topic    | B1 labels                        | 0.069 ±0.001 | 0.042 ±0.002 | 0.009 ±0.0   | 91.967 ±2.848       |

### E8b — institution similarity (truth: cosine of research profiles)

| level    | method                           | Spearman     | NDCG@10      |
|:---------|:---------------------------------|:-------------|:-------------|
| domain   | B6 plain encoder                 | 0.626 ±0.0   | 0.938 ±0.0   |
| domain   | SSE-treeSC                       | 0.943 ±0.001 | 0.98 ±0.0    |
| domain   | SSE-tree                         | 0.949 ±0.002 | 0.978 ±0.0   |
| domain   | SSE (yes/no levels)              | 0.922 ±0.002 | 0.978 ±0.0   |
| domain   | SSE-MRL (topic everywhere)       | 0.636 ±0.027 | 0.932 ±0.002 |
| domain   | B3 separate (graded+contrastive) | 0.941 ±0.003 | 0.979 ±0.001 |
| domain   | B4 CSN (graded+contrastive)      | 0.943 ±0.0   | 0.979 ±0.0   |
| domain   | B1 labels                        | 0.88 ±0.001  | 0.959 ±0.0   |
| field    | B6 plain encoder                 | 0.774 ±0.0   | 0.885 ±0.0   |
| field    | SSE-treeSC                       | 0.834 ±0.009 | 0.93 ±0.001  |
| field    | SSE-tree                         | 0.762 ±0.007 | 0.91 ±0.002  |
| field    | SSE (yes/no levels)              | 0.864 ±0.01  | 0.931 ±0.001 |
| field    | SSE-MRL (topic everywhere)       | 0.745 ±0.019 | 0.906 ±0.001 |
| field    | B3 separate (graded+contrastive) | 0.841 ±0.003 | 0.931 ±0.002 |
| field    | B4 CSN (graded+contrastive)      | 0.828 ±0.005 | 0.929 ±0.001 |
| field    | B1 labels                        | 0.84 ±0.001  | 0.925 ±0.0   |
| subfield | B6 plain encoder                 | 0.789 ±0.0   | 0.777 ±0.0   |
| subfield | SSE-treeSC                       | 0.825 ±0.007 | 0.816 ±0.002 |
| subfield | SSE-tree                         | 0.76 ±0.002  | 0.791 ±0.002 |
| subfield | SSE (yes/no levels)              | 0.831 ±0.004 | 0.811 ±0.001 |
| subfield | SSE-MRL (topic everywhere)       | 0.723 ±0.008 | 0.825 ±0.001 |
| subfield | B3 separate (graded+contrastive) | 0.819 ±0.006 | 0.818 ±0.001 |
| subfield | B4 CSN (graded+contrastive)      | 0.824 ±0.005 | 0.818 ±0.002 |
| subfield | B1 labels                        | 0.758 ±0.001 | 0.741 ±0.001 |
| topic    | B6 plain encoder                 | 0.715 ±0.0   | 0.559 ±0.0   |
| topic    | SSE-treeSC                       | 0.699 ±0.015 | 0.599 ±0.001 |
| topic    | SSE-tree                         | 0.65 ±0.005  | 0.57 ±0.002  |
| topic    | SSE (yes/no levels)              | 0.71 ±0.022  | 0.601 ±0.001 |
| topic    | SSE-MRL (topic everywhere)       | 0.656 ±0.012 | 0.605 ±0.001 |
| topic    | B3 separate (graded+contrastive) | 0.679 ±0.003 | 0.605 ±0.003 |
| topic    | B4 CSN (graded+contrastive)      | 0.68 ±0.008  | 0.604 ±0.003 |
| topic    | B1 labels                        | 0.488 ±0.002 | 0.389 ±0.001 |

### E6 — roll-up / drill-down inside Physical Sciences

| policy    | level    | method                           | ARI          | NMI          | n_main_groups   | coverage     |
|:----------|:---------|:---------------------------------|:-------------|:-------------|:----------------|:-------------|
| connected | field    | B6 plain encoder                 | 0.022 ±0.0   | 0.372 ±0.0   | 1.0 ±0.0        | 0.288 ±0.0   |
| connected | subfield | B6 plain encoder                 | 0.045 ±0.0   | 0.569 ±0.0   | 1.0 ±0.0        | 0.288 ±0.0   |
| connected | topic    | B6 plain encoder                 | 0.048 ±0.0   | 0.836 ±0.0   | 0.0 ±0.0        | 0.0 ±0.0     |
| connected | field    | SSE-treeSC                       | 0.059 ±0.018 | 0.398 ±0.015 | 3.333 ±1.0      | 0.262 ±0.016 |
| connected | subfield | SSE-treeSC                       | 0.071 ±0.026 | 0.611 ±0.015 | 4.333 ±2.0      | 0.197 ±0.019 |
| connected | topic    | SSE-treeSC                       | 0.109 ±0.014 | 0.828 ±0.001 | 3.0 ±1.0        | 0.076 ±0.013 |
| connected | field    | SSE-tree                         | 0.03 ±0.005  | 0.354 ±0.007 | 1.0 ±0.0        | 0.397 ±0.034 |
| connected | subfield | SSE-tree                         | 0.048 ±0.0   | 0.599 ±0.004 | 1.667 ±0.5      | 0.203 ±0.017 |
| connected | topic    | SSE-tree                         | 0.053 ±0.021 | 0.811 ±0.012 | 2.0 ±1.0        | 0.127 ±0.03  |
| connected | field    | SSE (yes/no levels)              | 0.047 ±0.038 | 0.365 ±0.045 | 2.333 ±1.5      | 0.397 ±0.116 |
| connected | subfield | SSE (yes/no levels)              | 0.051 ±0.024 | 0.583 ±0.037 | 3.333 ±2.0      | 0.272 ±0.082 |
| connected | topic    | SSE (yes/no levels)              | 0.106 ±0.005 | 0.827 ±0.007 | 4.0 ±2.5        | 0.09 ±0.057  |
| connected | field    | B3 separate (graded+contrastive) | 0.058 ±0.008 | 0.399 ±0.024 | 2.667 ±0.5      | 0.238 ±0.121 |
| connected | subfield | B3 separate (graded+contrastive) | 0.075 ±0.009 | 0.618 ±0.007 | 4.333 ±1.0      | 0.177 ±0.073 |
| connected | topic    | B3 separate (graded+contrastive) | 0.103 ±0.025 | 0.83 ±0.002  | 2.333 ±1.0      | 0.055 ±0.008 |
| connected | field    | B4 CSN (graded+contrastive)      | 0.039 ±0.011 | 0.366 ±0.014 | 1.667 ±0.5      | 0.359 ±0.051 |
| connected | subfield | B4 CSN (graded+contrastive)      | 0.041 ±0.013 | 0.579 ±0.012 | 2.667 ±1.0      | 0.29 ±0.015  |
| connected | topic    | B4 CSN (graded+contrastive)      | 0.11 ±0.018  | 0.825 ±0.005 | 4.333 ±1.0      | 0.105 ±0.03  |
| center    | field    | B6 plain encoder                 | 0.044 ±0.0   | 0.339 ±0.0   | 15.0 ±0.0       | 0.504 ±0.0   |
| center    | subfield | B6 plain encoder                 | 0.046 ±0.0   | 0.597 ±0.0   | 2.0 ±0.0        | 0.063 ±0.0   |
| center    | topic    | B6 plain encoder                 | 0.062 ±0.0   | 0.834 ±0.0   | 0.0 ±0.0        | 0.0 ±0.0     |
| center    | field    | SSE-treeSC                       | 0.232 ±0.005 | 0.437 ±0.003 | 14.0 ±1.5       | 0.67 ±0.036  |
| center    | subfield | SSE-treeSC                       | 0.163 ±0.009 | 0.583 ±0.008 | 11.333 ±1.5     | 0.331 ±0.035 |
| center    | topic    | SSE-treeSC                       | 0.165 ±0.008 | 0.816 ±0.005 | 5.0 ±1.0        | 0.064 ±0.012 |
| center    | field    | SSE-tree                         | 0.107 ±0.008 | 0.355 ±0.008 | 11.0 ±0.0       | 0.575 ±0.01  |
| center    | subfield | SSE-tree                         | 0.082 ±0.002 | 0.574 ±0.013 | 9.0 ±1.0        | 0.228 ±0.037 |
| center    | topic    | SSE-tree                         | 0.097 ±0.007 | 0.816 ±0.003 | 2.333 ±1.0      | 0.037 ±0.015 |
| center    | field    | SSE (yes/no levels)              | 0.275 ±0.01  | 0.45 ±0.001  | 13.667 ±1.0     | 0.734 ±0.037 |
| center    | subfield | SSE (yes/no levels)              | 0.178 ±0.011 | 0.578 ±0.006 | 13.0 ±1.0       | 0.362 ±0.033 |
| center    | topic    | SSE (yes/no levels)              | 0.176 ±0.007 | 0.818 ±0.001 | 4.0 ±0.0        | 0.053 ±0.001 |
| center    | field    | B3 separate (graded+contrastive) | 0.232 ±0.024 | 0.432 ±0.012 | 13.667 ±1.5     | 0.674 ±0.021 |
| center    | subfield | B3 separate (graded+contrastive) | 0.161 ±0.015 | 0.589 ±0.006 | 13.333 ±2.0     | 0.315 ±0.01  |
| center    | topic    | B3 separate (graded+contrastive) | 0.163 ±0.025 | 0.816 ±0.007 | 3.667 ±1.5      | 0.05 ±0.019  |
| center    | field    | B4 CSN (graded+contrastive)      | 0.234 ±0.027 | 0.43 ±0.011  | 11.333 ±1.0     | 0.68 ±0.015  |
| center    | subfield | B4 CSN (graded+contrastive)      | 0.156 ±0.011 | 0.583 ±0.007 | 14.333 ±1.5     | 0.341 ±0.048 |
| center    | topic    | B4 CSN (graded+contrastive)      | 0.162 ±0.022 | 0.819 ±0.002 | 2.667 ±0.5      | 0.034 ±0.011 |
