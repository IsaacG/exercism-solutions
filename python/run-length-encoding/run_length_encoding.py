import re


REP_RE = re.compile(r'(\d*)(\D)')


def decode(string):
  out = ''
  for m in REP_RE.finditer(string):
    cnt, char = m.groups()
    cnt = int(cnt) if cnt else 1
    out += char * cnt
  return out


def encode(string):
  if string == "":
    return string
  out = ''
  cnt = 0
  prev = string[0]
  for c in string:
    if c == prev:
      cnt += 1
    else:
      out += '%d%s' % (cnt, prev) if cnt > 1 else prev
      cnt = 1
    prev = c
  else:
    out += '%d%s' % (cnt, prev) if cnt > 1 else prev
  return out


# vim:ts=2:sw=2:expandtab
