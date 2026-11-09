#!/usr/bin/env bash
# Full AwA2 pipeline: wait for download -> CLIP features -> train SSE variants -> evaluate E1-E5.
#
# Logs:      logs/awa2/<step>.log       (full output of each step)
# Progress:  logs/PROGRESS.md           (one line per step: started / done / FAILED, with times)
set -uo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
export PYTHONUNBUFFERED=1
LOG=logs/awa2
PROG=logs/PROGRESS.md
mkdir -p "$LOG"
[ -f "$PROG" ] || printf "# Progress\n\n| time | step | status |\n|---|---|---|\n" > "$PROG"

note() { echo "| $(date '+%m-%d %H:%M:%S') | $1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }

step() {  # step <name> <command...>
  local name=$1; shift
  note "$name" "started"
  local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then
    note "$name" "done ($((SECONDS - t0)) s) — log: $LOG/$name.log"
  else
    note "$name" "**FAILED** — see $LOG/$name.log"
    exit 1
  fi
}

# 1) wait for the AwA2 download to finish, then check it is complete
ZIP=data/awa2/AwA2-data.zip
EXPECTED=13923888724
note "download" "waiting for AwA2 zip"
while pgrep -f "curl.*AwA2-data.zip" > /dev/null; do sleep 20; done
if [ "$(stat -c %s "$ZIP")" != "$EXPECTED" ]; then
  note "download" "**FAILED** — size $(stat -c %s "$ZIP") != $EXPECTED"
  exit 1
fi
note "download" "done (size OK)"

step extract   $PY -m sse.extract
step train_main $PY -m sse.train_sse --variant main
step train_hard $PY -m sse.train_sse --variant hard
step train_mrl  $PY -m sse.train_sse --variant mrl
step evaluate  $PY -m sse.evaluate
note "ALL" "finished — results: results/awa2/results.md"
