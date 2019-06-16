#!/usr/bin/env bash

@test "wink for 1" {
    run bash secret_handshake.sh 1
    [[ $status -eq 0 ]]
    [[ $output == "wink" ]]
}

@test "double blink for 10" {
    run bash secret_handshake.sh 2
    [[ $status -eq 0 ]]
    [[ $output == "double blink" ]]
}

@test "close your eyes for 100" {
    run bash secret_handshake.sh 4
    [[ $status -eq 0 ]]
    [[ $output == "close your eyes" ]]
}

@test "jump for 1000" {
    run bash secret_handshake.sh 8
    [[ $status -eq 0 ]]
    [[ $output == "jump" ]]
}

@test "combine two actions" {
    run bash secret_handshake.sh 3
    [[ $status -eq 0 ]]
    [[ $output == "wink,double blink" ]]
}

@test "all possible actions" {
    run bash secret_handshake.sh 15
    [[ $status -eq 0 ]]
    [[ $output == "wink,double blink,close your eyes,jump" ]]
}

@test "do nothing for zero" {
    run bash secret_handshake.sh 0
    [[ $status -eq 0 ]]
    [[ $output == "" ]]
}

@test "reversing no actions still gives no actions" {
    run bash secret_handshake.sh 16
    [[ $status -eq 0 ]]
    [[ $output == "" ]]
}

@test "reversing one action gives the same action" {
    run bash secret_handshake.sh 24
    [[ $status -eq 0 ]]
    [[ $output == "jump" ]]
}

@test "reverse two actions" {
    run bash secret_handshake.sh 19
    [[ $status -eq 0 ]]
    [[ $output == "double blink,wink" ]]
}

@test "reverse all possible actions" {
    run bash secret_handshake.sh 31
    [[ $status -eq 0 ]]
    [[ $output == "jump,close your eyes,double blink,wink" ]]
}
