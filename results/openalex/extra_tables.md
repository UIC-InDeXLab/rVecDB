### e9_joinkeys (3 seeds)

| method                         | split     | level    | P@10         | credit_text@10   | credit_coact@10   |
|:-------------------------------|:----------|:---------|:-------------|:-----------------|:------------------|
| SSE aligned                    | seen_test | domain   | 0.808 ±0.016 | nan              | nan               |
| SSE independent                | seen_test | domain   | 0.198 ±0.035 | nan              | nan               |
| B1 labels                      | seen_test | domain   | 0.697 ±0.013 | nan              | nan               |
| Raw encoders (SPECTER2 vs bge) | seen_test | domain   | 0.295 ±0.003 | nan              | nan               |
| Random                         | seen_test | domain   | 0.276 ±0.001 | nan              | nan               |
| SSE aligned                    | seen_test | field    | 0.471 ±0.011 | nan              | nan               |
| SSE independent                | seen_test | field    | 0.038 ±0.016 | nan              | nan               |
| B1 labels                      | seen_test | field    | 0.406 ±0.005 | nan              | nan               |
| Raw encoders (SPECTER2 vs bge) | seen_test | field    | 0.042 ±0.005 | nan              | nan               |
| Random                         | seen_test | field    | 0.038 ±0.002 | nan              | nan               |
| SSE aligned                    | seen_test | subfield | 0.242 ±0.011 | 0.349 ±0.006     | 0.239 ±0.007      |
| SSE independent                | seen_test | subfield | 0.008 ±0.004 | 0.078 ±0.011     | 0.023 ±0.005      |
| B1 labels                      | seen_test | subfield | 0.178 ±0.002 | 0.257 ±0.004     | 0.164 ±0.003      |
| Raw encoders (SPECTER2 vs bge) | seen_test | subfield | 0.009 ±0.001 | 0.078 ±0.001     | 0.024 ±0.000      |
| Random                         | seen_test | subfield | 0.008 ±0.001 | 0.072 ±0.000     | 0.020 ±0.000      |
| SSE aligned                    | unseen    | domain   | 0.798 ±0.005 | nan              | nan               |
| SSE independent                | unseen    | domain   | 0.192 ±0.039 | nan              | nan               |
| B1 labels                      | unseen    | domain   | 0.671 ±0.006 | nan              | nan               |
| Raw encoders (SPECTER2 vs bge) | unseen    | domain   | 0.312 ±0.001 | nan              | nan               |
| Random                         | unseen    | domain   | 0.279 ±0.006 | nan              | nan               |
| SSE aligned                    | unseen    | field    | 0.489 ±0.013 | nan              | nan               |
| SSE independent                | unseen    | field    | 0.035 ±0.012 | nan              | nan               |
| B1 labels                      | unseen    | field    | 0.410 ±0.015 | nan              | nan               |
| Raw encoders (SPECTER2 vs bge) | unseen    | field    | 0.046 ±0.003 | nan              | nan               |
| Random                         | unseen    | field    | 0.042 ±0.002 | nan              | nan               |
| SSE aligned                    | unseen    | subfield | 0.255 ±0.008 | 0.356 ±0.003     | 0.246 ±0.004      |
| SSE independent                | unseen    | subfield | 0.009 ±0.005 | 0.077 ±0.011     | 0.023 ±0.006      |
| B1 labels                      | unseen    | subfield | 0.182 ±0.007 | 0.266 ±0.003     | 0.171 ±0.004      |
| Raw encoders (SPECTER2 vs bge) | unseen    | subfield | 0.010 ±0.003 | 0.084 ±0.002     | 0.026 ±0.002      |
| Random                         | unseen    | subfield | 0.009 ±0.000 | 0.075 ±0.001     | 0.021 ±0.000      |

### e10_sweep (3 seeds)

| method               | level    |    tau | out_per_paper    | precision    | recall       | F1           |
|:---------------------|:---------|-------:|:-----------------|:-------------|:-------------|:-------------|
| SSE aligned          | domain   |   0    | 1394.879 ±9.285  | 0.307 ±0.001 | 0.999 ±0.000 | 0.469 ±0.001 |
| SSE aligned          | domain   |   0.05 | 1323.753 ±8.738  | 0.323 ±0.001 | 0.998 ±0.001 | 0.488 ±0.001 |
| SSE aligned          | domain   |   0.1  | 1241.762 ±10.324 | 0.343 ±0.001 | 0.996 ±0.001 | 0.511 ±0.001 |
| SSE aligned          | domain   |   0.15 | 1154.064 ±13.521 | 0.369 ±0.002 | 0.994 ±0.002 | 0.538 ±0.002 |
| SSE aligned          | domain   |   0.2  | 1065.677 ±17.081 | 0.397 ±0.004 | 0.989 ±0.001 | 0.567 ±0.004 |
| SSE aligned          | domain   |   0.25 | 980.323 ±19.820  | 0.429 ±0.006 | 0.983 ±0.001 | 0.598 ±0.005 |
| SSE aligned          | domain   |   0.3  | 899.783 ±20.457  | 0.463 ±0.007 | 0.974 ±0.001 | 0.628 ±0.006 |
| SSE aligned          | domain   |   0.35 | 824.436 ±20.244  | 0.499 ±0.009 | 0.961 ±0.002 | 0.657 ±0.008 |
| SSE aligned          | domain   |   0.4  | 754.504 ±19.885  | 0.536 ±0.010 | 0.944 ±0.002 | 0.683 ±0.008 |
| SSE aligned          | domain   |   0.45 | 688.945 ±19.058  | 0.573 ±0.011 | 0.922 ±0.003 | 0.707 ±0.008 |
| SSE aligned          | domain   |   0.5  | 626.819 ±17.386  | 0.611 ±0.012 | 0.894 ±0.003 | 0.726 ±0.008 |
| SSE aligned          | domain   |   0.55 | 567.631 ±14.615  | 0.649 ±0.012 | 0.860 ±0.003 | 0.739 ±0.008 |
| SSE aligned          | domain   |   0.6  | 509.949 ±10.853  | 0.688 ±0.012 | 0.819 ±0.005 | 0.747 ±0.008 |
| SSE aligned          | domain   |   0.65 | 451.675 ±7.309   | 0.728 ±0.011 | 0.768 ±0.006 | 0.747 ±0.008 |
| SSE aligned          | domain   |   0.7  | 391.066 ±4.252   | 0.770 ±0.011 | 0.704 ±0.009 | 0.735 ±0.010 |
| SSE aligned          | domain   |   0.75 | 325.493 ±4.744   | 0.816 ±0.011 | 0.621 ±0.013 | 0.705 ±0.012 |
| SSE aligned          | domain   |   0.8  | 254.108 ±6.812   | 0.869 ±0.010 | 0.516 ±0.014 | 0.648 ±0.014 |
| SSE aligned          | domain   |   0.85 | 179.587 ±7.828   | 0.928 ±0.008 | 0.389 ±0.018 | 0.548 ±0.018 |
| SSE aligned          | domain   |   0.9  | 103.913 ±7.798   | 0.976 ±0.002 | 0.237 ±0.018 | 0.381 ±0.023 |
| SSE aligned          | domain   |   0.95 | 20.603 ±3.890    | 0.994 ±0.003 | 0.048 ±0.009 | 0.091 ±0.017 |
| B1 labels (equality) | domain   | nan    | 434.122 ±9.216   | 0.715 ±0.017 | 0.724 ±0.006 | 0.719 ±0.011 |
| SSE aligned          | field    |   0    | 1368.428 ±6.197  | 0.042 ±0.001 | 0.998 ±0.001 | 0.081 ±0.002 |
| SSE aligned          | field    |   0.05 | 1250.756 ±10.175 | 0.046 ±0.001 | 0.996 ±0.002 | 0.088 ±0.002 |
| SSE aligned          | field    |   0.1  | 1113.035 ±13.684 | 0.052 ±0.001 | 0.993 ±0.004 | 0.098 ±0.002 |
| SSE aligned          | field    |   0.15 | 970.851 ±15.356  | 0.059 ±0.002 | 0.987 ±0.005 | 0.111 ±0.003 |
| SSE aligned          | field    |   0.2  | 835.358 ±13.584  | 0.068 ±0.002 | 0.977 ±0.005 | 0.126 ±0.003 |
| SSE aligned          | field    |   0.25 | 711.616 ±9.231   | 0.078 ±0.002 | 0.961 ±0.006 | 0.144 ±0.003 |
| SSE aligned          | field    |   0.3  | 598.904 ±4.331   | 0.091 ±0.002 | 0.938 ±0.004 | 0.165 ±0.003 |
| SSE aligned          | field    |   0.35 | 496.133 ±3.643   | 0.105 ±0.002 | 0.905 ±0.003 | 0.189 ±0.004 |
| SSE aligned          | field    |   0.4  | 403.156 ±6.198   | 0.123 ±0.002 | 0.859 ±0.001 | 0.216 ±0.003 |
| SSE aligned          | field    |   0.45 | 319.659 ±7.745   | 0.145 ±0.002 | 0.801 ±0.004 | 0.245 ±0.003 |
| SSE aligned          | field    |   0.5  | 246.591 ±8.607   | 0.170 ±0.003 | 0.726 ±0.008 | 0.276 ±0.003 |
| SSE aligned          | field    |   0.55 | 183.384 ±8.284   | 0.200 ±0.003 | 0.633 ±0.013 | 0.303 ±0.002 |
| SSE aligned          | field    |   0.6  | 129.634 ±7.122   | 0.234 ±0.004 | 0.524 ±0.014 | 0.323 ±0.001 |
| SSE aligned          | field    |   0.65 | 85.286 ±5.275    | 0.275 ±0.006 | 0.405 ±0.013 | 0.327 ±0.002 |
| SSE aligned          | field    |   0.7  | 50.179 ±3.589    | 0.326 ±0.007 | 0.282 ±0.013 | 0.302 ±0.007 |
| SSE aligned          | field    |   0.75 | 25.260 ±1.949    | 0.390 ±0.007 | 0.170 ±0.011 | 0.237 ±0.011 |
| SSE aligned          | field    |   0.8  | 9.633 ±1.088     | 0.466 ±0.008 | 0.078 ±0.009 | 0.133 ±0.013 |
| SSE aligned          | field    |   0.85 | 2.098 ±0.413     | 0.574 ±0.018 | 0.021 ±0.005 | 0.040 ±0.009 |
| SSE aligned          | field    |   0.9  | 0.082 ±0.049     | 0.771 ±0.049 | 0.001 ±0.001 | 0.002 ±0.001 |
| SSE aligned          | field    |   0.95 | 0.000 ±0.000     | 0.000 ±0.000 | 0.000 ±0.000 | 0.000 ±0.000 |
| B1 labels (equality) | field    | nan    | 50.789 ±0.857    | 0.442 ±0.005 | 0.388 ±0.002 | 0.414 ±0.003 |
| SSE aligned          | subfield |   0    | 1212.425 ±17.911 | 0.010 ±0.000 | 0.999 ±0.001 | 0.020 ±0.001 |
| SSE aligned          | subfield |   0.05 | 1040.927 ±18.199 | 0.012 ±0.000 | 0.997 ±0.002 | 0.024 ±0.001 |
| SSE aligned          | subfield |   0.1  | 869.705 ±15.221  | 0.014 ±0.000 | 0.994 ±0.003 | 0.028 ±0.001 |
| SSE aligned          | subfield |   0.15 | 714.825 ±11.066  | 0.017 ±0.000 | 0.990 ±0.004 | 0.034 ±0.001 |
| SSE aligned          | subfield |   0.2  | 580.906 ±8.293   | 0.021 ±0.000 | 0.982 ±0.006 | 0.041 ±0.001 |
| SSE aligned          | subfield |   0.25 | 466.182 ±8.323   | 0.026 ±0.000 | 0.969 ±0.008 | 0.051 ±0.001 |
| SSE aligned          | subfield |   0.3  | 367.874 ±9.387   | 0.032 ±0.000 | 0.947 ±0.009 | 0.062 ±0.001 |
| SSE aligned          | subfield |   0.35 | 284.187 ±9.290   | 0.040 ±0.001 | 0.916 ±0.006 | 0.077 ±0.001 |
| SSE aligned          | subfield |   0.4  | 213.853 ±8.397   | 0.051 ±0.001 | 0.865 ±0.005 | 0.096 ±0.002 |
| SSE aligned          | subfield |   0.45 | 155.367 ±7.441   | 0.065 ±0.002 | 0.800 ±0.006 | 0.120 ±0.003 |
| SSE aligned          | subfield |   0.5  | 107.717 ±6.099   | 0.083 ±0.003 | 0.717 ±0.012 | 0.150 ±0.004 |
| SSE aligned          | subfield |   0.55 | 70.428 ±4.552    | 0.109 ±0.004 | 0.609 ±0.013 | 0.184 ±0.005 |
| SSE aligned          | subfield |   0.6  | 42.722 ±3.120    | 0.142 ±0.006 | 0.484 ±0.013 | 0.220 ±0.007 |
| SSE aligned          | subfield |   0.65 | 23.334 ±1.855    | 0.188 ±0.009 | 0.349 ±0.014 | 0.244 ±0.009 |
| SSE aligned          | subfield |   0.7  | 11.113 ±1.109    | 0.251 ±0.018 | 0.222 ±0.018 | 0.235 ±0.013 |
| SSE aligned          | subfield |   0.75 | 4.286 ±0.550     | 0.336 ±0.028 | 0.115 ±0.012 | 0.171 ±0.015 |
| SSE aligned          | subfield |   0.8  | 1.150 ±0.223     | 0.461 ±0.053 | 0.042 ±0.008 | 0.077 ±0.014 |
| SSE aligned          | subfield |   0.85 | 0.144 ±0.045     | 0.622 ±0.103 | 0.007 ±0.003 | 0.014 ±0.005 |
| SSE aligned          | subfield |   0.9  | 0.004 ±0.004     | 0.667 ±0.500 | 0.000 ±0.000 | 0.001 ±0.001 |
| SSE aligned          | subfield |   0.95 | 0.000 ±0.000     | 0.000 ±0.000 | 0.000 ±0.000 | 0.000 ±0.000 |
| B1 labels (equality) | subfield | nan    | 25.241 ±0.166    | 0.169 ±0.012 | 0.341 ±0.023 | 0.226 ±0.015 |

### e11_groupk (3 seeds)

| part          | method                           | level    |   k/true | k              | NMI          | ARI          |
|:--------------|:---------------------------------|:---------|---------:|:---------------|:-------------|:-------------|
| impact of k   | B6 plain encoder                 | field    |     0.25 | 6.000 ±0.000   | 0.366 ±0.015 | 0.145 ±0.004 |
| impact of k   | SSE-treeSC                       | field    |     0.25 | 6.000 ±0.000   | 0.434 ±0.003 | 0.184 ±0.003 |
| impact of k   | B3 separate (graded+contrastive) | field    |     0.25 | 6.000 ±0.000   | 0.434 ±0.001 | 0.184 ±0.003 |
| impact of k   | B4 CSN (graded+contrastive)      | field    |     0.25 | 6.000 ±0.000   | 0.433 ±0.001 | 0.183 ±0.003 |
| impact of k   | B1 labels (fixed groups)         | field    |   nan    | 26.000 ±0.000  | 0.522 ±0.000 | 0.365 ±0.000 |
| impact of k   | B6 plain encoder                 | field    |     0.5  | 13.000 ±0.000  | 0.452 ±0.005 | 0.239 ±0.003 |
| impact of k   | SSE-treeSC                       | field    |     0.5  | 13.000 ±0.000  | 0.541 ±0.003 | 0.337 ±0.008 |
| impact of k   | B3 separate (graded+contrastive) | field    |     0.5  | 13.000 ±0.000  | 0.542 ±0.003 | 0.339 ±0.003 |
| impact of k   | B4 CSN (graded+contrastive)      | field    |     0.5  | 13.000 ±0.000  | 0.539 ±0.002 | 0.334 ±0.008 |
| impact of k   | B6 plain encoder                 | field    |     1    | 26.000 ±0.000  | 0.476 ±0.004 | 0.262 ±0.015 |
| impact of k   | SSE-treeSC                       | field    |     1    | 26.000 ±0.000  | 0.584 ±0.001 | 0.439 ±0.006 |
| impact of k   | B3 separate (graded+contrastive) | field    |     1    | 26.000 ±0.000  | 0.583 ±0.001 | 0.436 ±0.008 |
| impact of k   | B4 CSN (graded+contrastive)      | field    |     1    | 26.000 ±0.000  | 0.582 ±0.001 | 0.438 ±0.005 |
| impact of k   | B6 plain encoder                 | field    |     2    | 52.000 ±0.000  | 0.493 ±0.002 | 0.234 ±0.004 |
| impact of k   | SSE-treeSC                       | field    |     2    | 52.000 ±0.000  | 0.571 ±0.001 | 0.361 ±0.002 |
| impact of k   | B3 separate (graded+contrastive) | field    |     2    | 52.000 ±0.000  | 0.569 ±0.002 | 0.363 ±0.013 |
| impact of k   | B4 CSN (graded+contrastive)      | field    |     2    | 52.000 ±0.000  | 0.568 ±0.000 | 0.353 ±0.005 |
| impact of k   | B6 plain encoder                 | field    |     4    | 104.000 ±0.000 | 0.493 ±0.001 | 0.172 ±0.002 |
| impact of k   | SSE-treeSC                       | field    |     4    | 104.000 ±0.000 | 0.547 ±0.001 | 0.229 ±0.002 |
| impact of k   | B3 separate (graded+contrastive) | field    |     4    | 104.000 ±0.000 | 0.547 ±0.001 | 0.234 ±0.011 |
| impact of k   | B4 CSN (graded+contrastive)      | field    |     4    | 104.000 ±0.000 | 0.547 ±0.002 | 0.227 ±0.007 |
| impact of k   | B6 plain encoder                 | subfield |     0.25 | 61.000 ±0.000  | 0.540 ±0.004 | 0.229 ±0.001 |
| impact of k   | SSE-treeSC                       | subfield |     0.25 | 61.000 ±0.000  | 0.591 ±0.002 | 0.311 ±0.025 |
| impact of k   | B3 separate (graded+contrastive) | subfield |     0.25 | 61.000 ±0.000  | 0.591 ±0.000 | 0.298 ±0.009 |
| impact of k   | B4 CSN (graded+contrastive)      | subfield |     0.25 | 61.000 ±0.000  | 0.590 ±0.001 | 0.300 ±0.008 |
| impact of k   | B1 labels (fixed groups)         | subfield |   nan    | 67.333 ±0.500  | 0.467 ±0.000 | 0.150 ±0.000 |
| impact of k   | B6 plain encoder                 | subfield |     0.5  | 122.000 ±0.000 | 0.569 ±0.000 | 0.225 ±0.008 |
| impact of k   | SSE-treeSC                       | subfield |     0.5  | 122.000 ±0.000 | 0.608 ±0.002 | 0.274 ±0.005 |
| impact of k   | B3 separate (graded+contrastive) | subfield |     0.5  | 122.000 ±0.000 | 0.610 ±0.003 | 0.287 ±0.013 |
| impact of k   | B4 CSN (graded+contrastive)      | subfield |     0.5  | 122.000 ±0.000 | 0.607 ±0.001 | 0.277 ±0.004 |
| impact of k   | B6 plain encoder                 | subfield |     1    | 243.000 ±0.000 | 0.586 ±0.002 | 0.175 ±0.002 |
| impact of k   | SSE-treeSC                       | subfield |     1    | 243.000 ±0.000 | 0.616 ±0.001 | 0.214 ±0.005 |
| impact of k   | B3 separate (graded+contrastive) | subfield |     1    | 243.000 ±0.000 | 0.616 ±0.001 | 0.212 ±0.002 |
| impact of k   | B4 CSN (graded+contrastive)      | subfield |     1    | 243.000 ±0.000 | 0.616 ±0.000 | 0.207 ±0.006 |
| impact of k   | B6 plain encoder                 | subfield |     2    | 486.000 ±0.000 | 0.597 ±0.000 | 0.124 ±0.002 |
| impact of k   | SSE-treeSC                       | subfield |     2    | 486.000 ±0.000 | 0.619 ±0.001 | 0.147 ±0.005 |
| impact of k   | B3 separate (graded+contrastive) | subfield |     2    | 486.000 ±0.000 | 0.620 ±0.002 | 0.146 ±0.005 |
| impact of k   | B4 CSN (graded+contrastive)      | subfield |     2    | 486.000 ±0.000 | 0.618 ±0.000 | 0.138 ±0.005 |
| impact of k   | B6 plain encoder                 | subfield |     4    | 972.000 ±0.000 | 0.604 ±0.002 | 0.082 ±0.002 |
| impact of k   | SSE-treeSC                       | subfield |     4    | 972.000 ±0.000 | 0.621 ±0.001 | 0.091 ±0.003 |
| impact of k   | B3 separate (graded+contrastive) | subfield |     4    | 972.000 ±0.000 | 0.622 ±0.000 | 0.093 ±0.001 |
| impact of k   | B4 CSN (graded+contrastive)      | subfield |     4    | 972.000 ±0.000 | 0.621 ±0.001 | 0.089 ±0.002 |
| roll-up       | B6 plain encoder                 | domain   |     1    | 4.000 ±0.000   | 0.366 ±0.001 | 0.325 ±0.004 |
| roll-up       | B6 plain encoder                 | field    |     1    | 26.000 ±0.000  | 0.451 ±0.003 | 0.239 ±0.008 |
| roll-up       | B6 plain encoder                 | subfield |     1    | 243.000 ±0.000 | 0.552 ±0.000 | 0.147 ±0.002 |
| roll-up       | SSE-treeSC                       | domain   |     1    | 4.000 ±0.000   | 0.578 ±0.001 | 0.651 ±0.001 |
| roll-up       | SSE-treeSC                       | field    |     1    | 26.000 ±0.000  | 0.566 ±0.002 | 0.422 ±0.003 |
| roll-up       | SSE-treeSC                       | subfield |     1    | 243.000 ±0.000 | 0.592 ±0.001 | 0.189 ±0.004 |
| roll-up       | B3 separate (graded+contrastive) | domain   |     1    | 4.000 ±0.000   | 0.580 ±0.004 | 0.652 ±0.004 |
| roll-up       | B3 separate (graded+contrastive) | field    |     1    | 26.000 ±0.000  | 0.566 ±0.001 | 0.421 ±0.006 |
| roll-up       | B3 separate (graded+contrastive) | subfield |     1    | 243.000 ±0.000 | 0.594 ±0.000 | 0.196 ±0.002 |
| roll-up       | B4 CSN (graded+contrastive)      | domain   |     1    | 4.000 ±0.000   | 0.579 ±0.002 | 0.651 ±0.004 |
| roll-up       | B4 CSN (graded+contrastive)      | field    |     1    | 26.000 ±0.000  | 0.567 ±0.001 | 0.423 ±0.001 |
| roll-up       | B4 CSN (graded+contrastive)      | subfield |     1    | 243.000 ±0.000 | 0.593 ±0.001 | 0.188 ±0.002 |
| roll-up       | B1 labels (fixed groups)         | domain   |   nan    | 4.000 ±0.000   | 0.441 ±0.000 | 0.501 ±0.000 |
| roll-up       | B1 labels (fixed groups)         | field    |   nan    | 26.000 ±0.000  | 0.522 ±0.000 | 0.365 ±0.000 |
| roll-up       | B1 labels (fixed groups)         | subfield |   nan    | 67.333 ±0.500  | 0.467 ±0.000 | 0.150 ±0.000 |
| unseen topics | B6 plain encoder                 | subfield |     1    | 182.000 ±0.000 | 0.697 ±0.004 | 0.294 ±0.005 |
| unseen topics | SSE-treeSC                       | subfield |     1    | 182.000 ±0.000 | 0.686 ±0.003 | 0.300 ±0.013 |
| unseen topics | B3 separate (graded+contrastive) | subfield |     1    | 182.000 ±0.000 | 0.687 ±0.003 | 0.298 ±0.013 |
| unseen topics | B4 CSN (graded+contrastive)      | subfield |     1    | 182.000 ±0.000 | 0.689 ±0.003 | 0.297 ±0.010 |
| unseen topics | B1 labels (fixed groups)         | subfield |   nan    | 57.000 ±1.000  | 0.511 ±0.001 | 0.205 ±0.001 |
