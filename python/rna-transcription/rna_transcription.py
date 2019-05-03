def to_rna(s):
  swaps = (('G', 'X'), ('C', 'G'), ('X', 'C'), ('A', 'U'), ('T', 'A'))
  for x, y in swaps:
    s = s.replace(x, y)
  return s

# vim:ts=2:sw=2:expandtab
