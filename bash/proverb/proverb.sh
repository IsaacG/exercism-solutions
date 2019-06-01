#!/usr/bin/env bash

proverb () {
  words=( "$@" )
  for (( i = 0; i + 1 < $#; i++ )); do
    printf 'For want of a %s the %s was lost.\n' "${words[i]}" "${words[i+1]}"
  done
  (( $# )) && printf 'And all for the want of a %s.\n' "$1" || :
}

proverb "$@"

# vim:ts=2:sw=2:expandtab
