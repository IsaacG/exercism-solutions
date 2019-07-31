#!/usr/bin/env bash

decode () {
  out=()
  sum=0
  while (( $# )); do
    # Shift over the accumulated sum to make space for more.
    (( sum <<= 7 ))
    (( in = 16#$1 ))
    # Add in the next 7 bits of the input, ignoring the top bit.
    (( sum += (in & (1<<7) - 1) ))
    # Check the continue bit. If unset, add to the output.
    if ! (( in & ( 1 << 7 ) )); then
      out+=( $(printf %02X $sum) )
      sum=0
    elif (( $# == 1 )); then
      # Continue set and we're on the last input value?
      echo incomplete byte sequence
      exit 1
    fi
    shift
  done
  echo "${out[*]}"
}

# Encode each input value.
encode () {
  local out=()
  for arg; do
    out+=( $(encode_one $arg) )
  done
  echo "${out[*]}"
}

encode_one () {
  local in=$(( 16#$1 ))
  local out=()
  # Accumulate the last 7 bits of the input until we run out...
  # or if there is no output, ie 00=>00
  while (( $in )) || ! (( ${#out[@]} )); do
    # extract the last 7 bits
    byt=$(( in & ( 1 << 7 ) - 1 ))
    (( in >>= 7 ))
    # Set the 7th continue bit for all-but-the-last byte.
    (( ${#out[@]} )) && (( byt |= 1 << 7 ))
    out=( $(printf %02X $byt) "${out[@]}" )
  done
  echo "${out[*]}"
}

(( $# >= 2 )) || exit 1

case "$1" in
  encode) "$@";;
  decode) "$@";;
  *) echo unknown subcommand; exit 1;;
esac

# vim:ts=2:sw=2:expandtab
