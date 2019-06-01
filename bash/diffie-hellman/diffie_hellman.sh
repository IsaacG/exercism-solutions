#!/usr/bin/env bash

privateKey () {
  (( $# == 1 )) || exit 1
  echo $(( $RANDOM % ($1 - 2) + 2 ))
}

publicKey () {
  (( $# == 3 )) || exit 1
  local -i p=$1 g=$2 private=$3
  echo $(( g ** private % p ))
}

secret () {
  (( $# == 3 )) || exit 1
  local -i p=$1 public=$2 private=$3
  # overflow issues here
  # echo $(( public ** private % p ))
  bc <<< "$public ^ $private % $p"
}

"$@"

# vim:ts=2:sw=2:expandtab
