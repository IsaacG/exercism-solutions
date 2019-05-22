#!/usr/bin/env bash

alpha=$(printf '%s' {a..z})
alrev=$(printf '%s' {z..a})

transpose () {
  (( RANDOM % 2 )) && tr_transpose "$1" || bash_transpose "$1"
}

tr_transpose () {
  input=${1,,}
  input=${input// /}
  input=${input//[[:punct:]]/}
  tr "$alpha" "$alrev" <<< "${input}"
}

bash_transpose () {
  local -A map
  local -a alpha=( {a..z} )
  local -i i
  for (( i = 0; i < 26; i++ )); do
    map[${alpha[$i]}]=${alpha[25 - i]}
  done

  local input out ch
  input=${1,,}
  input=${input// /}
  input=${input//[[:punct:]]/}

  for (( i = 0; i < ${#input}; i++ )); do
    ch=${input:i:1}
    [[ ${map[$ch]} ]] && out+=${map[$ch]} || out+=$ch
  done
  echo "$out"
}

encode () {
  local i out=$(transpose "$1") res=''
  for (( i = 0; i < "${#out}"; i++ )); do
    res+="${out:i:1}"
    # Add spaces after every 5th char
    (( (i + 1) % 5 == 0 && (i + 1) < ${#out} )) && res+=' '
  done
  echo "$res"
}

decode () {
  transpose "$1"
}

"$@"

# vim:ts=2:sw=2:expandtab
