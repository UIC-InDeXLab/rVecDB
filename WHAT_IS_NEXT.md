# What is next

Last updated: 2026-11-09. Background: `AGENTS.md`, `experiment-plan.md`, `REPORT.md`.

## Main tasks

### 1. Use CLIP for text too, not only images
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
- Look for datasets where facets plus a hierarchy make sense. Examples: products with category trees and attributes, scientific or medical images with ontologies, geography, documents with topic trees.
- For each candidate, give: license, size, facets (blocks), hierarchy (prefix levels), and whether it has graded scores or only yes/no labels.

## Smaller open items
- **E7 (storage + query speed) is ON HOLD.** Don't start it until the user says so.
- The AwA2 hierarchy (Q2) row still uses SSE-tree. Rerun it with the combined loss (SSE-treeSC) so it matches iNat.
- Train a small CSN with a stronger sparsity penalty (~20 min), to compare total size and not only per-attribute size.
- Optional: MovieLens partial-correlation check per block.
- Hand-check `data/movielens/tag_groups.csv` (genre / tone / theme / style groups) with the user.
