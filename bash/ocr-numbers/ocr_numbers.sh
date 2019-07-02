#!/usr/bin/env bash

die () { echo "$1" >&2; exit 1; }

init_string='\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
                              '
# Read 10 chars and store them for comparison.
init () {
  _c=0
  for i in {0..9}; do
    getChar
    chars+=("$char")
  done <<< "$init_string"
}

# Read a "row" of text, ie 4 lines.
# Die if we don't read a 4x(3n).
readRow () {
  lines=()
  for i in {1..4}; do
    read -t.1 || break
    (( "${#REPLY}" % 3 )) && die "Number of input columns is not a multiple of three"
    lines+=( "$REPLY" )
  done
  case "${#lines[@]}" in
    0) return 1;;  # Out of input
    4) return 0;;  # Success
    *) die "Number of input lines is not a multiple of four";;  # Error
  esac
}

# Read the n'th char from the "row" of text.
readChar () {
  char=''
  for i in {0..3}; do
    char+="${lines[i]:3*$1:3}"$'\n'
  done
}

# Get the next character, reading more rows if needed.
getChar () {
  if (( _c * 3 + 3 > ${#lines[0]} )); then
    readRow || return
    _c=0
  fi
  readChar "$_c"
  ((_c++))
  return 0
}

main () {
  init
  out=''
  while getChar; do
    c=
    # Match the input to the known chars.
    for i in {0..9}; do
      if [[ $char = ${chars[i]} ]]; then
        c=$i
        break
      fi
    done
    # Add a comma if we read a new line.
    [[ -n "$out" ]] && (( _c == 1 )) && out+=,
    out+="${c:-?}"
  done
  echo "$out"
}

(( $# == 0 )) || exit 1
main

# vim:ts=2:sw=2:expandtab
