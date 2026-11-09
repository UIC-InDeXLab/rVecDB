# How the labels and the filter work (AwA2)

Code: `sse/awa2.py` (labels), `sse/baselines.py` (B1 classifiers), `sse/evaluate.py` (answer key, filter, ranking).

---

## Part 1 — Where the labels come from

AwA2 gives **one row per species** (50 species), not per photo.
Every photo of an otter gets the otter's row.

### Habitat and diet (scores)
People rated each species from 0 to 100 on 85 questions. We use:

- **Habitat (14):** arctic, coastal, desert, bush, plains, forest, fields, jungle, mountains, ocean, ground, water, tree, cave
- **Diet (5):** fish, meat, plankton, vegetation, insects

We divide by 100, so each species gets a list of numbers between 0 and 1:

```
otter habitat:  water 0.9, coastal 0.7, ground 0.4, ... desert 0.0
```

### Yes/no labels (for B1 and SSE-hard)
Simple cut: **score ≥ 0.5 → yes, otherwise no.**

```
otter habitat:  water YES, coastal YES, ground NO, ... desert NO
```

An animal can have several "yes" habitats.

### Taxonomy
Written by hand for the 50 species (`sse/taxonomy_awa2.py`): Order, Family, Genus.

```
giant panda:  Carnivora / Ursidae / Ailuropoda
polar bear:   Carnivora / Ursidae / Ursus
```

### Train / test
- **Train:** 24,270 photos from 40 species.
- **Test (the "database"):** 13,052 photos =
  6,067 new photos of the 40 species + 6,985 photos of **10 species never seen in training**.

---

## Part 2 — The answer key (what is "correct")

Example query:
> *Habitat like **this otter** (x). Sort by how close in the family tree to **this giant panda** (q).*

### Correct filter result
1. Compare the otter's 14 habitat numbers with every database photo's 14 numbers
   (cosine similarity: 1 = same habitats, 0 = nothing in common).
2. Keep the **top 10%, 25% or 50%** most similar (chosen at random per query).
   That set is the **correct filter result**.

Because labels are per species, all photos of one species get the same score. Ties can make the
kept set slightly bigger than the chosen percentage.

### Correct ranking
Points for each photo, compared with the panda:

| Relation to the panda | Points |
|---|---|
| same Family (bears) | 1.0 |
| same Order only (other carnivores) | 0.5 |
| otherwise | 0 |

A photo that **fails the filter gets 0 points**, even if it's a bear.

---

## Part 3 — How each method filters and ranks

Every method does the same 3 steps:

1. **Score** every database photo: "how similar is its habitat to the otter's?"
2. **Keep** the top N, where **N = size of the correct filter result**.
   (Same N for every method, so no method can win by keeping more or fewer.
   This is a simplification: a real system would pick a threshold instead.)
3. **Sort** the kept photos by "how close to the panda in the family tree" and return the **top 10**.

What changes is **how** each method scores in steps 1 and 3:

| Method | Habitat score (step 1) | Family-tree score (step 3) |
|---|---|---|
| **SSE** | similarity of the **habitat block** (numbers 65–96) | similarity of the **first 32 numbers** (Family zoom) |
| **SSE-hard** | same as SSE, but trained on yes/no labels | same as SSE |
| **B1 labels** | predicted yes/no habitats; score = **shared yes / total yes** (Jaccard) | predicted family: **same family = 1, same order = 0.5**, plain CLIP breaks ties |
| **B1-soft** | similarity of the classifier's 14 **probabilities** | similarity of the classifier's **family probabilities** |
| **B2 CLIP+text** | similarity of the photo's match to 14 habitat phrases ("an animal that lives in water") | similarity of the photo's match to family-name phrases |
| **B6 plain CLIP** | similarity of the full CLIP vector | similarity of the full CLIP vector |

---

## Part 4 — How B1's classifiers are built

- One **linear layer** on top of the same frozen CLIP vectors (no deep network).
- Trained on the **same 24,270 training photos** with the **same labels** SSE sees.
- 60 passes over the data, a few seconds on the GPU.

Five classifiers:

| Classifier | Output |
|---|---|
| Habitat | 14 yes/no answers (each "yes" if probability ≥ 0.5) |
| Diet | 5 yes/no answers |
| Order / Family / Genus | pick **one** label each |

**Important:** the Order/Family/Genus classifiers can only pick labels that appear in the
**40 training species**. A photo of an unseen species from a new family (e.g. raccoon,
family Procyonidae) is forced into a wrong family. This is the real weakness of labels,
and part of why B1 does worse on unseen species.

---

## Part 5 — How we score each query

| Measure | Question it answers | Range |
|---|---|---|
| **Filter correct (F1)** | Of the photos the method kept, how many are in the correct filter result? | 0–1 |
| **Filter AP** | If we sort all photos by the method's habitat score, are the correct ones near the top? (no cut needed) | 0–1 |
| **Top-10 pass the filter** | Of the 10 returned photos, how many truly pass the filter? | 0–1 |
| **Ranking quality (NDCG@10)** | Are the returned 10 as good as the best possible 10? (uses the points above) | 0–1 |

Averaged over 1,000 random queries. Also reported separately when the otter
(the filter reference) is from an unseen species.

---

## Part 6 — Design choices to know about

1. **Size-matched filter.** Every method keeps exactly N photos. Fair, but skips choosing a threshold.
   E5c checks thresholds separately.
2. **Labels are per species, not per photo.** A seal on a beach and a seal in water count the same.
3. **SSE-hard is strict.** During training it counted two species as "same habitat" only if
   **all 14** yes/no answers matched. This is likely why it did badly; a fairer version is next.
4. **Reference photos come from the test set.** The otter and panda photos are never training photos.
5. **One run, seed 0.** Needs 3 seeds before going in the paper.
