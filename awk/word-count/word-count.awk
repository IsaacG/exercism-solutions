#!/usr/bin/env gawk -f

BEGIN {
    FPAT = "[[:alnum:]]+('[[:alnum:]]+)?"
}
{
    $0 = tolower($0)
    for (i = 1; i <= NF; i++)
        count[$i]++
}
END {
    for (word in count)
        printf "%s: %d\n", word, count[word]
}
