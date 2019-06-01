#!/usr/bin/env bash

# Fun fact:
# (( foo )) && (( a=1, b=0 )) || (( a=2, b=0 )); echo $a
# will *always* *always* print 2. This is one of the dangers
# of using this notation. This occurs because b=0 evaluates
# to 0 and (( 0 )) is false.
# `true && false || cmd` evaluates (true && false), gets
# a false and then runs cmd.
# I had to work around this by ensuring that when I use
# `cond && (( ... )) || (( ... ))`, the last value inside
# the first `(( ... ))` must never be 0.
# The "correct" solution would be to use
# `if cond; then (( ... )); else (( ... )); fi`
# ... which I've since mostly switched to - in order to
# fit into the 60 columns wrapping :)


(( $# == 4 )) || exit 1
declare -ri capacity1=$1 capacity2=$2 goal=$3
declare -a to_explore  # Queue of scenarios to explore


# check_complete bucket1 bucket2 moves
# Check if we are done. If we are, print and exit.
check_complete () {
  local b1=$1 b2=$2 moves=$3
  if (( b1 == goal )); then
    goalBucket=one other=$b2
  elif (( b2 == goal )); then
    goalBucket=two other=$b1
  else
    return
  fi
  printf 'moves: %d, goalBucket: %s, otherBucket: %d\n' \
      "$moves" "$goalBucket" "$other"
  exit 0
}


# Conditionally, pour the full bucket into the empty bucket.
# If that leaves us water in both buckets, don't do anything.
# Next, fill the empty bucket and pour it into the full bucket.
# Now is a good time to check_complete.
# Finally, empty out any full buckets.
# Note, it's expected that this function is called with one
# bucket (partially/fully) filled and the other empty.
fill_pour_empty_append () {
  local b1=$1 b2=$2 moves=$3 swap=$4 c no_fill_pour=0
  # Rather than using b1|b2, use full|empty volume|capacity,
  # ie fv ev fc ec. It makes maths a lot simpler.
  local -i fv fc ev ec
  if (( b1 )); then
    (( fv=b1, fc=capacity1, ev=0, ec=capacity2 ))
  else
    (( fv=b2, fc=capacity2, ev=0, ec=capacity1 ))
  fi

  # Pour from one bucket into the other prior to fill&pour.
  if (( swap )); then
    if (( fv > ec )); then
      # Full bucket volume does not fit in the empty bucket.
      (( ev=ec, fv-=ev, moves++ ))
      (( no_fill_pour++ ))
    else
      (( c=b1, b1=b2, b2=c, c=fc, fc=ec, ec=c, moves++ ))
    fi
  fi

  (( space = fc-fv ))
  if (( no_fill_pour )); then
    :
  elif (( space == 0 )); then
    # We got a full and empty bucket. No filling needed.
    # Pour full into empty.
    if (( fc > ec )); then
      (( ev=ec, fv-=ec, moves++ ))
    else
      (( ev=fv, fv-=ev, moves++ ))
    fi
  elif (( space == ec )); then
    # we are just filling up the partially filled bucket
    (( fv+=ec, ev=0, moves++ ))
  else
    if (( space > ec )); then  # fill, pour, two moves
      (( fv+=ec, ev=0 ))
    else
      (( fv=fc, ev=ec-space ))
    fi
    (( moves += 2 ))
  fi

  # Convert back from full/empty to b1/b2
  (( b1 )) && (( b1=fv, b2=ev, 1 )) || (( b2=fv, b1=ev ))

  check_complete $b1 $b2 $moves
  (( b1 == capacity1 )) && (( b1=0, moves++ ))
  (( b2 == capacity2 )) && (( b2=0, moves++ ))
  to_explore+=( "$b1 $b2 $moves" )
}

buckets () {
  local -i b1 b2 moves=1
  local -a explored
  local start=$4

  # Initial conditions
  if [[ $start = 'one' ]]; then
    (( b2=0, b1=capacity1 ))
  else
    (( b1=0, b2=capacity2 ))
  fi
  # Pre-check if we are done before we start.
  check_complete $b1 $b2 1
  check_complete $capacity1 $b2 2
  check_complete $b1 $capacity2 2

  # We did not yet explore anything.
  # This line isn't strictly needed.
  for (( i = 0; i <= capacity1 || i <= capacity2; i++ )); do
    explored[i]=0
  done

  # Situations to start our exploring: the initial setup.
  to_explore=( "$b1 $b2 $moves" )

  # Read scenarios from the queue and maybe explore them
  while (( "${#to_explore[@]}" )); do
    # Pop!
    read b1 b2 moves <<< "${to_explore[0]}"
    to_explore=( "${to_explore[@]:1}" )

    # If we saw this one already, don't do it a second time.
    # Otherwise, mark it as seen.
    if (( explored[b1 ? b1 : b2] )); then
      continue
    else
      explored[b1 ? b1 : b2]=1
    fi
    # Uh ..... fine print says we must not consider these
    [[ $start = 'two' ]] && (( b1 == capacity1 && b2 == 0 )) && continue

    # Explore with and without an initial transfer
    fill_pour_empty_append $b1 $b2 $moves 0
    fill_pour_empty_append $b1 $b2 $moves 1
  done

  # Nothing left to explore! We've tried all the reachable
  # scenarios and what's left is bleak.
  echo "invalid goal"
  exit 1
}

buckets "$@"

# vim:ts=2:sw=2:expandtab
