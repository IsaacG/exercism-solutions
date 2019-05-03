def sq(n):
  return 2 ** (n - 1)


def valid(n):
  if n < 1 or n > 64:
    raise ValueError('Invalid')


def on_square(n):
  valid(n)
  return sq(n)


def total_after(n):
  valid(n)
  return sq(n + 1) - 1

# vim:ts=2:sw=2:expandtab
