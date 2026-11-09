#!/usr/bin/env bash
# E6 grouping + roll-up/drill-down for SSE-tree, B3 (tree), CSN (tree), plain CLIP — 3 seeds.
# Logs: logs/awa2_e6/<step>.log   Progress: logs/PROGRESS.md   Results: results/awa2/r4b_seed{s}/e6.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/awa2_e6; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | e6/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
for s in 0 1 2; do
  note "seed$s" "started"; t0=$SECONDS
  if $PY -m sse.e6_grouping --sse "tree_s$s" --extra "B3 separate=b3tree_s$s,B4 CSN=csntree_s$s" --out "r4b_seed$s" > "$LOG/seed$s.log" 2>&1
  then note "seed$s" "done ($((SECONDS - t0)) s) — results/awa2/r4b_seed$s/e6.md"
  else note "seed$s" "**FAILED** — see $LOG/seed$s.log"; exit 1; fi
done
note "ALL" "finished"
