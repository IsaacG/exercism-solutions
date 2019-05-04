#!/usr/bin/env bash

fail () {
  echo "Error: invalid input"
  exit 1
}

grains () {
  (( $# == 1 )) || fail
  if [[ $1 = total ]]; then
    bc <<< '(2 ^ 64) - 1'
  else
    (( $1 > 0 && $1 < 65 )) || fail
    bc <<< "2 ^ ($1 - 1)"
  fi
}

grains "$@"

# vim:ts=2:sw=2:expandtab
