#!/usr/bin/env bash

boolRC () { (( $? == 0 )) && echo true || echo false; }

luhn () {
  (( $# == 1 )) || return 1  # arg count
  input="${1// /}"
  (( ${#input} > 1 )) || return 1  # input length
  [[ $input = *[^0-9]* ]] && return 1  # non-digit

  # zero pad as needed so the even digits are the "every other starting from the right"
  (( ${#input} % 2 )) && input="0${input}"

  local -i sum=0 i v
  for ((i=0; i < ${#input}; i++)); do
    v="${input:i:1}"
    if (( i % 2 == 0 )); then
      (( v *= 2 ))
      (( v > 9 && (v -= 9) ))
    fi
    sum+="$v"
  done
  (( sum % 10 == 0 ))
}

luhn "$@"
boolRC

# vim:ts=2:sw=2:expandtab
