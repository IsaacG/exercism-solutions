#!/usr/bin/env gawk -f

BEGIN {
    sounds[3] = "Pling"; sounds[5] = "Plang"; sounds[7] = "Plong"
    for (factor in sounds)
        if (num % factor == 0)
            out = out sounds[factor]
    print (out ? out : num)
}
