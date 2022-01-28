#!/usr/bin/env bash

word_count () {
  shopt -s extglob
  (( $# == 1 )) || exit 1
  local -A count
  IFS=', ' read -ra words <<< "${1,,}"  # explicit word splitting
  IFS=$' \t\n'
  for w in "${words[@]}"; do
    w=${w##*([[:punct:]])}
    w=${w%%*([[:punct:]])}
    [[ $w ]] || continue
    (( 'count[$w]'++ ))
  done

  for w in "${!count[@]}"; do
    printf '%s: %d\n' "$w" "${count[$w]}"
  done
}

word_count "$@"

# vim:ts=2:sw=2:expandtab
