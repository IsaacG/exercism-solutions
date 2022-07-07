#!/usr/bin/env gawk -f

@include "join"

function piglaten(word) {
    if (match(word, "^[aeiou]"))                           return word "ay"
    if (match(word, "^[xy][^aeiou]"))                      return word "ay"
    if (match(word, "^([^aeiou]*qu)([aeiou].*)", groups))  return groups[2] groups[1] "ay"
    if (match(word, "^([^aeiou]*)([aeiouy].*)", groups))   return groups[2] groups[1] "ay"
    if (match(word, "^(.)(.*)", groups))                   return groups[2] groups[1] "ay"
}

{
    for (i = 1; i <= NF; i++)
        out[i] = piglaten($i)
    print join(out, 1, NF, " ")
}
