#!/usr/bin/env gawk -f

NR == 1 { first = $0 }
NR == 2 {
    if (length(first) != length) {
        print "strands must be of equal length"
        exit 1
    }

    diff = 0
    for (i = 1; i <= length; i++)
        if (substr(first, i, 1) != substr($0, i, 1))
            diff++
    print diff
}
