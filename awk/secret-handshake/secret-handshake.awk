#!/usr/bin/env gawk -f

BEGIN {
    n = split("wink,double blink,close your eyes,jump", actions, ",")
}

{
    for (i = 1; i <= n; i++)
        if (and($1, lshift(1, i - 1)))
            out[++count] = actions[i]

    # Join outputs, possibly in reverse.
    rev = and($1, 16)
    for (i = 1; i <= count; i++) {
        if (msg) msg = msg ","
        msg = msg out[rev ? count - i + 1 : i]
    }

    print msg
}
