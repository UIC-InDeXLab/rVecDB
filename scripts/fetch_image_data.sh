#!/usr/bin/env bash
# Download AwA2 (zip, read directly) and iNat 2021 validation (tar.gz, read directly) into data/.
# Logs: logs/data/<step>.log   Progress: logs/PROGRESS.md   Resumable (curl -C -).
set -uo pipefail
cd "$(dirname "$0")/.."
LOG=logs/data; PROG=logs/PROGRESS.md; mkdir -p "$LOG" data/awa2 data/inat
note() { echo "| $(date '+%m-%d %H:%M:%S') | data/$1 | $2 |" >> "$PROG"; echo "[$(date +%T)] $1: $2"; }
step() {
  local name=$1; shift
  note "$name" "started"; local t0=$SECONDS
  if "$@" > "$LOG/$name.log" 2>&1; then note "$name" "done ($((SECONDS - t0)) s)"
  else note "$name" "**FAILED** — see $LOG/$name.log"; return 1; fi
}
get() { local url=$1 out=$2 size=$3
  [ -f "$out" ] && [ "$(stat -c %s "$out")" = "$size" ] && return 0
  curl -fL --retry 20 --retry-delay 10 -C - -o "$out" "$url" && [ "$(stat -c %s "$out")" = "$size" ]; }
I=https://ml-inat-competition-datasets.s3.amazonaws.com/2021
step inat_val_json get $I/val.json.tar.gz data/inat/val.json.tar.gz "$(curl -sI $I/val.json.tar.gz | awk 'tolower($1)=="content-length:"{print $2+0}')" &
step inat_val get $I/val.tar.gz data/inat/val.tar.gz 8931661582 &
step awa2 get https://cvml.ista.ac.at/AwA2/AwA2-data.zip data/awa2/AwA2-data.zip 13923888724 &
wait
note ALL "finished"
