#!/usr/bin/env gawk -f

BEGIN {
    split("abcdefghijklmnopqrstuvwxyz", letters, "")
}
{
    $0 = tolower($0)
    for (i = 0; i <= 26; i++)
        if (! index($0, letters[i])) {
            print "false"
            exit
        }
    print "true"
}
