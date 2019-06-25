#!/usr/bin/env bash

# Input validation
(( $# == 3 )) || exit 1
if [[ $1 != "smallest" ]] && [[ $1 != "largest" ]]; then
  echo"first arg should be 'smallest' or 'largest'"
  exit 1
fi
(( $2 <= $3 )) || { echo "min must be <= max"; exit 1; }

palindrome_test () {
  local -i i
  for ((i = 0; i < "${#1}"; i++)); do
    [[ "${1:i:1}" = "${1: ${#1} - i - 1:1}" ]] || return 1
  done
  return 0
}

show () {
  printf '%d: ' "$1"
  for ((i = 1; i * i <= $1; i++ )); do
    (( $1 % i == 0 )) && printf '[%d, %d] ' "$i" "$(($1 / i))"
  done
  printf '\n'
}

# Compute all palindromes
found=()
for ((i = $2; i <= $3; i++)); do
  for ((j = i; j <= $3; j++)); do
    palindrome_test $((i * j)) && found+=( $((i * j)) )
  done
done

# Find min/max
(( $found )) || exit 0
min=$found
max=$found
for i in "${found[@]}"; do
  (( i < min )) && min=$i
  (( i > max )) && max=$i
done

# Show
case "$1" in
  "smallest") show "$min";;
  "largest") show "$max";;
esac

# vim:ts=2:sw=2:expandtab
