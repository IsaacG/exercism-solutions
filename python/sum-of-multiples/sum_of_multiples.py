def sum_of_multiples(limit, multiples):
  multiples = [m for m in multiples if m > 0]
  return sum(
    i for i in range(1, limit)
    if any(i % f == 0 for f in multiples))


# vim:ts=2:sw=2:expandtab
