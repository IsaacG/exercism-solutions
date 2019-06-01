#!/usr/bin/env bash

# Solution pretty much stolen from glennj.
# My first take did not use a stack, though it ought to have.
# See matching_brackets.non-stack.sh

# Track what brackets we are in using a stack. With each open, add that open
# to the stack. On close, assert it matches the top of the stack and pop.

declare -A pair=( [']']='[' [')']='(' ['}']='{' )

boolRC () { (( $? == 0 )) && echo true || echo false; }
(( $# == 1 )) || exit 1

matching () {
  input=$1 stack=""
  for (( i = 0; i < ${#input}; i++ )); do
    chr="${input:i:1}"
    case "$chr" in
      [\[\({] ) stack+=$chr;;
      [\]\)}] )
        p=${pair[$chr]}
        [[ $stack = *"$p" ]] || return 1
        stack=${stack%$p}
        ;;
    esac
  done
  # At the end, the stack must be empty.
  [[ $stack = '' ]]
}

matching "$1"
boolRC

# vim:ts=2:sw=2:expandtab
