#!/usr/bin/env bash

(( $# == 6 )) || exit 1

declare -a count inv_count
declare -i sum

setup () {
  for arg; do (( count[arg]++ )); (( sum += arg )); done
  for c in "${!count[@]}"; do (( inv_count[count[c]]=c )); done
}

type=$1; shift
setup "$@"
score=0
case "$type" in
  'ones') for arg; do (( arg == 1 && (score += arg) )); done;;
  'twos') for arg; do (( arg == 2 && (score += arg) )); done;;
  'threes') for arg; do (( arg == 3 && (score += arg) )); done;;
  'fours') for arg; do (( arg == 4 && (score += arg) )); done;;
  'fives') for arg; do (( arg == 5 && (score += arg) )); done;;
  'sixes') for arg; do (( arg == 6 && (score += arg) )); done;;
  'full house')
    [[ "${!inv_count[@]}" = "2 3" ]] && ((score=sum));;
  'four of a kind')
    [[ "${!inv_count[@]}" = "1 4" ]] && ((
      score = 4 * ${inv_count[4]} ))
    [[ "${!inv_count[@]}" = "5" ]] && ((
      score = 4 * ${inv_count[5]} ));;
  'little straight')
    [[ "${!count[@]}" = "1 2 3 4 5" ]] && ((score=30));;
  'big straight')
    [[ "${!count[@]}" = "2 3 4 5 6" ]] && ((score=30));;
  'choice') ((score=sum));;
  'yacht')
    (( $1 == $2 && $1 == $3 && $1 == $4 && $1 == $5 )) && ((
      score=50));;
esac

echo $score


# vim:ts=2:sw=2:expandtab
