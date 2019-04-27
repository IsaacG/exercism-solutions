#!/usr/bin/env bash

boolRC () { (( $? == 0 )) && echo true || echo false; }

isogram () {
  (( $# == 1 )) || exit 1
  local -A found  # track discovered letters
  local -i i  # loop counter
  local word=${1,,}  # lowercased word
  for (( i = 0; i < ${#word}; i++ )); do
    chr="${word:$i:1}"
    # Ignore non-alpha
    [[ $chr = [[:alpha:]] ]] || continue
    # Check for is-set and set the first time, fail the second.
    [[ -v found[$chr] ]] && return 1 || found[$chr]=''
  done
}

isogram "$@"
boolRC

# vim:ts=2:sw=2:expandtab
