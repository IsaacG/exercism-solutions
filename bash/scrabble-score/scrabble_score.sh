#!/usr/bin/env bash

score () {
  (( $# == 1 )) || exit 1
  local word="${1^^}"
  local -i score=0

  for (( i = 0; i < "${#word}"; i++ )); do
    case "${word:i:1}" in
      [AEIOULNRST] ) score+=1 ;;
      [DG]         ) score+=2 ;;
      [BCMP]       ) score+=3 ;;
      [FHVWY]      ) score+=4 ;;
      [K]          ) score+=5 ;;
      [JX]         ) score+=8 ;;
      [QZ]         ) score+=10 ;;
    esac
  done
  echo "$score"
}

score "$@"

# vim:ts=2:sw=2:expandtab
