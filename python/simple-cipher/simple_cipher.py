import random
import string


def add(a, b, rev):
  """Add two chars together. Or subtract, if rev."""
  val = ord(a) - ord('a')
  dist = ord(b) - ord('a')
  if rev:
    dist = -dist
  res = (val + dist) % 26
  return chr(res + ord('a'))


class Cipher(object):

  def __init__(self, key=None):
    if key is None:
      key = ''.join([a for a in random.choice(string.ascii_lowercase) for _ in range(100)])
    self.key = key

  def _key(self, i):
    return self.key[i % len(self.key)]

  def encode(self, text):
    return ''.join([add(c, self._key(i), False) for i, c in enumerate(text)])

  def decode(self, text):
    return ''.join([add(c, self._key(i), True) for i, c in enumerate(text)])


# vim:ts=2:sw=2:expandtab
