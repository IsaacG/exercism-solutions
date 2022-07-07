#!/usr/bin/env gawk -f

function die(msg) {
    print msg
    exit 1
}

$0 !~ /is .*\?$/ { die("syntax error") }
! /What is .*\?$/ { die("unknown operation") }
$0 !~ "is " digit ".*\\?$" { die("syntax error") }

BEGIN { digit = "(-?[[:digit:]]+)" }

{
    gsub(/What is /, "")
    gsub(/\?$/, "")
    while (NF > 1) {
        # print
        if (match($0, "^" digit " (plus|minus|multiplied by|divided by)")) {
            if (match($0, "^" digit " plus " digit, groups))
                sub(digit " plus " digit, groups[1] + groups[2])
            else if (match($0, "^" digit " minus " digit, groups))
                sub(digit " minus " digit, groups[1] - groups[2])
            else if (match($0, "^" digit " multiplied by " digit, groups))
                sub(digit " multiplied by " digit, groups[1] * groups[2])
            else if (match($0, "^" digit " divided by " digit, groups))
                sub(digit " divided by " digit, groups[1] / groups[2])
            else
                die("syntax error")
        }
        else if (match($0, "^" digit " [[:alpha:]]+"))
            die("unknown operation")
        else
            die("syntax error")
    }
    print
}
