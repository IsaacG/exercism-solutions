#!/usr/bin/env bash

(( $# == 1 )) || exit 1

say10 () {
  (( $1 >= 0 && $1 < 10 )) || exit 1
  case "$1" in
    0) printf zero;;
    1) printf one;;
    2) printf two;;
    3) printf three;;
    4) printf four;;
    5) printf five;;
    6) printf six;;
    7) printf seven;;
    8) printf eight;;
    9) printf nine;;
    *) exit 1;;
  esac
}

say_teen () {
  (( $1 >= 10 && $1 < 20 )) || exit 1
  case "$1" in
    10) printf tem;;
    11) printf eleven;;
    12) printf twelve;;
    13) printf thirteen;;
    14) printf fourteen;;
    15) printf fifteen;;
    16) printf sixteen;;
    17) printf seventeen;;
    18) printf eighteen;;
    19) printf nineteen;;
    *) exit 1;;
  esac
}

say100 () {
  (( $1 >= 0 && $1 < 100 )) || exit 1
  if (( $1 >= 0 && $1 < 10 )); then
    say10 "$1"
  else
    case "${1:0:1}" in
      1) say_teen "$1";;
      2) printf twenty;;
      3) printf thirty;;
      4) printf fourty;;
      5) printf fifty;;
      6) printf sixty;;
      7) printf seventy;;
      8) printf eighty;;
      9) printf ninety;;
      *) exit 1;;
    esac
    if (( $1 > 20 && "${1:1:1}" )); then
      printf '-'
      say10 "${1:1:1}"
    fi
  fi
}

say () {
  if (( $1 < 100 )); then
    say100 "$1"
  else
    say10 "${1:0:1}"
    printf ' hundred'
    (( "${1:1:2}" )) && printf ' ' && say100 "${1:1:2}"
  fi
}

say "$1"
true

# vim:ts=2:sw=2:expandtab
