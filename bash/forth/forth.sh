#!/usr/bin/env bash

shopt -s extglob
declare -A macro
declare -a stack

# Print an error message and fail-exit
die () { echo "$1"; exit 1; }

# Word is a number.
is_num () { [[ $1 = +([[:digit:]]) ]]; }

# Line is a macro definition (starts with ": ")
is_macro () { [[ $1 = ": "* ]]; }

# Push one item onto the stack.
push () { stack+=( "$@" ); }

# Pop one item from the stack into regA.
pop () {
  (( "${#stack[@]}" )) || die "empty stack"
  regA="${stack[-1]}"
  stack=( "${stack[@]::${#stack[@]}-1}" )
}

# Pop two items from the stack into regA, regB.
pop2 () {
  (( "${#stack[@]}" == 1 )) && die "only one value on the stack"
  pop
  regB=$regA
  pop
}

# Expand macros on a given input line.
# Does not expand macros when part of a macro definition, though. ie:
# : foo 5 ;
# : foo foo foo ;   ==expand==> : foo 5 5 ;
macro_exp () {
  local -a out in
  local t
  read -r -a in <<< "$1"
  if is_macro "$1"; then
    # Copy the first two words without modification.
    out=( "${in[@]:0:2}" )
    in=( "${in[@]:2: ${#in[@]} - 2}" )
  fi
  for t in "${in[@]}"; do
    # Copy over words, expanding macros as we go.
    [[ ${macro[$t]} ]] && out+=( "${macro[$t]}" ) || out+=( "$t" )
  done
  echo "${out[@]}"
}

# Add a macro definition.
add_macro () {
  local line=$1 name
  [[ $line = *" ;" ]] || die "macro not terminated with semicolon"
  # Remove the leading : and trailing ;
  line="${line% ;}"; line="${line#: }"
  # Split into name and definition
  read -r name line <<< "$line"
  [[ $line ]] || die "empty macro definition"
  is_num "$name" && die "illegal operation"  # Cannot redefine a number.
  macro[$name]="$line"
}

# Process a full line of text.
process_line () {
  local name line arg args
  line=$( macro_exp "$1" )
  if is_macro "$line"; then
    add_macro "$line"
  else
    read -r -a args <<< "$line"
    for arg in "${args[@]}"; do operate "$arg"; done
  fi
}

# Operate on a single word.
operate () {
  case "$1" in
    +([[:digit:]]) ) push "$1";;
    '+') pop2; push $(( regA + regB ));;
    '-') pop2; push $(( regA - regB ));;
    '*') pop2; push $(( regA * regB ));;
    '/')
      pop2
      (( regB )) || die "divide by zero"
      push $(( regA / regB ));;
    dup) pop; push "$regA" "$regA";;
    drop) pop;;
    swap) pop2; push "$regB" "$regA";;
    over) pop2; push "$regA" "$regB" "$regA";;
    *) die "undefined operation"
  esac
}

main () {
  while read -r line; do
    process_line "${line,,}"
  done
  echo "${stack[@]}"
}

main

# vim:ts=2:sw=2:expandtab
