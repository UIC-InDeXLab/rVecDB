#!/usr/bin/env bash
# OpenAlex (research papers): fetch papers + authors' papers (API key in .env) -> build (tables) -> encode (SPECTER2 vectors)
#   -> train 6 methods x 3 seeds -> E2/E2b/E3, E8 (joins + institutions), E6 x 3 seeds.
# Logs: logs/openalex/<step>.log   Progress: logs/PROGRESS.md
# Results: results/openalex/seed*/results.md, e8.md, e6_physical.md
# SPECTER2 needs `adapters`, which pins an older transformers -> it lives in its own env: ENC_PY=.venv-specter/bin/python
# (scripts/newlab.sh sets this). Or ENCODER=specter2_base (no adapter) / ENCODER=bge with the main .venv.
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}          # local fetch: PY=.venv-fetch/bin/python STOP_AFTER=build
ENCODER=${ENCODER:-specter2}
export PYTHONUNBUFFERED=1
LOG=logs/openalex; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | openalex/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
note "ALL" "started (encoder $ENCODER)"
[ -f data/openalex/papers/DONE ]   || step fetch_papers  $PY -m sse.openalex fetch         || exit 1
[ -f data/openalex/AUTHORS_DONE ]  || step fetch_authors $PY -m sse.openalex fetch_authors || exit 1
[ -f cache/openalex/aw.parquet ]   || step build $PY -m sse.openalex build || exit 1
[ "${STOP_AFTER:-}" = build ] && { note "ALL" "stopped after build (tables in cache/openalex/)"; exit 0; }
[ -f cache/openalex/aw_emb.npy ]   || step encode ${ENC_PY:-$PY} -m sse.openalex encode --encoder "$ENCODER" || exit 1
if [ -z "${SKIP_TRAIN:-}" ]; then          # SKIP_TRAIN=1: reuse trained models, only re-evaluate
for s in 0 1 2; do
  for m in treesc tree main mrl b3sc csnsc; do step "train_${m}_s$s" $PY -m sse.openalex train --method "$m" --seed "$s" || exit 1; done
done
fi
[ -f cache/openalex/related.npz ] || step related $PY -m sse.openalex related || exit 1   # semantic answer key (bge-large)
export OMP_NUM_THREADS=20 OPENBLAS_NUM_THREADS=20 MKL_NUM_THREADS=20
run3() { local pids=() fail=0; for s in 0 1 2; do step "$1_s$s" $PY -m sse.openalex "$1" --seed "$s" & pids+=($!); done
         for p in "${pids[@]}"; do wait "$p" || fail=1; done; [ $fail = 0 ] || { note ALL "**FAILED** in $1"; exit 1; }; }
run3 eval
run3 join
[ -n "${SKIP_E6:-}" ] || run3 e6
note "ALL" "finished — results/openalex/seed*/results.md, e8.md, e6_physical.md"
