import math

def triplets_with_sum(number):
  triplets = {}
  for a in range(1, number):
    for b in range(a, number - a):
      c = number - a - b
      if is_triplet((a, b, c)):
        triplets.add((a, b, c))
  return triplets


def triplets_in_range(start, end):
  triplets = {}
  for a in range(start, end):
    for b in range(a, end - a):
      c = math.sqrt(a*a + b*b)
      if c != int(c):
        continue
      if start <= sum([a, b, c]) <= end:
        triplets.add((a, b, c))
  return triplets


def is_triplet(triplet):
  a, b, c = triplet
  return a*a + b*b == c*c


# vim:ts=2:sw=2:expandtab
