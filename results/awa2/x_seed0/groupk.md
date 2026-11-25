### GROUP BY_k on AwA2 (6000 test images)

| part | method | level | k | k_true | NMI | ARI |
|---|---|---|---|---|---|---|
| habitat, impact of k | SSE | habitat | 2 | 4 | 0.467 | 0.342 |
| habitat, impact of k | SSE-treeSC | habitat | 2 | 4 | 0.465 | 0.350 |
| habitat, impact of k | B3 separate | habitat | 2 | 4 | 0.475 | 0.346 |
| habitat, impact of k | B4 CSN | habitat | 2 | 4 | 0.500 | 0.358 |
| habitat, impact of k | B6 plain CLIP | habitat | 2 | 4 | 0.339 | 0.308 |
| habitat, impact of k | SSE | habitat | 3 | 4 | 0.717 | 0.764 |
| habitat, impact of k | SSE-treeSC | habitat | 3 | 4 | 0.718 | 0.765 |
| habitat, impact of k | B3 separate | habitat | 3 | 4 | 0.717 | 0.765 |
| habitat, impact of k | B4 CSN | habitat | 3 | 4 | 0.731 | 0.777 |
| habitat, impact of k | B6 plain CLIP | habitat | 3 | 4 | 0.537 | 0.504 |
| habitat, impact of k | SSE | habitat | 4 | 4 | 0.711 | 0.761 |
| habitat, impact of k | SSE-treeSC | habitat | 4 | 4 | 0.709 | 0.759 |
| habitat, impact of k | B3 separate | habitat | 4 | 4 | 0.715 | 0.765 |
| habitat, impact of k | B4 CSN | habitat | 4 | 4 | 0.705 | 0.748 |
| habitat, impact of k | B6 plain CLIP | habitat | 4 | 4 | 0.532 | 0.418 |
| habitat, impact of k | SSE | habitat | 6 | 4 | 0.575 | 0.459 |
| habitat, impact of k | SSE-treeSC | habitat | 6 | 4 | 0.575 | 0.459 |
| habitat, impact of k | B3 separate | habitat | 6 | 4 | 0.691 | 0.653 |
| habitat, impact of k | B4 CSN | habitat | 6 | 4 | 0.573 | 0.453 |
| habitat, impact of k | B6 plain CLIP | habitat | 6 | 4 | 0.483 | 0.344 |
| habitat, impact of k | SSE | habitat | 8 | 4 | 0.611 | 0.389 |
| habitat, impact of k | SSE-treeSC | habitat | 8 | 4 | 0.655 | 0.471 |
| habitat, impact of k | B3 separate | habitat | 8 | 4 | 0.612 | 0.386 |
| habitat, impact of k | B4 CSN | habitat | 8 | 4 | 0.615 | 0.388 |
| habitat, impact of k | B6 plain CLIP | habitat | 8 | 4 | 0.492 | 0.301 |
| habitat, impact of k | SSE | habitat | 12 | 4 | 0.610 | 0.394 |
| habitat, impact of k | SSE-treeSC | habitat | 12 | 4 | 0.582 | 0.315 |
| habitat, impact of k | B3 separate | habitat | 12 | 4 | 0.613 | 0.361 |
| habitat, impact of k | B4 CSN | habitat | 12 | 4 | 0.590 | 0.334 |
| habitat, impact of k | B6 plain CLIP | habitat | 12 | 4 | 0.520 | 0.263 |
| habitat, impact of k | SSE | habitat | 16 | 4 | 0.591 | 0.301 |
| habitat, impact of k | SSE-treeSC | habitat | 16 | 4 | 0.590 | 0.301 |
| habitat, impact of k | B3 separate | habitat | 16 | 4 | 0.591 | 0.303 |
| habitat, impact of k | B4 CSN | habitat | 16 | 4 | 0.620 | 0.311 |
| habitat, impact of k | B6 plain CLIP | habitat | 16 | 4 | 0.528 | 0.235 |
| habitat, impact of k | B1 labels (predicted yes/no pattern) | habitat | 27 | 4 | 0.412 | 0.168 |
| roll-up / drill-down | SSE | order | 10 | 10 | 0.743 | 0.500 |
| roll-up / drill-down | SSE | family | 27 | 27 | 0.875 | 0.722 |
| roll-up / drill-down | SSE | genus | 40 | 40 | 0.869 | 0.675 |
| roll-up / drill-down | SSE-treeSC | order | 10 | 10 | 0.749 | 0.561 |
| roll-up / drill-down | SSE-treeSC | family | 27 | 27 | 0.864 | 0.698 |
| roll-up / drill-down | SSE-treeSC | genus | 40 | 40 | 0.848 | 0.609 |
| roll-up / drill-down | B3 separate | order | 10 | 10 | 0.754 | 0.560 |
| roll-up / drill-down | B3 separate | family | 27 | 27 | 0.870 | 0.708 |
| roll-up / drill-down | B3 separate | genus | 40 | 40 | 0.855 | 0.652 |
| roll-up / drill-down | B4 CSN | order | 10 | 10 | 0.798 | 0.687 |
| roll-up / drill-down | B4 CSN | family | 27 | 27 | 0.875 | 0.689 |
| roll-up / drill-down | B4 CSN | genus | 40 | 40 | 0.875 | 0.672 |
| roll-up / drill-down | B6 plain CLIP | order | 10 | 10 | 0.499 | 0.213 |
| roll-up / drill-down | B6 plain CLIP | family | 27 | 27 | 0.823 | 0.624 |
| roll-up / drill-down | B6 plain CLIP | genus | 40 | 40 | 0.832 | 0.572 |
| roll-up / drill-down | B1 labels (predicted) | order | 10 | 10 | 0.888 | 0.893 |
| roll-up / drill-down | B1 labels (predicted) | family | 23 | 27 | 0.875 | 0.794 |
| roll-up / drill-down | B1 labels (predicted) | genus | 32 | 40 | 0.878 | 0.758 |
| unseen species | SSE | family | 9 | 9 | 0.976 | 0.983 |
| unseen species | SSE-treeSC | family | 9 | 9 | 0.972 | 0.981 |
| unseen species | B3 separate | family | 9 | 9 | 0.977 | 0.984 |
| unseen species | B4 CSN | family | 9 | 9 | 0.976 | 0.984 |
| unseen species | B6 plain CLIP | family | 9 | 9 | 0.931 | 0.849 |
| unseen species | B1 labels (predicted) | family | 21 | 9 | 0.859 | 0.850 |
| unseen species | SSE | genus | 10 | 10 | 0.892 | 0.767 |
| unseen species | SSE-treeSC | genus | 10 | 10 | 0.937 | 0.866 |
| unseen species | B3 separate | genus | 10 | 10 | 0.899 | 0.781 |
| unseen species | B4 CSN | genus | 10 | 10 | 0.898 | 0.779 |
| unseen species | B6 plain CLIP | genus | 10 | 10 | 0.946 | 0.899 |
| unseen species | B1 labels (predicted) | genus | 28 | 10 | 0.862 | 0.820 |
