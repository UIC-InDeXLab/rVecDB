#!/usr/bin/env bash
# MovieLens (text): prep -> train SSE / SSE-hard / B3 / CSN x 3 seeds -> evaluate x 3 seeds.
# Logs: logs/movielens/<step>.log   Progress: logs/PROGRESS.md   Results: results/movielens/seed*/results.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/movielens; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | movielens/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
note "ALL" "started"
[ -f cache/movielens/text_emb.npy ] || step prep $PY -m sse.movielens prep || exit 1
for s in 0 1 2; do
  for m in sse hard b3 csn; do step "train_${m}_s$s" $PY -m sse.movielens train --method "$m" --seed "$s" || exit 1; done
done
export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20
pids=(); for s in 0 1 2; do step "eval_s$s" $PY -m sse.movielens eval --seed "$s" & pids+=($!); done
fail=0; for p in "${pids[@]}"; do wait "$p" || fail=1; done
[ $fail = 0 ] || { note "ALL" "**FAILED** in evaluation"; exit 1; }
note "ALL" "finished — results/movielens/seed*/results.md"
