#!/usr/bin/env bash

isPangran () {
  w="${1^^}"
  for c in {A..Z}; do
    [[ $w = *$c* ]] || return 1
  done
  return 0
}
boolRC () { (( $? == 0 )) && echo true || echo false; }

(( $# == 1 )) || exit 1
isPangran "$1"
boolRC

# vim:ts=2:sw=2:expandtab
