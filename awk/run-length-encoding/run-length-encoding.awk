#!/usr/bin/env gawk -f
BEGIN {
    if (type == "encode") FS = ""
    if (type == "decode") FPAT = "[[:digit:]]+|[[:alpha:] ]"
}

type == "encode" {
    for (i = 1; i <= NF + 1; i++) {
        if ($i != prior) {
            out = out (count > 1 ? count : "") prior
            prior = $i
            count = 0
        }
        count++
    }
    print out
}

type == "decode" {
    for (i = 1; i <= NF; i++) {
        count = 1
        if ($i + 0) {
            count = $i
            i++
        }
        for (j = 1; j <= count; j++)
            out = out $i
    }
    print out
}
