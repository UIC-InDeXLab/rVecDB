### Habitat filter with a text vs image reference (6000 test images, top 25% = true)

| method | slice | n | F1 | AP |
|---|---|---|---|---|
| SSE, text reference | all species | 50 | 0.706 | 0.785 |
| SSE, text reference | unseen species | 10 | 0.589 | 0.676 |
| SSE, text reference | seen species | 40 | 0.736 | 0.812 |
| SSE, image reference | all species | 50 | 0.793 | 0.877 |
| SSE, image reference | unseen species | 10 | 0.732 | 0.830 |
| SSE, image reference | seen species | 40 | 0.808 | 0.889 |
| CLIP, text reference | all species | 50 | 0.492 | 0.548 |
| CLIP, text reference | unseen species | 10 | 0.531 | 0.624 |
| CLIP, text reference | seen species | 40 | 0.482 | 0.528 |
| CLIP, image reference | all species | 50 | 0.485 | 0.540 |
| CLIP, image reference | unseen species | 10 | 0.573 | 0.660 |
| CLIP, image reference | seen species | 40 | 0.463 | 0.511 |
