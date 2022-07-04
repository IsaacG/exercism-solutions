#!/usr/bin/env gawk -f

BEGIN { FS = "[-:T ]" }
{
    for (i = 1; i <= 6; i++) timestamp = timestamp $i + 0 " "
    now = mktime(timestamp, 1)
    print strftime("%FT%T", now + 10^9, 1)
}
