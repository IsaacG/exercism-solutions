def triplets_with_sum(number):
  triplets = []
  for a in range(1, number):
    for b in range(a, number - a):
      c = number - a - b
      if is_triplet((a, b, c)):
        triplets.append((a, b, c))
  return triplets


def triplets_in_range(start, end):
  t = []
  for n in range(start, end + 1):
    t.extend(triplets_with_sum(n))
  return t


def is_triplet(triplet):
  a, b, c = triplet
  return a*a + b*b == c*c


# vim:ts=2:sw=2:expandtab
