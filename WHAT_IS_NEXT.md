# What is next

Last updated: 2026-11-25. Submission experiments done → `results/SUBMISSION_EXPERIMENTS.md`. Background: `AGENTS.md`, `experiment-plan.md`, `REPORT.md`.

## Main tasks

### 1. Use CLIP for text too, not only images — ✅ partly done (2026-11-25)
- Done: text references on AwA2 (species name via CLIP text → SSE projector), F1 0.71 vs 0.49 raw CLIP. MovieLens with CLIP text not done.
- Today MovieLens uses `BAAI/bge-base-en-v1.5`, because CLIP's text side cuts text at ~77 tokens.
- Goal: use the CLIP text side as well. For example, run text queries against image SSEs, and/or do a MovieLens run with CLIP text.
- Agree on the exact setup with the user before running anything.

### 2. Remove baselines that don't make sense
Current baselines:
- B1 classifier labels (+ filtered ANN)
- B2 CLIP soft attributes
- B3 separate vectors (multi-vector)
- B4 CSN (Conditional Similarity Networks)
- B5 VLM (Qwen2.5-VL-7B)
- B6 plain CLIP
- MRL / PCA prefixes (ablations only, not query baselines)

**Ask the user which ones to drop. Don't decide alone.**

### 3. Find benchmarks in other domains (not just animals)
- **Started (2026-11-20): OpenAlex research papers** — papers + authors + institutions, 4-level topic tree,
  SPECTER2 encoder. **v2 done** → `results/openalex/SUMMARY.md` (no topic level, join scored by P@10 vs random; semantic subfield credit added, §5). GROUP BY still weak. First VecJOIN result (Papers ⋈ Authors). Open: the separately-trained
  shared-join-key case. See the
  OpenAlex section in `experiment-plan.md`.
- Look for datasets where facets plus a hierarchy make sense. Examples: products with category trees and attributes, scientific or medical images with ontologies, geography, documents with topic trees.
- For each candidate, give: license, size, facets (blocks), hierarchy (prefix levels), and whether it has graded scores or only yes/no labels.
