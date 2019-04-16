#!/usr/bin/env bash

is_leap () {
  year="$1"
  (( year % 4 != 0 )) && return 1
  (( year % 400 == 0 )) && return 0
  (( year % 100 == 0 )) && return 1
  return 0  # Divisible by 4
}

main () {
  re='[^0-9]'
  if (( $# != 1 )) || [[ $1 =~ $re ]]; then
    printf 'Usage: leap.sh <year>\n'
    return 1
  fi
  is_leap "$1" && printf 'true\n' || printf 'false\n'
  :
}

main "$@"
