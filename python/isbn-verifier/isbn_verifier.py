from functools import reduce

reduction = lambda count, pair: count + pair[0] * pair[1]

def verify(isbn):
  isbn = isbn.replace('-', '')
  if len(isbn) != 10:
    return False
  nums = list(isbn)
  # The last character only can be 'X'. Map 'X' => 10
  if nums[-1] == 'X':
    nums[-1] = 10

  try:
    count = reduce(reduction, zip(map(int, nums), range(10, 0, -1)), 0)
  except ValueError:
    # Invalid input
    return False
  return count % 11 == 0


# vim:ts=2:sw=2:expandtab
