#!/usr/bin/env gawk -f

BEGIN { RS = "" }
{
    if (/?[[:space:]]*$/) {
        if (/[[:alpha:]]/ && $0 == toupper($0))
            print "Calm down, I know what I'm doing!"
        else
            print "Sure."
    }
    else if (/^[[:space:]]*$/) print "Fine. Be that way!" 
    else if (/[[:alpha:]]/ && $0 == toupper($0)) print "Whoa, chill out!"
    else print "Whatever."
    found = 1
}

END {
    if (!found) print "Fine. Be that way!" 
}
