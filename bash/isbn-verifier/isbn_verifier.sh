#!/usr/bin/env bash

boolRC () { (( $? == 0 )) && echo true || echo false; }

isbn10 () {
  local n="${1//-}" 
  local -i sum mul
  local char

  (( ${#n} != 10 )) && return 1
  [[ $n = [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9X] ]] || return 1
  for (( i = 0; i < 10; i++ )); do
    (( mul = 10 - i ))
    char="${n:i:1}"
    [[ $char = 'X' ]] && char=10
    (( sum += char * mul ))
  done
  (( sum % 11 == 0 ))
}

(( $# == 1 )) || exit 1
isbn10 "$1"
boolRC

# vim:ts=2:sw=2:expandtab
