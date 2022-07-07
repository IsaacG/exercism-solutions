#!/usr/bin/env gawk -f

BEGIN {
    FS = ""
    # Map student name to an offset.
    n = split("ABCDEFGHIJKL", letters)
    for (i = 1; i <= n; i++)
        if (letters[i] == substr(name, 1, 1))
            offset = i

    # Map plant letter to plant name.
    n = split("clover grass radishes violets", plants, " ")
    for (i = 1; i <= n; i++)
        plant[toupper(substr(plants[i], 1, 1))] = plants[i]
}
{ out = out " " plant[$(2 * offset - 1)] " " plant[$(2 * offset)] }
END { print(substr(out, 2)) }

