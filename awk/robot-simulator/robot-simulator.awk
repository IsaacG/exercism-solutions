#!/usr/bin/env gawk -f

BEGIN {
    # Compute the next direction for turns.
    split("north east south west", compass)
    for (i = 1; i <= 4; i++) {
        r[compass[i]] = compass[i % 4 + 1]
        l[compass[i % 4 + 1]] = compass[i]
    }

    # Set defaults
    if (!x) x = 0
    if (!y) y = 0
    if (!dir) dir = "north"

    if (!r[dir]) {
        err = "invalid direction"
    }
}

! /^[RLA]$/ { err = "invalid instruction" }
/R/ { dir = r[dir] }
/L/ { dir = l[dir] }
/A/ {
    switch(dir) {
    case "north": y++; break
    case "south": y--; break
    case "east": x++; break
    case "west": x--; break
    }
}
END {
    if (err) {
        print err
        exit 1
    } else {
        print x, y, dir }
    }
