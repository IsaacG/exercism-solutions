#!/usr/bin/env bash

# Maps A=>0 B=>1 C=>2
ord() { local val; LC_CTYPE=C printf -v val %d "'$1"; echo $(( val - 65 )); }
# Reverses ord
chr () { local val; printf -v val %o "$(( $1 + 65 ))"; printf "\\$val"; }

# Print one line of the diamond based on the row number and diamond size.
printLine () {
  local -i l=$1 size=$2 i pad inner
  local line=''

  # Outer space-padding
  (( pad = size - l ))
  # Inner space-padding
  (( inner = l * 2 - 1 ))

  # Outer padding
  for (( i = 0; i < pad; i++ )); do line+=' '; done
  # The left letter
  line+=$(chr $l)
  # Inner padding
  for (( i = 0; i < inner; i++ )); do line+=' '; done
  # The right letter
  (( l != 0 )) && line+=$(chr $l)
  # Outer padding
  for (( i = 0; i < pad; i++ )); do line+=' '; done
  echo "$line"
}

diamond () {
  local -i i size
  (( $# == 1 )) || exit 1
  # "Size" of the diamond for below
  size=$(ord $1)
  # Top half of the diamond
  for (( i = 0; i < size; i++ )); do printLine $i $size; done
  # Bottom half of the diamond
  for (( i = size; i >= 0; i-- )); do printLine $i $size; done


}

diamond "$@"

# vim:ts=2:sw=2:expandtab
