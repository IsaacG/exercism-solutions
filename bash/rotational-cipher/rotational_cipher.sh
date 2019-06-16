#!/usr/bin/env bash

chr () {
  local val
  printf -v val %o "$1"; printf "\\$val"
}

ord () {
  LC_CTYPE=C printf %d "'$1"
}


declare -i A=$(ord A) Z=$(ord Z) a=$(ord a) z=$(ord z) 
add () {
  [[ $1 = [^a-zA-Z] ]] && { printf '%s' "$1"; return; }
  local v=$(ord $1)
  local w=$(( v + $2 ))
  (( v >= A && v <= Z && w > Z )) && (( w-=26 ))
  (( v >= a && v <= z && w > z )) && (( w-=26 ))
  printf '%s' "$( chr "$w" )"
}

(( $# == 2 )) || exit 1

out=
rot=$(( $2 % 26 ))
for ((i=0; i < ${#1}; i++)); do
  out+=$(add "${1:i:1}" "$rot")
done
printf '%s' "$out"

# vim:ts=2:sw=2:expandtab
