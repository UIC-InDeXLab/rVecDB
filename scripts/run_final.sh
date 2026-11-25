#!/usr/bin/env bash
# Waits for the iNat rebuild and the AwA2 extras, then: iNat GROUP BY_k (3 seeds) and E7 cost (quiet server).
# Logs: logs/final/<step>.log   Progress: logs/PROGRESS.md
# Results: results/inat/seed*/groupk.md, results/awa2/x_cost/cost_n*.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
export PYTHONUNBUFFERED=1
LOG=logs/final; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | final/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
note ALL "started (waiting for inat round2)"
c0=$(grep -cE "inat2/ALL \| (finished|\*\*FAILED)" $PROG)
until [ "$(grep -cE "inat2/ALL \| (finished|\*\*FAILED)" $PROG)" -gt "$c0" ]; do sleep 60; done
for s in 0 1 2; do step "inat_groupk_s$s" $PY -m sse.inat_extra groupk --seed $s || true; done
note ALL "waiting for awa2_extra"
while pgrep -f "run_awa2[_]extra.sh" >/dev/null; do sleep 60; done
for n in 100000 1000000; do step "cost_n$n" env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 $PY -m sse.cost --n $n || true; done
note ALL "finished — results/inat/seed*/groupk.md, results/awa2/x_cost/"
