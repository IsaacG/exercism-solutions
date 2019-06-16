#!/usr/bin/env bash

codes=('wink' 'double blink' 'close your eyes' 'jump')

handshake () {
  (( $# == 1 )) || exit 1
  local -a out
  for ((i = 0; i < ${#codes[@]}; i++)); do
    if (( 1 << i & $1 )); then
      # Append or prepend based on reverse bit.
      (( 1 << 4 & $1 )) && out=( "${codes[i]}" "${out[@]}" ) || out+=( "${codes[i]}" )
    fi
  done
  local IFS=,; echo "${out[*]}"
}

handshake "$@"

# vim:ts=2:sw=2:expandtab
