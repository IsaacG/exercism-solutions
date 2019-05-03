from itertools import permutations

side_combos = ((0, 1, 2), (1, 2, 0), (2, 0, 1))

def is_valid(sides):
  return all(sides[a] <= sides[b] + sides[c]
             for a, b, c in side_combos) and sides[0]


def is_equilateral(sides):
  if not is_valid(sides):
    return False
  return all(sides[a] == sides[b] for a, b, _ in side_combos)


def is_isosceles(sides):
  if not is_valid(sides):
    return False
  return any(sides[a] == sides[b] for a, b, _ in side_combos)


def is_scalene(sides):
  if not is_valid(sides):
    return False
  return not any(sides[a] == sides[b] for a, b, _ in side_combos)

# vim:ts=2:sw=2:expandtab
