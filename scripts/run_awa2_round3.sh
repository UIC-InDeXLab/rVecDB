#!/usr/bin/env bash
# AwA2 round 3: graded family-tree training for the taxonomy prefixes (fix: Family prefix forgets Order).
#   SSE        = round-2 main (yes/no contrastive per level)
#   SSE-tree   = graded tree similarity only
#   SSE-treeSC = graded tree similarity + yes/no contrastive
# 3 seeds, all baselines, new check E2b (does each prefix keep coarser levels).
#
# Logs:      logs/awa2_round3/<step>.log      Progress: logs/PROGRESS.md
# Results:   results/awa2/r3_seed{0,1,2}/results.md  and  results/awa2/round3_summary.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/awa2_round3
PROG=logs/PROGRESS.md
mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | round3/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
note "ALL" "started (round 3: graded family-tree training)"
for s in 0 1 2; do
  step "train_tree_s$s"   $PY -m sse.train_sse --variant tree   --seed "$s" --name "tree_s$s"   || exit 1
  step "train_treesc_s$s" $PY -m sse.train_sse --variant treesc --seed "$s" --name "treesc_s$s" || exit 1
done
export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20
pids=()
for s in 0 1 2; do
  step "evaluate_s$s" $PY -m sse.evaluate --out "r3_seed$s" --seed "$s" --mrl "mrl_s$s" \
    --sse "SSE=main_wp0.5_s$s,SSE-tree=tree_s$s,SSE-treeSC=treesc_s$s" &
  pids+=($!)
done
fail=0; for p in "${pids[@]}"; do wait "$p" || fail=1; done
[ $fail = 0 ] || { note "ALL" "**FAILED** in evaluation"; exit 1; }
step "summarize" $PY -m sse.summarize_seeds --pattern "r3_seed*/results.json" --out round3_summary.md || exit 1
note "ALL" "finished — results: results/awa2/round3_summary.md"
