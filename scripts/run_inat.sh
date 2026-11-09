#!/usr/bin/env bash
# iNat 2021 (validation set): prep (metadata + CLIP) -> train 5 methods x 3 seeds -> E2/E2b/E3 x 3 seeds -> E6 x 3 seeds.
# Logs: logs/inat/<step>.log   Progress: logs/PROGRESS.md   Results: results/inat/seed*/results.md, e6.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/inat; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | inat/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
note "ALL" "started"
[ -f cache/inat/clip_img.npy ] || step prep $PY -m sse.inat prep || exit 1
for s in 0 1 2; do
  for m in tree main mrl b3 csn; do step "train_${m}_s$s" $PY -m sse.inat train --method "$m" --seed "$s" || exit 1; done
done
export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20
run3() { local pids=() fail=0; for s in 0 1 2; do step "$1_s$s" $PY -m sse.inat "$1" --seed "$s" & pids+=($!); done
         for p in "${pids[@]}"; do wait "$p" || fail=1; done; [ $fail = 0 ] || { note ALL "**FAILED** in $1"; exit 1; }; }
run3 eval
run3 e6
note "ALL" "finished — results/inat/seed*/results.md, e6.md"
