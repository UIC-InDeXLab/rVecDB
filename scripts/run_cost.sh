#!/usr/bin/env bash
# E7 cost (rerun with the block-columnar SSE layout and the materialised-CSN variant). Waits for other sse.cost runs.
# Logs: logs/cost/<step>.log   Progress: logs/PROGRESS.md   Results: results/awa2/x_cost/cost_n*.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LOG=logs/cost; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | cost/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() { local name=$1; shift; note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"; else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi; }
while pgrep -f "run_[f]inal.sh" >/dev/null; do sleep 20; done
for n in 100000 1000000; do step "cost_n$n" $PY -m sse.cost --n $n || exit 1; done
note ALL "finished — results/awa2/x_cost/"
