#!/usr/bin/env bash
# Run rVecDB training on the lab GPU server (ssh alias: newLab) from this machine.
#   bash scripts/newlab.sh setup     # copy code, create .venv (requirements.txt) + .venv-specter (torch + adapters) on the server
#   bash scripts/newlab.sh push      # copy code + data/openalex + cache/openalex (tables built locally)
#   bash scripts/newlab.sh run       # start scripts/run_openalex.sh on the server in the background (nohup)
#   bash scripts/newlab.sh status    # GPU use + last lines of the server's logs/PROGRESS.md
#   bash scripts/newlab.sh pull      # copy results/openalex + logs/openalex + PROGRESS.md back here
# Never sent to the server: paper/ (Overleaf, private), .env (API key; fetching runs locally), local venvs.
# The GPU is shared with other jobs: `run` never stops or touches them.
# All commands share ONE ssh connection (the server refuses rapid repeated connections).
set -euo pipefail
cd "$(dirname "$0")/.."
HOST=${HOST:-newLab}
RDIR=${RDIR:-Projects/rVecDB}
SSH_OPTS="-o BatchMode=yes -o ConnectTimeout=20 -o ControlMaster=auto -o ControlPath=$HOME/.ssh/cm-%r@%h:%p -o ControlPersist=8h"
rsh() { ssh $SSH_OPTS "$HOST" "cd $RDIR && $*"; }
code() {
  rsync -a -e "ssh $SSH_OPTS" --exclude paper/ --exclude .env --exclude '.venv*/' --exclude data/ --exclude cache/ \
        --exclude .claude/ --exclude results/ --exclude logs/ ./ "$HOST:$RDIR/"
  # logs/PROGRESS.md must exist on the server (steps append to it); never overwrite the server's copy
  rsh "mkdir -p logs results && touch logs/PROGRESS.md"
}

case "${1:-}" in
  setup)
    ssh $SSH_OPTS "$HOST" "mkdir -p $RDIR"
    code
    # main env = exactly requirements.txt (pip check must be clean)
    rsh "[ -x .venv/bin/python ] || python3.12 -m venv .venv"
    rsh ".venv/bin/pip uninstall -y -q adapters 2>/dev/null; .venv/bin/pip install -q --upgrade pip && \
         .venv/bin/pip install -q -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu128 && \
         .venv/bin/pip check"
    # SPECTER2 env: `adapters` pins an older transformers, so it gets its own env (used only by the encode step)
    rsh "[ -x .venv-specter/bin/python ] || python3.12 -m venv .venv-specter"
    rsh ".venv-specter/bin/pip install -q --upgrade pip && \
         .venv-specter/bin/pip install -q torch==2.11.0+cu128 --extra-index-url https://download.pytorch.org/whl/cu128 && \
         .venv-specter/bin/pip install -q adapters numpy pandas pyarrow scipy requests"
    # check torch sees the GPU and SPECTER2 + adapter load (CPU only: nothing touches the running GPU job)
    rsh ".venv/bin/python -c \"import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())\""
    rsh "CUDA_VISIBLE_DEVICES= .venv-specter/bin/python -c \"
from adapters import AutoAdapterModel
m = AutoAdapterModel.from_pretrained('allenai/specter2_base')
m.load_adapter('allenai/specter2', source='hf', load_as='proximity', set_active=True)
m.set_active_adapters('proximity')
print('specter2 + proximity adapter OK, active:', m.active_adapters)\""
    ;;
  push)
    code
    rsh "mkdir -p data/openalex cache/openalex"
    rsync -a -e "ssh $SSH_OPTS" --info=stats1 data/openalex/ "$HOST:$RDIR/data/openalex/"
    rsync -a -e "ssh $SSH_OPTS" --info=stats1 cache/openalex/ "$HOST:$RDIR/cache/openalex/"
    ;;
  run)
    rsh "pgrep -f 'scripts/run_[o]penalex.sh' >/dev/null && { echo 'already running'; exit 1; } || true"
    rsh "mkdir -p logs/openalex && SKIP_TRAIN=${SKIP_TRAIN:-} SKIP_E6=${SKIP_E6:-} ENC_PY=.venv-specter/bin/python setsid nohup bash scripts/run_openalex.sh > logs/openalex/run.out 2>&1 < /dev/null & echo started"
    ;;
  status)
    ssh $SSH_OPTS "$HOST" "nvidia-smi --query-gpu=memory.used,memory.total,utilization.gpu --format=csv,noheader; \
      nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader"
    rsh "grep openalex logs/PROGRESS.md | tail -15"
    ;;
  pull)
    mkdir -p results/openalex logs/openalex
    rsync -a -e "ssh $SSH_OPTS" "$HOST:$RDIR/results/openalex/" results/openalex/
    rsync -a -e "ssh $SSH_OPTS" "$HOST:$RDIR/logs/openalex/" logs/openalex/
    # server progress lines for OpenAlex, appended to the local PROGRESS.md (not already present)
    rsh "grep openalex/ logs/PROGRESS.md" | grep -vxFf logs/PROGRESS.md >> logs/PROGRESS.md || true
    ;;
  *) sed -n 2,8p "$0"; exit 1 ;;
esac
