#!/usr/bin/env bash

bottles () {
  (( $1 > 1 )) && printf '%d bottles' "$1"
  (( $1 == 1 )) && printf '1 bottle'
  (( $1 == 0 )) && printf 'no more bottles'
}

print_verse () {
  if (( $1 > 0 )); then
    printf '%s of beer on the wall, %s of beer.\n' "$(bottles $1)" "$(bottles $1)"
    (( $1 == 1 )) && s=it || s=one
    printf 'Take %s down and pass it around, %s of beer on the wall.\n' "$s" "$(bottles $(($1-1)) )"
  else
    printf 'No more bottles of beer on the wall, no more bottles of beer.\n'
    printf 'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
  fi
}

beer () {
  if ! (( $# == 1 || $# == 2 )); then
    echo '1 or 2 arguments expected'
    exit 1
  fi

  start=$1
  end=${2:-$start}

  if (( start < end )); then
    echo 'Start must be greater than End'
    exit 1
  fi

  for (( i = start; i > end; i-- )); do
    print_verse "$i"
    printf '\n'
  done
  print_verse "$end"
}

beer "$@"

# vim:ts=2:sw=2:expandtab
