#!/usr/bin/env gawk -f

# Read text in blocks of three chars.
BEGIN { FPAT = "..." }

# Detect invalid column count.
length % 3 { error = "Number of input columns is not a multiple of three" }

# Convert blocks of chars to output.
function decode() {
    out = out ","
    for (i in data) {
        switch(data[i]) {
        case "     |  |   ": out = out "1"; break
        case " _  _||_    ": out = out "2"; break
        case " _  _| _|   ": out = out "3"; break
        case "   |_|  |   ": out = out "4"; break
        case " _ |_  _|   ": out = out "5"; break
        case " _ |_ |_|   ": out = out "6"; break
        case " _   |  |   ": out = out "7"; break
        case " _ |_||_|   ": out = out "8"; break
        case " _ |_| _|   ": out = out "9"; break
        case " _ | ||_|   ": out = out "0"; break
        default: out = out "?"; break
        }
        delete data[i]
    }

}

# Collect blocks of data.
{
    for (i = 1; i <= NF; i++)
        data[i] = data[i] $i
    if (!(NR % 4)) decode()
}

END {
    if (NR % 4 && ! error) error = "Number of input lines is not a multiple of four"
    if (error) {
        print error
        exit 1
    }
    print substr(out, 2)
}

