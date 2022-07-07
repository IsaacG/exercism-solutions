#!/usr/bin/env gawk -f

function set(base, string) {
    n = split(string, chars)
    for (i = 1; i <= n; i++) vals[base * 10^(i-1)] = chars[i]
}
function concat(a, b) {
    vals[a - b] = vals[b] vals[a]
    vals[a/2 - b] = vals[b] vals[a/2]
}

BEGIN {
    # Set characters.
    set(1, "I X C M")
    set(5, "V L D")
    # Set compound characters.
    for (i = 0; i < 3; i++) concat(1 * 10^(i+1), 10^i)
    PROCINFO["sorted_in"] = "@ind_num_desc"
}

{
    num = $1
    out = ""
    for (i in vals) {
        while (num >= i + 0) {
            out = out vals[i]
            num -= i
        }
    }
    print out
}
