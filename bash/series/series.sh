#!/usr/bin/env bash

err () {
  echo "$1"
  exit 1
}

series () {
  (( $# == 2 )) || exit 1
  local str=$1 len=$2
  local -a out

  (( ${#str} == 0 )) && err "series cannot be empty"
  (( len == 0 )) && err "slice length cannot be zero"
  (( len < 0 )) && err "slice length cannot be negative"
  (( len > ${#str} )) && err "slice length cannot be greater than series length"

  for ((i=0; i+len <= ${#str}; i++)); do
    out+=( "${str:i:len}" )
  done
  IFS=' '; echo "${out[*]}"
}

series "$@"

# vim:ts=2:sw=2:expandtab
