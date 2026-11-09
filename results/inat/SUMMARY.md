# iNaturalist 2021 (validation set) — results in plain words (3 seeds)

Data: 100,000 photos, 10,000 species (animals, plants, fungi), full family tree per photo.
273 orders, 1,103 families, 4,884 genera. Split: 2,000 species fully unseen; others 7 train / 3 test photos.
SSE layout: [ taxonomy 128 | rest 640 ], prefixes 16 / 64 / 128 = Order / Family / Genus.
Spread across seeds ≤ 0.004. Per-seed tables: `seed*/results.md`, `seed*/e6_Aves.md`, `seed*/e6_Insecta.md`.
Logs: `logs/inat/`, `logs/inat_round2/`, `logs/inat_e6/`.

## Zoom levels (E2): mAP at each level's own prefix, unseen species

| | Order @16 | Family @64 | Genus @128 |
|---|---|---|---|
| **SSE-treeSC** (graded + contrastive) | **0.51** | **0.36** | **0.33** |
| SSE (yes/no levels) | 0.52 | 0.36 | 0.32 |
| SSE-tree (graded only) | 0.48 | 0.27 | 0.23 |
| MRL-style (Genus everywhere) | 0.42 | 0.35 | 0.32 |
| CLIP cut short (PCA) | 0.27 | 0.20 | 0.17 |

Seen-species test photos give the same picture (treeSC 0.51 / 0.32 / 0.22).

- Zoom levels work on a deep tree; Order peaks at its 16-prefix, Family at its 64-prefix.
- Level-specific training beats MRL-style at the coarse level (0.51 vs 0.42).
- **Graded-only training (which fixed AwA2) is weaker here at fine levels**: with ~5k genera, random
  pairs almost never share a genus, so the graded loss sees mostly "unrelated" pairs.
  **Graded + contrastive (treeSC) fixes it** and also keeps Order inside the Family prefix
  (same-order AUC 0.95 vs 0.93).

## General search (E3)
Same-species mAP: treeSC 0.12 vs CLIP 0.11; 78% of CLIP's top-10 kept.

## Roll-up / drill-down (E6), within one class, center rule, ARI

| | Birds: Order | Family | Genus | Insects: Order | Family | Genus |
|---|---|---|---|---|---|---|
| **SSE-treeSC** | **0.66** | **0.26** | **0.13** | **0.85** | **0.33** | **0.10** |
| B3 separate | 0.67 | 0.30 | 0.13 | 0.85 | 0.33 | 0.10 |
| CSN | 0.66 | 0.24 | 0.13 | 0.85 | 0.33 | 0.10 |
| plain CLIP | 0.21 | 0.04 | 0.03 | 0.28 | 0.16 | 0.03 |

- Grouping over ALL of iNat was degenerate at Family/Genus (~7 / ~2 test photos per group; NMI tuning
  rewarded all-singleton groups) → grouped within birds and insects, tuned with ARI.
- Order groups good and 3× plain CLIP; the connected rule chains again at the coarse level.
- SSE ≈ B3 ≈ CSN, as on AwA2.
