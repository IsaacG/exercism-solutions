#!/usr/bin/env bash

(( $# == 1 || $# == 2 )) || exit 1

modifier () {
  p=$1
  (( $p % 2 && p-- ))
  echo $(( p / 2 - 5 ))
}

roll () {
  local -i sum=0 min=6 i
  for i in {1..4}; do
    num=$(( RANDOM % 6 + 1 ))
    (( num < min && (min = num) ))
    (( sum += num ))
  done
  echo $(( sum - min ))
}

generate () {
    local -A attr
    for i in strength dexterity constitution intelligence wisdom charisma; do
      a=$( roll )
      attr[$i]=$a
      printf '%s %d\n' "$i" "$a"
    done
    printf '%s %d\n' hitpoints $(( 10 + ${attr[constitution]} ))
}

"$@"

# vim:ts=2:sw=2:expandtab
