#!/usr/bin/env bash

# run-length encode a string

@test "encode empty string" {
    expected=""
    run bash run_length_encoding.sh encode ""
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "encode single characters only are encoded without count" {
    expected="XYZ"
    run bash run_length_encoding.sh encode "XYZ"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "encode string with no single characters" {
    expected="2A3B4C"
    run bash run_length_encoding.sh encode "AABBBCCCC"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "encode single characters mixed with repeated characters" {
    expected="12WB12W3B24WB"
    run bash run_length_encoding.sh encode "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "encode multiple whitespace mixed in string" {
    expected="2 hs2q q2w2 "
    run bash run_length_encoding.sh encode "  hsqq qww  "
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "encode lowercase characters" {
    expected="2a3b4c"
    run bash run_length_encoding.sh encode "aabbbcccc"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

# run-length decode a string

@test "decode empty string" {
    expected=""
    run bash run_length_encoding.sh decode ""
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "single characters only" {
    expected="XYZ"
    run bash run_length_encoding.sh decode "XYZ"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "decode string with no single characters" {
    expected="AABBBCCCC"
    run bash run_length_encoding.sh decode "2A3B4C"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "decode single characters with repeated characters" {
    expected="WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    run bash run_length_encoding.sh decode "12WB12W3B24WB"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "decode multiple whitespace mixed in string" {
    expected="  hsqq qww  "
    run bash run_length_encoding.sh decode "2 hs2q q2w2 "
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

@test "decode lower case string" {
    expected="aabbbcccc"
    run bash run_length_encoding.sh decode "2a3b4c"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}

# encode and then decode

@test "encode followed by decode gives original string" {
    expected="zzz ZZ  zZ"
    run bash run_length_encoding.sh encode "zzz ZZ  zZ"
    [[ $status -eq 0 ]]
    encoded=$output
    run bash run_length_encoding.sh decode "$encoded"
    [[ $status -eq 0 ]]
    [[ $output == "$expected" ]]
}
