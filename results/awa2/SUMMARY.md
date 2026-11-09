# AwA2 — first results, in plain words

Run: 2026-11-05, 13:21–13:31. Full numbers: `results.md` / `results.json` (same folder).
Logs: `logs/awa2/*.log`. Progress: `logs/PROGRESS.md`.

Setup: frozen CLIP ViT-L/14 → small network → 768 numbers
`[ taxonomy 64 | habitat 32 | diet 16 | rest 656 ]`. Trained on 40 species.
Tested on 13,052 images: new photos of the 40 species + 10 species never seen
(persian cat, hippo, leopard, humpback whale, seal, chimpanzee, rat, giant panda, pig, raccoon).

| Goal | Result | Verdict |
|---|---|---|
| **G1** blocks mean what they should | Habitat block matches true habitat at **0.90** (labels 0.61, plain CLIP 0.31). Diet block **0.87**. | ✅ |
| **G2** zoom levels | Seen species: **8 dims → Order 0.996, 32 → Family 0.989, 64 → Genus 0.987** — each level is best at its own prefix. Unseen: Order at 8 dims **0.90** vs. 0.77 (one-label MRL-style) vs. 0.64 (CLIP cut short). | ✅ (needs iNat for a deeper test) |
| **G3** normal search still works | Same-species search **0.821** vs. CLIP 0.819; 84% same top-10. | ✅ |
| **G4** combined queries | Filter correct **0.75** (labels 0.48, label scores 0.67, CLIP 0.55). Ranking **0.55** (labels 0.38). | ✅ |
| **G4** no-mixing | Error **0.15 / 0.14** — lowest of all methods (others 0.19–0.55). | ✅ |
| **G5a** new species | Filter **0.72** on unseen-species references (labels 0.47). | ✅ |
| **G5b** in-between similarity | Trained on scores: **0.89** (labels 0.59). Trained on yes/no only: **0.20** — does NOT recover it. | ⚠️ half |
| **G5c** threshold as a dial | True similarity rises at **every** step, 0.10 → 0.92. Labels jump around. | ✅ |

## Things to fix / check next

1. **G5b, yes/no version.** SSE-hard treated two animals as "same habitat" only if all 14
   yes/no answers matched exactly. Try a fairer version (reward each shared habitat). If it still
   fails, the claim becomes "SSE *keeps* graded similarity", not "SSE *discovers* it".
2. **Taxonomy in E1/E4 is the weakest part** (E1 0.53 vs. labels 0.73 on the 0–3 tree score).
   Try a higher taxonomy loss weight (now 0.5).
3. **Only 56% of SSE's top-10 truly pass the filter.** Room to improve; partly the size-matched
   filter, partly taxonomy.
4. **Unseen split is easy for Family/Genus** (10 species, mostly in different families). iNat
   gives the real hierarchy test.
5. Single run, seed 0. Repeat with 3 seeds before anything goes in the paper.


---

# Round 2 — 3 seeds, fairer yes/no version, taxonomy weight

Full table: `round2_summary.md`. Logs: `logs/awa2_round2/`.

1. **Results are stable.** Across 3 random starts, every number moves by at most ±0.005.
   All round-1 conclusions hold.
2. **Fairer yes/no version (SSE-hardJ)** — credit for each shared habitat.
   In-between score rises 0.20 → **0.62**, but plain yes/no labels already get **0.59**.
   So SSE does not *discover* much graded similarity from yes/no labels.
   → Paper claim: **SSE keeps graded similarity when trained with it (0.89 vs labels 0.59)**,
   not "SSE discovers it from simple labels".
3. **Taxonomy weight 0.5 / 1 / 2 changes nothing.** The taxonomy loss is already at its floor.
4. **Why taxonomy looked weak in E1:** the E1 score mixes Family and Order.
   - Same family vs. not: SSE **0.994**, labels 0.985 → Family level is excellent.
   - Same order vs. not, using the Family prefix: SSE **0.82**, labels 0.96 → the Family prefix
     forgets Order.
   - This is a real finding: nested prefixes do not automatically keep coarser levels.
     Fix to try: train each prefix with graded family-tree similarity
     (same genus > same family > same order > different) instead of "same family or not".


---

# Round 3 — graded family-tree training (fix for "Family prefix forgets Order")

Full table: `round3_summary.md`. Logs: `logs/awa2_round3/`.

Each taxonomy prefix is now trained to match graded tree similarity
(same genus > same family > same order > unrelated), like the habitat block uses graded scores.

| | Before (SSE) | After (SSE-tree) | Labels (B1) |
|---|---|---|---|
| Family prefix: same family? | 0.995 | **0.996** | 0.985 |
| Family prefix: same **order**? | 0.82 | **0.955** | 0.96 |
| E1 taxonomy score | 0.53 | **0.72** | 0.73 |
| E4 ranking (NDCG@10) | 0.549 | **0.580** | 0.384 |
| New species, Order@8 | 0.89 | **0.94** | – |
| Seen species, Family@32 | **0.985** | 0.974 | – |

→ The fix works. Small cost on seen species; gains on new species and on ranking.
→ Lesson for the paper: **nested prefixes need graded (tree-aware) training to keep coarser levels.**


---

# Round 4 — trained competitors: B3 separate vectors, B4 CSN (3 seeds)

Full table: `round4_summary.md`. Logs: `logs/awa2_round4/`.

| | SSE-tree | B3 separate | B4 CSN | B1 labels |
|---|---|---|---|---|
| Habitat filter (F1) | 0.753 | **0.756** | 0.745 | 0.484 |
| In-between (E5b) | 0.890 | **0.892** | 0.878 | 0.591 |
| No-mixing error | 0.147 | **0.146** | 0.149 | 0.340 |
| Ranking (NDCG@10) | **0.580** | 0.541 | 0.543 | 0.384 |
| Numbers stored per item | **768** | 920 | 768 | 768 + labels |

- **B3 and CSN match SSE on habitat and diet.** This is what the plan expected for B3:
  SSE's advantage over separate vectors is **not accuracy**.
- SSE wins on ranking, but **not fairly yet** — only SSE had the graded tree training (round 3).
  Round 4b gives B3 and CSN the same training.
- CSN's learned masks each use ~380 of 768 dimensions and overlap ~50% with each other
  (about what random halves would give) → **no readable "this block = habitat" structure**.
- Likely paper message: SSE ≈ separate vectors in accuracy, with **one vector, one model,
  one index, less storage, and a readable layout**; much better than labels.


---

# Round 4b — fair comparison: B3 and CSN get the same graded tree training

Full table: `round4b_summary.md`. Logs: `logs/awa2_round4b/`.

| | SSE-tree | B3 separate | B4 CSN | B1 labels |
|---|---|---|---|---|
| Habitat filter (F1) | 0.753 | 0.756 | 0.753 | 0.484 |
| Ranking (NDCG@10) | 0.580 | 0.582 | 0.585 | 0.384 |
| In-between (E5b) | 0.890 | 0.892 | 0.889 | 0.591 |
| No-mixing error | 0.147 | 0.146 | 0.152 | 0.340 |
| E1 taxonomy | 0.722 | 0.724 | 0.731 | 0.727 |
| Numbers stored per item | **768** | 920 | 768 (+5 masks) | 768 + labels |

- **With the same training, all three tie** on every accuracy measure (differences ≤ 0.005).
- The accuracy gains come from the **training recipe** (graded targets: habitat scores, tree similarity),
  not from the block layout. Any of the three structures learns them equally well.
- So SSE's case vs. separate vectors / CSN must rest on:
  1. **Cost / compactness** — one vector; test SSE-256 vs B3-920 (next).
  2. **Readable layout** — fixed blocks and prefixes you can point at; CSN masks overlap ~50% (≈ random).
  3. **One model, one table column** — vs. 5 models + 6 columns for B3.
- Against labels (B1), SSE is far better everywhere except E1 taxonomy (tie).


---

# E6 — GROUP BY and roll-up / drill-down (3 seeds)

Full table: `e6_summary.md`. Per seed: `r4b_seed*/e6.md`. Logs: `logs/awa2_e6/`.
Grouping threshold κ is tuned on training images, not test.
True habitat groups = species clustered by their habitat scores: water · jungle · forest · fields/plains.

Two grouping rules:
- **connected** (the paper's current rule): connect items whose similarity ≥ κ; groups = what is connected.
- **center** (new): take a central item; everything within κ **of that center** is one group; repeat.

| Agreement with truth (NMI) | SSE connected | SSE center | B3 center | CSN center | CLIP center |
|---|---|---|---|---|---|
| Habitat GROUP BY | 0.17 | **0.50** | 0.51 | 0.58 | 0.39 |
| Zoom: Order | 0.85 | **0.84** | 0.85 | 0.86 | 0.50 |
| Zoom: Family | 0.85 | **0.88** | 0.88 | 0.89 | 0.73 |
| Zoom: Genus | **0.86** | 0.84 | 0.86 | 0.87 | 0.75 |

1. **The paper's "connected" rule chains on graded facets.** Habitat similarity changes smoothly
   (whale → seal → otter → beaver → … → deer), so everything links into 1–2 giant groups.
   For B3 and CSN it is unstable across seeds (spread ±0.25–0.29).
2. **The center rule fixes it**: habitat 0.17 → 0.50, stable (±0.02); about 5 main groups for 4 true ones.
3. **Roll-up / drill-down works with both rules**: Order 0.84, Family 0.88 — far above plain CLIP
   (0.50 / 0.73). Every small group sits inside exactly one bigger group by construction.
4. SSE ≈ B3 ≈ CSN again.
5. **For the paper:** the grouping policy matters; the paper should define a non-chaining
   (center-based) range grouping as the default, and mention chaining in Challenges.


---

# Round 5A — compactness: how small can SSE be? (3 seeds)

Full table: `round5_compact_summary.md`. Logs: `logs/awa2_round5/`.
Facet blocks stay the same size (taxonomy 64, habitat 32, diet 16); only the "rest" block shrinks.

| | SSE-768 | SSE-256 | **SSE-128** | B3 separate (920) |
|---|---|---|---|---|
| Habitat filter (F1) | 0.754 | 0.754 | **0.751** | 0.757 |
| Ranking (NDCG@10) | 0.576 | 0.576 | **0.576** | 0.579 |
| In-between (E5b) | 0.890 | 0.892 | **0.890** | 0.892 |
| No-mixing error | 0.163 | 0.157 | **0.161** | 0.162 |
| Zoom, new species (Order@8) | 0.945 | 0.946 | **0.946** | – |
| General species search (mAP) | 0.823 | 0.836 | **0.831** | CLIP 0.82–0.84 |
| Top-10 shared with CLIP | 0.86 | 0.71 | 0.46 | – |
| Numbers per item | 768 | 256 | **128** | 920 |

- **SSE-128 matches SSE-768 and B3-920 on every facet test**, and finds same-species images
  as well as full CLIP. It is **7× smaller than B3** and 6× smaller than CLIP alone.
- The only thing that drops is "same top-10 as CLIP" (0.86 → 0.46): the small SSE returns
  *different* but equally correct neighbours.
- Fairness note: most of B3's 920 is the general-search CLIP vector (768); its five facet
  vectors are 152. A compressed B3 (facets + a 128-d general vector) would be ~280 — still ~2×
  SSE-128, and still 5 models + 6 columns.
- → This is SSE's clearest win: **same accuracy, one small vector.**


---

# Round 5B — choosing the SSE version on a validation split (no test data)

Full table: `round5_val_summary.md`. 5 training species (antelope, beaver, mole, otter, walrus) act as
"unseen"; 15% of the remaining training images act as "seen test". The real test images are never used.

| (validation) | SSE (yes/no levels) | **SSE-tree** | SSE-treeSC |
|---|---|---|---|
| E1 family-tree score | 0.55 | **0.72** | 0.71 |
| E4 ranking (NDCG@10) | 0.571 | **0.608** | 0.605 |
| Family prefix keeps Order (AUC) | 0.84 | **0.96** | 0.95 |
| Habitat filter (F1) | 0.707 | 0.709 | 0.709 |

→ **SSE-tree is the right choice, confirmed without test data.** The paper can state it was picked on validation.


---

# Round 5C — Q2 queries: Order prototype filter + habitat BAND + ranking (3 seeds)

Full table: `q2_summary.md`. Query: animals in a given Order (via a "Carnivora"-style prototype vector),
whose habitat similarity to a reference animal lies in a BAND (e.g. 30th–60th percentile, "somewhat
similar but not too similar"), ranked by general similarity. No year condition (AwA2 has no dates).

| | SSE | B3 separate | CSN | B1 labels | B1-soft | plain CLIP |
|---|---|---|---|---|---|---|
| Order filter (F1) | 0.96 | 0.96 | 0.96 | 0.83 | **0.97** | 0.67 |
| Habitat band (F1) | **0.60** | **0.60** | **0.60** | 0.35 | 0.44 | 0.34 |
| Both together (F1) | **0.38** | **0.38** | **0.38** | 0.18 | 0.24 | 0.16 |
| Top-10 satisfying both | 0.35 | **0.37** | 0.31 | 0.22 | 0.27 | 0.14 |

- **Bands are where labels fail**: yes/no labels get 0.35 on the band (barely above plain CLIP),
  SSE gets 0.60. Labels can say "same habitat" but not "somewhat similar habitat".
- The Order prototype works (0.96): a named concept like "Carnivora" can be a vector.
- B3 / CSN again tie with SSE.
- Q2 is hard for everyone (both conditions together ≈ 0.38) — a band is a narrow target.


---

# B5 — ask an open AI model (Qwen2.5-VL-7B), Yes/No version

Full table: `b5/results.md`. 50 Q1 queries; every method scored on the SAME 200 candidates per query.
The model sees the reference and a candidate image, names both animals, then answers Yes/No
("similar habitat?", "same family?"). Score = its confidence in "Yes".

| | Habitat filter (F1) | Ranking (NDCG@10) | Speed |
|---|---|---|---|
| SSE | 0.75 | 0.72 | ms per query |
| B3 separate | 0.76 | 0.74 | ms |
| B1-soft | 0.66 | 0.69 | ms |
| plain CLIP | 0.55 | 0.49 | ms |
| **AI model (Yes/No)** | **0.48** | **0.31** | 16 pairs/s → ~27 min per query on 13k images |
| B1 labels | 0.44 | 0.49 | ms |

- Prompt note: asked for a one-word answer, the model said "No" even to brown bear vs polar bear
  (while naming both correctly). "Name both animals first, then answer" fixed this.
- **Not an upper bound here.** Likely because Yes/No is too coarse (it says "No" to ~95% of pairs) and
  its notion of "similar habitat" is stricter than the human ratings.
- Running next: a fairer 0–10 rating version.


# B5 — fairer version: 0–10 rating (same 50 queries × 200 candidates)

| | Habitat filter (F1) | Ranking (NDCG@10) | Speed |
|---|---|---|---|
| SSE | 0.75 | 0.72 | ms per query |
| B3 separate | 0.76 | 0.74 | ms |
| B1-soft (label scores) | 0.66 | 0.69 | ms |
| **AI model, 0–10 rating** | **0.53** | **0.57** | 8.9 pairs/s → ~25 min per query on 13k images |
| AI model, Yes/No | 0.48 | 0.31 | 16 pairs/s |
| plain CLIP | 0.55 | 0.49 | ms |
| B1 labels | 0.44 | 0.49 | ms |

- Graded answers help the AI model a lot on ranking (0.31 → 0.57), as expected.
- **Still clearly below SSE**, and ~10⁵–10⁶× slower per query. A 7B model's notion of "similar habitat"
  differs from the human ratings (e.g. polar bear vs seal: 2/10).
- Caveat for the paper: one open 7B model with one prompt; a much larger model might do better.
  Still, the cost argument holds regardless.
