#!/usr/bin/env bash

score=0
rolls=( "$@" )
frame_score=0
frame_roll=0
bonus=0

for (( i = 0; i < ${#rolls[@]}; i++ )); do
  (( frame_score += ${rolls[i]} ))
  (( frame_roll++ ))
  if (( frame_roll == 2 || frame_score == 10 )); then
    (( score += frame_score, last_frame = frame_score ))
    (( bonus )) && (( score += frame_score , bonus-- ))  # Double
    (( frame_score == 10 )) && (( bonus = 1 ))   # Spare
    (( ${rolls[i]} == 10 )) && (( bonus = 2 ))   # Strike
    (( frame_roll = 0, frame_score = 0 ))
  fi
done
(( score += frame_score ))

echo $score

# vim:ts=2:sw=2:expandtab
