#!/usr/bin/env bash

digit () {
  # digit 1:<number> 2:<order> 3:<10> 4:<5> 5:<1>
  # The same rules apply to each decimal place. Extract that digit and
  # use the 10|5|1 numerals to print that digit.
  (( d = $1 / $2 % 10 ))

  #  9 = 10-1; 4 = 5-1
  if (( d == 9 )); then
    printf '%s%s' $5 $3
  elif (( d == 4 )); then
    printf '%s%s' $5 $4
  else
    if (( d >= 5 )); then
      printf '%s' $4
      (( d -= 5 ))
    fi
    for (( i = 0; i < d; i++ )); do
      printf '%s' $5
    done
  fi
}
roman () {
  (( $# == 1 )) || exit 1
  digit $1 1000 _ _ M
  digit $1 100 M D C
  digit $1 10 C L X
  digit $1 1 X V I
  printf '\n'
}

roman "$@"

# vim:ts=2:sw=2:expandtab
