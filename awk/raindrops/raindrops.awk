#!/usr/bin/env gawk -f

BEGIN {
    if (! (num % 3)) out = out "Pling"
    if (! (num % 5)) out = out "Plang"
    if (! (num % 7)) out = out "Plong"
    if (! out) out = num
    print out
}
