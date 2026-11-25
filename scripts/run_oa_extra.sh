#!/usr/bin/env bash
# OpenAlex extras: E9 trained shared join keys, E10 join threshold sweep, E11 GROUP BY_k  (3 seeds each).
# Logs: logs/oa_extra/<step>.log   Progress: logs/PROGRESS.md
# Results: results/openalex/seed*/e9_joinkeys.md, e10_sweep.md, e11_groupk.md; 3-seed: results/openalex/extra_tables.md
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=16 OPENBLAS_NUM_THREADS=16 MKL_NUM_THREADS=16
LOG=logs/oa_extra; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | oa_extra/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
note ALL started
[ -f cache/openalex/author_bge.npy ] || step profile $PY -m sse.oa_extra profile || exit 1
for s in ${SEEDS:-0 1 2}; do
  for c in ${CMDS:-joinkeys sweep groupk}; do step "${c}_s$s" $PY -m sse.oa_extra "$c" --seed "$s" || exit 1; done
done
note ALL "finished — results/openalex/seed*/e9_joinkeys.md, e10_sweep.md, e11_groupk.md"
