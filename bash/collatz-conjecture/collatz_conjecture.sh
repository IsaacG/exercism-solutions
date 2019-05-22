#!/usr/bin/env bash

boolRC () { (( $? == 0 )) && echo true || echo false; }

collatz () {
  (( $# == 1 )) || exit 1
  (( $1 < 1 )) && { echo "Error: Only positive numbers are allowed"; exit 1; }

  declare -i count=0 val=$1
  until (( val == 1 )); do
    (( count++ ))
    (( val % 2 )) && (( val = val * 3 + 1 )) || (( val /= 2 ))
  done
  echo "$count"
}

collatz "$@"

# vim:ts=2:sw=2:expandtab
