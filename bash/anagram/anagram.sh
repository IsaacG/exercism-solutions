#!/usr/bin/env bash

isMatch () {
  (( ${#want[@]} == ${#count[@]} )) || return 1
  for k in "${!want[@]}"; do
    [[ -v 'count[$k]' ]] && (( count[$k] == want[$k] )) || return 1
  done
  return 0
}

anagram () {
  (( $# == 2 )) || exit 1
  read -a words <<< "$2"
  match="${1,,}"
  declare -a found

  declare -A want
  for (( i = 0; i < ${#match}; i++ )) do (( 'want[${match:$i:1}]'++ )); done
  for word in "${words[@]}"; do
    declare -A count
    w="${word,,}"
    [[ $w = $match ]] && continue  # Word is not its own anagram
    for (( i = 0; i < ${#w}; i++ )) do (( 'count[${w:$i:1}]'++ )); done
    isMatch && found+=($word)
    unset count
  done

  echo "${found[@]}"
}

anagram "$@"

# vim:ts=2:sw=2:expandtab
