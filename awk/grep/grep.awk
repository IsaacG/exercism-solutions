#!/usr/bin/env gawk -f

BEGIN {
    n = split(flags, f)
    for (i = 1; i <= n; i++) opt[f[i]] = 1
    IGNORECASE = opt["i"]
    if (opt["x"]) pattern = "^" pattern "$"
}

($0 ~ pattern) != opt["v"] {
    found = 1
    if (opt["l"]) {
        print FILENAME
        nextfile
    }
    print (ARGC > 2 ? FILENAME ":" : "") (opt["n"] ? FNR ":" : "") $0
}

END { if (!found) exit 1 }
