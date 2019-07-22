#!/usr/bin/env bash

die () { echo "$1"; exit 1; }
assert_num () { [[ $1 = *[^-[:digit:]]* ]] && die "invalid arguments"; }

(( $# == 2 || $# == 4 )) || die "invalid arguments"
assert_num "$1"
assert_num "$2"

day=$(( 24 * 60 ))

mod () {
  a=$1 b=$2
  echo $(( ( (a % b) + b) % b ))
}

hr=$( mod $1 24 )
min=$(( hr * 60 + $2 ))

shift; shift
if (( $# )); then
  assert_num "$2"
  case $1 in
  +) (( min += $2 )) ;;
  -) (( min -= $2 )) ;;
  *) die "invalid arguments"
  esac
fi

min=$( mod $min $day )
printf '%02d:%02d\n' $((min/60)) $((min%60))

# vim:ts=2:sw=2:expandtab
