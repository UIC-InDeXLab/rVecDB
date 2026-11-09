### B5 — 50 Q1 queries, each over the same 200 candidates for every method

VLM speed: 16.3 image pairs/s on the RTX 5090 (one query = 200 habitat + 200 family pairs).

| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|---|---|
| SSE | all | 50 | 0.747 | 0.840 | 0.710 | 0.720 |
| SSE | x unseen | 21 | 0.734 | 0.833 | 0.700 | 0.725 |
| B1 labels | all | 50 | 0.442 | 0.499 | 0.432 | 0.494 |
| B1 labels | x unseen | 21 | 0.360 | 0.415 | 0.400 | 0.516 |
| B1-soft | all | 50 | 0.658 | 0.751 | 0.652 | 0.688 |
| B1-soft | x unseen | 21 | 0.711 | 0.783 | 0.776 | 0.773 |
| B2 CLIP+text | all | 50 | 0.443 | 0.478 | 0.438 | 0.403 |
| B2 CLIP+text | x unseen | 21 | 0.468 | 0.515 | 0.467 | 0.373 |
| B6 plain CLIP | all | 50 | 0.545 | 0.620 | 0.472 | 0.487 |
| B6 plain CLIP | x unseen | 21 | 0.659 | 0.738 | 0.590 | 0.573 |
| B3 separate | all | 50 | 0.755 | 0.850 | 0.722 | 0.744 |
| B3 separate | x unseen | 21 | 0.752 | 0.850 | 0.748 | 0.765 |
| B4 CSN | all | 50 | 0.752 | 0.842 | 0.712 | 0.688 |
| B4 CSN | x unseen | 21 | 0.745 | 0.847 | 0.738 | 0.694 |
| B5 VLM (Qwen2.5-VL-7B) | all | 50 | 0.475 | 0.517 | 0.404 | 0.307 |
| B5 VLM (Qwen2.5-VL-7B) | x unseen | 21 | 0.529 | 0.584 | 0.490 | 0.376 |
| B5 VLM rating 0-10 | all | 50 | 0.534 | 0.597 | 0.602 | 0.570 |
| B5 VLM rating 0-10 | x unseen | 21 | 0.588 | 0.647 | 0.690 | 0.668 |
