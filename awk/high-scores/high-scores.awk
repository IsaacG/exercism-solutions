#!/usr/bin/env gawk -f

# Sort numerically, descending.
BEGIN { PROCINFO["sorted_in"] = "@val_num_desc" }


# Record scores.
/[[:digit:]]+/ { scores[++count] = $1 }

# Print the top n scores.
function show_top(n) {
    c = 0
    for (i in scores) {
        if (++c > n) break
        print scores[i]
    }
}

$1 == "personalBest" { show_top(1) }
$1 == "personalTopThree" { show_top(3) }
$1 == "list" { for (i = 1; i <= count; i++) print(scores[i]) }
$1 == "latest" { print(scores[count]) }
