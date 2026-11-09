#!/usr/bin/env bash
# AwA2 round 2:
#   (1) fairer yes/no-label SSE ("hardj": credit for each shared habitat)
#   (2) taxonomy weight 0.5 / 1 / 2
#   (3) everything with 3 random starts (seeds 0, 1, 2), then mean ± spread
#
# Logs:      logs/awa2_round2/<step>.log
# Progress:  logs/PROGRESS.md
# Results:   results/awa2/seed{0,1,2}/results.md   and   results/awa2/round2_summary.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/awa2_round2
PROG=logs/PROGRESS.md
mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | round2/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}

note "ALL" "started (round 2: hardj + taxonomy weight + 3 seeds)"

# ---- training: all variants x 3 seeds (seconds each, sequential on the GPU)
for s in 0 1 2; do
  for wp in 0.5 1 2; do
    step "train_main_wp${wp}_s$s" $PY -m sse.train_sse --variant main --w_prefix "$wp" --seed "$s" --name "main_wp${wp}_s$s" || exit 1
  done
  step "train_hard_s$s"  $PY -m sse.train_sse --variant hard  --seed "$s" --name "hard_s$s"  || exit 1
  step "train_hardj_s$s" $PY -m sse.train_sse --variant hardj --seed "$s" --name "hardj_s$s" || exit 1
  step "train_mrl_s$s"   $PY -m sse.train_sse --variant mrl   --seed "$s" --name "mrl_s$s"   || exit 1
done

# ---- evaluation: one run per seed, 3 in parallel (CPU-bound; ~20 threads each)
export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20
pids=()
for s in 0 1 2; do
  step "evaluate_s$s" $PY -m sse.evaluate --out "seed$s" --seed "$s" --mrl "mrl_s$s" \
    --sse "SSE=main_wp0.5_s$s,SSE-wp1=main_wp1_s$s,SSE-wp2=main_wp2_s$s,SSE-hard=hard_s$s,SSE-hardJ=hardj_s$s" &
  pids+=($!)
done
fail=0; for p in "${pids[@]}"; do wait "$p" || fail=1; done
[ $fail = 0 ] || { note "ALL" "**FAILED** in evaluation"; exit 1; }

step "summarize" $PY -m sse.summarize_seeds || exit 1
note "ALL" "finished — results: results/awa2/round2_summary.md"
