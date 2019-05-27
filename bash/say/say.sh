#!/usr/bin/env bash

# There's little help getting around these three functions as they basically
# spell out 0-10 for 0-10, 10-19, 20-90.

say1 () { # 1's place, ie 0-9
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
  esac
}

say_teen () { # 10-19
  case "$1" in
    10) printf ten;;
    11) printf eleven;;
    12) printf twelve;;
    13) printf thirteen;;
    14) printf fourteen;;
    15) printf fifteen;;
    16) printf sixteen;;
    17) printf seventeen;;
    18) printf eighteen;;
    19) printf nineteen;;
  esac
}

say10 () { # 10's place, ie 0-99
  if (( $1 >= 0 && $1 < 10 )); then
    say1 "$1"
  else
    case "${1:0:1}" in
      1) say_teen "$1";;
      2) printf twenty;;
      3) printf thirty;;
      4) printf forty;;
      5) printf fifty;;
      6) printf sixty;;
      7) printf seventy;;
      8) printf eighty;;
      9) printf ninety;;
    esac
    if (( $1 > 20 && "${1:1:1}" )); then
      printf '-'
      say1 "${1:1:1}"
    fi
  fi
}

# =======================
# First implementation

say_hundred () { # 100's place, ie 0-999
  local a=$(( $1 / 100 )) b=$(( $1 % 100 ))
  if (( ! a )); then
    say10 "$b"
  else
    say10 "$a"
    printf ' hundred'
    (( b )) && printf ' ' && say10 "$b"
  fi
}

say_thousand () { # 1000's place, ie 0-999,999
  local a=$(( $1 / 1000 )) b=$(( $1 % 1000 ))
  if (( ! a )); then
    say_hundred "$b"
    return
  else
    say_hundred "$a"
    printf ' thousand'
    (( b )) && printf ' ' && say_hundred "$b"
  fi
}

say_million () {
  local a=$(( $1 / 1000000 )) b=$(( $1 % 1000000 ))
  if (( ! a )); then
    say_thousand "$b"
    return
  else
    say_thousand "$a"
    printf ' million'
    (( b )) && printf ' ' && say_thousand "$b"
  fi
}

say_billion () {
  local a=$(( $1 / 1000000000 )) b=$(( $1 % 1000000000 ))
  if (( ! a )); then
    say_million "$b"
    return
  else
    say_million "$a"
    printf ' billion'
    (( b )) && printf ' ' && say_million "$b"
  fi
}

# First implementation
# =======================
# Second implementation
# Note how the previous functions all do the same thing with minor variations.
# The only caveat is moving from `say_hundred` to `say10`.
# Helper function `say_up` moves us up from million to thousand to hundred to 10.

places=(100 1000 1000000 1000000000)
names=(hundred thousand million billion)

say_up () {
  (( $2 )) && say_place "$1" "$(( $2 - 1 ))" || say10 "$1"
}

# Say the billion/million/thousand/hundred places.
say_place () {
  local place="${places[$2]}" name="${names[$2]}"
  local a=$(( $1 / place )) b=$(( $1 % place ))
  (( a )) && printf '%s %s' "$( say_up "$a" "$2" )" "$name"
  (( a && b )) && printf ' '
  (( ! a || b )) && say_up "$b" "$2"
}

# Second implementation
# =======================


main () {
  (( $# == 1 )) || exit 1
  if (( $1 < 0 || $1 > 999999999999 )); then
    echo "input out of range"
    exit 1
  fi

  first=$( say_billion "$1" )
  second=$( say_place "$1" 3 )
  [[ $first = $second ]] || { echo "First and second do not match!!"; exit 1; }
  echo "$first"
}

main "$@"

# vim:ts=2:sw=2:expandtab
