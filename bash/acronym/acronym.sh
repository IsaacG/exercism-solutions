#!/usr/bin/env bash

main () {
  # Change whitespace to newline
  # Take the first char on each line
  # Drop newlines and uppercase
  <<< "$1" tr '[:space:]-' '\n' \
  | sed 's/^\(.\).*/\1/' \
  | tr -d '\n' \
  | tr '[:lower:]' '[:upper:]'
}

main "$@"

# vim:ts=2:sw=2:expandtab
