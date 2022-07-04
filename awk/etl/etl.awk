#!/usr/bin/env gawk -f

{
    gsub(/[,":]+/, " ")
    $0 = tolower($0)
    for (i = 2; i <= NF; i++)
        out[$i] = $1
}
END {
    PROCINFO["sorted_in"] = "@ind_str_asc"
    for (i in out)
        printf "%s,%d\n", i, out[i]
}
