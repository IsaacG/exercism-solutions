#!/usr/bin/env bash

declare -A position

die () { echo "$*"; exit 1; }
boolRC () { (( $? == 0 )) && echo true || echo false; }

validate () {
  IFS=, read r c <<< "$1"
  (( r >= 0 )) || die 'row not positive'
  (( r < 8 )) || die 'row not on board'
  (( c >= 0 )) || die 'column not positive'
  (( c < 8 )) || die 'column not on board'
}

check () {
  [[ $1 == $2 ]] && die 'same position'
  IFS=, read rA cA <<< "$1"
  IFS=, read rB cB <<< "$2"
  ((
    rA == rB || cA == cB
    || (rB - rA) == (cB - cA) 
    || (rB - rA) == -(cB - cA)
  ))
}

main () {
  while (( $# )); do
    case "$1" in
      -[wb])
        validate "$2"
        position[${1#-}]=$2
        shift; shift;;
      *) echo Error; exit 1;;
    esac
  done
  [[ -v 'position[w]' && -v 'position[b]' ]] || die error
  check "${position[w]}" "${position[b]}"
}

main "$@"
boolRC

# vim:ts=2:sw=2:expandtab
