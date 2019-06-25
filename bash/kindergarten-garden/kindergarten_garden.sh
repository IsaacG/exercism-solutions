#!/usr/bin/env bash

declare -a names=(Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry)
declare -A plant=( [R]=radishes [G]=grass [C]=clover [V]=violets )

declare -a rows=( $1 ) out=()
declare name=$2

for (( i = 0; i <= 12; i++ )); do
  [[ "$name" = "${names[i]}" ]] && break
done
(( i == 12 )) && exit 1

add () { out+=( ${plant[$1]} ); }
add ${rows[0]:i*2+0:1}
add ${rows[0]:i*2+1:1}
add ${rows[1]:i*2+0:1}
add ${rows[1]:i*2+1:1}
echo "${out[*]}"


# vim:ts=2:sw=2:expandtab
