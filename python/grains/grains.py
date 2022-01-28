def sq(n):
  return 2 ** (n - 1)


def valid(n):
  if n < 1 or n > 64:
    raise ValueError('square must be between 1 and 64')


def square(n):
  valid(n)
  return sq(n)


def total():
  return sq(64 + 1) - 1

# vim:ts=2:sw=2:expandtab
