#!/usr/bin/env bash

initial=(
  'This is the house that Jack built.'
  'This is the malt'
  'This is the rat'
  'This is the cat'
  'This is the dog'
  'This is the cow with the crumpled horn'
  'This is the maiden all forlorn'
  'This is the man all tattered and torn'
  'This is the priest all shaven and shorn'
  'This is the rooster that crowed in the morn'
  'This is the farmer sowing his corn'
  'This is the horse and the hound and the horn'
)

refrain=(
  'that lay in the house that Jack built.'
  'that ate the malt'
  'that killed the rat'
  'that worried the cat'
  'that tossed the dog'
  'that milked the cow with the crumpled horn'
  'that kissed the maiden all forlorn'
  'that married the man all tattered and torn'
  'that woke the priest all shaven and shorn'
  'that kept the rooster that crowed in the morn'
  'that belonged to the farmer sowing his corn'
)


(( $# == 2 )) || exit 1

phrase () {
  local -i i=$(($1 - 1))
  printf '%s\n' "${initial[i]}"
  for (( i-- ; i >= 0; i-- )); do
    printf '%s\n' "${refrain[i]}"
  done
  printf '\n'
}

house () {
  if (( $1 > $2 )) || (( $1 < 1 || $2 < 1 )) || (( $1 > 12 || $2 > 12 )); then
    echo invalid
    return 1
  fi
  local -i i
  for (( i = $1; i <= $2; i++ )); do
    phrase "$i"
  done
}

house "$@"

# vim:ts=2:sw=2:expandtab
