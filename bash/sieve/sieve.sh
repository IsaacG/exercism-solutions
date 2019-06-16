#!/usr/bin/env bash

(( $# == 1 )) || exit 1

declare -a primes out

# Initialize to all-primes
for ((i=2; i<=$1; i++)); do primes[i]=1; done

for ((i=2; i<=$1; i++)); do
  (( primes[i] )) || continue
  out+=( $i )
  for ((j=2*i; j<=$1; j+=i)); do primes[j]=0; done
done

echo "${out[@]}"

# vim:ts=2:sw=2:expandtab
