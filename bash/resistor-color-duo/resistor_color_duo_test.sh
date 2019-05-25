#!/usr/bin/env bash

@test "brown black" {
    run bash resistor_color_duo.sh brown black
    [[ $status -eq 0 ]]
    [[ $output == "10" ]]
}

@test "blue grey" {
    run bash resistor_color_duo.sh blue grey
    [[ $status -eq 0 ]]
    [[ $output == "68" ]]
}

@test "yellow violet" {
    run bash resistor_color_duo.sh yellow violet
    [[ $status -eq 0 ]]
    [[ $output == "47" ]]
}

@test "orange orange" {
    run bash resistor_color_duo.sh orange orange
    [[ $status -eq 0 ]]
    [[ $output == "33" ]]
}

@test "invalid color" {
    run bash resistor_color_duo.sh foo
    [[ $status -eq 1 ]]
    [[ $output == "invalid color" ]]
}
