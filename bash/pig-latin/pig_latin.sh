#!/usr/bin/env bash

rule1='^(xr|yt|[aeiou])'
rule2='^([^aeiou][^aeiouy]*)(.*)'
rule3='^([^aeiou]*)(qu)(.*)'

igpay_aysay () {
  if [[ $1 =~ $rule1 ]]; then
    printf '%say' "$1"
  elif [[ $1 =~ $rule3 ]]; then
    m=( "${BASH_REMATCH[@]}" )
    printf '%s%s%say' "${m[3]}" "${m[1]}" "${m[2]}"
  elif [[ $1 =~ $rule2 ]]; then
    printf '%s%say' "${BASH_REMATCH[2]}" "${BASH_REMATCH[1]}"
  fi
}

words=()
while (( $# )); do
  words+=( $(igpay_aysay "$1" ) )
  shift
done
echo "${words[@]}"

# vim:ts=2:sw=2:expandtab
