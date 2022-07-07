#!/usr/bin/env -S gawk -f

{
    if (!($1 % 4)) {
        if ($1 % 100 || !($1 % 400)) print "true"
        else print "false"
    } else {
        print "false"
    }
}
