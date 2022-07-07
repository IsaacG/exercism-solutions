#!/usr/bin/env gawk -f

# These variables are initialized on the command line (using '-v'):
# - action
# - grade

BEGIN {
    FS = ","
    PROCINFO["sorted_in"] = "sort"
}
function sort(i1, v1, i2, v2) {
    if (v1 != v2) return (v1 < v2 ? -1 : 1)
    return (i1 < i2 ? -1 : 1)
}

{ if (!($1 in roster)) roster[$1] = $2 }

function filter(student) {
    return (action == "roster" || roster[student] == grade) ? 1 : 0
}

END {
    for (student in roster) if (filter(student)) out = out "," student
    print substr(out, 2)
}
