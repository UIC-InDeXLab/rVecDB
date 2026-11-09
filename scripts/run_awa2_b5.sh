#!/usr/bin/env bash
# B5: ask an open vision-language model (Qwen2.5-VL-7B) — score, then compare with all methods.
# Logs: logs/awa2_b5/<step>.log   Progress: logs/PROGRESS.md   Results: results/awa2/b5/results.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/awa2_b5; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | b5/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
for st in ${B5_STEPS:-score evaluate}; do
  note "$st" "started"; t0=$SECONDS
  if $PY -m sse.b5_vlm "$st" > "$LOG/$st.log" 2>&1; then note "$st" "done ($((SECONDS - t0)) s)"
  else note "$st" "**FAILED** — see $LOG/$st.log"; exit 1; fi
done
note "ALL" "finished — results/awa2/b5/results.md"
