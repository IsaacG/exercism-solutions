#!/usr/bin/env gawk -f

@include "join"

BEGIN {
    FS = ","
    all = "eggs,peanuts,shellfish,strawberries,tomatoes,chocolate,pollen,cats"
    n = split(all, allergens)
}

function allergies(num) {
    for (i = 1; i <= n; i++)
        if (and(lshift(1, i - 1), num))
            got[i] = allergens[i]
}

$2 == "list" {
    allergies($1)
    for (i = 1; i <= n; i++)
        if (i in got)
            out = out "," got[i]
    print(substr(out, 2))
}

$2 == "allergic_to" {
    allergies($1)
    out = "false"
    for (i = 1; i <= n; i++) {
        if (i in got && got[i] == $3)
            out = "true"
    }
    print out
}
