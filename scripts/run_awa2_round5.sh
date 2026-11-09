#!/usr/bin/env bash
# AwA2 round 5 — three things, 3 seeds each:
#   A) compactness: SSE at 768 / 256 / 128 numbers vs B3 separate vectors (920)
#   B) validation split: pick the SSE version (main / tree / treeSC) WITHOUT looking at test
#   C) Q2 queries: Order prototype filter + habitat BAND + ranking
# Logs: logs/awa2_round5/<step>.log   Progress: logs/PROGRESS.md
# Results: results/awa2/round5_compact_summary.md, round5_val_summary.md, r5_seed*/q2.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/awa2_round5; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | round5/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
parallel3() {  # parallel3 <name-prefix> <function>   runs <function> s for s=0,1,2 in parallel
  local pids=() fail=0
  for s in 0 1 2; do "$2" "$s" & pids+=($!); done
  for p in "${pids[@]}"; do wait "$p" || fail=1; done
  [ $fail = 0 ] || { note "ALL" "**FAILED** in $1"; exit 1; }
}
note "ALL" "started (round 5: compactness + validation pick + Q2)"

# ---------- training (GPU, seconds each)
for s in 0 1 2; do
  step "train_tree256_s$s" $PY -m sse.train_sse --variant tree --dim 256 --seed "$s" --name "tree256_s$s" || exit 1
  step "train_tree128_s$s" $PY -m sse.train_sse --variant tree --dim 128 --seed "$s" --name "tree128_s$s" || exit 1
  for v in main tree treesc; do
    step "train_VAL_${v}_s$s" env SSE_VAL=1 $PY -m sse.train_sse --variant "$v" --seed "$s" --name "val_${v}_s$s" || exit 1
  done
done

export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20

# ---------- A) compactness
evalA() { step "eval_compact_s$1" $PY -m sse.evaluate --out "r5c_seed$1" --seed "$1" --mrl "" --no-baselines \
  --sse "SSE-768=tree_s$1,SSE-256=tree256_s$1,SSE-128=tree128_s$1" --extra "B3 separate (920)=b3tree_s$1"; }
parallel3 compactness evalA
step "summarize_compact" $PY -m sse.summarize_seeds --pattern "r5c_seed*/results.json" --out round5_compact_summary.md || exit 1

# ---------- B) validation pick (real test images are never used)
evalB() { step "eval_VAL_s$1" env SSE_VAL=1 $PY -m sse.evaluate --out "val_seed$1" --seed "$1" --mrl "" --no-baselines \
  --sse "SSE=val_main_s$1,SSE-tree=val_tree_s$1,SSE-treeSC=val_treesc_s$1"; }
parallel3 validation evalB
step "summarize_val" $PY -m sse.summarize_seeds --pattern "val_seed*/results.json" --out round5_val_summary.md || exit 1

# ---------- C) Q2
evalC() { step "q2_s$1" $PY -m sse.q2 --sse "tree_s$1" --extra "B3 separate=b3tree_s$1,B4 CSN=csntree_s$1" --out "r5_seed$1" --seed "$1"; }
parallel3 q2 evalC

note "ALL" "finished — results/awa2/round5_compact_summary.md, round5_val_summary.md, r5_seed*/q2.md"
