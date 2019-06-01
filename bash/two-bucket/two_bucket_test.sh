#!/usr/bin/env bash

@test "Measure using bucket one of size 3 and bucket two of size 5 - start with bucket one" {
    #skip
    expected="moves: 4, goalBucket: one, otherBucket: 5"
    run bash two_bucket.sh 3 5 1 "one"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "Measure using bucket one of size 3 and bucket two of size 5 - start with bucket two" {
    expected="moves: 8, goalBucket: two, otherBucket: 3"
    run bash two_bucket.sh 3 5 1 "two"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}
#   3|5
#   ---
#1. 0|5 5  
#2. 3|2
#3. 0|2 2
#4. 2|0
#5. 2|5
#6. 3|4 4
#7. 0|4
#8. 3|1 1


# 2|5
# 3|1

@test "Measure using bucket one of size 7 and bucket two of size 11 - start with bucket one" {
    expected="moves: 14, goalBucket: one, otherBucket: 11"
    run bash two_bucket.sh 7 11 2 "one"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "Measure using bucket one of size 7 and bucket two of size 11 - start with bucket two" {
    expected="moves: 18, goalBucket: two, otherBucket: 7"
    run bash two_bucket.sh 7 11 2 "two"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "Measure one step using bucket one of size 1 and bucket two of size 3 - start with bucket two" {
    expected="moves: 1, goalBucket: two, otherBucket: 0"
    run bash two_bucket.sh 1 3 3 "two"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "Measure using bucket one of size 2 and bucket two of size 3 - start with bucket one and end with bucket two" {
    expected="moves: 2, goalBucket: two, otherBucket: 2"
    run bash two_bucket.sh 2 3 3 "one"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}
#  2|3
#  ---
#1 2|0
#  0|2
#   | 
#   | 
#   | 

# error cases
@test "goal is too big for the buckets" {
    run bash two_bucket.sh 1 2 3 "one"
    [[ $status -ne 0 ]]
    [[ $output == *"invalid goal"* ]]
}

@test "cannot satisfy the goal" {
    run bash two_bucket.sh 6 8 3 "one"
    [[ $status -ne 0 ]]
    [[ $output == *"invalid goal"* ]]
}
