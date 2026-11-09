# Relational-Vector Databases with Schema-Structured Embeddings — Experiment Report

*Status: complete draft for discussion · covers everything run up to 2026-11-06 · E7 (cost/speed) is on hold*

---

## How to read this report

- **Part 1** explains the idea from scratch. Skip it if you know the paper.
- **Part 2** lists what we set out to show (the goals). Every result later points back to one of these.
- **Part 3** explains how we tested: data, models, competitors, and how answers are scored.
- **Part 4** gives the results, one goal at a time. Each section has the same shape:
  *the question → how we tested → numbers → what it means → caveats.*

All numbers are averages over **3 random training runs (seeds)** unless marked otherwise. The spread
between runs is tiny (usually ±0.005 or less), so differences of a few hundredths are real only when
they are bigger than that.

---

# Part 1 — The idea in plain words

## 1.1 The problem

Vector databases store an **embedding** (a list of numbers, e.g. 768 of them) for each object — an
image, a text — and can find "similar" objects. But "similar" means *similar overall*. Real questions
are usually about **specific aspects**:

> *"Find animals that live in a place like a **swan** does,
> and sort them by how close they are to a **panda** in the family tree."*

Today you can only answer this if someone **stored columns** like `habitat = wetland` and
`family = Ursidae` for every object. In many domains (ecology, medicine, user uploads) those columns
do not exist, are expensive to create, or are too coarse ("wetland" vs "forest" says nothing about
*how* similar two habitats are).

## 1.2 Our idea: Schema-Structured Embeddings (SSE)

We make one embedding whose numbers are **organized by meaning**. The embedding is split into
**blocks**; each block is responsible for one aspect (a "facet"):

```
one embedding, 768 numbers
[ taxonomy | habitat | diet | rest ]
     64        32       16     656
```

- **taxonomy** block: where the animal sits in the family tree
- **habitat** block: where it lives
- **diet** block: what it eats
- **rest**: everything else, so ordinary "find similar" search still works

A block that represents a **hierarchy** has **zoom levels**, called **prefixes**:

```
taxonomy numbers 1–8   → Order   (coarse: carnivores, rodents, …)
taxonomy numbers 1–32  → Family  (bears, dogs, cats, …)
taxonomy numbers 1–64  → Genus   (fine: Ursus, Panda, …)
```

With this, the example question becomes pure vector math, with **no stored labels**:

- **Filter:** keep animals whose *habitat block* is close to the swan's habitat block.
- **Rank:** sort them by how close their *taxonomy numbers 1–32 (Family)* are to the panda's.

The paper also defines database operations on top: **GROUP BY** on a block, **roll-up / drill-down**
across zoom levels, **joins** on a block.

## 1.3 How we build an SSE

We take an existing, frozen model (**CLIP** for images, **bge** for text) and train a **small
network on top** (two layers) that outputs the 768 structured numbers. The big model is never
changed. Training takes **seconds** on our GPU.

### What the training looks at

Training shows the network many **pairs** of training items (e.g. two animal photos) and asks for
three things at once:

| Part of training | What it asks for | Example |
|---|---|---|
| **Keep general similarity** | The full 768-number vector should rate the pair about as similar as CLIP does | Two photos of the same dog stay close overall |
| **Facet blocks** | The *habitat block* should rate the pair as similar as their **true habitat similarity** (same for diet, etc.) | Swan vs. otter → habitat blocks close; swan vs. camel → far |
| **Zoom levels** | Each *prefix* should rate the pair by the family tree at its level: same genus > same family > same order > unrelated | Bear vs. dog: close at the Order prefix (both carnivores), far at the Genus prefix |

### Do we need labels?

**Only for the training items, and only once.**
- **AwA2:** 40 rows of species ratings covered all 24,270 training photos.
- **iNat:** its built-in taxonomy.
- **MovieLens:** its tag scores.

Graded similarity works better than yes/no labels (4.5b).

**After training, no labels are needed.** New items get their SSE straight from the photo or text.
The 10 unseen AwA2 species and 2,000 unseen iNat species never had labels and still worked (4.2,
4.5a).

**With no labels at all,** something must still define "habitat". That could be a knowledge base,
or an AI model rating training pairs once. The AI-model option is not tested yet.

---

# Part 2 — What we wanted to show

## 2.1 The goals

| # | Goal | In plain words |
|---|---|---|
| **G1** | Blocks mean what they should | The habitat block knows habitat, the taxonomy block knows taxonomy, and they don't mix. |
| **G2** | Zoom levels work | The short prefix captures Order, the medium one Family, the full block Genus. |
| **G3** | Normal search still works | Adding structure does not hurt plain "find similar" search. |
| **G4** | Combined queries give correct answers | Questions like the swan/panda one return the right objects. |
| **G5** | It works where labels fail | (a) species never seen in training, (b) "in-between" similarity (a seal is *somewhat* like a swan), (c) a threshold that acts like a precise dial. |
| **G6** | Database operations work | GROUP BY on a block makes sensible groups; roll-up / drill-down moves cleanly between levels. |
| **G7** | It is practical | Small, cheap and fast compared to the alternatives. *(Storage part done; speed study E7 is on hold.)* |

**How the goals fit together.** The paper makes one big promise: *one embedding with meaningful
parts can answer database-style questions without stored labels.* That promise breaks down into
three layers, and we check each one:

```
Layer 1 — the parts are right       G1 (blocks = facets)    G2 (prefixes = zoom levels)   G3 (nothing lost)
Layer 2 — queries on top are right  G4 (filter + rank)      G5 (cases where labels fail)  G6 (GROUP BY, roll-up)
Layer 3 — it is worth using         G7 (size, speed)
```

If Layer 1 fails, nothing above it can work. Layer 2 is what a database user actually sees. Layer 3
is what decides whether anyone would build this.

## 2.2 Each goal explained

Every goal below has the same parts: **the claim**, **why it matters**, **an example**, **what could
go wrong**, **how we test it**, **what success looks like**, and **the short answer** (details in
Part 4).

---

### G1 — Each block means what it should (and only that)

- **The claim.** The habitat block (numbers 65–96) holds *where the animal lives*. The diet block
  holds *what it eats*. The taxonomy block holds *where it sits in the family tree*. Each block
  holds its own facet and **not** the others.
- **Why it matters.** Every query in the paper reads one block, e.g. "habitat close to the swan".
  If the habitat block secretly encodes "looks like a bird", the filter returns birds, not
  water animals.
- **Example.** A **swan** and an **otter** look nothing alike, but both live in water, so their
  *habitat blocks* should be close. A **swan** and an **ostrich** are both birds, but they live in
  very different places, so their habitat blocks should be far apart, even though their taxonomy
  blocks are close.
- **What could go wrong.**
  - (1) The block learns little: training is too weak.
  - (2) The blocks **leak** into each other: the habitat block secretly learns taxonomy instead of
    habitat. This can happen because in our data many water animals are close relatives. Killer
    whale, blue whale, humpback whale and dolphin are all cetaceans; seal and walrus are both
    pinnipeds. So on most training pairs, "lives in water" and "is a whale-or-seal kind of animal"
    give the same answer. The network can take the **shortcut** of recognizing the animal *kind*
    (easy to see in a photo) instead of learning habitat.

    The shortcut is caught on pairs where **habitat and taxonomy disagree**:

    | Pair | True habitat | True taxonomy | A real habitat block says | A leaked habitat block says |
    |---|---|---|---|---|
    | otter – weasel | different (water vs fields/ground) | same family (Mustelidae) | **far** ✓ | close ✗ (relatives) |
    | otter – seal | same (water) | different families | **close** ✓ | farther ✗ |
    | polar bear – grizzly bear | different (arctic vs forest) | same genus (*Ursus*) | **far** ✓ | close ✗ (relatives) |

    With a leaked block, a "habitat like the otter's" query would return weasels. We check for this in
    two places: here in G1, by also comparing the habitat block with *true taxonomy*, where a high
    score would mean leakage; and in G4's **no-mixing test**, which uses exactly such disagreeing
    pairs.

    The habitat–taxonomy score is not expected to be 0: habitat and taxonomy really do overlap
    somewhat in nature. What we look for is that it is **much lower** than the habitat–habitat score.
- **How we test it.** We take 200,000 random pairs of test photos. For each block, we check whether
  its similarity goes up and down with the **true** similarity of that facet (the "match score").
  To check **leakage**, we also compare each block with the *other* facets; that score should be
  lower. Competitors are scored the same way, each using its own way of measuring habitat
  similarity (see 2.4).
- **Success looks like.** Two separate checks:
  1. **Accuracy, compared across methods:** SSE's habitat view follows true habitat better than
     stored labels and much better than plain CLIP. The same holds for diet and taxonomy.
  2. **Separation, inside SSE only:** SSE's habitat block follows habitat **much more** than it
     follows diet or taxonomy. For example, a swan and an otter score high, a swan and an ostrich
     score low.
- **Short answer.** ✅ Habitat 0.90, diet 0.87, taxonomy 0.72; plain CLIP only ≈0.3. The habitat
  block matches diet only 0.42 and taxonomy only 0.31, so the blocks stay mostly separate.
  Separate vectors (B3) and CSN do equally well. → **4.1**

---

### G2 — The zoom levels (prefixes) work

- **The claim.** Inside the taxonomy block, the **first few numbers** answer the coarse question
  (same *Order*?), **more** numbers answer the medium question (same *Family*?), and **all** numbers
  answer the fine question (same *Genus*?). One block, three levels, picked by how many numbers you
  read.
- **Why it matters.** This is what makes **roll-up / drill-down** possible without storing three
  label columns, and it lets a query say "close at the Family level".
- **Example.** Polar bear, giant panda, wolf. At the **Order** level (first 8 numbers) all three are
  carnivores, so all are close. At the **Family** level (first 32) the polar bear and panda are both
  bears, so they stay close, while the wolf (dog family) moves away. At the **Genus** level (all 64)
  the polar bear (*Ursus*) and panda (*Ailuropoda*) separate too.
- **What could go wrong.**
  - (1) A short prefix is just a blurry copy of the full vector, not a real "Order" view.
  - (2) Training the finer level makes the coarser one **forget**, e.g. the Family prefix no longer
    knows that bears and wolves share an Order. This actually happened.
  - (3) It only works on a tiny tree (AwA2, 50 species), not a real one.
- **How we test it.** We cut the block to 8 / 32 / 64 numbers (16 / 64 / 128 on iNat) and search
  for "same Order", "same Family" and "same Genus" (measure: mAP). We do this on **seen and unseen
  species**, and on two trees: AwA2 (small) and iNat (10,000 species, deep). We compare with
  "MRL-style" (nested prefixes, but every prefix trained on the same fine label) and with CLIP
  shortened by PCA. Both are nested but **not** trained level by level.
- **Success looks like.** Each prefix is good at its own level, keeps the coarser levels, and beats
  the nested-but-not-level-trained versions.
- **Short answer.** ✅ AwA2 Order at 8 numbers: 0.99 seen / 0.94 unseen (MRL-style 0.78, PCA 0.65).
  On iNat, level-specific training also clearly wins. ⚠️ It needs **tree-aware training**; plain
  nesting is not enough. → **4.2**

---

### G3 — Ordinary search still works

- **The claim.** Adding blocks does not hurt plain "find things similar to this photo" search with
  the **full** vector.
- **Why it matters.** A database will still get plain similarity queries. If SSE makes those worse,
  people would need to keep the old embedding too, and SSE loses its "one vector" advantage.
- **Example.** Search with a zebra photo. The top results should still be zebras, as with CLIP.
- **What could go wrong.** Squeezing facets into blocks uses up "space", so general look-alike
  information is lost.
- **How we test it.** Same-species search (mAP) with the full SSE vs. plain CLIP (bge for movies),
  plus how many of the top-10 results are the same as CLIP's.
- **Success looks like.** About equal to CLIP.
- **Short answer.** ✅ AwA2 0.82 vs CLIP 0.82; iNat 0.12 vs 0.11; top-10 lists mostly shared
  (74–86%). → **4.3**

---

### G4 — Combined queries give correct answers

- **The claim.** The paper's example queries, written as vector math on blocks, return the right
  objects. This is G1 + G2 *used together*, as a real query.
- **Why it matters.** This is the user-facing promise: the swan/panda figure in the paper.
- **Example.** *"Animals that live in a place like a swan's (**filter** on the habitat block), sorted
  by how close they are to a panda at the Family level (**rank** on the taxonomy prefix)."* An ideal
  answer contains only water animals, ranked with the polar bear first (a bear, like the panda),
  then other carnivores such as otter and seal, then unrelated water animals such as whales. Desert
  and forest animals should not appear at all.
- **What could go wrong.**
  - (1) The filter lets wrong items through or drops right ones.
  - (2) The ranking is off.
  - (3) **Facet mixing**: the habitat filter is fooled by taxonomy. Starting from a swan you get
    "birds"; starting from a polar bear you get "bears".
- **How we test it.** 1,000 random filter-and-rank queries on AwA2, scored with the graded answer
  key: filter F1 (are the right items kept?) and NDCG@10 (are the top 10 the best ones, in order?).
  For mixing: two references with **the same habitat but different taxonomy** (swan vs. otter)
  should give the same filter result, and so should two with the same Family but different habitat
  (polar bear vs. giant panda). The difference is the "no-mixing error". Plus **Q2-style** queries
  from the paper: an *Order prototype* combined with a *habitat band* ("somewhat similar", not
  "very similar").
- **Success looks like.** Clearly better than labels and plain CLIP on F1, NDCG and mixing.
- **Short answer.** ✅ Filter 0.75 vs labels 0.48; ranking 0.58 vs 0.38; mixing error lowest
  (0.15). Habitat band 0.60 vs labels 0.35. B3 and CSN tie with SSE. → **4.4**

---

### G5 — It works where labels fail

This is the **reason** for SSE over plain label columns, so it has three parts, each a specific
weakness of labels:

- **(a) New kinds of objects (unseen species).**
  - *Labels fail* because a classifier can only output classes it was trained on. A giant panda
    photo gets forced into some wrong known species or habitat class.
  - *SSE claim:* a panda photo still lands in sensible places in each block.
  - *Test:* combined queries whose reference is one of the 10 never-trained species.
- **(b) In-between similarity.**
  - *Labels fail* because a label is yes/no: "seal: ocean", "swan: lake" counts as simply
    *different*. But a seal is *somewhat* like a swan in habitat (both water), and a camel is not
    at all.
  - *SSE claim:* the habitat block knows "somewhat similar".
  - *Test:* take only pairs that labels call "different habitat" and check whether the method still
    ranks them by true closeness (seal–swan above camel–swan).
  - We also train SSE on yes/no labels only (SSE-hard) to see whether it can *discover* in-between
    similarity by itself.
- **(c) A threshold that works like a precise dial.**
  - *Labels fail* because a label gives one cut ("same habitat or not"), with nothing in between.
  - *SSE claim:* moving the similarity threshold step by step gives results that get steadily more
    similar, like a volume knob.
  - *Test:* sort results by the method's habitat score into 10 steps and measure the **true**
    similarity in each step. It should rise at every step.
- **Success looks like.** SSE beats labels on all three, clearly.
- **Short answer.**
  - (a) ✅ Unseen species: 0.72 vs labels 0.47.
  - (b) ✅ 0.89 vs labels 0.59, but ⚠️ only when trained on graded scores. From yes/no labels
    alone it gets 0.62 ≈ labels.
  - (c) ✅ The SSE dial rises at every step (0.10 → 0.92); labels jump around.
  
  → **4.5**

---

### G6 — Database operations work: GROUP BY and roll-up / drill-down

- **The claim.** The paper's new operators work on vectors:
  - **GROUP BY a block:** group items whose habitat blocks are close, *without* a habitat column.
  - **Roll-up / drill-down:** group at the Order prefix, then split each group at the Family prefix,
    then at the Genus prefix. Each small group sits inside exactly one bigger group, like a
    folder tree.
- **Why it matters.** These are the "relational" half of "relational-vector database". Search alone
  (G4) is something vector databases already do; grouping by a *facet* is new.
- **Example.**
  - *GROUP BY habitat:* water animals (whales, seal, otter, beaver, hippo, polar bear) in one
    group, jungle animals in another, and so on.
  - *Drill-down:* "Carnivores" → splits into "bears", "cats", "dogs", … → "bears" splits into
    *Ursus* and *Ailuropoda*.
- **What could go wrong.**
  - (1) **Chaining**: whale ~ seal ~ otter ~ beaver ~ … ~ deer are each similar to the next, so a
    rule that "links neighbors" puts everything into one giant group. This happened with the
    paper's current rule.
  - (2) The groups at different levels do not nest properly.
  - (3) It only works on a tiny tree.
- **How we test it.**
  - *True habitat groups:* we cluster the 50 species by their human habitat ratings into 4 groups
    (water / jungle / forest / plains).
  - We run GROUP BY on the test photos and compare the groups found with the true ones (NMI / ARI),
    for the paper's "connected" rule and a new "center" rule (both explained with an example in
    4.6).
  - We do the same at Order / Family / Genus on AwA2 and on iNat birds and insects (deep tree).
  - The grouping threshold is tuned on **training** photos only.
- **Success looks like.** Groups match the truth well and clearly beat plain CLIP, and every level
  nests inside the one above.
- **Short answer.**
  - ✅ Roll-up / drill-down works: AwA2 0.84 / 0.88 / 0.84. On iNat, Order is about 3× better than
    CLIP.
  - ⚠️ Habitat GROUP BY is only moderate (0.50), and **only with the new "center" rule**. The
    paper's rule gives 0.17.
  
  → **4.6**

---

### G7 — It is practical (size and speed)

- **The claim.** One SSE vector is cheaper than the alternatives:
  - **smaller** than storing separate vectors per facet (B3);
  - **far faster** than asking an AI model per pair (B5);
  - **no extra index** per facet.
- **Why it matters.** If SSE were as accurate but 5× bigger or slower, nobody would use it. And
  since B3 and CSN *tie* SSE on accuracy (G1, G4), cost is where SSE has to win.
- **Example.** To answer "habitat like a swan, Family like a panda", B3 must store and index a
  habitat vector, three taxonomy vectors and a general vector (6 columns, 5 models). SSE stores one
  vector and reads parts of it.
- **What could go wrong.** Shrinking SSE might cost accuracy; a vector DB might not speed up
  "read only part of a vector" in practice.
- **How we test it.**
  - *Done:* shrink only the "rest" part of SSE (768 → 256 → 128 numbers) and re-run the key tests;
    compare the size with B3. We also measured how fast the AI model (B5) is.
  - *On hold (E7):* storage on disk and query speed inside a real vector database.
- **Success looks like.** The same accuracy at a much smaller size.
- **Short answer.** ✅ SSE-128 ≈ SSE-768 ≈ B3, at **128 vs 920 numbers (7× smaller)**. The AI model
  is about 9–16 pairs per second, far too slow to scan a database. ⏸️ The speed study is on hold.
  → **4.7, 4.8**

---

## 2.3 Who we must beat (and why each one matters)

| # | Competitor | How it answers the swan/panda question | Why a reviewer would ask about it |
|---|---|---|---|
| B1 | **Labels + filter** | Train classifiers, store predicted labels ("wetland", "Ursidae") as columns, filter on them | The standard database answer today |
| B2 | **CLIP + text prompts** | No training: compare each image with phrases like "an animal living in water" | Cheap, no training at all |
| B3 | **Separate vectors** | One separate small vector per facet / level, stored as separate columns (pgvector, Milvus) | What practitioners do today |
| B4 | **CSN** (Conditional Similarity Networks, Veit et al. 2017) | One vector plus a *learned* mask per facet | The closest published idea |
| B5 | **Ask an AI model** | Show a vision-language model both images and ask (Qwen2.5-VL-7B) | Possibly most accurate, but slow |
| B6 | **Plain embedding** | Use the normal CLIP / bge vector for everything | The lowest bar |
| — | **MRL-style** (ablation, not a competitor) | Nested prefixes, but every prefix trained on the same label | Tests whether *level-specific* training matters |

**Fairness rules:** every method uses the **same frozen base model**, the **same training labels**, and
(for methods that train) the **same loss recipe**. Only *how meaning is stored* differs.

## 2.4 How each competitor works, step by step

### The common frame: every method answers the same four questions

To be compared, every method must be able to say, for **any two items**:

| Question | Used in |
|---|---|
| How similar are these two in **habitat**? | G1, G4 filter, G5, G6 |
| How similar are they in **diet**? | G1 |
| How similar are they in **taxonomy** (at the Family level, or at Order / Genus)? | G1, G2, G4 ranking, G6 |
| How similar are they **overall**? | G3 (plain search) |

Each method answers with **one number per question**. The tests only use these numbers, so the
methods differ only in **how they compute them**.

**Everyone starts from the same input.** Every photo is run once through CLIP's image encoder,
which gives 768 numbers per photo. These are saved and shared by all methods. No method sees the
photo pixels again, except B5 (the AI model).

**How a combined query runs (G4), the same for every method.** The query is *"habitat like the
swan's, ranked by Family closeness to the panda"*:

1. **Filter.** Compute every photo's *habitat similarity* to the swan photo. Keep the top **N**,
   where N is how many photos *truly* pass. We give every method the same N, so no method wins or
   loses just by choosing a better cut-off. We only test whether it keeps the *right* N.
2. **Rank.** Among the kept photos, sort by *taxonomy similarity* to the panda photo. Return the
   top 10.

---

### B6: Plain CLIP (or plain bge for movies), the "do nothing" floor

- **What it stores per item:** the 768 CLIP numbers. Nothing else.
- **Training:** none.
- **How it answers all four questions:** the cosine between the two photos' 768-number vectors. It
  is the **same number** for habitat, diet, taxonomy and overall, because CLIP has no parts.
- **Example:** cosine(swan, ostrich) = high (both look like big birds). So plain CLIP says "similar
  habitat", which is wrong.
- **Why it's here:** it shows what you get with no facet structure at all. Any method worse than
  this is useless.

---

### B2: CLIP + text prompts, the "just ask CLIP in words" method

- **What it stores per item:** a short score profile per facet:

  | Facet | Profile length | What each number is |
  |---|---|---|
  | Habitat | 14 | one per habitat sentence |
  | Diet | 5 | one per diet sentence |
  | Taxonomy | one per name | one per taxonomy name |

- **Training:** none.
- **How it is built:**
  1. Write one sentence per habitat: "a photo of an animal that lives in water", "… in a desert",
     "… in a forest", … (14 sentences, matching AwA2's 14 habitat ratings). Diet: "… that eats
     fish", "… eats meat", "… eats plants", "… eats insects", "… eats plankton". Taxonomy: "a photo of
     an animal of the family Ursidae", one per name.
  2. CLIP's **text** encoder turns each sentence into 768 numbers (once).
  3. For each photo, compute the cosine between its CLIP vector and each sentence vector. This gives
     the photo's **profile**.
  4. Subtract each sentence's average score over all photos. Otherwise every photo scores about 0.2
     on everything and all profiles look alike.
- **How it answers "habitat similarity of two photos":** the cosine of their two **14-number**
  profiles.
- **Worked example (3 sentences instead of 14):**
  ```
               water  desert  forest
  swan       [ 0.30   0.10    0.15 ]   leans "water"
  otter      [ 0.28   0.09    0.20 ]   leans "water"
  camel      [ 0.11   0.31    0.12 ]   leans "desert"

  cosine(swan, otter) → high  → "similar habitat"   ✓
  cosine(swan, camel) → low   → "different habitat" ✓
  ```
- **Overall similarity:** plain CLIP cosine.
- **Movies:** one sentence per tag in the facet ("a movie that is dark", "a movie that is funny",
  …), encoded with bge.
- **Why it's here:** it is the cheapest possible facet method, with no training and no labels. The
  profile has the same shape as a classifier's habitat scores, but its numbers come from CLIP's
  word matching instead of a trained classifier.
- **Weakness:** CLIP matches what is *visible* in the photo. A deer photographed in a zoo shows grass
  and a fence, not a forest. We used one phrasing per habitat; averaging several phrasings is a
  standard trick that could make it a bit stronger (not tried).

---

### B1: Labels + filter, today's standard database answer

The usual way to support these queries today: **predict labels, store them as columns, filter on
them.**

- **What it stores per item:** predicted label columns, e.g.:
  ```
  photo_123:  habitat = {water, ocean, coastal}   diet = {fish, meat}
              order = Carnivora   family = Phocidae   genus = Phoca
  ```
- **Training:** five small classifiers, each a **single linear layer** on top of the CLIP vector
  (a "linear probe", the standard cheap classifier), trained on the **training photos only**:

  | Classifier | Output | Training answer comes from |
  |---|---|---|
  | Habitat | 14 yes/no answers ("lives in water?" …) | "yes" if AwA2's human rating ≥ 50 / 100 |
  | Diet | 5 yes/no answers | same rule |
  | Order | one Order name | the hand-written family tree |
  | Family | one Family name | same |
  | Genus | one Genus name | same |

  The taxonomy classifiers can only output names that appear among the **40 training species**.
  An unseen species, e.g. giant panda, is forced into one of the known names.
- **How it answers "habitat similarity":** the overlap of the two yes-sets (Jaccard = shared ÷
  total):
  ```
  swan  = {water, coastal, ground}
  otter = {water, coastal, ground, forest}
  overlap = 3 shared / 4 total = 0.75
  ```
- **How it answers "taxonomy similarity":** 1 if the predicted Family is the same, 0.5 if only the
  Order is the same, 0 otherwise. A tiny bit of CLIP similarity is added only to break ties.
- **Overall similarity:** plain CLIP cosine.
- **Movies:** one yes/no classifier per facet, with one output per tag ("is this movie *dark*?"),
  trained on "tag score ≥ 0.5".
- **Why it's here:** it is what a database user does today. Its weaknesses are exactly what G5
  tests: it can't express "somewhat similar", and it can't name unseen species correctly.

---

### B3: Separate vectors, what practitioners do today

Vector databases (pgvector, Milvus, …) let you store **several vector columns** per row. So a
natural design is one small vector per facet and per level.

- **What it stores per item:** six vectors, **920 numbers** in total:

  | Column | Size |
  |---|---|
  | habitat vector | 32 |
  | diet vector | 16 |
  | Order vector | 8 |
  | Family vector | 32 |
  | Genus vector | 64 |
  | plain CLIP vector (for overall search) | 768 |

- **Training:** **five separate small networks** (each takes the CLIP vector, 2 layers). Each one is
  trained **only** on its own goal, with the **same loss SSE uses for that part**. For example, the
  habitat network learns "cosine of two habitat vectors ≈ their true habitat similarity". In the
  final runs, the taxonomy networks get the same graded family-tree loss as SSE-tree.
- **How it answers:** habitat = cosine of the two habitat vectors; Family = cosine of the two
  Family vectors; overall = plain CLIP cosine.
- **Difference from SSE:** SSE is **one** network and **one** 768-number vector. Its parts are fixed
  slices (habitat = numbers 65–96), and the zoom levels are *prefixes of the same block*, not three
  separate vectors. B3 needs 5 models + CLIP, 6 columns and 6 indexes.
- **iNat:** only the three taxonomy vectors (Order 16, Family 64, Genus 128). "B3-SC" is the version
  trained with the same graded + yes/no recipe as SSE-treeSC.
- **Why it's here:** it is the obvious engineering alternative. If SSE is not better than this,
  why bother? (Answer from the results: same accuracy; SSE wins on size and simplicity, see 4.7.)

---

### B4: CSN, Conditional Similarity Networks, the closest published idea

From Veit et al., CVPR 2017. Like SSE, it puts **all facets into one vector**. The difference is how
it decides which numbers belong to which facet.

**The idea in one sentence.** Each item gets one vector. Each facet gets a **mask**: a list of
weights, one per number in the vector, that says *how much each number matters for this facet*.
To compare two items on a facet, you first multiply both vectors by that facet's mask, then compare.

**A tiny example (6 numbers instead of 768, two facets):**

```
                     n1    n2    n3    n4    n5    n6
seal vector       [ 0.9   0.1   0.8   0.2   0.7   0.3 ]
otter vector      [ 0.8   0.2   0.1   0.9   0.6   0.4 ]

habitat mask      [ 1.2   0.0   0.0   0.0   0.9   0.0 ]   ← learned: n1 and n5 matter for habitat
taxonomy mask     [ 0.0   0.0   1.1   0.8   0.0   0.5 ]   ← learned: n3, n4, n6 matter for taxonomy
```

- **Habitat similarity:** multiply both vectors by the habitat mask, which keeps only n1 and n5:
  ```
  seal  → [1.08, 0, 0, 0, 0.63, 0]
  otter → [0.96, 0, 0, 0, 0.54, 0]    → cosine ≈ 1.0   "same habitat"  ✓ (both water)
  ```
- **Taxonomy similarity:** multiply by the taxonomy mask, which keeps n3, n4 and n6:
  ```
  seal  → [0, 0, 0.88, 0.16, 0, 0.15]
  otter → [0, 0, 0.11, 0.72, 0, 0.20] → cosine ≈ 0.35  "not closely related"  ✓
  ```

The same two stored vectors give different answers depending on which mask you use.

**How it is trained (our version):**
1. **One network** (the same small kind SSE uses) turns each photo's CLIP vector into 768 numbers.
2. **Five masks** are learned at the same time: habitat, diet, Order, Family and Genus. Each is
   768 weights.
   - Weights can't be negative.
   - They start around 0.9 (random), as in the CSN paper.
3. **The loss for each facet is the same as SSE's.** For a batch of photos, the masked cosines
   should match the true similarity table of that facet: habitat ratings for habitat, the family
   tree for Order / Family / Genus. CSN also gets SSE's "whole vector should stay similar to CLIP"
   loss.
4. **A sparsity penalty**, as in the CSN paper, pushes mask weights toward 0, so each mask is
   encouraged to use only the numbers it really needs.

Training learns the network and the masks together. So **CSN decides by itself** which numbers go to
which facet.

**What it stores:** one 768-number vector per photo, plus the five masks **once** for the whole
database.

**SSE is a special case of CSN.** An SSE block is just a mask fixed by hand. It has 1s on the
block's numbers and 0s everywhere else, and blocks never overlap:

```
SSE habitat "mask":  [0 … 0 | 1 1 … 1 | 0 … 0]   numbers 65–96 = 1, the rest = 0   (fixed, no overlap)
CSN habitat mask:    [0.0 1.3 0.0 0.4 0.9 …]      ~370 numbers non-zero, spread out (learned)
```

So the experiment asks: **does it help to *learn* the masks (CSN), or is a fixed, readable layout
(SSE) just as good?**

**What we found.**
- **Accuracy: a tie.** With the same losses, CSN ≈ SSE ≈ B3 on every AwA2 test, and CSN is slightly
  better on MovieLens.
- **The learned masks are not separated** (table in 4.7). Each mask uses about **370–420 of the 768 numbers**, and
  any two masks share about **half** of their numbers. The habitat mask and the Genus mask overlap
  as much as the habitat and diet masks do. So CSN's facets are spread out and mixed. You can't
  point at "the habitat part" of a CSN vector, read it, or store it separately. In SSE you can
  (numbers 65–96).
- **No zoom levels by design.** Order, Family and Genus are three unrelated masks. Nothing makes the
  Order mask a "shorter version" of the Family mask, as SSE's prefixes are. On our data, the shared
  family-tree loss made it work anyway.

**Why it's here:** it is the closest published method, so a reviewer will ask "isn't this just
CSN?". The answer: same accuracy, but SSE's layout is **fixed and readable**. Each facet is a known
slice, and zoom levels are prefixes. That is what lets a database refer to "the habitat block" in a
query plan, an index or a schema.

---

### B5: Ask an AI model, the "just use a big model" method

- **Model:** Qwen2.5-VL-7B, an open vision-language model that reads images and text together.
- **What it stores per item:** nothing. It looks at the photos **at query time**.
- **How it answers "habitat similarity":** it receives **both photos in one prompt** plus a
  question. We tested two versions:
  - **Yes/No:** *"Image 1 and Image 2 each show an animal. First name both animals. Then decide: do
    these two animals typically live in similar natural habitats? End with 'Answer: Yes' or
    'Answer: No'."* Score = the model's probability of answering "Yes".
  - **Rating 0–10:** the same, but *"rate how similar their typical natural habitats are, from 0
    (completely different) to 10 (the same)"*. Score = the number it gives. This is fairer, since
    our answer key is graded.
  - The taxonomy question asks whether the two belong to the same biological family (Yes/No), or
    rates how related they are (0 = different orders, 5 = same order, 10 = same family).
- **Why "name both animals first":** with a one-word answer, the model said "No" even to *brown bear
  vs polar bear, same family?*. Asking it to name both animals first fixed that.
- **Size of the test:** it is slow, about 9–16 pairs per second, so it ran on **50 queries × 200
  candidate photos**. All other methods were scored on **the same 50 × 200** for a fair comparison.
- **Why it's here:** the "LOTUS-style" alternative of letting a large model judge every candidate.
  It might be the most accurate, but it can't scan a real database: 1 million candidates would take
  about a day per query.

---

### Not competitors: ablations that test one specific design choice

#### MRL-style (Matryoshka), does the *training per level* matter?

**What the original MRL is.** Matryoshka Representation Learning (Kusupati et al., NeurIPS 2022)
trains one embedding so that its **first 8, 16, 32, … numbers each work on their own**, like nested
Russian dolls. Every prefix is trained on **the same task with the same labels**, e.g. "which of the
1,000 ImageNet classes is this?". The goal is **cost**: search quickly with a short prefix, then
re-check the top results with the full vector. A short MRL prefix is a **blurrier version of the
same meaning**.

**How SSE differs.** SSE also nests prefixes, but each prefix gets a **different meaning**: short =
Order, medium = Family, full = Genus. So each prefix is trained with **its own level's labels**. A
short SSE prefix is a **coarser meaning**, not a blurrier copy.

**Example: what each method wants from the short (Order) prefix, for a bear and a wolf.**

| | Same Genus? | Same Order? | MRL's short prefix should… | SSE's short prefix should… |
|---|---|---|---|---|
| grizzly bear – wolf | no | **yes** (both carnivores) | push them **apart** (different genus) | pull them **together** (same Order) |
| grizzly bear – polar bear | **yes** | yes | pull together | pull together |
| grizzly bear – mouse | no | no | push apart | push apart |

They disagree exactly on pairs like bear–wolf: **same Order, different Genus**. That is where an
Order-level query ("other carnivores") needs the right answer.

**How we built the MRL-style version.** Exactly SSE, with the same blocks, habitat and diet training,
and "stay close to CLIP" loss. The one change: **all three taxonomy prefixes (8, 32 and 64 numbers)
are trained to separate Genus**, instead of Order / Family / Genus. Any difference in the results
therefore comes from that one choice.

**What we found** (search for "same Order", "same Family", "same Genus" with each prefix):

| AwA2 | Order @8 | Family @32 | Genus @64 |
|---|---|---|---|
| SSE (per-level training), seen species | **1.00** | **0.99** | 0.99 |
| MRL-style (Genus everywhere), seen species | 0.70 | 0.89 | 0.99 |
| SSE (per-level training), unseen species | **0.91** | 0.96 | 0.98 |
| MRL-style, unseen species | 0.78 | 0.95 | 0.98 |

*(SSE here is the version with the same yes/no loss type as MRL-style, so only the targets differ.
The final SSE-tree is higher still: 0.94 at Order on unseen species.)* On iNat (unseen species):
Order @16 is SSE 0.52 vs MRL-style 0.42; at Genus both are about 0.32.

- **At Genus they are equal.** Both were trained for Genus on the full block.
- **At coarser levels MRL-style is clearly worse** (Order 0.70 vs 1.00 on seen species). Its short
  prefix is a blurry *Genus* detector. It gets Order partly right only because animals of the same
  genus also share an Order.
- **Conclusion:** nesting alone does not give zoom levels. **Level-specific training does.** This is
  the main difference between SSE and MRL, and worth one sentence in the paper's related work.

#### CLIP-PCA, is a short prefix "coarse" for free?

Keep only the first 8 / 16 / 32 / … "main directions" of the CLIP vectors (PCA). This
is nested for free, with no training. It tests whether a short prefix is good at coarse levels on
its own. (Answer: no, much weaker at Order: 0.65 vs 0.94 on unseen AwA2 species.)

**SSE variants** (SSE-hard, SSE-tree, SSE-treeSC, …) are described in 3.3.

---

### Summary table

| Method | Trains? | Models | Stored per item | Habitat similarity = | Can handle unseen kinds? | Can say "somewhat similar"? |
|---|---|---|---|---|---|---|
| B6 plain CLIP | no | 0 | 768 numbers | cosine of whole vectors | yes (but blind to facets) | yes (but wrong facet) |
| B2 CLIP + text | no | 0 | 14 + 5 + … scores | cosine of sentence-score profiles | yes | yes (weak) |
| B1 labels | yes | 5 classifiers | label columns | overlap of yes-sets | ❌ forced into known names | ❌ only shared labels |
| B3 separate | yes | 5 networks | 6 vectors, 920 numbers | cosine of habitat vectors | yes | yes |
| B4 CSN | yes | 1 network + 5 masks | 768 numbers | cosine after habitat mask | yes | yes |
| B5 AI model | no | 1 big model | nothing | the model's answer, per pair | yes | yes (rating version) |
| **SSE** | yes | **1 network** | **768 numbers (or 128)** | **cosine of the habitat block** | yes | yes |

---

# Part 3 — How we tested

## 3.1 Datasets

| Dataset | What it is | Used for | Size |
|---|---|---|---|
| **AwA2** (main) | Animal photos; people rated each species on 85 attributes, e.g. otter, "water": 79/100 | G1, G2, G3, G4, G5, G6, Q2, B5, compactness | 37,322 images, 50 species |
| **iNaturalist 2021** (validation set) | Nature photos with the **full family tree** per photo, plus date and location | G2, G6 on a **deep** tree | 100,000 images, 10,000 species |
| **MovieLens + TMDB** | Movies with plot summaries; every movie scored 0–1 on ~1,100 descriptive tags | G1, G3, G4, G5 on **text** | 13,227 movies |
| Animals-90 | The photos in `overleaf/animals/` | Pictures for the paper only | — |

**Facets per dataset**

| Dataset | Blocks | Where the "truth" comes from |
|---|---|---|
| AwA2 | taxonomy (Order / Family / Genus), habitat, diet | Taxonomy: written by hand for the 50 species. Habitat (14 scores) and diet (5 scores): AwA2's human ratings |
| iNat | taxonomy (Order / Family / Genus) | iNat's own taxonomy (273 orders, 1,103 families, 4,884 genera) |
| MovieLens | genre, tone, theme, style | The ~1,100 tags sorted into these 4 groups (drafted by Claude, file `data/movielens/tag_groups.csv`; 305 tags such as actor names, awards and "awful" are excluded) |

**Splits: training and test never overlap**

Every dataset is split into a **training set** (used to train SSE and every competitor) and a
**test set** (the "database" we search and group). No test item is ever seen in training. Each test
set has two kinds of items:

- **Seen-test:** *new* items of a kind that training has seen, e.g. a new zebra photo when training had other zebra photos.
- **Unseen:** items of a kind that training **never** saw, e.g. giant panda photos when training had no pandas at all. This is the harder test.

| Dataset | Training set | Test: seen-test | Test: unseen | How we split |
|---|---|---|---|---|
| **AwA2** | **24,270** photos of 40 species | **6,067** new photos of those 40 species | **6,985** photos of 10 species never trained on | AwA2's official 10 test species; 20% of the other species' photos held out at random |
| **iNat** | **56,000** photos (7 per species × 8,000 species) | **24,000** photos (3 per species, same 8,000) | **20,000** photos of 2,000 species never trained on | 20% of species picked at random as unseen |
| **MovieLens** | **9,884** movies | **3,343** movies | — | 75% / 25% of movies at random. Every test movie is new, but no movie is a "kind", so there is no unseen part |

So the AwA2 **test database = 6,067 + 6,985 = 13,052 photos**, and the iNat test database is
**44,000 photos**.

The 10 unseen AwA2 species are persian cat, hippopotamus, leopard, humpback whale, seal, chimpanzee,
rat, **giant panda**, pig and raccoon.

**Where the labels are used.** Labels of **training** items are used to train. Labels of **test**
items are used **only to grade the answers**, never as input to SSE. The one exception is competitor
B1 (labels + filter): it trains its classifiers on the training labels and then *predicts* labels
for the test items.

**Validation split (AwA2 only), for choosing settings without peeking at the test set.** Inside the
24,270 training photos we made a mini train/test split:

| Part | Size |
|---|---|
| Mini-training | 19,069 photos of 35 species |
| Mini-test, seen | 3,365 photos (15% of those 35 species' photos) |
| Mini-test, unseen | 1,836 photos of 5 species treated as unseen (antelope, beaver, mole, otter, walrus) |
| Real test set (13,052) | **not touched at all** |

The choice of SSE version (4.9) was made on this validation split only.

## 3.2 The answer key: how we know the "right" answer

AwA2 gives, for each species, human ratings (0–100) of 85 properties (Osherson et al. 1991, Kemp et
al. 2006). E.g. otter: water 79, coastal 36, desert 0. **The true similarity of two animals is the
cosine of their property scores**: 14 habitat properties for habitat, 5 diet properties for diet.
Every photo gets its species' value. MovieLens works the same way, using the cosine of the movies'
tag scores.

Example, habitat similarity to the **otter**: seal 0.91, humpback whale 0.90, beaver 0.86, polar
bear 0.75, hippo 0.66, moose 0.24, zebra 0.09.

Taxonomy (Order / Family / Genus) is written by hand for AwA2, and given with each photo for iNat.

## 3.3 The SSE versions we trained

We trained several versions of SSE. **They all share the same base:**
- the same frozen CLIP (or bge) vector as input;
- the same small network on top of it;
- the same layout: taxonomy numbers 1–64 (zoom levels: 1–8 = Order, 1–32 = Family, 1–64 = Genus),
  habitat 65–96, diet 97–112, the rest = everything else;
- the same goal to **stay similar to CLIP** (the full vector should rate pairs about as CLIP does).

They differ in **three training choices**. Each choice was tested for a reason.

### The taxonomy hierarchy

Taxonomy has three nested levels, from broad to narrow: **Order ⊃ Family ⊃ Genus**. Each Family sits
inside one Order, and each Genus inside one Family. Example: Carnivora (meat-eaters) ⊃ Ursidae
(bears) ⊃ *Ursus* (grizzly, polar bear).

| | Orders | Families | Genera | Zoom prefix (numbers of the taxonomy block) |
|---|---|---|---|---|
| AwA2 | 10 | 27 | 40 | Order 1–8 · Family 1–32 · Genus 1–64 |
| iNat | 273 | 1,103 | 4,884 | Order 1–16 · Family 1–64 · Genus 1–128 |

### Choice 1: how the zoom levels (taxonomy prefixes) are taught

Look at the **Family prefix** (numbers 1–32) and three pairs: grizzly and
polar bear are both bears (same Family); a wolf is a meat-eater like the bears, but in the dog
family (same Order, different Family); a mouse is a rodent (different Order).

| Pair | The truth |
|---|---|
| grizzly – polar bear | same Family (bears) |
| grizzly – wolf | different Family, but same Order (both carnivores) |
| grizzly – mouse | different Order |

**Option A, yes/no ("contrastive").** The prefix only learns "same Family or not":
```
grizzly – polar bear  → pull together
grizzly – wolf        → push apart
grizzly – mouse       → push apart, just as hard as the wolf
```
How it works: in each training batch, for each photo, the other photos **with the same label**
should end up as its nearest neighbors, ahead of every photo with a different label. All "different"
photos are treated as equally different.

*Problem:* wolf and mouse count as equally far, so the Family prefix **forgets that bear and wolf
share an Order**. We measured this with a simple check: take a random same-Order pair and a random
different-Order pair; how often does the Family prefix rate the same-Order pair as closer? Only
**82%** of the time.

**Option B, graded tree.** Each prefix gets a **target number** for every pair, and learns to make
its cosine equal to that number:

| Prefix | Same Genus | Same Family only | Same Order only | Different Order |
|---|---|---|---|---|
| Order (1–8) | 1 | 1 | 1 | 0 |
| Family (1–32) | 1 | 1 | **0.5** | 0 |
| Genus (1–64) | 1 | **0.67** | **0.33** | 0 |

So the Family prefix learns grizzly–polar bear → 1, grizzly–wolf → **0.5**, grizzly–mouse → 0. It
still knows bear is closer to wolf than to mouse. This **fixed** the AwA2 problem (the same check: 82% → 95.5%).

*Problem on iNat:* iNat has ~5,000 genera. Two random photos almost never share a genus, or even a
family, so nearly every target in a batch is 0. The model gets very little signal about what *is*
the same, and Family / Genus got worse.

**Option C, both together (A + B).** Add the two losses:
- The graded part (B) keeps coarser levels in each prefix.
- The yes/no part (A) gives a strong signal even when matches are rare, because it focuses on the
  few same-label photos in each batch.

This works well on **both** AwA2 and iNat.

### Choice 2: how the habitat and diet blocks are taught

**Option G, graded (the normal way).** The habitat block learns to make its cosine for a pair equal
to the **true habitat similarity** from 3.2 (otter – seal → 0.91, otter – moose → 0.24, …).

**Option Y, yes/no only.** We first round the human ratings to yes/no (rating ≥ 50 → "yes"), then
train on that. This exists **only for one test (G5b)**: if SSE is given only yes/no labels, can it
still learn "somewhat similar" on its own? Two ways to turn yes/no labels into a training target:
- **Y1, all-or-nothing:** two species count as "same habitat" (target 1) only if **all 14 yes/no
  answers match**; otherwise 0. Very strict: otter and seal → 0.
- **Y2, overlap:** target = shared "yes" answers ÷ all "yes" answers of either. Otter {water} vs seal
  {arctic, coastal, ocean, water} → 1/4 = 0.25. Fairer, because it gives partial credit.

### Choice 3: total size

The taxonomy, habitat and diet blocks always keep their size (64 + 32 + 16 = 112 numbers). Only the
**rest** shrinks: total 768 (rest = 656), 256 (rest = 144) or 128 (rest = 16). This tests how small
SSE can be (G7, section 4.7).

### The versions, and where each one is used

| Version | Zoom levels (Choice 1) | Habitat / diet (Choice 2) | Size | Why it exists | Used in |
|---|---|---|---|---|---|
| SSE (yes/no levels) | A: yes/no | G: graded | 768 | the first version | showed the "forgets the Order" problem (4.2) |
| **SSE-tree** | B: graded tree | G: graded | 768 | fixes that problem | **the final AwA2 numbers** (G1–G6) |
| **SSE-treeSC** | C: both | G: graded | 768 | works on AwA2 *and* iNat | **iNat** (4.2, 4.6b); **recommended** recipe |
| SSE-hard | A: yes/no | **Y1: all-or-nothing** | 768 | can SSE discover "somewhat similar" from yes/no? | G5b only |
| SSE-hardJ | A: yes/no | **Y2: overlap** | 768 | same question, fairer version | G5b only |
| SSE-256 / SSE-128 | B: graded tree | G: graded | **256 / 128** | how small can SSE be? | G7 only (4.7) |

"SC" stands for "supervised contrastive", the technical name of Option A.

**MovieLens** has no hierarchy, so there are no zoom levels. Its SSE uses only Choice 2: **G**
(graded tag profiles) for the main version, **Y2** for its "SSE-hard".

**Which one should the paper use?** SSE-treeSC. On the AwA2 **validation split** (no test data
used), it is within 0.01 of SSE-tree. On iNat it ties the best version, while SSE-tree falls behind
(4.2, 4.9). It is the only version that is best or tied-best on both. The final AwA2 tables report
SSE-tree, which was chosen first; on AwA2 the two are practically the same.

**Not an SSE version:** the MRL-style model (2.4) is built like SSE, but every zoom level is trained
on Genus. It is an ablation, not a candidate.

## 3.4 How we score (glossary of measures)

| Measure | Plain meaning | Range |
|---|---|---|
| **Match score** (Spearman) | Does the method's similarity go up and down together with the true similarity? | 0 = unrelated, 1 = perfect |
| **mAP** | When you search for "same Order" (etc.), are the right items at the top? | 0–1, higher better |
| **AUC** | Pick a random "same Family" pair and a random "different Family" pair: how often does the method rank the first higher? | 0.5 = coin flip, 1 = always |
| **Filter F1** | Of the items that should pass the filter, how many does the method let through (and how few wrong ones)? | 0–1 |
| **Ranking (NDCG@10)** | Are the top-10 results the truly best ones, in the right order? | 0–1 |
| **No-mixing error** | Two references with the same habitat but different taxonomy should give the same filter result. How far off is the method? | lower is better |
| **Group agreement** (NMI / ARI) | Do the groups found match the true groups? (ARI is stricter: it does not reward putting everything alone) | 0 = random, 1 = perfect |

---

# Part 4 — Results, goal by goal

The final AwA2 numbers use **SSE-tree** (chosen on the validation split, see 4.9). Competitors B3 and
CSN are given the **same** training recipe.

## 4.1 G1 — Do blocks mean what they should?

**Question.** Does the habitat block follow habitat, the diet block diet, the taxonomy block
taxonomy — and *not* each other?

**Test.** 200,000 random pairs of test images. For each block, the match score with each true facet.

**Result (AwA2, each block vs. its own facet):**

| Method | Habitat | Diet | Taxonomy |
|---|---|---|---|
| **SSE-tree** | **0.90** | **0.87** | **0.72** |
| B3 separate vectors | 0.91 | 0.87 | 0.72 |
| B4 CSN | 0.90 | 0.87 | 0.73 |
| B1 labels | 0.61 | 0.59 | 0.73 |
| B6 plain CLIP | 0.31 | 0.28 | 0.24 |
| B2 CLIP + text | 0.26 | 0.17 | 0.24 |

**Separation:** the SSE habitat block tracks diet only at 0.42 and taxonomy at 0.31 — clearly lower
than habitat (0.90).

**Meaning.** ✅ Each block captures its facet well and stays mostly separate. Plain CLIP cannot do
this at all (≈0.3). Labels are good at taxonomy (a fixed tree) but weak on graded facets.

**Caveat.** B3 and CSN do equally well.

## 4.2 G2 — Do the zoom levels work?

**Question.** Is the short prefix best for Order, the medium one for Family, the full one for Genus?

**Test.** Cut the taxonomy block to different lengths; for each length, search for "same Order /
Family / Genus" and measure mAP.

**AwA2** (prefixes 8 / 32 / 64):

| | Order @8 | Family @32 | Genus @64 |
|---|---|---|---|
| **SSE-tree, seen species** | **0.99** | **0.97** | **0.97** |
| **SSE-tree, unseen species** | **0.94** | **0.99** | **0.99** |
| MRL-style (Genus label everywhere), unseen | 0.78 | 0.95 | 0.98 |
| CLIP cut short (PCA), unseen | 0.65 | 0.86 | 0.94 |

**iNat — a deep tree** (273 orders, 1,103 families, 4,884 genera; prefixes 16 / 64 / 128):

| Unseen species | Order @16 | Family @64 | Genus @128 |
|---|---|---|---|
| **SSE-treeSC** | **0.51** | **0.36** | **0.33** |
| SSE (yes/no levels) | 0.52 | 0.36 | 0.32 |
| SSE-tree (graded only) | 0.48 | 0.27 | 0.23 |
| MRL-style | 0.42 | 0.35 | 0.32 |
| CLIP cut short (PCA) | 0.27 | 0.20 | 0.17 |

On iNat, Order peaks exactly at its 16-number prefix and Family at its 64-number prefix.

**Does each zoom level keep the coarser levels?** (AUC, AwA2, Family prefix)

| | Same Family? | Same Order? |
|---|---|---|
| SSE (yes/no levels) | 0.995 | **0.82** ← forgets the Order |
| **SSE-tree** | 0.996 | **0.955** |
| B1 labels | 0.985 | 0.96 |

**Meaning.**
- ✅ Zoom levels work, on a small tree (AwA2) and a deep one (iNat), and beat simply cutting CLIP short by a wide margin.
- ✅ **Level-specific training matters**: MRL-style (same label everywhere) is clearly weaker at the coarse level (0.78 vs 0.94 on AwA2; 0.42 vs 0.51 on iNat).
- ⚠️ **Nesting alone does not keep coarser levels**: the first version's Family prefix forgot the Order. Training with *graded tree similarity* fixed it.
- iNat numbers are low in absolute terms: 10,000 species from 7 photos each is a very hard task. The *comparison* is what matters.

## 4.3 G3 — Does normal search still work?

**Test.** Search for the same species with the full vector; compare with plain CLIP.

| | Same-species search (mAP) | Top-10 shared with CLIP |
|---|---|---|
| AwA2: SSE-tree | 0.82 (CLIP 0.82) | 86% |
| iNat: SSE-treeSC | 0.12 (CLIP 0.11) | 78% |
| MovieLens: SSE | – | 74% of bge's top-10 |

**Meaning.** ✅ Adding structure costs nothing for ordinary search — it is equal or slightly better.

## 4.4 G4 — Do combined queries give correct answers?

**Question.** For swan/panda-style queries — filter on habitat (reference image *x*), rank by
Family closeness (reference image *q*) — are the answers right?

**Test.** 1,000 random queries on AwA2, graded answer key.

| Method | Filter F1 | Top-10 that truly pass | Ranking (NDCG@10) | No-mixing error (A / B) |
|---|---|---|---|---|
| **SSE-tree** | **0.75** | **0.56** | **0.58** | **0.15 / 0.14** |
| B3 separate vectors | 0.76 | 0.56 | 0.58 | 0.15 / 0.15 |
| B4 CSN | 0.75 | 0.56 | 0.59 | 0.15 / 0.14 |
| B6 plain CLIP | 0.55 | 0.33 | 0.40 | 0.32 / 0.19 |
| B1 labels | 0.48 | 0.36 | 0.38 | 0.34 / 0.55 |
| B2 CLIP + text | 0.47 | 0.37 | 0.41 | 0.38 / 0.21 |

No-mixing: A = two references with the same habitat but different Order (swan vs. otter); B = same
Family but different habitat (polar bear vs. giant panda). Lower error = the habitat filter is not
fooled by taxonomy.

**Meaning.** ✅ SSE answers combined queries far better than labels (0.75 vs 0.48 filter, 0.58 vs
0.38 ranking) and plain CLIP, and mixes facets the least. This turns the panda figure into numbers.

### Q2-style queries (from the paper): Order prototype + habitat *band*

*"Animals in a given Order (e.g. a 'Carnivora' prototype vector), whose habitat is **somewhat**
similar to a reference — between the 30th and 60th percentile, say — ranked by overall similarity."*

| | SSE | B3 | CSN | B1 labels | Plain CLIP |
|---|---|---|---|---|---|
| Order filter F1 | 0.96 | 0.96 | 0.96 | 0.83 | 0.67 |
| **Habitat band F1** | **0.60** | **0.60** | **0.60** | 0.35 | 0.34 |
| Both conditions F1 | 0.38 | 0.38 | 0.38 | 0.18 | 0.16 |

**Meaning.** ✅ A named concept works as a prototype vector (0.96). **Bands are where labels fail**:
a label can say "same habitat", not "somewhat similar habitat".

## 4.5 G5 — Does it work where labels fail?

**(a) Species never seen in training** (filter F1, queries whose reference is an unseen species):
SSE **0.72** · plain CLIP 0.62 · **B1 labels 0.47**. ✅

**(b) In-between similarity.** Among pairs that yes/no labels call "different habitat", does the
method still know which are closer (seal vs. camel)?

| | Score |
|---|---|
| **SSE (trained on graded scores)** | **0.89** |
| SSE-hard (trained on yes/no only, credit per shared habitat) | 0.62 |
| B1 labels | 0.59 |
| SSE-hard (yes/no, "same only if all 14 match") | 0.20 |
| Plain CLIP | 0.23 |

**Meaning.** ✅ SSE **keeps** graded similarity when trained with it (0.89 vs labels 0.59).
⚠️ It does **not discover** graded similarity from yes/no labels alone (0.62 ≈ labels 0.59).

**(c) Threshold as a dial.** Sort results by the method's habitat score into 10 steps; measure the
*true* similarity in each step:

```
SSE:         0.10 → 0.23 → 0.37 → 0.46 → 0.51 → 0.55 → 0.61 → 0.66 → 0.79 → 0.92  (rises every step)
B1 labels:   0.35 → 0.23 → 0.30 → 0.55 → 0.58 → 0.54 → 0.57 → 0.61 → 0.62 → 0.78  (jumps around)
Plain CLIP:  0.44 → 0.42 → 0.42 → 0.42 → 0.44 → 0.46 → 0.50 → 0.55 → 0.64 → 0.84  (flat, then rises)
```

✅ The SSE threshold is a precise, monotone dial over the widest range.

## 4.6 G6 — Do GROUP BY and roll-up / drill-down work?

**Question.** GROUP BY on the habitat block: are the groups the real habitat groups? Grouping at the
Order, then Family, then Genus prefix: do the groups match the true tree?

**Test.** True habitat groups = the 50 species clustered by their habitat ratings → **water**
(whales, seal, otter, beaver, hippo, polar bear) · **jungle/tropical** · **forest** · **fields/plains**.
Grouping threshold tuned on *training* images. Two grouping rules were compared.

### The two grouping rules, with an example

**Why a rule is needed at all.** With no habitat column, GROUP BY must put photos whose habitat
blocks are "close enough" (similarity ≥ a threshold **κ**) in one group. But closeness alone does
not decide the groups. If A is close to B and B is close to C, while A is *not* close to C, is C in
A's group? The paper notes this itself and says a GROUP BY must state its **rule**.

**Example: 7 animals, κ = 0.7.** These are the only close pairs; every other pair is below 0.7:

```
whale – seal   0.85        otter – beaver 0.75
seal  – otter  0.80        beaver – moose 0.72
whale – otter  0.72        moose – deer   0.90
camel: close to nobody
```

| Animal | Close neighbors | How many |
|---|---|---|
| **otter** | whale, seal, beaver | **3** |
| whale | seal, otter | 2 |
| seal | whale, otter | 2 |
| beaver | otter, moose | 2 |
| moose | beaver, deer | 2 |
| deer | moose | 1 |
| camel | — | 0 |

**Rule A: "connected" (the paper's current rule).** Draw a line between every close pair. A group
is everything you can reach by following lines.

```
Group 1: {whale, seal, otter, beaver, moose, deer}   ← whale and deer together!
Group 2: {camel}
```

Whale and deer are not close (similarity ≈ 0.1), but the **chain** whale → seal → otter → beaver →
moose → deer connects them. The paper states this openly: a group may contain pairs that are not
close, as long as a chain links them. Habitat changes **gradually** from one animal to the next, so
on the real data almost everything chains into one or two giant groups.

**Rule B: "center" (our fix).** Every member must be close to **one center**, not just to some
neighbor in a chain.

1. **Round 1.** The animal with the most close neighbors becomes the first **center**: the
   **otter** (3). Its group = the otter + everything close **to the otter itself**:
   `{otter, whale, seal, beaver}`. The moose is *not* included: it is close to the beaver, but
   not to the otter. Remove these 4.
2. **Round 2.** Left: moose, deer, camel. Next center: the **moose**. Its group = the moose + what
   is close to it and not yet taken: `{moose, deer}`. The beaver is close to the moose, but it is
   already in group 1, so it stays there.
3. **Round 3.** Left: the camel. It becomes its own group: `{camel}`.

```
Group 1: {otter, whale, seal, beaver}    ← water animals
Group 2: {moose, deer}                   ← deer-like animals
Group 3: {camel}
```

**Why it works, and the costs.**
- **No long chains:** all members are close to the same center, so a group cannot stretch from whale
  to deer.
- **Why start with the item with the most neighbors?** It sits in the middle of a crowded area, so it
  is a typical member. The big, meaningful groups form first, and leftovers form small groups at the
  end.
- **Cost 1:** an item close to two centers joins whichever center comes first. The beaver could
  arguably go with the moose, but the otter took it first.
- **Cost 2:** the result depends on the order of centers. It is not one unique "natural" answer as
  in Rule A. This is the usual price for avoiding chaining, and the paper's text would need to state
  it ("other policies … must be specified").

In the real experiment, the same procedure runs on thousands of test photos' habitat blocks, with κ
chosen on the training photos. For roll-up / drill-down, the chosen rule is applied level by level
*inside* each parent group (Order groups → Family groups inside each → Genus groups inside each), as
the paper defines.

**AwA2** (group agreement, NMI):

| | SSE connected | **SSE center** | B3 center | CSN center | Plain CLIP center |
|---|---|---|---|---|---|
| Habitat GROUP BY | 0.17 | **0.50** | 0.51 | 0.58 | 0.39 |
| Roll-up / drill-down: Order | 0.85 | **0.84** | 0.85 | 0.86 | 0.50 |
| … Family | 0.85 | **0.88** | 0.88 | 0.89 | 0.73 |
| … Genus | 0.86 | **0.84** | 0.86 | 0.87 | 0.75 |

**iNat** (deep tree): see 4.6b.

**Meaning.**
- ✅ Roll-up / drill-down works and is far better than plain CLIP at the coarse level. Every small group sits inside exactly one bigger group, by construction.
- ⚠️ **The paper's "connected" rule breaks on graded facets.** Habitat changes smoothly (whale → seal → otter → beaver → … → deer), so everything links into one or two giant groups (0.17). The **center rule fixes it** (0.50).
- Habitat grouping is still only moderate (0.50): four coarse "true" groups are a crude summary of graded habitats.

### 4.6b iNat roll-up / drill-down (deep tree)

A random sample of all of iNat has only ~7 test photos per family and ~2 per genus, which makes
grouping meaningless at those levels (first try). So we group **within one big class**,
and tune the threshold with **ARI**, which does not reward putting every photo alone.

Group agreement (ARI, 1 = perfect), **center** rule:

| | Birds: Order (32) | Family (147) | Genus (648) | Insects: Order (17) | Family (190) | Genus (1,472) |
|---|---|---|---|---|---|---|
| **SSE-treeSC** | **0.66** | **0.26** | **0.13** | **0.85** | **0.33** | **0.10** |
| B3 separate vectors | 0.67 | 0.30 | 0.13 | 0.85 | 0.33 | 0.10 |
| B4 CSN | 0.66 | 0.24 | 0.13 | 0.85 | 0.33 | 0.10 |
| SSE-tree (graded only) | 0.65 | 0.13 | 0.07 | 0.83 | 0.23 | 0.05 |
| Plain CLIP | 0.21 | 0.04 | 0.03 | 0.28 | 0.16 | 0.03 |

(6,586 bird and 11,281 insect test photos. Numbers in brackets = number of true groups.)

With the paper's **connected** rule the coarse level often chains into one giant group (birds, Order:
CSN 0.04, B3 0.12, SSE-treeSC 0.48; insects, Order: SSE-treeSC 0.62 vs. 0.85 with the center rule).

**Meaning.**
- ✅ Roll-up / drill-down works on a deep tree: Order groups are good (0.66 birds, 0.85 insects) and **3× better than plain CLIP**; Family is moderate; Genus is hard for everyone (hundreds of genera, ~10 photos each).
- ✅ The **center rule is again more robust** than the connected rule.
- SSE-treeSC ≈ B3 ≈ CSN, and graded-only training (SSE-tree) is again weaker at fine levels on iNat.

## 4.7 G7 (part) — Compactness: how small can SSE be?

The facet blocks stay the same; only the "rest" block shrinks.

| | SSE-768 | SSE-256 | **SSE-128** | B3 separate vectors |
|---|---|---|---|---|
| Habitat filter F1 | 0.754 | 0.754 | **0.751** | 0.757 |
| Ranking (NDCG@10) | 0.576 | 0.576 | **0.576** | 0.579 |
| In-between score | 0.890 | 0.892 | **0.890** | 0.892 |
| Zoom, unseen species, Order | 0.945 | 0.946 | **0.946** | – |
| Same-species search | 0.823 | 0.836 | **0.831** | (CLIP ≈ 0.83) |
| **Numbers stored per item** | 768 | 256 | **128** | **920** |

**Meaning.** ✅ **A 128-number SSE does everything the 920-number separate-vectors setup does — 7×
smaller**, in one vector from one model. It even does ordinary species search as well as full CLIP.

**Fairness note.** Most of B3's 920 numbers is the CLIP vector kept for general search; its five facet
vectors are 152. A slimmed B3 (facets + a 128-number general vector) would be ~280 — still ~2× SSE-128,
and still five models and six columns.

### Size per attribute: SSE vs CSN

Both store **one 768-number vector per item**; CSN's masks are stored once for the whole database. But
the number of values **each attribute uses** is very different (AwA2, final runs, range over 3 seeds):

| Attribute | SSE | CSN (non-zero mask values) |
|---|---|---|
| habitat | 32 (numbers 65–96) | 365–375 |
| diet | 16 (numbers 97–112) | 382–390 |
| Order | 8 (numbers 1–8) | 410–425 |
| Family | 32 (numbers 1–32) | 398–427 |
| Genus | 64 (numbers 1–64) | 391–435 |
| Overlap between two attributes | none, by design | each pair shares 49–59% of the smaller mask |

So in CSN, each attribute effectively uses **~10× more numbers**, and the attributes share numbers. This
matters when a database works with one attribute: a habitat comparison, a habitat-only index, or
returning the habitat attribute all touch 32 numbers in SSE and ~370 in CSN.

**Caveats.**
- The original CSN paper reports much sparser masks. We set the sparsity penalty ourselves (the paper
  does not give its value), and ours was probably too weak. A stronger penalty could shrink CSN's
  attributes, though they would still be learned and possibly overlapping, not fixed.
- We did not train a small CSN. So "each attribute is smaller in SSE" is shown; "SSE is smaller than
  CSN in total" is not. Both are suggested follow-ups (~20 min).

## 4.8 B5 — Asking an AI model instead

**Test.** For 50 queries, every method scores the **same 200 candidate images**. The AI model
(Qwen2.5-VL-7B, open, run locally) sees the reference and a candidate, names both animals, then
answers. Two versions: Yes/No, and a 0–10 rating.

| | Habitat filter F1 | Ranking (NDCG@10) | Speed |
|---|---|---|---|
| **SSE** | **0.75** | **0.72** | milliseconds per query |
| B3 separate vectors | 0.76 | 0.74 | ms |
| **AI model, 0–10 rating** | 0.53 | 0.57 | 8.9 pairs/s → ~25 min per query over 13k images |
| AI model, Yes/No | 0.48 | 0.31 | 16 pairs/s |
| Plain CLIP | 0.55 | 0.49 | ms |
| B1 labels | 0.44 | 0.49 | ms |

**Meaning.** The AI model is **not** an upper bound here: below SSE in accuracy and ~10⁵–10⁶× slower.
Its idea of "similar habitat" differs from the human ratings (polar bear vs. seal: 2/10).

**Caveats.** One open 7B model, one prompt style. A much larger model might be more accurate — the
speed argument holds regardless. Prompt note: asked for a one-word answer, the model said "No" even to
"brown bear vs. polar bear, same family?" (while naming both correctly); asking it to name both
animals first fixed this.

## 4.9 Choosing the SSE version without looking at test data

On the AwA2 validation split (no test images used):

| | SSE (yes/no levels) | **SSE-tree** | SSE-treeSC |
|---|---|---|---|
| Taxonomy match score (E1) | 0.55 | **0.72** | 0.71 |
| Query ranking (NDCG) | 0.571 | **0.608** | 0.605 |
| Family prefix keeps Order (AUC) | 0.84 | **0.96** | 0.95 |

On iNat, SSE-tree is worse but **SSE-treeSC ties the best version** (4.2). → **Recommended recipe:
SSE-treeSC** (graded tree similarity + contrastive) — it is the only one that is best or tied-best on
both datasets.

## 4.10 Generality — text (MovieLens)

**Each block vs. its own facet** (match score):

| | Genre | Tone | Theme | Style |
|---|---|---|---|---|
| **SSE** | **0.35** | **0.27** | **0.31** | **0.25** |
| B3 separate vectors | 0.35 | 0.28 | 0.31 | 0.25 |
| B4 CSN | 0.39 | 0.31 | 0.35 | 0.29 |
| Plain bge | 0.17 | 0.11 | 0.19 | 0.10 |
| B1 labels | 0.01 | 0.03 | 0.05 | 0.04 |

**Combined queries:** filter F1 — SSE 0.35, plain bge 0.29, labels 0.18. **Threshold dial:** SSE rises
at every step; labels are flat.

**Meaning.**
- ✅ SSE carries over to text: about **2× the plain text vector**, far above labels (labels are nearly useless here: most movies get no "yes" tag).
- CSN is slightly better on text (+0.03–0.04) — the only place a competitor clearly beats SSE.
- Absolute numbers are low for everyone: a short plot summary says little about tags like "atmospheric" or "great cinematography".
- ⚠️ **Movie facets overlap in reality.** How similar two movies are in genre, tone, theme and style is strongly linked (0.55–0.69), much more than for animals (0.26–0.43). A dark film is usually a thriller with grim themes. So *no* method can separate movie facets cleanly, and MovieLens cannot demonstrate G1's "don't mix" part.
