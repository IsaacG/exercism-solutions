#!/usr/bin/env bash

boolRC () { (( $? == 0 )) && echo true || echo false; }

invalid () {
  echo 'Invalid number.  [1]NXX-NXX-XXXX N=2-9, X=0-9'
  exit 1
}

phone () {
  (( $# == 1 )) || exit 1
  num="${1//[^[:digit:]]/}"
  (( ${#num} == 11 )) && [[ $num = 1* ]] && num="${num:1:10}"
  (( ${#num} != 10 )) && invalid
  [[ ${num:0:1} = [01] || ${num:3:1} = [01] ]] && invalid
  echo "$num"
}

phone "$@"

# vim:ts=2:sw=2:expandtab
