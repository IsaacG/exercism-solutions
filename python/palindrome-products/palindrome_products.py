def is_palindrome(n):
  return str(n) == str(n)[::-1]
  
def op_palindrome(max_factor, min_factor, op):
  if min_factor > max_factor:
    raise ValueError("Bad input")

  factors = set()
  p = None
  for i in range(min_factor, max_factor + 1):
    for j in range(i, max_factor + 1):
      if p and op(i * j, p): continue
      if not is_palindrome(i * j): continue
      if i * j != p:
        factors.clear()
        p = i * j
      factors.add((i, j))

  if p is None:
    return p, []
  return p, factors


def largest_palindrome(max_factor, min_factor):
  return op_palindrome(max_factor, min_factor, lambda x, y: x < y)


def smallest_palindrome(max_factor, min_factor):
  return op_palindrome(max_factor, min_factor, lambda x, y: x > y)


# vim:ts=2:sw=2:expandtab
