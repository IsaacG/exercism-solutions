#!/usr/bin/env gawk -f

BEGIN {
    l = length(num)
    for (i = 1; i <= l; i++) 
        sum += substr(num, i, 1) ^ l

    print (sum == num) ? "true" : "false"
}
