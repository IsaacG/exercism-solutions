#!/usr/bin/env bash

# Read a string into the `list` variable.
toList () {
  l=$1
  l=${l#[}; l=${l%]}; l=${l//, / }
  read -a list <<< "$l"
}

# Check if listA == listB[offset:len(listA)]
matches () {
  local i len="${#listA[@]}" offset=$1
  (( len > ${#listB[@]} - offset )) && return 1
  for (( i = 0; i < len; i++ )); do
    [[ ${listA[i]} = ${listB[i + offset]} ]] || return 1
  done
  return 0
}

# Check if listA isSubset listB[i] for all i
isSubset () {
  (( ${#listB[@]} >= ${#listA[@]} )) || return 1
  for (( i = 0; i < ${#listB[@]} - ${#listA[@]} + 1; i++ )); do
    matches $i && return 0
  done
  return 1
}

main () {
  toList "$1"; a=( "${list[@]}" )
  toList "$2"; b=( "${list[@]}" )

  # Set listA and listB for other functions.
  listA=( "${a[@]}" ) listB=( "${b[@]}" )
  if isSubset; then
    if (( ${#listA[@]} == ${#listB[@]} )); then
      echo equal
    else
      echo sublist
    fi
  else
    # Swap listA and listB for supersets.
    listA=( "${b[@]}" ) listB=( "${a[@]}" )
    if isSubset; then
      echo superlist
    else
      echo unequal
    fi
  fi
}

main "$@"


# vim:ts=2:sw=2:expandtab
