#!/usr/bin/env gawk -f

BEGIN { FPAT = "[[:alpha:]']+" }

{
    for (i = 1; i <= NF; i++) out = out substr($i, 1, 1)
    print toupper(out)
}
