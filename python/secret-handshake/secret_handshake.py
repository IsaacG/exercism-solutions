CMDS = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(number):
  number = int(number, 2)
  c = []
  for i, j in enumerate(CMDS):
    if number & 1 << i:
      c.append(j)
  if number & 1 << 4:
    c.reverse()
  return c


# vim:ts=2:sw=2:expandtab