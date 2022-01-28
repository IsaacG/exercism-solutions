#!/bin/python3

import collections
import string


def count_words(sentence):
    for i in ",_":
        sentence = sentence.replace(i, " ")
    words = [w.strip(string.punctuation) for w in sentence.lower().split()]
    return collections.Counter(w for w in words if w)
