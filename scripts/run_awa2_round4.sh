#!/usr/bin/env bash
# AwA2 round 4: the trained competitors B3 (separate vectors) and B4 (CSN), 3 seeds,
# compared against SSE and all earlier baselines.
#
# Usage: scripts/run_awa2_round4.sh <sse_tag_prefix>     e.g.  scripts/run_awa2_round4.sh tree   (uses tree_s0, tree_s1, tree_s2)
# Logs:      logs/awa2_round4/<step>.log      Progress: logs/PROGRESS.md
# Results:   results/awa2/r4_seed{0,1,2}/results.md  and  results/awa2/round4_summary.md
set -uo pipefail
cd "$(dirname "$0")/.."
SSE_TAG=${1:?give the SSE tag prefix, e.g. tree}
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/awa2_round4
PROG=logs/PROGRESS.md
mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | round4/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
note "ALL" "started (round 4: B3 separate vectors + B4 CSN vs SSE=$SSE_TAG)"
for s in 0 1 2; do
  step "train_b3_s$s"  $PY -m sse.train_baselines --method b3  --seed "$s" || exit 1
  step "train_csn_s$s" $PY -m sse.train_baselines --method csn --seed "$s" || exit 1
done
export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20
pids=()
for s in 0 1 2; do
  step "evaluate_s$s" $PY -m sse.evaluate --out "r4_seed$s" --seed "$s" --mrl "mrl_s$s" \
    --sse "SSE=${SSE_TAG}_s$s" --extra "B3 separate=b3_s$s,B4 CSN=csn_s$s" &
  pids+=($!)
done
fail=0; for p in "${pids[@]}"; do wait "$p" || fail=1; done
[ $fail = 0 ] || { note "ALL" "**FAILED** in evaluation"; exit 1; }
step "summarize" $PY -m sse.summarize_seeds --pattern "r4_seed*/results.json" --out round4_summary.md || exit 1
note "ALL" "finished — results: results/awa2/round4_summary.md"
