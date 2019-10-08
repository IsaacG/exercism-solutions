def primes(limit):
  limit += 1
  l = [True for i in range(limit)]
  for i in range(2, limit):
    if not l[i]:
      continue
    for j in range(2 * i, limit, i):
      l[j] = False
  return [i for i, v in enumerate(l) if i > 1 and v]


# vim:ts=2:sw=2:expandtab
