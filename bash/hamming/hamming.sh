#!/usr/bin/env bash

error () {
  printf '%s\n' "$*"
  exit 1
}

main () {
  (( $# == 2 )) || error 'Usage: hamming.sh <string1> <string2>'
  
  # Regular vars are easier to read when doing fancy parameter expansion.
  a=$1 b=$2 
  # Using the a==b||... pattern everywhere in this function. I like consistency.
  (( ${#a} == ${#b} )) || error 'left and right strands must be of equal length'

  declare -i count
  for (( i = 0; i < ${#a}; i++ )); do
    [[ ${a:i:1} == "${b:i:1}" ]] || count+=1
  done

  printf '%d\n' "$count"
}

main "$@"
