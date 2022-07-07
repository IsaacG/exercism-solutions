#!/usr/bin/env gawk -f

BEGIN {
    key = tolower(key)
    # Count letters.
    for (i = 1; i <= length(key); i++)
        count[substr(key, i, 1)]++
}

function is_anagram(word,  needs) {
    word = tolower(word)
    # The key is not an anagram of itself.
    if (word == key) return 0
    # Anagrams must be the same length.
    if (length(word) != length(key)) return 0
    # Count letters and compare.
    for (i = 1; i <= length(word); i++)
        needs[substr(word, i, 1)]++
    for (i in needs)
        if (!(i in count) || count[i] < needs[i])
            return 0
    return 1
}

is_anagram($1)
