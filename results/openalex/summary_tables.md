# OpenAlex — summary over 3 seeds

### E2 — mAP of each level at its OWN prefix (domain@16, field@64, subfield@128)

| split     | method                            | domain       | field        | subfield     |
|:----------|:----------------------------------|:-------------|:-------------|:-------------|
| seen_test | SSE-treeSC                        | 0.755 ±0.001 | 0.43 ±0.001  | 0.305 ±0.0   |
| seen_test | SSE-tree                          | 0.751 ±0.0   | 0.298 ±0.003 | 0.204 ±0.001 |
| seen_test | SSE (yes/no levels)               | 0.751 ±0.001 | 0.442 ±0.001 | 0.308 ±0.001 |
| seen_test | SSE-MRL (finest level everywhere) | 0.567 ±0.004 | 0.366 ±0.0   | 0.309 ±0.001 |
| seen_test | Encoder-PCA                       | 0.525 ±0.0   | 0.242 ±0.0   | 0.2 ±0.0     |
| unseen    | SSE-treeSC                        | 0.753 ±0.004 | 0.457 ±0.004 | 0.4 ±0.001   |
| unseen    | SSE-tree                          | 0.763 ±0.002 | 0.386 ±0.003 | 0.356 ±0.001 |
| unseen    | SSE (yes/no levels)               | 0.745 ±0.004 | 0.454 ±0.004 | 0.391 ±0.001 |
| unseen    | SSE-MRL (finest level everywhere) | 0.579 ±0.004 | 0.437 ±0.001 | 0.39 ±0.001  |
| unseen    | Encoder-PCA                       | 0.532 ±0.0   | 0.356 ±0.0   | 0.379 ±0.0   |

### E2 — prefix length where each level peaks (should be 16 / 64 / 128)

| split     | method                            |   domain |   field |   subfield |
|:----------|:----------------------------------|---------:|--------:|-----------:|
| seen_test | Encoder-PCA                       |        8 |      32 |        128 |
| seen_test | SSE (yes/no levels)               |       16 |      64 |        128 |
| seen_test | SSE-MRL (finest level everywhere) |       16 |     128 |        128 |
| seen_test | SSE-tree                          |       16 |      64 |        128 |
| seen_test | SSE-treeSC                        |       16 |      64 |        128 |
| unseen    | Encoder-PCA                       |        8 |      64 |        128 |
| unseen    | SSE (yes/no levels)               |       16 |      64 |        128 |
| unseen    | SSE-MRL (finest level everywhere) |       16 |     128 |        128 |
| unseen    | SSE-tree                          |       16 |      64 |        128 |
| unseen    | SSE-treeSC                        |       16 |      64 |        128 |

### E2b — pair AUC per view (does a finer view keep coarser levels?)

| method                           | view       | same-domain AUC   | same-field AUC   | same-subfield AUC   |
|:---------------------------------|:-----------|:------------------|:-----------------|:--------------------|
| SSE-treeSC                       | domain     | 0.912 ±0.001      | 0.826 ±0.002     | 0.836 ±0.003        |
| SSE-treeSC                       | field      | 0.835 ±0.003      | 0.911 ±0.003     | 0.927 ±0.003        |
| SSE-treeSC                       | subfield   | 0.797 ±0.005      | 0.893 ±0.002     | 0.942 ±0.002        |
| SSE-tree                         | domain     | 0.908 ±0.001      | 0.826 ±0.001     | 0.838 ±0.003        |
| SSE-tree                         | field      | 0.888 ±0.001      | 0.859 ±0.001     | 0.883 ±0.002        |
| SSE-tree                         | subfield   | 0.87 ±0.002       | 0.855 ±0.001     | 0.888 ±0.002        |
| SSE (yes/no levels)              | domain     | 0.905 ±0.001      | 0.832 ±0.001     | 0.843 ±0.002        |
| SSE (yes/no levels)              | field      | 0.766 ±0.013      | 0.922 ±0.001     | 0.934 ±0.001        |
| SSE (yes/no levels)              | subfield   | 0.745 ±0.013      | 0.896 ±0.002     | 0.946 ±0.001        |
| B3 separate (graded+contrastive) | domain     | 0.912 ±0.001      | 0.824 ±0.002     | 0.835 ±0.002        |
| B3 separate (graded+contrastive) | field      | 0.838 ±0.003      | 0.913 ±0.001     | 0.927 ±0.002        |
| B3 separate (graded+contrastive) | subfield   | 0.79 ±0.006       | 0.891 ±0.001     | 0.943 ±0.002        |
| B4 CSN (graded+contrastive)      | domain     | 0.913 ±0.003      | 0.821 ±0.004     | 0.831 ±0.005        |
| B4 CSN (graded+contrastive)      | field      | 0.841 ±0.001      | 0.912 ±0.002     | 0.927 ±0.001        |
| B4 CSN (graded+contrastive)      | subfield   | 0.8 ±0.002        | 0.893 ±0.002     | 0.942 ±0.001        |
| B1 labels                        | all levels | 0.798 ±0.0        | 0.845 ±0.0       | 0.896 ±0.0          |
| B6 plain encoder                 | full       | 0.627 ±0.0        | 0.784 ±0.0       | 0.866 ±0.0          |

### E2s — paper -> 10 nearest papers: exact label (P@10) and tree credit

| split     | level    | method                            | P@10         | tree_credit@10   | credit_text@10   | credit_coact@10   |
|:----------|:---------|:----------------------------------|:-------------|:-----------------|:-----------------|:------------------|
| seen_test | domain   | SSE-treeSC                        | 0.815 ±0.005 | 0.815 ±0.005     | nan              | nan               |
| seen_test | domain   | SSE-tree                          | 0.833 ±0.009 | 0.833 ±0.009     | nan              | nan               |
| seen_test | domain   | SSE (yes/no levels)               | 0.805 ±0.004 | 0.805 ±0.004     | nan              | nan               |
| seen_test | domain   | SSE-MRL (finest level everywhere) | 0.836 ±0.003 | 0.836 ±0.003     | nan              | nan               |
| seen_test | domain   | B3 separate (graded+contrastive)  | 0.818 ±0.007 | 0.818 ±0.007     | nan              | nan               |
| seen_test | domain   | B4 CSN (graded+contrastive)       | 0.846 ±0.001 | 0.846 ±0.001     | nan              | nan               |
| seen_test | domain   | Encoder-PCA                       | 0.794 ±0.0   | 0.794 ±0.0       | nan              | nan               |
| seen_test | domain   | B6 plain encoder                  | 0.815 ±0.0   | 0.815 ±0.0       | nan              | nan               |
| seen_test | domain   | B1 labels                         | 0.82 ±0.001  | 0.82 ±0.001      | nan              | nan               |
| seen_test | domain   | Random                            | 0.274 ±0.0   | 0.274 ±0.0       | nan              | nan               |
| seen_test | field    | SSE-treeSC                        | 0.638 ±0.002 | 0.749 ±0.001     | nan              | nan               |
| seen_test | field    | SSE-tree                          | 0.598 ±0.005 | 0.729 ±0.003     | nan              | nan               |
| seen_test | field    | SSE (yes/no levels)               | 0.626 ±0.003 | 0.739 ±0.003     | nan              | nan               |
| seen_test | field    | SSE-MRL (finest level everywhere) | 0.657 ±0.002 | 0.758 ±0.002     | nan              | nan               |
| seen_test | field    | B3 separate (graded+contrastive)  | 0.637 ±0.005 | 0.748 ±0.003     | nan              | nan               |
| seen_test | field    | B4 CSN (graded+contrastive)       | 0.648 ±0.004 | 0.756 ±0.002     | nan              | nan               |
| seen_test | field    | Encoder-PCA                       | 0.6 ±0.0     | 0.717 ±0.0       | nan              | nan               |
| seen_test | field    | B6 plain encoder                  | 0.582 ±0.0   | 0.698 ±0.0       | nan              | nan               |
| seen_test | field    | B1 labels                         | 0.584 ±0.001 | 0.706 ±0.001     | nan              | nan               |
| seen_test | field    | Random                            | 0.039 ±0.0   | 0.156 ±0.0       | nan              | nan               |
| seen_test | subfield | SSE-treeSC                        | 0.508 ±0.003 | 0.681 ±0.001     | 0.621 ±0.002     | 0.545 ±0.002      |
| seen_test | subfield | SSE-tree                          | 0.451 ±0.003 | 0.64 ±0.003      | 0.57 ±0.002      | 0.489 ±0.003      |
| seen_test | subfield | SSE (yes/no levels)               | 0.5 ±0.002   | 0.675 ±0.001     | 0.616 ±0.002     | 0.538 ±0.002      |
| seen_test | subfield | SSE-MRL (finest level everywhere) | 0.501 ±0.004 | 0.674 ±0.002     | 0.616 ±0.003     | 0.539 ±0.004      |
| seen_test | subfield | B3 separate (graded+contrastive)  | 0.509 ±0.003 | 0.679 ±0.003     | 0.622 ±0.002     | 0.545 ±0.003      |
| seen_test | subfield | B4 CSN (graded+contrastive)       | 0.5 ±0.002   | 0.673 ±0.002     | 0.614 ±0.002     | 0.538 ±0.002      |
| seen_test | subfield | Encoder-PCA                       | 0.463 ±0.0   | 0.635 ±0.0       | 0.576 ±0.0       | 0.5 ±0.0          |
| seen_test | subfield | B6 plain encoder                  | 0.451 ±0.0   | 0.616 ±0.0       | 0.563 ±0.0       | 0.486 ±0.0        |
| seen_test | subfield | B1 labels                         | 0.393 ±0.003 | 0.59 ±0.001      | 0.519 ±0.002     | 0.434 ±0.002      |
| seen_test | subfield | Random                            | 0.01 ±0.0    | 0.108 ±0.0       | 0.072 ±0.0       | 0.022 ±0.0        |
| unseen    | domain   | SSE-treeSC                        | 0.815 ±0.004 | 0.815 ±0.004     | nan              | nan               |
| unseen    | domain   | SSE-tree                          | 0.852 ±0.008 | 0.852 ±0.008     | nan              | nan               |
| unseen    | domain   | SSE (yes/no levels)               | 0.8 ±0.004   | 0.8 ±0.004       | nan              | nan               |
| unseen    | domain   | SSE-MRL (finest level everywhere) | 0.866 ±0.006 | 0.866 ±0.006     | nan              | nan               |
| unseen    | domain   | B3 separate (graded+contrastive)  | 0.823 ±0.002 | 0.823 ±0.002     | nan              | nan               |
| unseen    | domain   | B4 CSN (graded+contrastive)       | 0.896 ±0.001 | 0.896 ±0.001     | nan              | nan               |
| unseen    | domain   | Encoder-PCA                       | 0.854 ±0.0   | 0.854 ±0.0       | nan              | nan               |
| unseen    | domain   | B6 plain encoder                  | 0.909 ±0.0   | 0.909 ±0.0       | nan              | nan               |
| unseen    | domain   | B1 labels                         | 0.9 ±0.001   | 0.9 ±0.001       | nan              | nan               |
| unseen    | domain   | Random                            | 0.263 ±0.0   | 0.263 ±0.0       | nan              | nan               |
| unseen    | field    | SSE-treeSC                        | 0.759 ±0.004 | 0.827 ±0.002     | nan              | nan               |
| unseen    | field    | SSE-tree                          | 0.772 ±0.006 | 0.84 ±0.004      | nan              | nan               |
| unseen    | field    | SSE (yes/no levels)               | 0.711 ±0.003 | 0.791 ±0.003     | nan              | nan               |
| unseen    | field    | SSE-MRL (finest level everywhere) | 0.776 ±0.003 | 0.838 ±0.003     | nan              | nan               |
| unseen    | field    | B3 separate (graded+contrastive)  | 0.766 ±0.007 | 0.833 ±0.006     | nan              | nan               |
| unseen    | field    | B4 CSN (graded+contrastive)       | 0.778 ±0.002 | 0.842 ±0.002     | nan              | nan               |
| unseen    | field    | Encoder-PCA                       | 0.807 ±0.0   | 0.863 ±0.0       | nan              | nan               |
| unseen    | field    | B6 plain encoder                  | 0.803 ±0.0   | 0.856 ±0.0       | nan              | nan               |
| unseen    | field    | B1 labels                         | 0.752 ±0.003 | 0.817 ±0.002     | nan              | nan               |
| unseen    | field    | Random                            | 0.043 ±0.0   | 0.153 ±0.0       | nan              | nan               |
| unseen    | subfield | SSE-treeSC                        | 0.712 ±0.004 | 0.809 ±0.004     | 0.777 ±0.003     | 0.736 ±0.004      |
| unseen    | subfield | SSE-tree                          | 0.723 ±0.003 | 0.82 ±0.002      | 0.783 ±0.002     | 0.745 ±0.002      |
| unseen    | subfield | SSE (yes/no levels)               | 0.687 ±0.003 | 0.791 ±0.002     | 0.758 ±0.003     | 0.713 ±0.003      |
| unseen    | subfield | SSE-MRL (finest level everywhere) | 0.688 ±0.002 | 0.791 ±0.003     | 0.758 ±0.002     | 0.713 ±0.002      |
| unseen    | subfield | B3 separate (graded+contrastive)  | 0.705 ±0.009 | 0.805 ±0.008     | 0.772 ±0.008     | 0.73 ±0.009       |
| unseen    | subfield | B4 CSN (graded+contrastive)       | 0.713 ±0.002 | 0.81 ±0.001      | 0.778 ±0.001     | 0.737 ±0.002      |
| unseen    | subfield | Encoder-PCA                       | 0.744 ±0.0   | 0.831 ±0.0       | 0.801 ±0.0       | 0.765 ±0.0        |
| unseen    | subfield | B6 plain encoder                  | 0.73 ±0.0    | 0.814 ±0.0       | 0.786 ±0.0       | 0.75 ±0.0         |
| unseen    | subfield | B1 labels                         | 0.625 ±0.002 | 0.739 ±0.002     | 0.701 ±0.001     | 0.651 ±0.002      |
| unseen    | subfield | Random                            | 0.018 ±0.0   | 0.108 ±0.0       | 0.078 ±0.0       | 0.029 ±0.0        |

### E3 — general search

| method                            | overlap@10_with_encoder   | topic_mAP_encoder   | topic_mAP_SSE   |
|:----------------------------------|:--------------------------|:--------------------|:----------------|
| SSE-treeSC                        | 0.843 ±0.008              | 0.413 ±0.0          | 0.427 ±0.0      |
| SSE-tree                          | 0.87 ±0.006               | 0.413 ±0.0          | 0.419 ±0.0      |
| SSE (yes/no levels)               | 0.774 ±0.004              | 0.413 ±0.0          | 0.43 ±0.001     |
| SSE-MRL (finest level everywhere) | 0.809 ±0.001              | 0.413 ±0.0          | 0.427 ±0.001    |

### E8a — Papers VecJOIN Authors (P@10 / F1: paper's area = author's main area)

| query_split   | level    | method                            | P@10         | P@10_active   | tree_credit@10   | credit_text@10   | credit_coact@10   | join_F1      | Spearman     | NDCG@10      |
|:--------------|:---------|:----------------------------------|:-------------|:--------------|:-----------------|:-----------------|:------------------|:-------------|:-------------|:-------------|
| seen_test     | domain   | B6 plain encoder                  | 0.775 ±0.0   | 0.887 ±0.0    | 0.775 ±0.0       | nan              | nan               | 0.446 ±0.0   | 0.298 ±0.0   | 0.712 ±0.0   |
| unseen        | domain   | B6 plain encoder                  | 0.792 ±0.0   | 0.9 ±0.0      | 0.792 ±0.0       | nan              | nan               | 0.455 ±0.0   | 0.302 ±0.0   | 0.727 ±0.0   |
| seen_test     | domain   | SSE-treeSC                        | 0.807 ±0.001 | 0.903 ±0.002  | 0.807 ±0.001     | nan              | nan               | 0.752 ±0.001 | 0.723 ±0.002 | 0.743 ±0.002 |
| unseen        | domain   | SSE-treeSC                        | 0.794 ±0.002 | 0.898 ±0.004  | 0.794 ±0.002     | nan              | nan               | 0.733 ±0.001 | 0.717 ±0.001 | 0.735 ±0.001 |
| seen_test     | domain   | SSE-tree                          | 0.809 ±0.003 | 0.907 ±0.001  | 0.809 ±0.003     | nan              | nan               | 0.75 ±0.001  | 0.712 ±0.002 | 0.747 ±0.001 |
| unseen        | domain   | SSE-tree                          | 0.799 ±0.001 | 0.905 ±0.001  | 0.799 ±0.001     | nan              | nan               | 0.728 ±0.001 | 0.702 ±0.004 | 0.743 ±0.0   |
| seen_test     | domain   | SSE (yes/no levels)               | 0.808 ±0.003 | 0.906 ±0.002  | 0.808 ±0.003     | nan              | nan               | 0.732 ±0.002 | 0.703 ±0.001 | 0.744 ±0.002 |
| unseen        | domain   | SSE (yes/no levels)               | 0.792 ±0.003 | 0.902 ±0.003  | 0.792 ±0.003     | nan              | nan               | 0.719 ±0.001 | 0.699 ±0.002 | 0.736 ±0.002 |
| seen_test     | domain   | SSE-MRL (finest level everywhere) | 0.807 ±0.002 | 0.907 ±0.003  | 0.807 ±0.002     | nan              | nan               | 0.559 ±0.01  | 0.497 ±0.018 | 0.745 ±0.001 |
| unseen        | domain   | SSE-MRL (finest level everywhere) | 0.801 ±0.002 | 0.904 ±0.002  | 0.801 ±0.002     | nan              | nan               | 0.562 ±0.007 | 0.503 ±0.012 | 0.743 ±0.001 |
| seen_test     | domain   | B3 separate (graded+contrastive)  | 0.806 ±0.002 | 0.902 ±0.001  | 0.806 ±0.002     | nan              | nan               | 0.753 ±0.001 | 0.728 ±0.004 | 0.744 ±0.001 |
| unseen        | domain   | B3 separate (graded+contrastive)  | 0.795 ±0.001 | 0.901 ±0.003  | 0.795 ±0.001     | nan              | nan               | 0.733 ±0.002 | 0.717 ±0.005 | 0.738 ±0.001 |
| seen_test     | domain   | B4 CSN (graded+contrastive)       | 0.811 ±0.004 | 0.913 ±0.002  | 0.811 ±0.004     | nan              | nan               | 0.751 ±0.002 | 0.73 ±0.005  | 0.744 ±0.002 |
| unseen        | domain   | B4 CSN (graded+contrastive)       | 0.808 ±0.0   | 0.915 ±0.001  | 0.808 ±0.0       | nan              | nan               | 0.73 ±0.004  | 0.717 ±0.008 | 0.744 ±0.0   |
| seen_test     | domain   | B1 labels                         | 0.754 ±0.012 | 0.783 ±0.005  | 0.754 ±0.012     | nan              | nan               | 0.67 ±0.001  | 0.615 ±0.003 | 0.709 ±0.016 |
| unseen        | domain   | B1 labels                         | 0.71 ±0.008  | 0.75 ±0.004   | 0.71 ±0.008      | nan              | nan               | 0.64 ±0.001  | 0.572 ±0.002 | 0.675 ±0.014 |
| seen_test     | domain   | Random (base rate)                | 0.274 ±0.0   | 0.372 ±0.0    | 0.274 ±0.0       | nan              | nan               | 0.43 ±0.0    | 0.0 ±0.0     | nan          |
| unseen        | domain   | Random (base rate)                | 0.279 ±0.0   | 0.38 ±0.0     | 0.279 ±0.0       | nan              | nan               | 0.437 ±0.0   | 0.0 ±0.0     | nan          |
| seen_test     | field    | B6 plain encoder                  | 0.453 ±0.0   | 0.596 ±0.0    | 0.618 ±0.0       | nan              | nan               | 0.2 ±0.0     | 0.315 ±0.0   | 0.404 ±0.0   |
| unseen        | field    | B6 plain encoder                  | 0.518 ±0.0   | 0.665 ±0.0    | 0.66 ±0.0        | nan              | nan               | 0.223 ±0.0   | 0.314 ±0.0   | 0.456 ±0.0   |
| seen_test     | field    | SSE-treeSC                        | 0.532 ±0.002 | 0.678 ±0.002  | 0.679 ±0.001     | nan              | nan               | 0.358 ±0.007 | 0.43 ±0.006  | 0.469 ±0.001 |
| unseen        | field    | SSE-treeSC                        | 0.56 ±0.001  | 0.701 ±0.001  | 0.692 ±0.0       | nan              | nan               | 0.372 ±0.006 | 0.416 ±0.007 | 0.49 ±0.0    |
| seen_test     | field    | SSE-tree                          | 0.483 ±0.002 | 0.624 ±0.0    | 0.652 ±0.002     | nan              | nan               | 0.252 ±0.001 | 0.368 ±0.003 | 0.433 ±0.002 |
| unseen        | field    | SSE-tree                          | 0.546 ±0.001 | 0.689 ±0.004  | 0.686 ±0.0       | nan              | nan               | 0.284 ±0.002 | 0.364 ±0.003 | 0.481 ±0.002 |
| seen_test     | field    | SSE (yes/no levels)               | 0.536 ±0.001 | 0.682 ±0.001  | 0.681 ±0.001     | nan              | nan               | 0.387 ±0.003 | 0.452 ±0.001 | 0.472 ±0.001 |
| unseen        | field    | SSE (yes/no levels)               | 0.551 ±0.001 | 0.693 ±0.002  | 0.684 ±0.0       | nan              | nan               | 0.396 ±0.003 | 0.445 ±0.005 | 0.484 ±0.001 |
| seen_test     | field    | SSE-MRL (finest level everywhere) | 0.53 ±0.002  | 0.675 ±0.003  | 0.675 ±0.001     | nan              | nan               | 0.339 ±0.001 | 0.426 ±0.003 | 0.468 ±0.002 |
| unseen        | field    | SSE-MRL (finest level everywhere) | 0.559 ±0.003 | 0.7 ±0.004    | 0.688 ±0.003     | nan              | nan               | 0.351 ±0.003 | 0.417 ±0.005 | 0.49 ±0.002  |
| seen_test     | field    | B3 separate (graded+contrastive)  | 0.533 ±0.004 | 0.678 ±0.003  | 0.68 ±0.003      | nan              | nan               | 0.362 ±0.004 | 0.431 ±0.004 | 0.47 ±0.002  |
| unseen        | field    | B3 separate (graded+contrastive)  | 0.556 ±0.001 | 0.698 ±0.002  | 0.69 ±0.001      | nan              | nan               | 0.377 ±0.004 | 0.425 ±0.003 | 0.487 ±0.002 |
| seen_test     | field    | B4 CSN (graded+contrastive)       | 0.531 ±0.002 | 0.679 ±0.002  | 0.679 ±0.002     | nan              | nan               | 0.359 ±0.002 | 0.43 ±0.003  | 0.469 ±0.002 |
| unseen        | field    | B4 CSN (graded+contrastive)       | 0.562 ±0.002 | 0.706 ±0.002  | 0.694 ±0.002     | nan              | nan               | 0.376 ±0.002 | 0.418 ±0.004 | 0.493 ±0.002 |
| seen_test     | field    | B1 labels                         | 0.479 ±0.004 | 0.548 ±0.008  | 0.633 ±0.004     | nan              | nan               | 0.332 ±0.002 | 0.432 ±0.002 | 0.445 ±0.005 |
| unseen        | field    | B1 labels                         | 0.502 ±0.003 | 0.563 ±0.004  | 0.636 ±0.003     | nan              | nan               | 0.348 ±0.002 | 0.427 ±0.002 | 0.463 ±0.005 |
| seen_test     | field    | Random (base rate)                | 0.04 ±0.0    | 0.063 ±0.0    | 0.158 ±0.0       | nan              | nan               | 0.077 ±0.0   | 0.0 ±0.0     | nan          |
| unseen        | field    | Random (base rate)                | 0.041 ±0.0   | 0.064 ±0.0    | 0.161 ±0.0       | nan              | nan               | 0.079 ±0.0   | 0.0 ±0.0     | nan          |
| seen_test     | subfield | B6 plain encoder                  | 0.299 ±0.0   | 0.361 ±0.0    | 0.525 ±0.0       | 0.362 ±0.0       | 0.259 ±0.0        | 0.152 ±0.0   | 0.236 ±0.0   | 0.301 ±0.0   |
| unseen        | subfield | B6 plain encoder                  | 0.344 ±0.0   | 0.416 ±0.0    | 0.568 ±0.0       | 0.395 ±0.0       | 0.293 ±0.0        | 0.17 ±0.0    | 0.238 ±0.0   | 0.341 ±0.0   |
| seen_test     | subfield | SSE-treeSC                        | 0.357 ±0.003 | 0.433 ±0.003  | 0.582 ±0.003     | 0.412 ±0.001     | 0.308 ±0.001      | 0.28 ±0.003  | 0.289 ±0.002 | 0.36 ±0.001  |
| unseen        | subfield | SSE-treeSC                        | 0.366 ±0.0   | 0.445 ±0.002  | 0.597 ±0.001     | 0.424 ±0.0       | 0.32 ±0.0         | 0.27 ±0.002  | 0.286 ±0.003 | 0.362 ±0.0   |
| seen_test     | subfield | SSE-tree                          | 0.312 ±0.001 | 0.379 ±0.001  | 0.552 ±0.0       | 0.379 ±0.0       | 0.276 ±0.0        | 0.186 ±0.003 | 0.25 ±0.001  | 0.318 ±0.001 |
| unseen        | subfield | SSE-tree                          | 0.357 ±0.002 | 0.436 ±0.002  | 0.592 ±0.001     | 0.412 ±0.001     | 0.31 ±0.001       | 0.192 ±0.003 | 0.256 ±0.001 | 0.354 ±0.001 |
| seen_test     | subfield | SSE (yes/no levels)               | 0.357 ±0.003 | 0.433 ±0.002  | 0.582 ±0.002     | 0.414 ±0.001     | 0.31 ±0.001       | 0.286 ±0.004 | 0.294 ±0.001 | 0.36 ±0.0    |
| unseen        | subfield | SSE (yes/no levels)               | 0.358 ±0.003 | 0.435 ±0.002  | 0.591 ±0.003     | 0.42 ±0.001      | 0.315 ±0.001      | 0.274 ±0.006 | 0.288 ±0.002 | 0.355 ±0.001 |
| seen_test     | subfield | SSE-MRL (finest level everywhere) | 0.359 ±0.002 | 0.436 ±0.003  | 0.583 ±0.002     | 0.415 ±0.001     | 0.311 ±0.001      | 0.291 ±0.001 | 0.29 ±0.001  | 0.362 ±0.001 |
| unseen        | subfield | SSE-MRL (finest level everywhere) | 0.358 ±0.003 | 0.435 ±0.002  | 0.589 ±0.003     | 0.42 ±0.001      | 0.315 ±0.001      | 0.274 ±0.002 | 0.288 ±0.003 | 0.356 ±0.001 |
| seen_test     | subfield | B3 separate (graded+contrastive)  | 0.36 ±0.003  | 0.436 ±0.003  | 0.583 ±0.002     | 0.413 ±0.001     | 0.31 ±0.001       | 0.289 ±0.004 | 0.292 ±0.0   | 0.361 ±0.001 |
| unseen        | subfield | B3 separate (graded+contrastive)  | 0.365 ±0.003 | 0.445 ±0.003  | 0.595 ±0.002     | 0.423 ±0.001     | 0.32 ±0.002       | 0.277 ±0.002 | 0.281 ±0.001 | 0.362 ±0.002 |
| seen_test     | subfield | B4 CSN (graded+contrastive)       | 0.356 ±0.001 | 0.433 ±0.002  | 0.581 ±0.001     | 0.411 ±0.001     | 0.308 ±0.001      | 0.282 ±0.002 | 0.29 ±0.001  | 0.359 ±0.002 |
| unseen        | subfield | B4 CSN (graded+contrastive)       | 0.366 ±0.002 | 0.446 ±0.002  | 0.598 ±0.001     | 0.424 ±0.001     | 0.32 ±0.001       | 0.27 ±0.003  | 0.283 ±0.002 | 0.361 ±0.001 |
| seen_test     | subfield | B1 labels                         | 0.199 ±0.006 | 0.247 ±0.008  | 0.426 ±0.006     | 0.32 ±0.007      | 0.212 ±0.006      | 0.143 ±0.0   | 0.259 ±0.001 | 0.207 ±0.007 |
| unseen        | subfield | B1 labels                         | 0.205 ±0.006 | 0.255 ±0.011  | 0.44 ±0.005      | 0.33 ±0.009      | 0.223 ±0.007      | 0.162 ±0.001 | 0.258 ±0.0   | 0.207 ±0.008 |
| seen_test     | subfield | Random (base rate)                | 0.009 ±0.0   | 0.012 ±0.0    | 0.109 ±0.0       | 0.073 ±0.0       | 0.021 ±0.0        | 0.018 ±0.0   | 0.0 ±0.0     | nan          |
| unseen        | subfield | Random (base rate)                | 0.01 ±0.0    | 0.013 ±0.0    | 0.112 ±0.0       | 0.075 ±0.0       | 0.022 ±0.0        | 0.019 ±0.0   | 0.0 ±0.0     | nan          |

### E8b — institution similarity (truth: cosine of research profiles)

| level    | method                            | Spearman     | NDCG@10      |
|:---------|:----------------------------------|:-------------|:-------------|
| domain   | B6 plain encoder                  | 0.626 ±0.0   | 0.938 ±0.0   |
| domain   | SSE-treeSC                        | 0.944 ±0.003 | 0.98 ±0.0    |
| domain   | SSE-tree                          | 0.95 ±0.001  | 0.979 ±0.0   |
| domain   | SSE (yes/no levels)               | 0.922 ±0.002 | 0.979 ±0.0   |
| domain   | SSE-MRL (finest level everywhere) | 0.783 ±0.015 | 0.957 ±0.001 |
| domain   | B3 separate (graded+contrastive)  | 0.945 ±0.001 | 0.98 ±0.0    |
| domain   | B4 CSN (graded+contrastive)       | 0.943 ±0.001 | 0.98 ±0.0    |
| domain   | B1 labels                         | 0.88 ±0.001  | 0.959 ±0.0   |
| field    | B6 plain encoder                  | 0.774 ±0.0   | 0.885 ±0.0   |
| field    | SSE-treeSC                        | 0.827 ±0.018 | 0.93 ±0.001  |
| field    | SSE-tree                          | 0.747 ±0.007 | 0.905 ±0.001 |
| field    | SSE (yes/no levels)               | 0.867 ±0.01  | 0.932 ±0.001 |
| field    | SSE-MRL (finest level everywhere) | 0.857 ±0.018 | 0.923 ±0.002 |
| field    | B3 separate (graded+contrastive)  | 0.828 ±0.007 | 0.929 ±0.001 |
| field    | B4 CSN (graded+contrastive)       | 0.824 ±0.006 | 0.929 ±0.0   |
| field    | B1 labels                         | 0.84 ±0.001  | 0.925 ±0.0   |
| subfield | B6 plain encoder                  | 0.789 ±0.0   | 0.777 ±0.0   |
| subfield | SSE-treeSC                        | 0.82 ±0.011  | 0.817 ±0.001 |
| subfield | SSE-tree                          | 0.752 ±0.004 | 0.79 ±0.002  |
| subfield | SSE (yes/no levels)               | 0.83 ±0.003  | 0.813 ±0.001 |
| subfield | SSE-MRL (finest level everywhere) | 0.819 ±0.011 | 0.814 ±0.001 |
| subfield | B3 separate (graded+contrastive)  | 0.825 ±0.005 | 0.818 ±0.002 |
| subfield | B4 CSN (graded+contrastive)       | 0.825 ±0.002 | 0.817 ±0.002 |
| subfield | B1 labels                         | 0.758 ±0.001 | 0.741 ±0.001 |

### E6 — roll-up / drill-down inside Physical Sciences

| policy    | level    | method                           | ARI          | NMI          | n_main_groups   | coverage     |
|:----------|:---------|:---------------------------------|:-------------|:-------------|:----------------|:-------------|
| connected | field    | B6 plain encoder                 | 0.022 ±0.0   | 0.372 ±0.0   | 1.0 ±0.0        | 0.288 ±0.0   |
| connected | subfield | B6 plain encoder                 | 0.045 ±0.0   | 0.569 ±0.0   | 1.0 ±0.0        | 0.288 ±0.0   |
| connected | field    | SSE-treeSC                       | 0.062 ±0.023 | 0.396 ±0.016 | 3.0 ±1.0        | 0.257 ±0.023 |
| connected | subfield | SSE-treeSC                       | 0.073 ±0.02  | 0.61 ±0.007  | 4.333 ±1.0      | 0.212 ±0.005 |
| connected | field    | SSE-tree                         | 0.029 ±0.003 | 0.348 ±0.003 | 1.0 ±0.0        | 0.429 ±0.01  |
| connected | subfield | SSE-tree                         | 0.053 ±0.004 | 0.605 ±0.003 | 1.667 ±0.5      | 0.183 ±0.003 |
| connected | field    | SSE (yes/no levels)              | 0.064 ±0.043 | 0.383 ±0.045 | 3.0 ±1.5        | 0.332 ±0.128 |
| connected | subfield | SSE (yes/no levels)              | 0.09 ±0.018  | 0.614 ±0.003 | 5.667 ±0.5      | 0.233 ±0.044 |
| connected | field    | B3 separate (graded+contrastive) | 0.041 ±0.011 | 0.369 ±0.011 | 1.667 ±0.5      | 0.344 ±0.034 |
| connected | subfield | B3 separate (graded+contrastive) | 0.063 ±0.024 | 0.601 ±0.012 | 4.0 ±2.0        | 0.237 ±0.026 |
| connected | field    | B4 CSN (graded+contrastive)      | 0.03 ±0.003  | 0.359 ±0.004 | 1.0 ±0.0        | 0.365 ±0.019 |
| connected | subfield | B4 CSN (graded+contrastive)      | 0.057 ±0.027 | 0.591 ±0.023 | 4.0 ±2.5        | 0.272 ±0.023 |
| center    | field    | B6 plain encoder                 | 0.044 ±0.0   | 0.339 ±0.0   | 15.0 ±0.0       | 0.504 ±0.0   |
| center    | subfield | B6 plain encoder                 | 0.046 ±0.0   | 0.597 ±0.0   | 2.0 ±0.0        | 0.063 ±0.0   |
| center    | field    | SSE-treeSC                       | 0.22 ±0.014  | 0.429 ±0.004 | 14.0 ±1.5       | 0.706 ±0.047 |
| center    | subfield | SSE-treeSC                       | 0.158 ±0.008 | 0.581 ±0.008 | 14.333 ±0.5     | 0.35 ±0.044  |
| center    | field    | SSE-tree                         | 0.084 ±0.014 | 0.358 ±0.016 | 10.0 ±2.0       | 0.523 ±0.041 |
| center    | subfield | SSE-tree                         | 0.08 ±0.007  | 0.585 ±0.014 | 7.0 ±1.0        | 0.189 ±0.046 |
| center    | field    | SSE (yes/no levels)              | 0.295 ±0.012 | 0.454 ±0.004 | 12.333 ±0.5     | 0.739 ±0.043 |
| center    | subfield | SSE (yes/no levels)              | 0.173 ±0.004 | 0.575 ±0.015 | 14.333 ±1.5     | 0.385 ±0.065 |
| center    | field    | B3 separate (graded+contrastive) | 0.241 ±0.022 | 0.433 ±0.007 | 13.333 ±0.5     | 0.673 ±0.042 |
| center    | subfield | B3 separate (graded+contrastive) | 0.16 ±0.009  | 0.58 ±0.013  | 13.0 ±2.0       | 0.355 ±0.036 |
| center    | field    | B4 CSN (graded+contrastive)      | 0.224 ±0.007 | 0.428 ±0.003 | 11.667 ±1.5     | 0.68 ±0.021  |
| center    | subfield | B4 CSN (graded+contrastive)      | 0.153 ±0.002 | 0.595 ±0.005 | 13.333 ±2.5     | 0.295 ±0.014 |
