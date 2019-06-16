#!/usr/bin/env bash

# Handle poor inputs and special requirements.
check () {
  (( $# == 2 )) || { echo 1; exit 0; }
  shopt -s extglob
  [[ $1 == +(0) ]] && { echo 0; exit 0; }
  (( $2 == 0 )) && { echo 1; exit 0; }
  [[ $1 = *[^[:digit:]]* ]] && { echo "input must only contain digits"; exit 1; }
  (( ${#1} < $2 )) && { echo "span must be smaller than string length"; exit 1; }
  (( $2 < 0 )) && { echo "span must be greater than zero"; exit 1; }
  return 0
}

# Compute the max for a span.
part () {
  local -i max last=1
  for ((i = 0; i < $2 && i < ${#1}; i++)); do (( last *= ${1:i:1} )); done
  max=$last
  for ((i = 0; i + $2 < ${#1}; i++)); do
    (( last = ( last / ${1:i:1} * ${1:i+$2:1} ) ))
    (( last > max && (max=last) ))
  done
  echo "$max"
}

# Compute the max for all spans.
largest () {
  local -i max=0
  IFS=0 read -a parts <<< "$1"
  for run in "${parts[@]}"; do
    (( ${#run} >= $2 )) || continue
    new=$( part $run $2 )
    (( new > max && (max=new) ))
  done
  echo "$max"
}

check "$@"
largest "$@"

# vim:ts=2:sw=2:expandtab
