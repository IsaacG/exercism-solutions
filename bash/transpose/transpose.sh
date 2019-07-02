#!/usr/bin/env bash

(( $# == 0 )) || exit 1

mapfile -t lines
# Figure out the number of output lines, ie the max input line len.
max=0
for l in "${lines[@]}"; do
  (( ${#l} > max )) && max=${#l}
done

# For each column, output a line.
for ((i = 0; i < max; i++)); do
  r= s=
  for l in "${lines[@]}"; do
    # Build the line, tracking spaces separately.
    # Only fill in spaces when they are followed by non-space.
    if (( ${#l} > i )); then
      r+="$s${l:i:1}"
      s=
    else
      s+=' '
    fi
  done
  echo "$r"
done

# vim:ts=2:sw=2:expandtab
