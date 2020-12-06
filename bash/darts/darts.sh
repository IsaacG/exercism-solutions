#!/usr/bin/env bash

die () { echo "$1"; exit 1; }

(( $# != 2 )) && die "Invalid arg count"
for i; do [[ $i = *[^[:digit:].-]* ]] && die "Non-numeric arg"; done

bc <<< "scale=4 
        x=$1 ; y=$2 ; d=sqrt(x^2 + y^2 )
        if (d <= 1) 10 else if (d <= 5) 5 else if (d <= 10) 1 else 0"
exit 0
