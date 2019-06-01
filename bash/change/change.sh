#!/usr/bin/env bash

declare -a count=(0) using=(0)
# globals for convenience
target=$1; shift; coins=( $@ )

die () { echo "$@"; exit 1; }

# Compute the optimal coins/count for each value up until target.
# Apply dynamic programming. Try using each coin N and see if count(target-N)+1 is the min count.
# count(target) = min( count(target-N)+1 for N in coins )
# using(target) stores the coin N for which we got to the min.
compute () {
  for (( i = 1; i <= target; i++ )); do
    min=0  # not yet found
    count[i]= using[i]=  # add an empty element.
    for n in "${coins[@]}"; do
      (( n > i )) && continue # ignore coins larger than target
      [[ ${count[i-n]} ]] || continue  # no solution for i-n; ignore
      maybe=$(( ${count[i-n]} + 1 ))
      if (( ! min )) || (( maybe < min )); then
        min=$maybe
        count[i]=$maybe
        using[i]=$n
      fi
    done
  done
}

show () {
  # Check if we were able to solve it.
  [[ -z ${count[target]} ]] && die "can't make target with given coins"

  # Walk back using the used[target] list, accumulating the coins we used.
  used=()
  while (( target > 0 )); do
     used+=("${using[target]}")
     (( target -= "${using[target]}" ))
  done

  # Sort the used list.
  sorted=()
  for n in "${coins[@]}"; do
    for u in "${used[@]}"; do
      (( n == u )) && sorted+=( $n )
    done
  done
  echo "${sorted[@]}"
}

main () {
  # Catch a negative value.
  (( target < 0 )) && die "target can't be negative"

  compute

  show
}

main "$@"
# vim:ts=2:sw=2:expandtab
