#!/usr/bin/env bash

# Convert an int to a char. 0 == a
chr () {
  local val
  printf -v val %o "$(( $1 + 97 ))"; printf "\\$val"
}

# Convert a char to an int. 0 == a
ord() {
  local val
  LC_CTYPE=C printf -v val %d "'$1"
  printf '%d' $(( val - 97 ))
}

# Clean up input. Lowercase, alpha-only.
clean () {
  local val=$1
  val="${val,,}"
  val="${val//[^[:alnum:]]/}"
  printf '%s' "$val"
}

# Affine encoding.
# E(x) = (ax + b) mod m
# m == 26 (len {a..z})
# a, b = args
encode () {
  local -i a=$1 b=$2 i=0 x y
  local txt="$(clean "$3")" out=""
  assert_coprime "$a"

  for ((i = 0; i < "${#txt}"; i++)); do
    x=$(ord "${txt:i:1}")
    if (( x >= 0 && x < 26 )); then
      (( y = (a * x + b) % 26 ))
      out+="$(chr "$y")"
    else
      out+="${txt:i:1}"
    fi
  done
  chunk "$out"
}

# Print output in 5-char segments.
chunk () {
  local i txt=$1 out=""
  for ((i = 0; i < "${#txt}"; i++)); do
    (( i && i % 5 == 0 )) && out+=" "
    out+="${txt:i:1}"
  done
  printf '%s\n' "$out"
}

# Modular Multiplicative Inverse
mmi () {
  local -i n=1 a=$1
  until (( a * n % 26 == 1 )); do n+=1; done
  echo "$n"
}

# Must be coprime with m, ie divisible by 2 or 13
assert_coprime () {
  # a=$1 m=26
  if ! (( $1 % 2 && $1 % 13 )) ; then
    echo "a and m must be coprime."
    exit 1
  fi
}

# Affine decoding.
# D(y) = n * (y - b) mod m
# n=a^-1
# m == 26 (len {a..z})
# a, b = args
decode () {
  local -i a=$1 b=$2 i=0 x y
  local txt="$(clean "$3")" out=""
  assert_coprime "$a"
  local -i n=$(mmi $a)

  for ((i = 0; i < "${#txt}"; i++)); do
    y=$(ord "${txt:i:1}")
    if (( y >= 0 && y < 26 )); then
      (( x = (n * (y - b)) % 26 ))
      (( x<0 && (x+=26) ))
      out+="$(chr "$x")"
    else
      out+="${txt:i:1}"
    fi
  done
  echo "$out"
}

(( $# == 4 )) || exit 1

"$@"

# vim:ts=2:sw=2:expandtab
