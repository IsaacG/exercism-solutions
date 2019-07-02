#!/usr/bin/env bash

(( $# == 1 )) || exit 1

syntax_err () {
  echo "syntax error"
  exit 1
}
unknown () {
  echo "unknown operation"
  exit 1
}

declare -r operations='(plus)|(minus)|(multiplied by)|(divided by)'
declare -r op_re='^(.*[-[:digit:]]+) ([ [:lower:]]+) ([-[:digit:]]+)$'
declare -r format="^What is ?(.*)\?$"

evaluate () {
  [[ $1 ]] || syntax_err
  [[ $1 = *[^-[:digit:]]* ]] || { echo "$1"; return; }
  [[ $1 =~ $operations ]] || unknown

  [[ $1 =~ $op_re ]] || syntax_err
  local a="${BASH_REMATCH[1]}"
  local op="${BASH_REMATCH[2]}"
  local b="${BASH_REMATCH[3]}"
  a=$(evaluate "$a") || return
  case "$op" in
    plus           ) echo $((a + b));;
    minus          ) echo $((a - b));;
    'multiplied by') echo $((a * b));;
    'divided by'   ) echo $((a / b));;
    *              ) syntax_err;;
  esac
}

main () {
  [[ $1 =~ $format ]] || unknown
  evaluate "${BASH_REMATCH[1]}"
}

main "$1"

# vim:ts=2:sw=2:expandtab
