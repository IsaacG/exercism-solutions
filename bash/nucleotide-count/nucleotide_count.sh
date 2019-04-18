#!/usr/bin/env bash

main () {
  if [[ $1 = *[^ACGT]* ]]; then
    printf 'Invalid nucleotide in strand\n'
    return 1
  fi

  for n in A C G T; do
    ns=$(tr -cd $n <<< "$1")
    printf '%s: %d\n' "$n" "${#ns}"
  done
}

main "$@"

# vim:ts=2:sw=2:expandtab
