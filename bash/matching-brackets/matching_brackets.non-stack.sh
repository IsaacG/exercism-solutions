#!/usr/bin/env bash

# My first solution before I read glennj's solution and realized
# that I ought to be using a stack.

declare -r brackets='[\[\](){}]'

boolRC () { (( $? == 0 )) && echo true || echo false; }
(( $# == 1 )) || exit 1

matching () {
  local start=0 input=$1 len=${#1} end

  # Trim anything prior to a bracket
  while [[ ${input:start:1} != $brackets ]] && (( start <= len )); do (( start++ )); done
  input=${input:start:len-start}

  # Empty == done and good
  [[ -z $input ]] && return

  # Split into the inner and rest:  "[$inner]$rest"
  end=$(get_len "$input") || return 1
  local inner=${input:1:end-1}
  local rest=${input:end+1:len-end}

  # echo "Inner: '$inner'" >&2
  # echo "Rest: '$rest'" >&2

  matching "$inner" || return 1
  matching "$rest" || return 1
}

get_len () {
  local input=$1
  local -i s=0 c=0 p=0 # square curl parenthesis. Could use a mapping from ]->[ )->( }->{ and a map of ([{
  local -i pos=0 len=${#input}

  while : ; do
    (( pos == len )) && return 1  # Got to the end without balancing open and closes
    case "${input:pos:1}" in
      \[ ) (( s++ ));;
      \] ) (( s-- ));;
      \{ ) (( c++ ));;
      \} ) (( c-- ));;
      \( ) (( p++ ));;
      \) ) (( p-- ));;
    esac
    (( s < 0 || c < 0 || p < 0 )) && return 1  # cannot have more close than open
    (( s || c || p )) || { echo $pos; return; } # close matches open; this span is an inner span
    (( pos++ ))
  done
}

matching "$1"
boolRC

# vim:ts=2:sw=2:expandtab
