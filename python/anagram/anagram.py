from collections import defaultdict


def count(word):
  m = defaultdict(int)
  for c in word.lower():
    m[c] += 1
  return m


def find_anagrams(word, candidates):
  wcount = count(word)

  return [c for c in candidates
          if c.lower() != word.lower() and wcount == count(c)]


# vim:ts=2:sw=2:expandtab
