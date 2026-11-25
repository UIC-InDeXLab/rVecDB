#!/usr/bin/env bash
# AwA2 for the submission: rebuild the paper's models (CLIP ViT-L/14), re-evaluate, then the new experiments:
#   GROUP BY_k + REP + aggregates (Q4/Q5), text references, block-size allocation (validation), EVA-CLIP encoder.
# Logs: logs/awa2_extra/<step>.log   Progress: logs/PROGRESS.md
# Results: results/awa2/x_eval_seed*/ (main tables), x_q2_seed*/, x_seed*/{groupk,agg,textq}.md, x_rep/,
#          x_blocksize.md, results/awa2_eva/ (EVA encoder)
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
export PYTHONUNBUFFERED=1
LOG=logs/awa2_extra; PROG=logs/PROGRESS.md; mkdir -p "$LOG"
note() { echo "| $(date '+%m-%d %H:%M:%S') | awa2_extra/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
par3() { local pids=() fail=0; for s in 0 1 2; do "$@" "$s" & pids+=($!); done
         for p in "${pids[@]}"; do wait "$p" || fail=1; done; [ $fail = 0 ] || { note ALL "**FAILED** in $1"; exit 1; }; }
note ALL started
while [ "$(stat -c %s data/awa2/AwA2-data.zip 2>/dev/null)" != 13923888724 ]; do sleep 30; done

# ---- 1. features + models (paper encoder) ----
[ -f cache/awa2/clip_img.npy ] && [ -f cache/awa2/clip_text.npz ] || step extract $PY -m sse.extract || exit 1
python3 -c "import numpy as np; assert 'species' in np.load('cache/awa2/clip_text.npz')" 2>/dev/null || \
  step extract_text $PY -m sse.extract || exit 1
train_all() {   # train_all <cache-env-prefix> <seed>
  local s=$2
  for v in tree treesc mrl; do [ -f "${1:-cache/awa2}/emb_${v}_s$s.npy" ] || step "${3:-}train_${v}_s$s" env SSE_CACHE=${1:-cache/awa2} $PY -m sse.train_sse --variant $v --seed $s --name ${v}_s$s || return 1; done
  for b in b3 csn; do [ -f "${1:-cache/awa2}/${b}tree_s$s.npz" ] || step "${3:-}train_${b}tree_s$s" env SSE_CACHE=${1:-cache/awa2} $PY -m sse.train_baselines --method $b --tree --seed $s || return 1; done
}
for s in 0 1 2; do train_all cache/awa2 $s || exit 1
  for d in 128 256; do [ -f cache/awa2/emb_treesc${d}_s$s.npy ] || step "train_treesc${d}_s$s" $PY -m sse.train_sse --variant treesc --dim $d --seed $s --name treesc${d}_s$s || exit 1; done
done
export OMP_NUM_THREADS=16 OPENBLAS_NUM_THREADS=16 MKL_NUM_THREADS=16
ev() { step "eval_s$1" $PY -m sse.evaluate --out "x_eval_seed$1" --seed "$1" --mrl "mrl_s$1" \
        --sse "SSE-treeSC=treesc_s$1,SSE-tree=tree_s$1,SSE-treeSC-256=treesc256_s$1,SSE-treeSC-128=treesc128_s$1" \
        --extra "B3 separate=b3tree_s$1,B4 CSN=csntree_s$1"; }
par3 ev
q2() { step "q2_s$1" $PY -m sse.q2 --sse "treesc_s$1" --extra "B3 separate=b3tree_s$1,B4 CSN=csntree_s$1" --out "x_q2_seed$1" --seed "$1"; }
par3 q2

# ---- 2. new experiments ----
for s in 0 1 2; do for c in groupk agg textq; do step "${c}_s$s" $PY -m sse.awa2_extra $c --seed $s || exit 1; done; done
step rep $PY -m sse.awa2_extra rep --seed 0 || exit 1

# ---- 3. block-size allocation (validation split only) ----
for s in 0 1 2; do
  for d in 1 2 3 4 6 8 12 16 24 32 48 64 96 128; do t=bs_hab${d}_s$s
    [ -f results/awa2/x_blocksize/$t.json ] && continue
    step "train_$t" env SSE_VAL=1 $PY -m sse.train_sse --variant treesc --hab $d --seed $s --name $t || exit 1
    step "eval_$t"  env SSE_VAL=1 $PY -m sse.awa2_extra blockeval --tag $t || exit 1; done
  for d in 1 2 3 4 6 8 12 16 24 32 64; do t=bs_diet${d}_s$s
    [ -f results/awa2/x_blocksize/$t.json ] && continue
    step "train_$t" env SSE_VAL=1 $PY -m sse.train_sse --variant treesc --diet $d --seed $s --name $t || exit 1
    step "eval_$t"  env SSE_VAL=1 $PY -m sse.awa2_extra blockeval --tag $t || exit 1; done
done
step blocksummary $PY -m sse.awa2_extra blocksummary || exit 1

# ---- 4. EVA-CLIP encoder (same pipeline, cache/awa2_eva) ----
E=cache/awa2_eva; mkdir -p $E; cp -n cache/awa2/images.parquet cache/awa2/classes.pkl $E/
[ -f $E/clip_img.npy ] || step eva_extract env SSE_CACHE=$E CLIP_MODEL=EVA02-L-14 CLIP_PRETRAINED=merged2b_s4b_b131k $PY -m sse.extract || exit 1
for s in 0 1 2; do train_all $E $s eva_ || exit 1; done
eve() { step "eva_eval_s$1" env SSE_CACHE=$E SSE_OUT=results/awa2_eva $PY -m sse.evaluate --out "seed$1" --seed "$1" --mrl "mrl_s$1" \
        --sse "SSE-treeSC=treesc_s$1,SSE-tree=tree_s$1" --extra "B3 separate=b3tree_s$1,B4 CSN=csntree_s$1"; }
par3 eve
note ALL "finished — results/awa2/x_*, results/awa2/x_blocksize.md, results/awa2_eva/"
