#!/usr/bin/env bash
# iNat round 2: combined loss (graded tree + yes/no contrastive) for SSE, B3, CSN — 3 seeds — then re-run E2/E2b/E3.
# Logs: logs/inat_round2/<step>.log   Progress: logs/PROGRESS.md   Results: results/inat/seed*/results.md (overwritten, now incl. new methods)
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/inat_round2; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | inat2/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() { local name=$1; shift; note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"; else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi; }
note "ALL" "started (treeSC for SSE, B3, CSN)"
for s in 0 1 2; do for m in treesc b3sc csnsc; do step "train_${m}_s$s" $PY -m sse.inat train --method "$m" --seed "$s" || exit 1; done; done
export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20
pids=(); for s in 0 1 2; do step "eval_s$s" $PY -m sse.inat eval --seed "$s" & pids+=($!); done
fail=0; for p in "${pids[@]}"; do wait "$p" || fail=1; done
[ $fail = 0 ] || { note ALL "**FAILED** in eval"; exit 1; }
note "ALL" "finished — results/inat/seed*/results.md"
