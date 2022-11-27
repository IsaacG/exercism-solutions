#!/usr/bin/env bash

color () {
  case "${1,}" in
    black) echo 0;;
    brown) echo 1;;
    red) echo 2;;
    orange) echo 3;;
    yellow) echo 4;;
    green) echo 5;;
    blue) echo 6;;
    violet) echo 7;;
    grey) echo 8;;
    white) echo 9;;
    *) return 1;;
  esac
}

die () { echo "$1"; exit 1; } >&2

resist () {
  units=(ohms kiloohms megaohms gigaohms)
  a=$(color "$1") || die "invalid color"
  b=$(color "$2") || die "invalid color"
  c=$(color "$3") || die "invalid color"
  total="$(( (10 * a + b) * 10 ** c ))"

  scale=0
  while (( total && total % 1000 == 0 )); do (( total /= 1000, scale++ )); done
  echo "${total} ${units[scale]}"
}

resist "$@"
# vim:ts=2:sw=2:expandtab
