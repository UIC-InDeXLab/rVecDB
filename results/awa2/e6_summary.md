# E6 — GROUP BY and roll-up/drill-down, mean over 3 seeds

Policy 'connected' = paper's range-connected components (can chain); 'center' = center-based ranges (no chaining).
Main groups = groups with >= 1% of items. Coverage = share of items in main groups. kappa tuned on training images.

| grouping | policy | method | NMI | ± | ARI | main groups | coverage |
|---|---|---|---|---|---|---|---|
| habitat | center | B3 separate | 0.511 | 0.014 | 0.445 | 4.7 | 0.98 |
| habitat | center | B4 CSN | 0.583 | 0.113 | 0.562 | 8.0 | 0.97 |
| habitat | center | B6 plain CLIP | 0.392 | 0.000 | 0.096 | 22.0 | 0.58 |
| habitat | center | SSE | 0.500 | 0.017 | 0.451 | 5.0 | 0.98 |
| habitat | connected | B3 separate | 0.326 | 0.254 | 0.246 | 3.3 | 0.98 |
| habitat | connected | B4 CSN | 0.517 | 0.292 | 0.483 | 8.0 | 0.97 |
| habitat | connected | B6 plain CLIP | 0.402 | 0.000 | 0.136 | 19.0 | 0.70 |
| habitat | connected | SSE | 0.168 | 0.000 | 0.062 | 2.0 | 0.98 |
| nested family | center | B3 separate | 0.881 | 0.005 | 0.853 | 19.0 | 0.87 |
| nested family | center | B4 CSN | 0.894 | 0.001 | 0.899 | 20.0 | 0.88 |
| nested family | center | B6 plain CLIP | 0.732 | 0.000 | 0.529 | 20.0 | 0.66 |
| nested family | center | SSE | 0.877 | 0.010 | 0.873 | 20.0 | 0.85 |
| nested family | connected | B3 separate | 0.853 | 0.010 | 0.731 | 15.7 | 0.91 |
| nested family | connected | B4 CSN | 0.851 | 0.016 | 0.713 | 14.0 | 0.94 |
| nested family | connected | B6 plain CLIP | 0.726 | 0.000 | 0.551 | 19.0 | 0.70 |
| nested family | connected | SSE | 0.852 | 0.012 | 0.724 | 15.7 | 0.92 |
| nested genus | center | B3 separate | 0.863 | 0.006 | 0.781 | 22.3 | 0.73 |
| nested genus | center | B4 CSN | 0.865 | 0.012 | 0.783 | 23.7 | 0.77 |
| nested genus | center | B6 plain CLIP | 0.747 | 0.000 | 0.573 | 14.0 | 0.47 |
| nested genus | center | SSE | 0.839 | 0.004 | 0.726 | 24.0 | 0.71 |
| nested genus | connected | B3 separate | 0.882 | 0.011 | 0.837 | 23.0 | 0.85 |
| nested genus | connected | B4 CSN | 0.872 | 0.003 | 0.823 | 23.0 | 0.84 |
| nested genus | connected | B6 plain CLIP | 0.776 | 0.000 | 0.695 | 19.0 | 0.70 |
| nested genus | connected | SSE | 0.859 | 0.012 | 0.792 | 22.7 | 0.85 |
| nested order | center | B3 separate | 0.845 | 0.002 | 0.880 | 8.7 | 0.95 |
| nested order | center | B4 CSN | 0.862 | 0.008 | 0.891 | 8.3 | 0.95 |
| nested order | center | B6 plain CLIP | 0.495 | 0.000 | 0.142 | 20.0 | 0.66 |
| nested order | center | SSE | 0.842 | 0.001 | 0.871 | 8.7 | 0.95 |
| nested order | connected | B3 separate | 0.805 | 0.023 | 0.853 | 9.0 | 0.93 |
| nested order | connected | B4 CSN | 0.820 | 0.006 | 0.869 | 7.0 | 0.96 |
| nested order | connected | B6 plain CLIP | 0.486 | 0.000 | 0.153 | 19.0 | 0.70 |
| nested order | connected | SSE | 0.851 | 0.045 | 0.887 | 8.3 | 0.95 |
