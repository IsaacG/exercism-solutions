#!/usr/bin/env bash

declare -a rails

# Zigzag up and down N rails, laying out text.
zigzag () {
  local n=$1 in=$2 d=1 r=0
  for (( i = 0; i < ${#in}; i++ )); do
    rails[$r]+=${in:i:1}
    (( r += d ))
    (( (r == 0) || (r == n - 1) )) && (( d *= -1 ))
  done
}

# Encode by zigzagging the text across rails and
# printing the rails.
encode () {
  zigzag "$@"
  printf '%s' "${rails[@]}"; printf \\n
}

decode () {
  local n=$1 in=$2 i rails out idx=0 l d offset
  # Zigzag the text to determine how many chars per rail.
  zigzag "$@"
  # Lay out input in blocks onto the rails,
  # using the previous data for lengths.
  for (( i = 0; i < "${#rails[@]}"; i++ )); do
    l=${#rails[i]}
    rails[i]="${in:idx:l}"
    (( idx += l ))
  done

  # Read the data off the rails in a zigzag order.
  idx=0 d=1 r=0
  for (( i = 0; i < ${#in}; i++ )); do
    # Top and bottom rail got one char per zigzag.
    # The rest got two chars.
    if (( (r == 0) || (r == n - 1) )); then
      offset=idx
    else
      (( offset = 2 * idx + ((d == 1) ? 0 : 1) ))
    fi
    out+="${rails[r]:offset:1}"
    # Move to the next rail. Update idx and direction.
    (( r += d ))
    (( (r == 0) || (r == n - 1) )) && (( d *= -1 ))
    (( r == 0 )) && (( idx++ ))
  done
  echo "$out"
}


main () {
  (( $# == 3 )) || { echo "Invalid usage"; exit 1; }
  (( $2 > 0 )) || { echo "Invalid rail count"; exit 1; }

  case "$1" in
    -e) encode "$2" "$3";;
    -d) decode "$2" "$3";;
    *) exit 1;;
  esac
}
main "$@"

# vim:ts=2:sw=2:expandtab
