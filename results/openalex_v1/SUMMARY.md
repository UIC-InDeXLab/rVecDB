# OpenAlex (research papers) — what we found

Run: 2026-11-20 on newLab, 3 seeds (spread ≤ ±0.01 on almost every number; full tables with spreads in
`summary_tables.md`, per seed in `seed*/`). Logs: `logs/openalex/`.

## The setup, in one paragraph

**99,873 papers** (title + abstract) from all of science, 4,000 per field. Each paper has an OpenAlex topic
path, e.g. *"Biofuel from Hydroprocessing Fish Oil"* → Physical Sciences > Chemical Engineering > Catalysis >
Catalysis and Hydrodesulfurization Studies. Frozen **SPECTER2** (768 numbers) → small projector → SSE
`[ topic 128 | rest 640 ]`, zoom levels **8 = domain, 32 = field, 64 = subfield, 128 = topic**.
20% of topics are never seen in training. Separately: **5,120 authors** (their 106k *other* papers, none in the
training sample) at **300 institutions**. An author's vector = average SSE of their papers; an institution's =
average of its authors. **No author or institution label is used anywhere in training.**

## ✅ 1. Zoom levels work — again only with per-level training

Each level is best at its own prefix (domain @8, field @32, subfield @64, topic @128, seen topics).

| mAP at the level's own prefix (seen topics) | domain @8 | field @32 | subfield @64 | topic @128 |
|---|---|---|---|---|
| **SSE-treeSC** | **0.76** | **0.43** | **0.30** | **0.31** |
| MRL-style (topic everywhere) | 0.52 | 0.29 | 0.26 | 0.31 |
| Cut-short SPECTER2 (PCA) | 0.54 | 0.24 | 0.20 | 0.25 |

Same on unseen topics (domain 0.75 vs 0.54 / 0.54; field 0.45 vs 0.40 / 0.35). At the finest levels MRL catches
up (unseen subfield: MRL 0.41 vs SSE 0.40) — as on AwA2/iNat, the gain is at the **coarse** levels.

## ✅ 2. Normal search is not hurt

Same-topic search with the full vector: **SSE 0.253 vs SPECTER2 0.237**; 81% of the top-10 are the same.

## ✅ 3. The first VecJOIN result: Papers ⋈ Authors

*"Join this paper with authors who work in its area"* — at each zoom level. Truth = share of the author's papers
in the paper's area (graded). A pair counts as correct when that share ≥ 50%. Threshold picked on training papers.

| Join F1 (seen topics) | domain | field | subfield | topic |
|---|---|---|---|---|
| **SSE-treeSC** | **0.75** | **0.33** | **0.23** | **0.21** |
| Predicted labels (B1) | 0.66 | 0.31 | 0.13 | 0.01 |
| Plain SPECTER2 | 0.43 | 0.15 | 0.09 | 0.11 |

→ Labels are fine for coarse joins but **collapse at fine levels** (topic F1 0.01): a classifier has to name one
of ~3,000 topics exactly. The SSE prefix only needs to be *close*. Same story as AwA2's "in-between" result.
Graded agreement (Spearman) at domain level: SSE 0.72 · labels 0.62 · SPECTER2 0.30.

## ✅ 4. Institutions get a research profile for free

*"Institutions with a research profile like UIC's"* — compared to the true profiles (from their authors' papers):

| Spearman with true profile similarity | domain | field | subfield | topic |
|---|---|---|---|---|
| **SSE-treeSC** | **0.94** | **0.83** | **0.83** | 0.70 |
| Predicted labels (B1) | 0.88 | 0.84 | 0.76 | 0.49 |
| Plain SPECTER2 | 0.63 | 0.77 | 0.79 | **0.72** |

→ Clear win at domain level, tie with labels at field level, small win at subfield. At the topic level plain
SPECTER2 is as good (but SSE ranks the top-10 better: NDCG 0.60 vs 0.56).

## ⚠️ 5. GROUP BY inside one domain: works with the center rule, but weak

Physical Sciences test papers, grouped field → subfield → topic (ARI, 1 = perfect):

| | field | subfield | topic |
|---|---|---|---|
| **SSE-treeSC, center rule** | **0.23** | **0.16** | **0.17** |
| SSE-treeSC, connected rule | 0.06 | 0.07 | 0.11 |
| Plain SPECTER2, center rule | 0.04 | 0.05 | 0.06 |

→ SSE is ~5× better than SPECTER2, and the "connected" rule chains again (as on AwA2/iNat). But absolute numbers
are low: research areas blend into each other much more than animal families.

## 🔍 Same pattern as the image datasets

- **SSE ≈ B3 (separate vectors) ≈ CSN** on every accuracy number (within ~0.01). The edge is structure/size, not accuracy.
- **SSE-treeSC is the right recipe here too.** Graded-only (SSE-tree) keeps coarse levels best but is clearly worse
  at fine levels (field join F1 0.25 vs 0.33); yes/no-only is ≈ treeSC but its finer prefixes forget the domain more.
- **Finer prefixes partly forget coarse levels:** topic view, same-domain AUC: treeSC 0.73 · tree 0.84 · labels 0.77.

## ⚠️ Caveats

1. **"Truth" is itself a model.** OpenAlex topics are assigned by OpenAlex's own text classifier, not by people.
   So this measures agreement with OpenAlex's labels.
2. Author truth uses the same labels (share of the author's papers per area); author records in OpenAlex can be
   merged or split wrongly.
3. Authors and institutions get their vectors by *averaging* paper SSEs from the same model, so they are aligned
   by construction. The paper's harder case (two relations trained separately, aligned via a shared join key) is
   **not** tested here.
4. Physical Sciences has more papers (38k) because it has more fields; each field got the same 4,000.
