#!/usr/bin/env bash

(( $# == 1 )) || exit 1
row=()

for ((i = 0; i < $1; i++)); do
  next=(1)
  for ((j = 1; j < i; j++)); do
    next+=( $(( ${row[j-1]} + ${row[j]} )) )
  done
  (( i )) && next+=(1)
  row=( "${next[@]}" )

  for ((j = i + 1; j < $1; j++)); do printf ' '; done
  echo "${row[@]}"
done

# vim:ts=2:sw=2:expandtab
