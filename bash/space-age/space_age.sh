#!/usr/bin/env bash

(( $# == 2 )) || exit 1

declare -ri earth_year=31557600 # seconds
declare -rA mapping=(
  [Earth]=1
  [Mercury]=0.2408467
  [Venus]=0.61519726
  [Mars]=1.8808158
  [Jupiter]=11.862615
  [Saturn]=29.447498
  [Uranus]=84.016846
  [Neptune]=164.79132
)
declare -r planet=$1 seconds=$2

if [[ -n ${mapping[$planet]} ]]; then
  expr="$seconds / ($earth_year * ${mapping[$planet]})"
  printf '%.2f\n' $(bc <<< "scale=3; $expr")
else
  printf 'not a planet\n'
  exit 1
fi


# vim:ts=2:sw=2:expandtab
