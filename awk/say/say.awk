#!/usr/bin/env gawk -f

BEGIN {
    split("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen ninteen", ones)
    split("ten twenty thirty forty fifty sixty seventy eighty ninty", tens)
}

function say(num, base) {
    num = int(num / 10 ^ base) % (10 ^ (base + 3))
    out = ""
    if (num >= 100) {
        out = " " ones[int(num / 100)] " hundred"
        num = num % 100
    }
    if (num >= 20) {
        out = out " " tens[int(num / 10)]
        num = num % 10
        if (num > 0)
            out = out "-" ones[num]
    }
    else if (num > 0) {
        out = out " " ones[num]
    }
    return substr(out, 2)
}

$1 < 0 || $1 >= 10^12 {
    print "input out of range"
    exit 1
}

$1 == 0 { print "zero" }

$1 {
    out = ""
    num = $1
    if (num >= 10^9) {
        out = out " " say(num, 9) " billion"
        num = num % 10^9
    }
    if (num >= 10^6) {
        out = out " " say(num, 6) " million"
        num = num % 10^6
    }
    if (num >= 10^3) {
        out = out " " say(num, 3) " thousand"
        num = num % 10^3
    }
    if (num > 0 || ! out) {
        out = out " " say(num, 0) ""
    }
    print substr(out, 2)
}
