#!/usr/bin/env bash

allergens=(
  eggs
  peanuts
  shellfish
  strawberries
  tomatoes
  chocolate
  pollen
  cats
)

boolRC () { (( $? == 0 )) && echo true || echo false; }

(( $# == 3 || $# == 2 )) || exit 1

allergic_to () {
  score=$1
  allergen=$2
  v=1
  for a in "${allergens[@]}" ; do
    if [[ $a = "$allergen" ]]; then
      (( score & v ))
      boolRC
    fi
    (( v <<= 1 ))
  done
}

list () {
  score=$1
  v=1
  allergies=()
  for a in "${allergens[@]}" ; do
    (( score & v )) && allergies+=( "$a" )
    (( v <<= 1 ))
  done
  echo "${allergies[@]}"
}

"$2" "$1" "$3"

# vim:ts=2:sw=2:expandtab
