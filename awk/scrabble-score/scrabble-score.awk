#!/usr/bin/env gawk -f

BEGIN { FS = ""; score = 0 }
{
	$0 = toupper($0)
	for (i = 1; i <= NF; i++) {
        out = out $i
		switch ($i) {
		case /[AEIOULNRST]/: score += 1; break
		case /[DG]/: score += 2; break
		case /[BCMP]/: score += 3; break
		case /[FHVWY]/: score += 4; break
		case /[K]/: score += 5; break
		case /[JX]/: score += 8; break
		case /[QZ]/: score += 10; break
        }
    }

    print out "," score
}
