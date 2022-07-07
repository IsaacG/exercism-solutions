#!/usr/bin/env gawk -f

@load "ordchr"

BEGIN { FS = "|" }

function mmi(a) {
    n = 1
    while ( a * n % 26 != 1 ) n++
    return n
}
function achr(letter) {
    if (letter < 0) letter += 26
    return chr(letter + ord("a"))
}
function aord(letter) {
    return ord(letter) - ord("a")
}
function encode(a, b, n, letter) {
    return achr((a * aord(letter) + b) % 26)
}
function decode(a, b, n, letter) {
    return achr((n * (aord(letter) - b)) % 26)
}

!($2 % 2 && $2 % 13) { print "a and m must be coprime."; exit 1 }

{
    fn = ($1 == "encode") ? "encode" : "decode"
    $0 = tolower($0)
    n = mmi($2)
    for (i = 1; i <= length($4); i++) {
        letter = substr($4, i, 1)
        if (letter ~ /[[:alpha:]]/)
            out = out @fn($2, $3, n, letter)
        else if (letter ~ /[[:digit:]]/)
            out = out letter
    }

    if ($1 == "encode") {
        for (i = 1; i <= length(out); i += 5)
            chunked = chunked " " substr(out, i, 5)
        print substr(chunked, 2)
    } else print out
}
