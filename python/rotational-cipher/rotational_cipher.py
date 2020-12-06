import string

def rotate(text, key):
  return ''.join(_add(t, key) for t in text)

def _add(char, key):
  if char in string.ascii_uppercase:
    return chr((ord(char) + key - ord('A')) % 26 + ord('A'))
  elif char in string.ascii_lowercase:
    return chr((ord(char) + key - ord('a')) % 26 + ord('a'))
  else:
    return char


# vim:ts=2:sw=2:expandtab
