#!/usr/bin/env gawk -f

BEGIN { FS = "" }

{
    # Record all edges/corners.
    for (i = 1; i <= NF; i++) {
        if ($i == "+")
            corner[NR][i] = 1
        if ($i == "+" || $i == "|")
            vert[NR][i] = 1
        if ($i == "+" || $i == "-")
            horiz[NR][i] = 1
    }
}

END {
    count = 0
    # Check rectangles by corners.
    for (y1 in corner) for (x1 in corner[y1]) for (y2 in corner) for (x2 in corner[y2]) {
        # Convert str to int.
        y1 = y1 + 0; y2 = y2 + 0; x1 = x1 + 0; x2 = x2 + 0
        # if (x1 == 8 && y1 == 3) printf("(%d, %d) x (%d, %d)\n", x1, y1, x2, y2)
        if (x1 >= x2 || y1 >= y2)
            continue
        if (!corner[y1][x2] || !corner[y2][x1])
            continue
        matches = 1
        for (y = y1; y <= y2; y++)
            if (!vert[y][x1] || !vert[y][x2])
                matches = 0
        for (x = x1; x <= x2; x++)
            if (!horiz[y1][x] || !horiz[y2][x])
                matches = 0
        if (matches)
            count += 1
    }
    print count
}
