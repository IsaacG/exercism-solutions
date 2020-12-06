import re

def abbreviate(words):
  words = re.sub(r'[-_]', ' ', words).split()
  return ''.join(w[0] for w in words).upper()


# vim:ts=2:sw=2:expandtab
