# OpenAlex (research papers) — v2 results

Run: 2026-11-20 on newLab, 3 seeds (spread ≤ ±0.02 everywhere). Full tables: `summary_tables.md`;
per seed: `seed*/`. Logs: `logs/openalex/`. Earlier version (with the topic level): `../openalex_v1/`.

## The setup

**99,873 papers** (title + abstract) from all of science. Each has a path like *"Biofuel from Hydroprocessing
Fish Oil"* → Physical Sciences > Chemical Engineering > Catalysis. Frozen **SPECTER2** → small projector → SSE
`[ taxonomy 128 | rest 640 ]`, zoom levels **16 = domain (4), 64 = field (26), 128 = subfield (250)** —
the same shape as iNat's Order / Family / Genus. 20% of the finer topics are never seen in training.
**5,120 authors** at **300 institutions**: an author's vector = average SSE of their *other* papers.
No author or institution label is used in training.

**What changed from v1, and why.** v1 also had a 4th level, topic (4,016 topics, ~9 papers each). It was too
sparse: for 58% of papers *no* author worked mainly in that topic, so the join score there meant little. v1 also
counted an author as "right" only if ≥ 50% of their papers were in the area — only 39% of researchers have
that at subfield level. v2 drops the topic level and asks a clearer question (below).

## ✅ 1. The join: *"which authors work on what this paper is about?"*

For each paper, return the 10 closest authors. **P@10 = how many of those 10 have the paper's area as their
main area.** "Random" = picking 10 authors blindly.

| P@10 (seen topics) | domain (4) | field (26) | subfield (250) |
|---|---|---|---|
| **SSE-treeSC** | **0.81** | **0.53** | **0.36** |
| Predicted labels (B1) | 0.75 | 0.48 | 0.20 |
| Plain SPECTER2 | 0.78 | 0.45 | 0.30 |
| Random | 0.27 | 0.04 | 0.009 |

→ At subfield level, **3–4 of the 10 returned authors work mainly in the paper's exact subfield (out of 250)** —
**40× better than random**, 1.8× better than stored labels. At field level, 5 of 10 (13× random).
Same on unseen topics (subfield 0.37; labels 0.21).

As a database join with a threshold (F1, threshold chosen on training papers):
domain 0.75 · field 0.36 · subfield 0.28 for SSE vs labels 0.67 / 0.33 / 0.14 vs random 0.43 / 0.08 / 0.02.

## ✅ 2. Zoom levels work — only with per-level training

mAP of retrieving papers of the same domain / field / subfield, each at its own prefix. All methods peak at the
right prefix (16 / 64 / 128); MRL and PCA don't.

| mAP (seen topics) | domain @16 | field @64 | subfield @128 |
|---|---|---|---|
| **SSE-treeSC** | **0.76** | **0.43** | **0.31** |
| MRL-style (subfield everywhere) | 0.57 | 0.37 | 0.31 |
| Cut-short SPECTER2 (PCA) | 0.53 | 0.24 | 0.20 |

## ✅ 3. Institutions: *"institutions with a research profile like UIC's"*

| Spearman with true profile similarity | domain | field | subfield |
|---|---|---|---|
| **SSE-treeSC** | **0.94** | 0.83 | **0.82** |
| Predicted labels (B1) | 0.88 | 0.84 | 0.76 |
| Plain SPECTER2 | 0.63 | 0.77 | 0.79 |

## ⚠️ 4. GROUP BY is still weak

Grouping Physical Sciences papers into fields → subfields (center rule): ARI **0.22 / 0.16** vs SPECTER2
0.04 / 0.05. 5× better than SPECTER2, but low in absolute terms. The "connected" rule chains again (0.06).
The grouping rule picks its own number of groups from a similarity threshold, and research areas blend into
each other, so the groups come out uneven.

## 🔍 Same pattern as the image datasets

- **SSE ≈ B3 ≈ CSN** on every number (within ~0.01). The edge is the single compact vector, not accuracy.
- **treeSC ≈ yes/no-only**, both clearly better than graded-only (SSE-tree) at field/subfield
  (subfield P@10 0.36 vs 0.31).
- Normal search is not hurt (same-topic mAP 0.25 vs SPECTER2 0.24).

## ⚠️ Caveats

1. "Truth" = OpenAlex's own topic labels, assigned by OpenAlex's text classifier — so this measures agreement
   with those labels. 38% of papers have a primary-topic confidence below 0.9.
2. Author and institution vectors are averages from the same model, so they line up automatically. The harder
   case (two relations trained separately, aligned by a shared join key) is not tested yet.

## ✅ 5. Semantic credit at subfield level (2026-11-20)

A near-miss gets partial credit by how related the two subfields are (1 = same, 0 = at or below the median
pair). Two answer keys: **text** = bge-large similarity of subfield descriptions + topic names/keywords;
**co-activity** = how often the same authors publish in both. Examples: `related_examples.md`.

| subfield, seen topics | papers: exact | papers: text credit | authors: exact | authors: text credit |
|---|---|---|---|---|
| **SSE-treeSC** | **0.51** | **0.62** | **0.36** | **0.41** |
| Plain SPECTER2 | 0.45 | 0.56 | 0.30 | 0.36 |
| Predicted labels (B1) | 0.39 | 0.52 | 0.20 | 0.32 |
| Random | 0.01 | 0.07 | 0.009 | 0.07 |

Co-activity credit has the same ranking (papers 0.55 / 0.49 / 0.43 / 0.02). The author credit is weighted by
the author's share of papers in each subfield, so an author who works in several areas never reaches 1.
The scale is conservative: even close pairs get only 0.3–0.45 (AI ↔ Computer Vision 0.32).
