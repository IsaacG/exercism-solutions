#!/usr/bin/env bash

sqSum () {
  local -i sum
  for (( i=1; i<= $1; i++ )); do sum+="$i"; done
  echo "$(( sum**2 ))"
}

sumSq () {
  local -i sum
  for (( i=1; i<= $1; i++ )); do (( sum += i**2 )); done
  echo "$sum"
}

sumDiff () {
  echo $(( $(sqSum "$1") - $(sumSq "$1") ))
}

main () {
  case "$1" in
    square_of_sum) echo $(sqSum "$2");;
    sum_of_squares) echo $(sumSq "$2");;
    difference) echo $(sumDiff "$2");;
    *) echo "Invalid operation: $1"; exit 1;;
  esac
}

(( $# == 2 )) || exit 1
main "$@"

# vim:ts=2:sw=2:expandtab
