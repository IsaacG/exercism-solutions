from functools import reduce

# Reduce a list of pairs by adding 1 on differing, otherwise count doesn't change.
reduction = lambda count, pair: count if pair[0] == pair[1] else count + 1

def distance(strand_a, strand_b):
  if len(strand_a) != len(strand_b):
    raise ValueError("Lengths differ")
  d = reduce(reduction, zip(strand_a, strand_b), 0)
  assert d == alt_distance(strand_a, strand_b)
  return d

def alt_distance(strand_a, strand_b):
  if len(strand_a) != len(strand_b):
    raise ValueError("Lengths differ")
  return len([a for a, b in zip(strand_a, strand_b) if a != b])

# vim:ts=2:sw=2:expandtab
