#!/usr/bin/env bash

(( $# == 1 )) || exit 1
(( $1 > 0 )) || { echo "Classification is only possible for natural numbers."; exit 1; }

aliquot () {
  local -i sum=0
  for ((i = 1; i*2 <= $1; i++)); do (( $1 % i == 0 && (sum+=i) )); done
  echo "$sum"
}

a=$(aliquot "$1")
(( a == $1 )) && echo perfect
(( a > $1 )) && echo abundant
(( a < $1 )) && echo deficient
exit 0

# vim:ts=2:sw=2:expandtab
