import math

def score(x, y):
    diag = math.sqrt(x*x + y*y)
    if diag <= 1:
      return 10
    if diag <= 5:
      return 5
    if diag <= 10:
      return 1
    return 0


# vim:ts=2:sw=2:expandtab
