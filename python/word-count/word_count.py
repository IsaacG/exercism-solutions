#!/bin/python3

import collections
import string


def count_words(sentence):
  for i in ',_':
    sentence = sentence.replace(i, ' ')
  clean = lambda x: x.strip(string.punctuation).lower()
  words = [clean(w) for w in sentence.split()]
  return collections.Counter(w for w in words if w)

# vim:ts=2:sw=2:expandtab
