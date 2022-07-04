#!/usr/bin/env gawk -f

BEGIN { name = "you" }
NF { name = $0 }
END { printf "One for %s, one for me.\n", name }
