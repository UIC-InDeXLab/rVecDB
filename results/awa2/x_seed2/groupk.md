### GROUP BY_k on AwA2 (6000 test images)

| part | method | level | k | k_true | NMI | ARI |
|---|---|---|---|---|---|---|
| habitat, impact of k | SSE | habitat | 2 | 4 | 0.483 | 0.390 |
| habitat, impact of k | SSE-treeSC | habitat | 2 | 4 | 0.485 | 0.391 |
| habitat, impact of k | B3 separate | habitat | 2 | 4 | 0.491 | 0.377 |
| habitat, impact of k | B4 CSN | habitat | 2 | 4 | 0.491 | 0.399 |
| habitat, impact of k | B6 plain CLIP | habitat | 2 | 4 | 0.400 | 0.314 |
| habitat, impact of k | SSE | habitat | 3 | 4 | 0.703 | 0.759 |
| habitat, impact of k | SSE-treeSC | habitat | 3 | 4 | 0.705 | 0.761 |
| habitat, impact of k | B3 separate | habitat | 3 | 4 | 0.679 | 0.728 |
| habitat, impact of k | B4 CSN | habitat | 3 | 4 | 0.702 | 0.755 |
| habitat, impact of k | B6 plain CLIP | habitat | 3 | 4 | 0.532 | 0.497 |
| habitat, impact of k | SSE | habitat | 4 | 4 | 0.710 | 0.740 |
| habitat, impact of k | SSE-treeSC | habitat | 4 | 4 | 0.711 | 0.741 |
| habitat, impact of k | B3 separate | habitat | 4 | 4 | 0.611 | 0.649 |
| habitat, impact of k | B4 CSN | habitat | 4 | 4 | 0.618 | 0.653 |
| habitat, impact of k | B6 plain CLIP | habitat | 4 | 4 | 0.483 | 0.375 |
| habitat, impact of k | SSE | habitat | 6 | 4 | 0.661 | 0.692 |
| habitat, impact of k | SSE-treeSC | habitat | 6 | 4 | 0.661 | 0.692 |
| habitat, impact of k | B3 separate | habitat | 6 | 4 | 0.692 | 0.733 |
| habitat, impact of k | B4 CSN | habitat | 6 | 4 | 0.668 | 0.699 |
| habitat, impact of k | B6 plain CLIP | habitat | 6 | 4 | 0.519 | 0.348 |
| habitat, impact of k | SSE | habitat | 8 | 4 | 0.662 | 0.497 |
| habitat, impact of k | SSE-treeSC | habitat | 8 | 4 | 0.615 | 0.439 |
| habitat, impact of k | B3 separate | habitat | 8 | 4 | 0.613 | 0.427 |
| habitat, impact of k | B4 CSN | habitat | 8 | 4 | 0.614 | 0.418 |
| habitat, impact of k | B6 plain CLIP | habitat | 8 | 4 | 0.559 | 0.347 |
| habitat, impact of k | SSE | habitat | 12 | 4 | 0.637 | 0.429 |
| habitat, impact of k | SSE-treeSC | habitat | 12 | 4 | 0.637 | 0.429 |
| habitat, impact of k | B3 separate | habitat | 12 | 4 | 0.654 | 0.443 |
| habitat, impact of k | B4 CSN | habitat | 12 | 4 | 0.626 | 0.422 |
| habitat, impact of k | B6 plain CLIP | habitat | 12 | 4 | 0.519 | 0.261 |
| habitat, impact of k | SSE | habitat | 16 | 4 | 0.615 | 0.341 |
| habitat, impact of k | SSE-treeSC | habitat | 16 | 4 | 0.615 | 0.341 |
| habitat, impact of k | B3 separate | habitat | 16 | 4 | 0.610 | 0.338 |
| habitat, impact of k | B4 CSN | habitat | 16 | 4 | 0.552 | 0.268 |
| habitat, impact of k | B6 plain CLIP | habitat | 16 | 4 | 0.514 | 0.224 |
| habitat, impact of k | B1 labels (predicted yes/no pattern) | habitat | 27 | 4 | 0.413 | 0.168 |
| roll-up / drill-down | SSE | order | 10 | 10 | 0.773 | 0.645 |
| roll-up / drill-down | SSE | family | 27 | 27 | 0.882 | 0.728 |
| roll-up / drill-down | SSE | genus | 40 | 40 | 0.862 | 0.612 |
| roll-up / drill-down | SSE-treeSC | order | 10 | 10 | 0.773 | 0.651 |
| roll-up / drill-down | SSE-treeSC | family | 27 | 27 | 0.865 | 0.665 |
| roll-up / drill-down | SSE-treeSC | genus | 40 | 40 | 0.857 | 0.631 |
| roll-up / drill-down | B3 separate | order | 10 | 10 | 0.817 | 0.695 |
| roll-up / drill-down | B3 separate | family | 27 | 27 | 0.871 | 0.700 |
| roll-up / drill-down | B3 separate | genus | 40 | 40 | 0.876 | 0.685 |
| roll-up / drill-down | B4 CSN | order | 10 | 10 | 0.806 | 0.686 |
| roll-up / drill-down | B4 CSN | family | 27 | 27 | 0.886 | 0.742 |
| roll-up / drill-down | B4 CSN | genus | 40 | 40 | 0.888 | 0.714 |
| roll-up / drill-down | B6 plain CLIP | order | 10 | 10 | 0.554 | 0.265 |
| roll-up / drill-down | B6 plain CLIP | family | 27 | 27 | 0.809 | 0.584 |
| roll-up / drill-down | B6 plain CLIP | genus | 40 | 40 | 0.842 | 0.586 |
| roll-up / drill-down | B1 labels (predicted) | order | 10 | 10 | 0.886 | 0.892 |
| roll-up / drill-down | B1 labels (predicted) | family | 23 | 27 | 0.875 | 0.795 |
| roll-up / drill-down | B1 labels (predicted) | genus | 32 | 40 | 0.877 | 0.757 |
| unseen species | SSE | family | 9 | 9 | 0.902 | 0.800 |
| unseen species | SSE-treeSC | family | 9 | 9 | 0.912 | 0.804 |
| unseen species | B3 separate | family | 9 | 9 | 0.914 | 0.805 |
| unseen species | B4 CSN | family | 9 | 9 | 0.909 | 0.803 |
| unseen species | B6 plain CLIP | family | 9 | 9 | 0.923 | 0.811 |
| unseen species | B1 labels (predicted) | family | 21 | 9 | 0.860 | 0.850 |
| unseen species | SSE | genus | 10 | 10 | 0.935 | 0.873 |
| unseen species | SSE-treeSC | genus | 10 | 10 | 0.936 | 0.873 |
| unseen species | B3 separate | genus | 10 | 10 | 0.942 | 0.880 |
| unseen species | B4 CSN | genus | 10 | 10 | 0.944 | 0.881 |
| unseen species | B6 plain CLIP | genus | 10 | 10 | 0.989 | 0.993 |
| unseen species | B1 labels (predicted) | genus | 28 | 10 | 0.861 | 0.819 |
