# Notes for agents working on rVecDB

Read this first. Then read `experiment-plan.md` (Status section at the top) and `REPORT.md`.

## What this project is

Experiments for the paper *"Toward Relational-Vector Databases with Schema-Structured Embeddings"*
(VLDB 2027 vision paper, UIC InDeXLab).

**Idea in one line:** one embedding vector, split into fixed **blocks** (taxonomy | habitat | diet | rest),
so a database can run filters, rankings, bands and GROUP BY on facets of *unlabeled* data.
The taxonomy block has nested **prefixes** = zoom levels (Order ⊂ Family ⊂ Genus).

Example query: *"animals that live where a swan lives, ranked by family-tree closeness to a panda."*

How the embedding is built: frozen **CLIP ViT-L/14** (768-d) → small learned projector → SSE vector.

## What's left to do

See **[WHAT_IS_NEXT.md](WHAT_IS_NEXT.md)**: (1) CLIP for text too, (2) remove baselines that don't
make sense, (3) benchmarks in non-animal domains, plus smaller open items. E7 is on hold.
Keep that file updated as tasks start/finish.

## Key results so far (short)

- SSE blocks mean their facet and clearly beat stored labels, especially on unseen species and
  graded ("in-between") similarity.
- Prefixes work on AwA2 and iNat, but only with level-specific, tree-aware training
  (**SSE-treeSC** = graded + contrastive is the recommended recipe on both datasets).
- With the same training, **SSE ≈ B3 ≈ CSN in accuracy**. SSE's edge is structural: one compact
  vector (SSE-128 matches B3-920, 7× smaller) with a fixed, readable layout. Cost (E7) must show the rest.
- GROUP BY: the paper's "connected" rule chains on graded facets; a **center-based** rule works.
- VLM (B5) is not an upper bound and is far too slow (~9–16 pairs/s).
- MovieLens: works (~2× plain text embedding) but movie facets overlap in reality, so it shows
  generality, not facet separation.

Full numbers: `REPORT.md`, `results/*/SUMMARY.md`, `results/awa2/WHAT_WE_KNOW.md`.

## Repo layout

| Path | What |
|---|---|
| `experiment-plan.md` | Plan + **Status table at the top (keep updated)** |
| `REPORT.md` | Full write-up of all results |
| `sse/` | Code. `awa2.py`, `inat.py`, `movielens.py` (dataset pipelines), `train_sse.py`, `train_baselines.py`, `evaluate.py`, `e6_grouping.py`, `q2.py`, `b5_vlm.py`, `extract.py` (CLIP features) |
| `scripts/run_*.sh` | One script per round; each logs every step |
| `logs/PROGRESS.md` | One line per step: started / done / FAILED with times |
| `logs/<round>/<step>.log` | Full output per step |
| `results/` | Per-seed outputs and summaries (`results/awa2`, `results/inat`, `results/movielens`) |
| `data/movielens/tag_groups.csv` | Hand-editable tag → facet mapping (source of truth) |

Not in git: `data/` (23 GB), `cache/` (24 GB features/embeddings), `.venv/`.
**The paper (`overleaf/`) is NOT in this repo** — it lives on Overleaf only. This GitHub repo is
public: never commit the paper source or paper-draft PDFs.

## Setup from scratch

Hardware used: 1× RTX 5090 (32 GB), 64 cores, 123 GB RAM.

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
```

Data (put under `data/`):
- AwA2: `data/awa2/AwA2-data.zip` (13,923,888,724 bytes) from https://cvml.ista.ac.at/AwA2/ — read directly from the zip.
- iNat 2021 **validation** set: `data/inat/val.tar.gz` + `data/inat/val.json.tar.gz`
  (iNat 2021 competition, github.com/visipedia/inat_comp). Read directly from the tar.
- MovieLens 25M: `data/movielens/ml-25m/` from https://files.grouplens.org/datasets/movielens/ml-25m.zip
- Movie plots: `data/movielens/tmdb/movies_metadata.csv` (HF dataset `amnacodes/movies_metadata`, "The Movies Dataset").

Then run the scripts in order (each skips steps whose cache already exists), e.g.
`bash scripts/run_awa2.sh`, `bash scripts/run_inat.sh`, `bash scripts/run_movielens.sh`, then later rounds.
Pipelines also have CLIs, e.g. `.venv/bin/python -m sse.inat train --method tree --seed 0`.

## Working rules (from the user)

- **Logs + progress always.** Every run writes `logs/<round>/<step>.log` and appends to
  `logs/PROGRESS.md`. Copy the `note`/`step` helpers from an existing `scripts/run_*.sh`.
  Tell the user where logs are in every update.
- **Keep the Status section of `experiment-plan.md` updated** when a step starts/finishes
  (status only; exact times go in `PROGRESS.md`).
- **Explain simply:** small concrete example first (swan / seal / camel), short sections, small tables.
- 3 seeds for anything reported; report the spread.
- Don't re-argue settled decisions: datasets (AwA2 main, iNat 2021, MovieLens, Animals-90 for figures),
  768-d SSE from frozen CLIP ViT-L/14, AwA2 layout `[taxonomy 64 | habitat 32 | diet 16 | rest 656]`
  with prefixes 8/32/64, iNat `[taxonomy 128 | rest 640]` with 16/64/128,
  hard label = AwA2 score ≥ 50, MRL is only an ablation.
