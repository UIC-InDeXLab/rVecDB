# Submission experiments (2026-11-25)

All run on newLab, 3 seeds. Written into the paper's `exp.tex` (Q2–Q8). Logs: `logs/awa2_extra/`, `logs/oa_extra/`,
`logs/inat/`, `logs/inat_round2/`, `logs/final/`, `logs/cost/`, `logs/data/`; one line per step in `logs/PROGRESS.md`.

| Experiment | Code | Results |
|---|---|---|
| AwA2 rebuild + main tables (treeSC) | `scripts/run_awa2_extra.sh` | `results/awa2/x_eval_summary.md`, `x_q2_seed*/` |
| GROUP BY_k (AwA2 / iNat / OpenAlex) | `sse/awa2_extra.py groupk`, `sse/inat_extra.py`, `sse/oa_extra.py groupk` | `results/awa2/x_summary.md`, `results/inat/x_summary.md`, `results/openalex/extra_tables.md` |
| REP(g,5) (query Q4) | `sse/awa2_extra.py rep` | `results/awa2/x_rep/` |
| Aggregates (query Q5) | `sse/awa2_extra.py agg` | `results/awa2/x_summary.md` |
| Text references | `sse/awa2_extra.py textq` | `results/awa2/x_summary.md` |
| Block-size allocation | `sse/awa2_extra.py blockeval/blocksummary` | `results/awa2/x_blocksize.md` |
| EVA-CLIP encoder | `scripts/run_awa2_extra.sh` part 4 | `results/awa2_eva/summary.md` |
| Trained shared join keys, threshold sweep | `sse/oa_extra.py joinkeys/sweep` | `results/openalex/extra_tables.md` |
| Cost (E7) | `sse/cost.py`, `scripts/run_cost.sh` | `results/awa2/x_cost/cost_n1000000.md` |

## Where SSE wins (headline numbers)

| | SSE | Labels | Encoder |
|---|---|---|---|
| AwA2 habitat GROUP BY_k (NMI) | **0.68** | 0.41 | 0.51 |
| iNat birds, unseen genera GROUP BY_k (NMI) | **0.75** | 0.47 | 0.66 |
| Aggregates per Order (Spearman, AVG) | **0.77** | 0.55 | 0.53 |
| Habitat filter, text reference (F1) | **0.71** | — | 0.49 |
| Separately trained join keys, field P@10 | **0.47** | 0.41 | 0.04 (different encoders) |
| EVA encoder: filter F1 | **0.76** | 0.44 | 0.53 |

Cost at 1M objects: SSE-128 stores 0.52 GB (B3 3.68 GB, 7×), Q1 in 31 ms (CSN 280 ms, B3 24 ms); habitat HNSW 0.38 GB (CSN 3.3 GB).

## Honest weak spots (framed in the paper)
- SSE ≈ B3 ≈ CSN in accuracy; SSE's edge is storage/cost and the single fixed layout.
- Seen-class taxonomy grouping: trained label classifiers beat k-means (AwA2 Order NMI 0.89 vs 0.78).
- Join with one global threshold at field level is below labels (F1 0.32 vs 0.41); top-k join is better.
- Unseen-topic subfield grouping on OpenAlex: SSE 0.69 ≈ plain encoder 0.70.
