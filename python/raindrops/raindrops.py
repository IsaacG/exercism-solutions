def convert(number):
  sounds = [(3, 'Pling'), (5, 'Plang'),  (7, 'Plong')]
  return ''.join(s for f, s in sounds if number % f == 0) or str(number)


# vim:ts=2:sw=2:expandtab
