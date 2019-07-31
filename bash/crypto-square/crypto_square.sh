#!/usr/bin/env bash

(( $# == 1 )) || exit 1

# Clean input: convert to lower and remove all non-alnum.
clean_input () {
  local input=$1
  input=${input,,}
  input=${input//[^[:alnum:]]/}
  echo "$input"
}

# Compute rows and columns.
get_size () {
  local -i r c
  for (( c = 1; c * c < $1; c++ )); do : ; done
  (( r = (c * (c - 1) >= $1) ? (c - 1) : c ))
  echo $r $c
}

# Convert the input to blocks of text.
chunks () {
  local s=$1 c=$2
  local i out
  for (( i = 0; i < "${#s}"; i++ )); do
    (( i && !(i % c) )) && out+=" "
    out+=${s:i:1}
  done
  echo "$out"
}

# Rotate the input chunks.
rotate () {
  local r=$1 c=$2
  shift; shift
  local s=( "$@" )

  local i j out
  for (( i = 0; i < c; i++ )); do
    for (( j = 0; j < r; j++ )); do
      chr=${s[j]:i:1}
      out+=${chr:- }
    done
    (( i + 1 < c )) && out+=" "
  done
  echo "$out"
}

main () {
  input=$(clean_input "$1")
  read r c <<< $(get_size "${#input}")
  s=( $( chunks "$input" $c ) )
  rotate $r $c "${s[@]}"
}


main "$1"

# vim:ts=2:sw=2:expandtab
