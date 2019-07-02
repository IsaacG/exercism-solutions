#!/usr/bin/env bash

a=97

chr () {
  local val
  printf -v val %o "$(( $1 + a))"; printf "\\$val"
}

ord () {
  local val
  LC_CTYPE=C printf -v val %d "'$1"; printf '%d' "$((val - a))"
}

rot_chr () {
  local key=$1 direction=$2 input=$3
  local dist=$(ord "$key") orig=$(ord "$input")

  if [[ $direction = encode ]]; then
    echo "$( chr $(( (orig + dist) % 26 )) )"
  elif [[ $direction = decode ]]; then
    echo "$( chr $(( (orig + 26 - dist) % 26 )) )"
  fi
}

rotate () {
  local key=$1 direction=$2 input=${3,,}
  [[ $key = *[^[:lower:]]* ]] && { echo invalid key; exit 1; }
  for (( i = 0; i < "${#input}"; i++ )); do
    k="${key:i % ${#key}:1}"
    out+=$(rot_chr "$k" "$direction" "${input:i:1}")
  done
  echo "$out"
}

main () {
  if [[ $1 = key ]] && (( $# == 1 )); then
    for (( i = 0; i < 100; i++ )); do
      key+=$( chr $((RANDOM % 26)) )
    done
    echo "$key"
  elif [[ $1 = -k ]] && (( $# == 4 )); then
    shift
    rotate "$@"
  else
    echo "invalid usage"; exit 1
  fi
}

main "$@"

# vim:ts=2:sw=2:expandtab
