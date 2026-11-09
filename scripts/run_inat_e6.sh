#!/usr/bin/env bash
# iNat E6 v2: roll-up / drill-down within one class (Aves, Insecta), kappa tuned by ARI on training images, 3 seeds.
# Logs: logs/inat_e6/<step>.log   Progress: logs/PROGRESS.md   Results: results/inat/seed*/e6_<class>.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python; export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=20
LOG=logs/inat_e6; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | inat-e6/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
note ALL started
for c in Aves Insecta; do
  pids=(); for s in 0 1 2; do ( note "${c}_s$s" started; t0=$SECONDS
    if $PY -m sse.inat e6 --seed "$s" --cls "$c" > "$LOG/${c}_s$s.log" 2>&1; then note "${c}_s$s" "done ($((SECONDS-t0)) s)"
    else note "${c}_s$s" "**FAILED** — see $LOG/${c}_s$s.log"; exit 1; fi ) & pids+=($!); done
  fail=0; for p in "${pids[@]}"; do wait "$p" || fail=1; done; [ $fail = 0 ] || { note ALL "**FAILED**"; exit 1; }
done
note ALL "finished — results/inat/seed*/e6_<class>.md"
