#!/usr/bin/env bats
# generated on 2022-11-02T20:59:42Z
load bats-extra

@test 'an empty string' {
    #[[ $BATS_RUN_SKIPPED == "true" ]] || skip

    run jq -r -f reverse-string.jq << 'END_INPUT'
        {
          "value": ""
        }
END_INPUT

    assert_success
    expected=''
    assert_equal "$expected" "$output"
}

@test 'a word' {
    [[ $BATS_RUN_SKIPPED == "true" ]] || skip

    run jq -r -f reverse-string.jq << 'END_INPUT'
        {
          "value": "robot"
        }
END_INPUT

    assert_success
    expected='tobor'
    assert_equal "$expected" "$output"
}

@test 'a capitalized word' {
    [[ $BATS_RUN_SKIPPED == "true" ]] || skip

    run jq -r -f reverse-string.jq << 'END_INPUT'
        {
          "value": "Ramen"
        }
END_INPUT

    assert_success
    expected='nemaR'
    assert_equal "$expected" "$output"
}

@test 'a sentence with punctuation' {
    [[ $BATS_RUN_SKIPPED == "true" ]] || skip

    run jq -r -f reverse-string.jq << 'END_INPUT'
        {
          "value": "I'm hungry!"
        }
END_INPUT

    assert_success
    expected='!yrgnuh m'\''I'
    assert_equal "$expected" "$output"
}

@test 'a palindrome' {
    [[ $BATS_RUN_SKIPPED == "true" ]] || skip

    run jq -r -f reverse-string.jq << 'END_INPUT'
        {
          "value": "racecar"
        }
END_INPUT

    assert_success
    expected='racecar'
    assert_equal "$expected" "$output"
}

@test 'an even-sized word' {
    [[ $BATS_RUN_SKIPPED == "true" ]] || skip

    run jq -r -f reverse-string.jq << 'END_INPUT'
        {
          "value": "drawer"
        }
END_INPUT

    assert_success
    expected='reward'
    assert_equal "$expected" "$output"
}

