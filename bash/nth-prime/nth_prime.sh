#!/usr/bin/env bash

(( $# == 1 )) || exit 1
(( $1 > 0 )) || { echo "invalid input"; exit 1; }

count=0
for ((i = 2; count < $1; i++)); do
  prime=1
  for (( j = 2; j * j <= i; j++ )); do
    (( i % j == 0 )) && { prime=0; break; }
  done
  (( prime && count++ ))
done

echo "$((i - 1))"

# vim:ts=2:sw=2:expandtab
