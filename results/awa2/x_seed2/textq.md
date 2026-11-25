### Habitat filter with a text vs image reference (6000 test images, top 25% = true)

| method | slice | n | F1 | AP |
|---|---|---|---|---|
| SSE, text reference | all species | 50 | 0.709 | 0.784 |
| SSE, text reference | unseen species | 10 | 0.615 | 0.688 |
| SSE, text reference | seen species | 40 | 0.733 | 0.808 |
| SSE, image reference | all species | 50 | 0.794 | 0.881 |
| SSE, image reference | unseen species | 10 | 0.740 | 0.838 |
| SSE, image reference | seen species | 40 | 0.808 | 0.892 |
| CLIP, text reference | all species | 50 | 0.492 | 0.548 |
| CLIP, text reference | unseen species | 10 | 0.531 | 0.624 |
| CLIP, text reference | seen species | 40 | 0.482 | 0.528 |
| CLIP, image reference | all species | 50 | 0.497 | 0.553 |
| CLIP, image reference | unseen species | 10 | 0.583 | 0.664 |
| CLIP, image reference | seen species | 40 | 0.476 | 0.526 |
