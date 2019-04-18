#!/usr/bin/env bash

main () {
  local -i sum
  l="${#1}"
  for (( i=0; i < l; i++ )); do
    sum+=$(( ${1:i:1} ** l ))
  done
  (( sum == $1 )) && echo true || echo false
}

main "$@"

# vim:ts=2:sw=2:expandtab
