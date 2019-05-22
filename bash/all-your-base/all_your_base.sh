#!/usr/bin/env bash

(( $# == 3 )) || exit 1

error () {
  echo Error
  exit 1
}

toDecimal () {
  ibase=$1
  read -a words <<< "$2"
  local -i result=0 power=${#words[@]}

  (( ibase > 1 )) || return 1

  for w in "${words[@]}"; do
    (( w >= 0 && w < ibase )) || return 1
    # Reduce the power/place by one place. Add the digit's value to result.
    (( power-- , result += w * ibase ** power ))
  done
  echo "$result"
}

fromDecimal () {
  val=$1 obase=$2 result=()
  (( obase > 1 )) || return 1
  while (( val )); do
    (( digit = val % obase ))  # Extract one digit.
    (( val -= digit , val /= obase ))  # Reduce and shift the remainder.
    result=( "$digit" "${result[@]}" )
  done
  echo "${result[@]}"
}

decimalVal="$(toDecimal "$1" "$2")" || error
fromDecimal "$decimalVal" "$3" || error

# vim:ts=2:sw=2:expandtab
