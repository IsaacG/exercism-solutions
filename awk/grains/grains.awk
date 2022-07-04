#!/usr/bin/env gawk -f

$1 == "total" {
    print 2 ^ 64 - 1
    exit
}
1 <= $1 && $1 <= 64 {
    print 2 ^ ($1 - 1)
    exit
}
{
    print "square must be between 1 and 64"
    exit 1
}
