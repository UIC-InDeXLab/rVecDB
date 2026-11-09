# rVecDB — Experiment Plan

Last updated: 2026-11-09

---

## 📍 Status (kept up to date)

Legend: ✅ done · 🔄 running · ⏳ next · ⬜ not started · ⏸️ on hold · ⚠️ needs attention

**Where things are**
- Progress tracker (live, one line per step): `logs/PROGRESS.md`
- Step logs: `logs/awa2/*.log` (round 1), `logs/awa2_round2/*.log` (round 2), `logs/awa2_round3/*.log` (round 3), `logs/awa2_round4/*.log` (round 4), `logs/awa2_round4b/*.log`, `logs/awa2_e6/*.log`, `logs/awa2_round5/*.log`, `logs/awa2_b5/*.log`, `logs/movielens/*.log`, `logs/inat/*.log`, `logs/inat_round2/*.log`, `logs/inat_e6/*.log`
- Results: `results/awa2/SUMMARY.md` (round 1, plain words), `results/awa2/round2_summary.md` (round 2)
- Code: `sse/` · run scripts (in `scripts/`): `run_awa2.sh`, `run_awa2_round2.sh`, `run_awa2_round3.sh`, `run_awa2_round4.sh`, `run_awa2_round4b.sh`, `run_awa2_e6.sh`, `run_awa2_round5.sh`, `run_awa2_b5.sh`, `run_movielens.sh`, `run_inat.sh`, `run_inat_round2.sh`, `run_inat_e6.sh`

**Setup**

| Step | Status | Notes |
|---|---|---|
| Server + Python env | ✅ | RTX 5090 (32 GB), 64 cores, 123 GB RAM. `.venv/` |
| AwA2 download (14 GB) | ✅ | `data/awa2/AwA2-data.zip`, read directly from zip |
| CLIP vectors, AwA2 | ✅ | 37,322 images → `cache/awa2/clip_img.npy` |

**AwA2 — round 1 (one seed)** ✅ → `results/awa2/SUMMARY.md`

| Exp | Goal | Status | Result |
|---|---|---|---|
| E1 | G1 blocks mean what they should | ✅ | Habitat 0.90, diet 0.87 (labels 0.61, CLIP 0.31). ⚠️ Taxonomy 0.53 vs labels 0.73 |
| E2 | G2 zoom levels | ✅ | Order best at 8, Family at 32, Genus at 64 (0.99 each, seen species) |
| E3 | G3 normal search | ✅ | 0.821 vs CLIP 0.819 |
| E4 | G4 combined queries | ✅ | Filter 0.75 (labels 0.48); ranking 0.55 (labels 0.38); least mixing |
| E5a | G5 new species | ✅ | Filter 0.72 (labels 0.47) |
| E5b | G5 in-between | ⚠️ | Scores-trained 0.89 (labels 0.59); yes/no-trained only 0.20 |
| E5c | G5 threshold dial | ✅ | Rises every step, 0.10 → 0.92 |

**AwA2 — round 2** ✅ → `results/awa2/round2_summary.md`

| Step | Status | Result |
|---|---|---|
| 3 seeds for everything | ✅ | Very stable: spread ≤ 0.005 on every number. Round-1 results hold. |
| Fairer yes/no-label SSE (SSE-hardJ) | ✅ ⚠️ | In-between 0.62 (was 0.20), but labels alone get 0.59 → SSE does **not** discover much beyond labels. Paper claim: SSE **keeps** graded similarity when trained with it (0.89). |
| Taxonomy weight 0.5 / 1 / 2 | ✅ | No effect: the taxonomy loss is already at its floor. |
| Why taxonomy looked weak (diagnosis) | ✅ ⚠️ | Family level is excellent (same-family AUC 0.994 vs labels 0.985). Weak spot: the **Family prefix forgets Order** (same-order AUC 0.82 vs labels 0.96). Nesting alone does not keep coarser levels. |

**AwA2 — round 3** ✅ → `results/awa2/round3_summary.md`

| Step | Status | Result |
|---|---|---|
| Graded family-tree training (SSE-tree) × 3 seeds | ✅ | **Fix works.** Family prefix now keeps Order: same-order 0.82 → **0.955** (labels 0.96) |
| Effect on queries (E4) | ✅ | Ranking 0.549 → **0.580**; filter unchanged (0.75) |
| Effect on E1 taxonomy | ✅ | 0.53 → **0.72** (labels 0.73) — the old ⚠️ is resolved |
| Effect on new species (zoom) | ✅ | Order@8 0.89 → **0.94**, Family@32 0.96 → **0.99** |
| Cost | ✅ | Seen-species zoom drops slightly (0.985 → 0.974) |
| Chosen for next rounds | ✅ | **SSE-tree** — confirmed on a validation split in round 5 |

**AwA2 — round 4** ✅ → `results/awa2/round4_summary.md`

| Step | Status | Result |
|---|---|---|
| B3 separate vectors × 3 seeds | ✅ | **Matches SSE** on habitat/diet: filter 0.756 vs 0.753, in-between 0.892 vs 0.890, no-mixing equal |
| B4 CSN × 3 seeds | ✅ | Also close: filter 0.745, in-between 0.878. Learned masks overlap ~50% (≈ random) — not interpretable |
| Ranking (family tree) | ⚠️ | SSE 0.580 vs B3 0.541 / CSN 0.543 — **not fair yet**: only SSE had graded tree training |
| Takeaway | ⚠️ | SSE's edge over B3 / CSN is **not accuracy** (confirmed in 4b) → must be shown by cost (E7), compactness (SSE-256), readable layout |

**AwA2 — round 4b + E6** ✅ → `results/awa2/round4b_summary.md`, `results/awa2/e6_summary.md`

| Step | Status | Why |
|---|---|---|
| B3 + CSN with the same graded tree training as SSE × 3 seeds | ✅ ⚠️ | **All three tie** on every accuracy measure (within ±0.005): filter 0.753–0.756, ranking 0.580–0.585, in-between 0.889–0.892 |
| E6 first try (seed 0) | ✅ ⚠️ | Roll-up/drill-down good (Order 0.84, CLIP 0.49). Habitat GROUP BY weak for all — crude "true groups" + many tiny leftover groups |
| E6 improved: better habitat truth (water / jungle / forest / plains) + main-group coverage | ✅ ⚠️ | Roll-up/drill-down solid (0.84–0.88). Habitat: paper's "connected" rule **chains** on graded facets → 2 giant groups |
| E6 with a second grouping rule: center-based ranges (no chaining), × 3 seeds | ✅ | **Yes.** Habitat: SSE 0.17 → **0.50** (CLIP 0.39); stable across seeds. Zoom: Order 0.84, Family 0.88 (CLIP 0.49 / 0.73). SSE ≈ B3 ≈ CSN again → `results/awa2/e6_summary.md` |

**AwA2 — round 5** ✅ → `results/awa2/round5_compact_summary.md`, `round5_val_summary.md`, `r5_seed*/q2.md`

| Step | Status | Why |
|---|---|---|
| Compactness: SSE at 768 / 256 / 128 numbers vs B3 (920), × 3 seeds | ✅ | **SSE-128 = same accuracy as SSE-768 and B3-920** on every facet test; general species search also unchanged (0.83 vs CLIP 0.82–0.84). 7× smaller than B3 |
| Validation split: pick main / tree / treeSC without test (5 training species act as "unseen") | ✅ | **SSE-tree confirmed on validation**: ranking 0.608 vs 0.571 (old), family-tree 0.72 vs 0.55; treeSC ≈ tree |
| Q2 queries: Order prototype filter + habitat band + ranking, × 3 seeds | ✅ | Habitat **band** 0.60 vs labels 0.35, label scores 0.44, CLIP 0.34. Order prototype 0.96. B3/CSN ≈ SSE → `results/awa2/q2_summary.md` |

**AwA2 — B5: ask an AI model** ✅ → `results/awa2/b5/results.md`

| Step | Status | Notes |
|---|---|---|
| Install + download Qwen2.5-VL-7B (~16 GB) | ✅ | |
| Prompt check by hand | ✅ ⚠️ | One-word answer: model says "No" even to brown bear vs polar bear (it names them right). Fix: "name both animals first, then answer" → correct on all test pairs |
| Score 50 queries × 200 candidates, Yes/No version (20k image pairs) | ✅ | 16.3 pairs/s; 2% replies without a clear answer |
| Compare all methods on the same candidates | ✅ ⚠️ | **AI model is NOT an upper bound**: filter 0.48 / ranking 0.31 vs SSE 0.75 / 0.72. Likely cause: Yes/No is too coarse (says "No" to ~95%) |
| Fairer AI version: 0–10 rating instead of Yes/No | ✅ | Better (filter 0.53, ranking 0.57) but **still below SSE** (0.75 / 0.72), labels-scores (0.66 / 0.69) and B3. 8.9 pairs/s → ~25 min per query on 13k images |

**MovieLens (text)** ✅ (first pass)

| Step | Status | Notes |
|---|---|---|
| Download MovieLens 25M (tag genome: 13,816 movies × 1,128 tags) | ✅ | `data/movielens/ml-25m/` |
| Plot text: TMDB overviews ("The Movies Dataset", HF mirror `amnacodes/movies_metadata`, MIT) | ✅ | **13,248 movies (96%)** have a plot; median ~290 characters. Also gives release year, budget |
| Draft tag groups: genre 120 · tone 130 · style 85 · theme 488 · other (excluded) 305 | ✅ ⚠️ | `data/movielens/tag_groups.csv` — **please check by hand** |
| Text encoder | ✅ ⚠️ | Using (please confirm): a sentence model with 768 numbers (BAAI/bge-base-en-v1.5) instead of CLIP text (CLIP cuts text at ~77 tokens) |
| Embed (bge-base), train SSE / SSE-hard / B3 / CSN × 3 seeds, run E1, E3, E4, E5 | ✅ ⚠️ | SSE ≈ 2× plain bge, far above labels; ≈ B3, CSN slightly better. Low absolute numbers (plot text is a weak signal). **Movie facets overlap in reality (0.55–0.69)** → separation can't be shown cleanly here → `results/movielens/SUMMARY.md` |
| Partial-correlation check (own facet, controlling for the others) | ⏳ | Optional: isolates each block's own signal on text |

**iNat (deep family tree, scale)** ✅ → `results/inat/SUMMARY.md`

| Step | Status | Notes |
|---|---|---|
| Download iNat 2021 validation set (8.9 GB: 100k images, 10k species, 10 per species, full family tree, location + date) | ✅ | `logs/inat/download.log`. The 45 GB training set would nearly fill the disk → later, only if E7 needs it |
| CLIP vectors (read straight from the archive, no unpacking) | ✅ | 100k images in 3.5 min |
| Split: 20% of species fully held out ("unseen"); others 7 train / 3 test images | ✅ | 56k train / 24k seen test / 20k unseen (2,000 species). Tree: 273 orders, 1,103 families, 4,884 genera |
| Train SSE-tree `[ taxonomy 128 | rest 640 ]`, prefixes 16 / 64 / 128 = Order / Family / Genus; SSE (yes/no levels); MRL; B3; CSN × 3 seeds | ✅ | |
| E2 zoom levels, E2b, E3 | ✅ ⚠️ | Zoom works: Order peaks at its 16-prefix (0.52), Family at its 64-prefix (0.32), far above cut-short CLIP (0.33 / 0.17). **But graded tree training is worse here than yes/no levels** (Family 0.23 vs 0.32) — with ~5k genera, random pairs almost never share a genus |
| E6 roll-up / drill-down, first try | ✅ ⚠️ | Order level works (ARI 0.67 vs CLIP 0.00). Family/Genus degenerate: only ~7 / ~2 test images per group in the sample, and NMI tuning rewards all-singleton groupings |
| E6 v2: within one class (birds, insects), κ tuned by ARI | ✅ | Center rule: Order 0.66 birds / 0.85 insects (CLIP 0.21 / 0.28); connected rule chains again. SSE ≈ B3 ≈ CSN |
| Round 2: combined loss (graded + contrastive) for SSE, B3, CSN × 3 seeds | ✅ | **treeSC fixes it**: 0.51 / 0.36 / 0.33 (unseen), ties the best; keeps Order in the Family prefix. Recommended recipe for both datasets |

**Final report** ✅ → `REPORT.md` (complete draft, for discussion and edits)

**Next**

| Step | Status |
|---|---|
| E7 cost (storage + query speed) | ⏸️ on hold — start only when you say so |
| Use CLIP for text too (not only images) — e.g. CLIP text encoder for MovieLens / text queries | ⬜ |
| Remove baselines that don't make sense (decide which with the user first) | ⬜ |
| Find benchmarks in other domains (not just animals) where facets + hierarchy make sense | ⬜ |

---

## The big idea (read this first)

We want to show one thing:

> **Our embeddings let you ask database questions about data that has no labels.**

Example question:

> *"Find animals that live in a place like a **swan** does.
> Sort them by how close they are to a **panda** in the family tree."*

Nobody wrote "habitat" or "family" into the data. The embedding knows it.

---

## How our embedding looks

Every image becomes **768 numbers**, split into parts (called **blocks**).
Each block holds one kind of meaning.

```
[ taxonomy | habitat | diet | rest ]
     64        32       16     656      = 768 numbers
```

- **taxonomy** = where the animal sits in the family tree
- **habitat**  = where the animal lives
- **diet**     = what the animal eats
- **rest**     = everything else (keeps normal search working)

The taxonomy block has **zoom levels** (called **prefixes**):

```
numbers 1–8   →  Order   (big groups, e.g. carnivores)
numbers 1–32  →  Family  (e.g. bears)
numbers 1–64  →  Genus   (e.g. pandas)
```

How we build it: take **CLIP** (an existing image/text model, kept unchanged),
and train a **small network** on top that outputs these 768 numbers.

---

## The data

| Dataset | What it is | Why we use it |
|---|---|---|
| **AwA2** (main) | 37k animal photos, 50 species. People scored each species, e.g. "lives in water: 90/100" | Has habitat and diet scores. Has 10 species set aside as "never seen" |
| **iNaturalist 2021 mini** | 500k nature photos, 10k species, full family tree for each photo | Deep family tree. Big enough to test speed |
| **MovieLens Tag Genome** | ~10k movies, each scored 0–1 on ~1,100 tags ("dark", "funny", "time travel") | Shows it works on text, not just images |
| **Animals-90** | The photos in `overleaf/animals/` | Pictures for the paper only |

**Block layouts per dataset:**

```
AwA2:      [ taxonomy 64 | habitat 32 | diet 16 | rest 656 ]
iNat:      [ taxonomy 128 | rest 640 ]            zoom levels: 16 / 64 / 128
MovieLens: [ genre 32 | tone 32 | theme 32 | style 32 | rest 640 ]
```

**Two kinds of test data:**
- **Seen** — new photos of species the model trained on.
- **Unseen** — species the model never saw.

**Answer key:** we use **scores**, not just yes/no.
A seal is 0.6 like a swan (both live in water). A camel is 0.0.
This lets us reward "close but not exact" answers.

---

## The 7 goals

Each goal = one thing we must prove = one experiment.

| # | Goal | In plain words |
|---|---|---|
| **G1** | Blocks mean what they should | The habitat block knows habitat. The taxonomy block knows taxonomy. They don't mix. |
| **G2** | Zoom levels work | Short prefix = Order. Medium = Family. Full = Genus. |
| **G3** | Normal search still works | Adding blocks does not hurt plain "find similar" search. |
| **G4** | Questions get correct answers | Questions like the swan/panda one return the right animals. |
| **G5** | It works where labels fail | New species. "In-between" cases. Stricter threshold = closer matches. |
| **G6** | Grouping and zooming work | GROUP BY on a block makes sensible groups. Zoom in/out works. |
| **G7** | It's cheap | Less storage and fast, compared to other methods. |

**Order:** G1 → G2 → G3 (embedding is good) → G4 → G5 (answers are good) → G6 (database operations) → G7 (cost).

> **Note on G1 and G2:** we train for these directly, so they are not automatic wins.
> What we really check: does it work on **new species**? Do the blocks **interfere**?
> Was our special training **needed**?

---

## What we compare against (baselines)

All of them use the **same CLIP** and the **same labels** as us. Only the method differs.

| # | Name | How it works |
|---|---|---|
| **B1** | Labels + filter | Predict a label ("wetland") for every photo. Store it. Filter on it. |
| **B2** | CLIP + text | No training. Compare photos to phrases like "an animal living in water". |
| **B3** | Separate vectors | One separate vector per attribute. Stored as separate columns. |
| **B4** | CSN | Closest past work. One vector with a learned mask per attribute. |
| **B5** | Ask an AI model | Ask a vision-language model about each photo. Slow but accurate. |
| **B6** | Plain CLIP | Use the normal CLIP vector for everything. The lowest bar. |

**Build order:** B6 + B2 (no training) → B1 → B3 → B4 → B5.

### B1 — Labels + filter, step by step
1. **We train the classifiers ourselves** (on the same CLIP, same labels).
2. Labels come from AwA2 scores: **score ≥ 50 → yes**. An animal can have several habitats.
3. Run the classifiers on every photo. Save the labels as columns.
4. To answer the swan/panda question:
   - swan → "wetland", panda → "bear family"
   - keep rows where habitat = wetland
   - sort: same genus first, then same family, then same order
5. Variant **B1-soft**: save the classifier's scores instead of one label.

### B3 — Separate vectors, step by step
1. Train **one small network per attribute**: habitat, diet, Order, Family, Genus.
2. Store each as its own column (PostgreSQL + pgvector), plus the plain CLIP vector:
   ```sql
   animals(id, clip, habitat, diet, ord, family, genus)
   ```
3. Swan/panda question:
   ```sql
   SELECT id FROM animals
   WHERE similarity(habitat, :swan_habitat) >= :threshold
   ORDER BY distance(family, :panda_family)
   LIMIT 10;
   ```
4. Expect: **similar accuracy, but more storage** (920 numbers vs. our 768),
   5 models, 6 indexes, and the family tree stored 3 times.

### B4 — CSN
Included in the **first round**. Reviewers will ask "how is this different from CSN?"

### B5 — AI model
A **free open model** (e.g. Qwen2-VL or LLaVA), run locally.
Only on a **small sample** (~100 questions × a few hundred photos).

---

## The experiments

Each experiment answers one goal. Same format for each.

### E1 — Do blocks mean what they should? (G1)
- **Data:** AwA2, MovieLens
- **Do:** For each block, check how well it matches **each** attribute.
- **Hope:** Each block matches its own attribute, not the others.
- **Compare to:** B2, B4, B6
- **Figure:** A grid (blocks × attributes). Bright on the diagonal.

### E2 — Do zoom levels work? (G2)
- **Data:** iNat (AwA2 as a second check)
- **Do:** Cut the taxonomy block to different lengths. Check how well each length finds the same Order / Family / Genus.
- **Hope:** Order works with a short cut. Genus needs the full block.
- **Compare to:**
  - same training but one label for all levels
  - cutting a plain embedding
- **Extra:** Show that "switch to the Family zoom" ≠ "loosen the threshold at Genus zoom".
- **Figure:** Line chart. Accuracy vs. length. One line per level.

### E3 — Does normal search still work? (G3)
- **Data:** All three
- **Do:** Plain "find similar" with our full vector vs. plain CLIP. Also try a smaller 256-number version.
- **Hope:** Almost the same results.
- **Figure:** Small table.

### E4 — Do questions get correct answers? (G4)
- **Data:** AwA2, MovieLens
- **Do:** Make ~1,000 questions like the swan/panda one. Check against the answer key.
- **Measure:**
  - Did the right animals pass the filter?
  - Are the closest ones at the top?
  - **No mixing:** swan and otter share a habitat → filtering by either should give similar results.
- **Compare to:** All baselines (B1–B6)
- **Figure:** Main results table + the panda/swan picture.

### E5 — Does it work where labels fail? (G5)
- **Data:** AwA2 (MovieLens too)
- **Do:** Same questions as E4, split into 3 cases:
  - **(a) New species** the model never saw.
  - **(b) In-between:** train a version on **yes/no labels only**. Does it still know a seal is closer to a swan than a camel is?
  - **(c) Threshold:** stricter threshold → closer matches, step by step?
- **Hope:** We hold up. Labels (B1) break on (a) and can't do (b) or (c).
- **Figure:** Bar chart. Us vs. B1, per case.

### E6 — Do grouping and zooming work? (G6)
- **Data:** AwA2 (habitat), iNat (family tree)
- **Do:**
  - GROUP BY on the habitat block. Do groups match real habitats?
  - Group at Order / Family / Genus zoom. Do groups match each level?
- **Figure:** Small table. Match score per level (0 = random, 1 = perfect).

### E7 — Is it cheap? (G7) — light version
- **Data:** iNat
- **Do:**
  - **Storage:** us vs. B1 vs. B3
  - **Speed:** simple timing, us vs. B1 vs. B5
- **Hope:** About as cheap as labels. Much less storage than separate vectors. Much faster than the AI model.
- **Figure:** Accuracy vs. cost. One dot per method.

---

## Grouping and zooming, explained

### Grouping
Normal SQL needs a `habitat` column to GROUP BY. **We don't have one.**
So instead:

1. Connect two animals if their **habitat blocks are similar enough**.
2. Each connected cluster = one group.
3. Count or average per group, like normal SQL.

```
swan — duck — otter     → group 1 (water animals)
camel — fennec fox      → group 2 (desert animals)
polar bear              → group 3 (alone)
```

The similarity cut-off controls group size: low → few big groups, high → many small groups.

### Zooming (roll-up / drill-down)
Like zooming on a map, using the taxonomy zoom levels:

```
Order:    [ Carnivores ]              [ Rodents ]
           /     |     \                  |
Family: [Bears] [Dogs] [Cats]          [Mice]
           |
Genus:  [Ursus] [Panda]
```

- **Drill-down** = zoom in. Split a group using a longer prefix.
- **Roll-up** = zoom out. Merge back using a shorter prefix.

We always split **inside** the parent group.
So "Bears" is always inside "Carnivores", and counts add up.

---

## Priorities (fastest path to results)

**Today — AwA2 only, everything on cached CLIP vectors:**
1. Download AwA2, compute CLIP vectors once (minutes on the RTX 5090).
2. Train SSE (main), SSE-hard (for E5b), SSE-MRL (for E2). Seconds each.
3. Baselines that need no or little training: **B6** plain CLIP, **B2** CLIP+text, **B1** labels (+ B1-soft).
4. Run **E1, E2, E3, E4, E5** → `results/awa2/results.md`.

**Next:**
5. **B3** separate vectors, **B4** CSN.
6. **E6** grouping and zooming.
7. **MovieLens** (E1, E4, E5 on text).

**Later:**
8. **iNat** — disk is tight (56 GB free); start with the iNat *validation* set (100k images, ~9 GB) instead of the 500k training set.
9. **B5** open AI model on a small sample. **E7** cost.

**Q2 (simple choice):** run it on AwA2 **without** the year condition: Order-level filter + habitat similarity band + morphology/full-vector ranking.

**Code:** `/home/mohsen/rVecDB/sse/` — run everything with `scripts/run_awa2.sh`.

---

## Decisions made

| Topic | Decision |
|---|---|
| Main data | AwA2 |
| Other data | iNat 2021 mini, MovieLens Tag Genome, Animals-90 (pictures only) |
| Base model | CLIP ViT-L/14, unchanged |
| Embedding size | 768 (same as CLIP). 256 version tested once (E3, E7) |
| Training labels | Both: scores for the main model; yes/no only for E5(b) |
| Yes/no rule | Score ≥ 50 → yes |
| iNat levels | Order / Family / Genus |
| MovieLens blocks | Genre, Tone, Theme, Style (tags sorted into groups by LLM, checked by hand) |
| B4 (CSN) | First round |
| B5 (AI model) | Free open model, small sample |
| E7 (cost) | Light version |

## Still open

1. How many questions per experiment, and which thresholds to try.
2. Final block sizes for iNat and MovieLens (start values above; tune once).

## Known limit (say it in the paper)

Habitat labels are **per species, not per photo**.
A swan photographed on grass still counts as "wetland".
