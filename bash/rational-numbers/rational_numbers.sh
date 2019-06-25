#!/usr/bin/env bash

(( $# == 3 )) || (( $# == 2 )) || exit 1

op=$1; shift
IFS='/' read a1 b1 <<< "$1"
(( $# == 2 )) && IFS='/' read a2 b2 <<< "$2"

add () { (( a3 = a1 * b2 + a2 * b1 , b3 = b1 * b2 )); }
subtract () { (( a3 = a1 * b2 - a2 * b1 , b3 = b1 * b2 )); }
multiply () { (( a3 = a1 * a2, b3 = b1 * b2 )); }
divide () { (( a3 = a1 * b2 , b3 = a2 * b1 )); }
abs () { (( a3 = a1 > 0 ? a1 : -a1, b3 = b1 > 0 ? b1 : -b1 )); }
pow () { (( a3 = a1 ** a2 , b3 = b1 ** a2 )); }
reduce () { (( a3 = a1 , b3 = b1 )); }
rpow () { ((  )); }  # How would I do nth_root() in bash? Brute force?!

reduce_print () {
  # a=abs(a) b=abs(b)
  (( a = a3 > 0 ? a3 : -a3, b = b3 > 0 ? b3 : -b3 ))
  # https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclid's_algorithm
  while ((b)); do (( c = a % b, a = b, b = c )); done
  (( b3 < 0 )) && (( a3 = -a3 , b3 = -b3 ))
  printf '%d/%d\n' "$((a3/a))" "$((b3/a))"
}

case "$op" in
  '+') add;;
  '-') subtract;;
  '*') multiply;;
  '/') divide;;
  *) "$op";;
esac

reduce_print

# vim:ts=2:sw=2:expandtab
