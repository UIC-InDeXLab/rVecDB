# MovieLens (text) — first results, in plain words (3 seeds)

Setup: 13,227 movies (9,884 train / 3,343 test). Text = title + TMDB plot overview, encoded with
bge-base (768 numbers, frozen). Facets = tag-genome scores grouped into genre (120 tags), tone (130),
theme (488), style (85). SSE layout: [ genre 32 | tone 32 | theme 32 | style 32 | rest 640 ].
Truth = cosine of centered genome scores per facet (graded). Spread across seeds ≤ 0.005 everywhere.
Logs: `logs/movielens/`. Per-seed tables: `seed*/results.md`.

## 1. Each block vs its own facet (E1, Spearman; higher = better)

| | genre | tone | theme | style |
|---|---|---|---|---|
| **SSE** | **0.35** | **0.27** | **0.31** | **0.25** |
| B3 separate | 0.35 | 0.28 | 0.31 | 0.25 |
| B4 CSN | 0.39 | 0.31 | 0.35 | 0.29 |
| B1-soft (label scores) | 0.33 | 0.22 | 0.28 | 0.20 |
| plain bge | 0.17 | 0.11 | 0.19 | 0.10 |
| text prompts | 0.11 | 0.07 | 0.10 | 0.04 |
| B1 labels (yes/no) | 0.01 | 0.03 | 0.05 | 0.04 |
| SSE-hard (yes/no training) | 0.22 | 0.15 | 0.21 | 0.14 |

## 2. Filter on one facet, rank on another (E4)

| | Filter (F1) | Top-10 truly pass | Ranking (NDCG@10) |
|---|---|---|---|
| **SSE** | **0.35** | **0.31** | **0.12** |
| B3 separate | 0.35 | 0.32 | 0.12 |
| B4 CSN | 0.36 | 0.32 | 0.13 |
| B1-soft | 0.33 | 0.28 | 0.09 |
| plain bge | 0.29 | 0.25 | 0.09 |
| B1 labels | 0.18 | 0.17 | 0.04 |

## 3. Threshold as a dial (E5c, tone)
SSE rises at every step (true similarity −0.12 → 0.17); labels are flat (0.00 → 0.01).

## What it means

1. **SSE works on text too**: about 2× plain bge on every facet, far above yes/no labels (which are
   nearly useless here: most movies get no "yes" tags at threshold 0.5).
2. **SSE ≈ B3; CSN slightly better on text** (+0.03–0.04 on E1). Same picture as AwA2: the structure
   choice matters little for accuracy; SSE's case is size and simplicity.
3. **Absolute numbers are low** (0.25–0.35): a short plot summary carries limited information about
   tags like "great cinematography" or "atmospheric". This is a ceiling of the input, not of SSE.
4. **Movie facets overlap a lot in reality.** How similar two movies are in genre, tone, theme and
   style is strongly linked (true-facet overlap 0.55–0.69 vs 0.26–0.43 on AwA2). So every block also
   tracks the other facets (≈0.24 vs ≈0.31 for its own), and the "no mixing" test cannot be shown
   cleanly on this dataset.
   → For the paper, MovieLens shows **generality to text**; AwA2 remains the dataset that shows
   **facet separation**. A partial-correlation analysis (own facet, controlling for the others)
   could still isolate each block's own signal — not done yet.
5. E3: SSE's full vector keeps 74% of bge's top-10 neighbours (CSN 64%).
