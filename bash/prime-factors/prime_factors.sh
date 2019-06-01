#!/usr/bin/env bash

(( $# == 1 )) || exit 1

factors () {
  local -i num=$1 i=2
  local -a results
  while (( num > 1 )); do
    while (( num % i == 0 )); do
      results+=( $i )
      (( num = num / i ))
    done
    (( i == 2 && (i+=1) || (i+=2) ))
  done
  echo "${results[@]}"
}

factors "$@"

# vim:ts=2:sw=2:expandtab
