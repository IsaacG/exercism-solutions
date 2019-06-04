#!/usr/bin/env bash

num_print () {
  [[ $last ]] || return
  (( count == 1 )) && printf '%s' "$last" || printf '%d%s' "$count" "$last"
}

encode () {
  declare input=$1 last=''
  declare -i count=0

  for (( i = 0; i < ${#input}; i++ )); do
    chr="${input:i:1}"
    if [[ $chr = $last ]]; then
      count+=1
    else
      num_print "$last" "$count"
      last=$chr
      count=1
    fi
  done
  num_print "$last" "$count"
}

decode () {
  local input=$1
  while [[ $input ]]; do
    num_re='^([[:digit:]]+)([[:alpha:][:space:]])'
    if [[ $input =~ $num_re ]]; then
      for (( i=0; i < ${BASH_REMATCH[1]}; i++ )); do
        printf '%s' "${BASH_REMATCH[2]}"
      done
      input="${input:${#BASH_REMATCH[0]}}"
    else
      printf '%s' "${input:0:1}"
      input="${input:1}"
    fi
  done
}

(( $# == 2 )) && "$@"
printf '\n'

# vim:ts=2:sw=2:expandtab
