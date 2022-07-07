#!/usr/bin/env gawk -f

@load "ordchr"

function spaces(n) {
    out = ""
    for (i = 1; i <= n; i++) out = out " "
    return out
}

function line(width, char) {
    printf "%1$s%3$s%2$s%3$s%1$s\n", spaces(width - char), spaces(2 * char - 1), chr(ord("A") + char)
}

function line_a(width) { printf "%1$sA%1$s\n", spaces(width) }

{
    d = ord($1) - ord("A")
    line_a(d)
    for (j = 1; j <= d; j++) line(d, j)
    for (j = d - 1; j > 0; j--) line(d, j)
    if (d) line_a(d)
}
