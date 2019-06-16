#!/usr/bin/env bash

translate () {
  (( $# == 1 )) || exit 1
  out=()
  for ((i=0; i+2 < ${#1}; i+=3)); do
    case "${1:i:3}" in
      AUG) out+=(Methionine);;
      UUU|UUC) out+=(Phenylalanine);;
      UUA|UUG) out+=(Leucine);;
      UCU|UCC|UCA|UCG) out+=(Serine);;
      UAU|UAC) out+=(Tyrosine);;
      UGU|UGC) out+=(Cysteine);;
      UGG) out+=(Tryptophan);;
      UAA|UAG|UGA) break;; # STOP
      *) echo "Invalid codon"; return 1;;
    esac
  done
  echo "${out[*]}"
}

translate "$@"

# vim:ts=2:sw=2:expandtab
