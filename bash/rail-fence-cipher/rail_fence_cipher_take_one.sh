#!/usr/bin/env bash

chunk () {
  local len=$1 in=$2 i out
  for (( i = 0; i < ${#in}; i += len )); do
    out+=( "${in:i:len}" )
  done
  echo "${out[*]}"
}

get_one () {
  local offset=$1 i out
  shift; local -a chunks=( "$@" )

  for ((i = 0; i < ${#chunks[@]}; i++)); do
    out+=${chunks[i]:offset:1}
  done
  echo "$out"
}

get_two () {
  local a=$1 b=$2 i out
  shift; shift; local -a chunks=( "$@" )

  for ((i = 0; i < ${#chunks[@]}; i++)); do
    out+=${chunks[i]:a:1}
    out+=${chunks[i]:b:1}
  done
  echo "$out"
}

encode () {
  local rails=$1 in=$2 len i r out chunks
  local -a chunks
  (( len = rails * 2 - 2 ))
  chunks=( $(chunk $len "$in") )

  out+=$( get_one 0 "${chunks[@]}" )
  for ((r = 1; r < rails - 1; r++)); do
    out+=$( get_two $r $(( 1 + rails - r )) "${chunks[@]}" )
  done
  out+=$( get_one $(( r = rails - 1 )) "${chunks[@]}" )
  echo "$out"
}

