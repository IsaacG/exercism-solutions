#!/usr/bin/env bash

(( $# == 1 )) || exit 1

declare -a pairs

for (( a = 1; a <= $1; a++ )); do
  for (( b = a; b <= $1; b++ )); do
    (( cc = a**2 + b**2 ))
    (( cc > $1 ** 2 )) && break
    for (( c = 1; c**2 < cc; c++ )); do
      :
    done
    (( c**2 == cc )) && (( a + b + c == $1 )) && pairs+=( "$a,$b,$c" )
  done
done

IFS=$'\n'; echo "${pairs[*]}"


# vim:ts=2:sw=2:expandtab
