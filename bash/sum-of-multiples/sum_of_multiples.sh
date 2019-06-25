#!/usr/bin/env bash

(( $# )) || exit 1

sum=0
limit=$1; shift

for (( i=1; i<limit; i++ )); do
  for f; do
    if (( f && i % f == 0 )); then
      (( sum += i ))
      break
    fi
  done
done

echo "$sum"

# vim:ts=2:sw=2:expandtab
