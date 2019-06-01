import collections
import string

def is_isogram(word):
  c = collections.Counter([
      i for i in word.lower() if i in string.ascii_letters])
  if not c:
    return True
  return c.most_common(1)[0][1] <= 1

# vim:ts=2:sw=2:expandtab
