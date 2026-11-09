# What we know so far (AwA2)

Snapshot: 2026-11-05, after rounds 1–2 (round 3 was still running).
Numbers are averages over 3 random starts; they move by at most ±0.005 between runs.

---

## The setup, in one paragraph

We take **37,322 animal photos** (50 species), turn each into a **CLIP** vector, and train a small
network that rewrites it as **768 numbers in blocks**:
`[ taxonomy 64 | habitat 32 | diet 16 | rest 656 ]`.
The taxonomy block has zoom levels: first 8 numbers = Order, first 32 = Family, all 64 = Genus.
We train on **40 species** and test on new photos of those 40 **plus 10 species the model never saw**
(including the **giant panda**, the seal and the leopard).

---

## ✅ What works

### 1. Each block really holds its meaning
How well a block's similarity matches the true similarity (1 = perfect):

| | Habitat | Diet |
|---|---|---|
| **SSE (its own block)** | **0.90** | **0.87** |
| Classifier scores (B1-soft) | 0.76 | 0.79 |
| Yes/no labels (B1) | 0.61 | 0.59 |
| Plain CLIP | 0.31 | 0.28 |
| CLIP + text prompts | 0.26 | 0.17 |

→ Plain CLIP and text prompts **can't** answer "habitat like a swan". The blocks can.

### 2. The blocks don't mix
Swan vs. otter (same habitat, different family) should give **similar** habitat-filter results.
Polar bear vs. panda (same family, different habitat) should give **different** ones.
Error (lower = better): **SSE 0.15** · others 0.19 – 0.55.
→ The habitat block isn't secretly "looks like the same animal". This is the panda figure, as a number.

### 3. The example queries give better answers
"Filter by habitat like X, rank by family closeness to Y" — 1,000 queries:

| | Filter correct | Ranking quality |
|---|---|---|
| **SSE** | **0.75** | **0.55** |
| Classifier scores | 0.67 | 0.46 |
| Yes/no labels (the usual DB approach) | 0.48 | 0.38 |
| Plain CLIP | 0.55 | 0.40 |

### 4. It works on species it never saw
Filter correct when the reference animal is an unseen species: **SSE 0.72** vs. labels 0.47.

### 5. The threshold works like a smooth dial
Stricter threshold → truly closer habitats, **at every step** (0.10 → 0.92).
Labels jump up and down; plain CLIP stays flat until the very end.

### 6. Zoom levels work — and need special training
Each prefix is best at **its own** level (seen species): Order @8 = 0.998, Family @32 = 0.995, Genus @64 = 0.993.
On unseen species, Order with 8 numbers:

| | Order @ 8 numbers |
|---|---|
| **SSE (a label per level)** | **0.90** |
| Same training, Genus label everywhere (MRL-style) | 0.78 |
| Just cutting CLIP short (PCA) | 0.64 |

→ Nesting alone doesn't give you levels; you have to train each level.

### 7. Normal search is not hurt
Same-species search: **SSE 0.822** vs. CLIP 0.819. 84% of the top-10 results are the same.

### 8. Results are stable
Three random starts → every number within ±0.005.

---

## ⚠️ What doesn't work (yet)

### A. SSE does not *discover* "in-between" from yes/no labels
Trained on **scores** ("lives in water: 90/100"): in-between score **0.89** (labels: 0.59).
Trained on **yes/no labels only**: 0.20 (strict version), 0.62 (fairer version) — barely above
the labels themselves (0.59).
→ **SSE keeps graded similarity when you give it; it doesn't invent it.**

### B. The Family prefix forgets the Order
| Question | SSE Family prefix | Labels |
|---|---|---|
| Same **family** or not? | **0.994** | 0.985 |
| Same **order** or not? | 0.82 | **0.96** |

A bear and a dog (both carnivores) look as unrelated as a bear and a mouse.
→ Nested prefixes don't automatically keep the coarser level. **Round 3 tests a fix**
(train each prefix with graded family-tree similarity).

### C. Giving taxonomy more weight does nothing
Weights 0.5 / 1 / 2 → identical results. Its loss is already at the floor; the fix has to change
*what* it learns (point B), not *how much*.

### D. Only ~56% of SSE's top-10 truly pass the habitat filter
Best of all methods (labels: 36%), but room to improve.

---

## 🔍 Side findings

- **CSN (closest prior work)**: its learned masks overlap ~50% — about what random would give.
  They don't specialize per attribute, so you can't read off "this part = habitat". SSE's blocks are
  fixed and readable by design. (Full accuracy comparison: round 4.)
- **Separate vectors (B3)** are trained; they store 920 numbers per item vs. SSE's 768.
  (Accuracy comparison: round 4.)

---

## 📄 What this means for the paper

**Claims the data supports:**
1. One embedding can hold several queryable facets that stay separate.
2. Database-style queries on unlabeled data beat the "classifier → labels → filter" approach.
3. It works on unseen species.
4. Thresholds act as a smooth, meaningful dial (labels can't do this).
5. Zoom levels work, but only with per-level training (vs. MRL-style).
6. It costs nothing for normal search.

**Claims to change or drop:**
- ❌ "SSE recovers in-between similarity from simple labels." → ✅ "SSE **keeps** graded similarity
  that labels throw away."
- ⚠️ "Prefixes give a clean hierarchy" — true per level, but coarser levels fade in longer prefixes
  (pending the round-3 fix).

---

## ⚠️ Caveats (be honest about these)

1. **Labels are per species, not per photo.** A swan on grass is still "wetland".
2. **Settings were chosen by looking at test results.** Before final numbers, pick settings on a
   separate validation split.
3. **The unseen-species test is small and easy for Family/Genus** (10 species, mostly in different
   families). iNat is the real hierarchy test.
4. **One dataset, all mammals.** MovieLens (text) and iNat (all of nature) still to come.
5. **Not yet compared** to separate vectors (B3), CSN (B4) or an AI model (B5) on accuracy.

---

## What's running / next

- 🔄 Round 3: graded family-tree training (fix for B).
- ⏳ Round 4: B3 separate vectors + B4 CSN, 3 seeds.
- ⬜ Then: validation split · E6 grouping/zooming · MovieLens · iNat + cost · B5.
