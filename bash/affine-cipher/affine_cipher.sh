#!/usr/bin/env bash

chr () {
  local val
  printf -v val %o "$(( $1 + 97 ))"; printf "\\$val"
}

ord() {
  local val
  LC_CTYPE=C printf -v val %d "'$1"
  printf '%d' $(( val - 97 ))
}

(( $# == 4 )) || exit 1

clean () {
  local val=$1
  val="${val,,}"
  val="${val// /}"
  val="${val//[^[:alnum:]]/}"
  printf '%s' "$val"
}


encode () {
  local -i a=$1 b=$2 i=0 x y
  local txt="$(clean "$3")" out=""

  # Cannot be divisible by 2 or 13
  if ! (( a % 2 && a % 13 )) ; then
    echo "a and m must be coprime."
    exit 1
  fi

  for ((i = 0; i < "${#txt}"; i++)); do
    x=$(ord "${txt:i:1}")
    if (( x >= 0 && x < 26 )); then
      (( y = (a * x + b) % 26 ))
      out+="$(chr "$y")"
    else
      out+="${txt:i:1}"
    fi
  done
  chunk "$out"
}

chunk () {
  local i txt=$1 out=""
  for ((i = 0; i < "${#txt}"; i++)); do
    (( i && i % 5 == 0 )) && out+=" "
    out+="${txt:i:1}"
  done
  printf '%s\n' "$out"
}

decode () {
  :
}

"$@"

# vim:ts=2:sw=2:expandtab
