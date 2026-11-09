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
