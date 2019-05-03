
tests = ((400, True), (100, False), (4, True))

def is_leap_year(year):
  for div, res in tests:
    if year % div == 0:
      return res
  return False

# vim:ts=2:sw=2:expandtab
