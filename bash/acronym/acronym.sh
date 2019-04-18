#!/usr/bin/env bash

withCoreTools () {
  # Change whitespace to newline
  # Take the first char on each line
  # Drop newlines and uppercase
  <<< "$1" tr '[:space:]-' '\n' \
  | sed 's/^\(.\).*/\1/' \
  | tr -d '\n' \
  | tr '[:lower:]' '[:upper:]'
}

main () {
  local acr

  # Split into word/array, translating - to ' '
  read -a words <<< "${1//-/ }"
  # Accumulate the first char of each word
  for i in "${words[@]}"; do acr+="${i:0:1}"; done
  # Print out the uppercased result
  printf '%s\n' "${acr^^}"
}

main "$@"

# vim:ts=2:sw=2:expandtab
