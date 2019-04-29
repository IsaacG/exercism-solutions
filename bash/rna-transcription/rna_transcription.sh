#!/usr/bin/env bash

transcribe () {
  (( $# == 1 )) || exit 0
  [[ $1 ]] || exit 0
  [[ $1 = *[^GTAC]* ]] && { echo "Invalid nucleotide detected."; exit 1; }
  
  word=$1
  for pair in A:U T:A G:X C:G X:C; do
    find="${pair:0:1}"
    replace="${pair:2:1}"
    word=${word//$find/$replace}
  done

  echo "$word"
}

transcribe "$@"

# vim:ts=2:sw=2:expandtab
