#!/usr/bin/env bash

(( $# == 0 || $# == 3 || $# == 4 )) || exit 1 

declare -A right left
declare -a compass=(north east south west north)

# Build right/left from a list instead of manually typing
# out both circles.
init () {
  for (( i = 0; i < ${#compass[@]} - 1; i++ )); do
    right[${compass[$i]}]=${compass[$i+1]}
    left[${compass[$i+1]}]=${compass[$i]}
  done
}

die () { echo "$1"; exit 1; }

main () {
  local x=${1:-0} y=${2:-0} d=${3:-north}
  [[ -v 'right[$d]' ]] || die "invalid direction"
  if (( $# == 4 )); then
    o=$4
    for (( i = 0; i < ${#o}; i++ )); do
      case ${o:i:1} in
        R) d=${right[$d]};;
        L) d=${left[$d]};;
        A)
          case $d in
            east)  ((x++));;
            west)  ((x--));;
            north) ((y++));;
            south) ((y--));;
          esac;;
        *) die "invalid instruction"
      esac
    done
  fi
  echo $x $y $d
}

init
main "$@"

# vim:ts=2:sw=2:expandtab
