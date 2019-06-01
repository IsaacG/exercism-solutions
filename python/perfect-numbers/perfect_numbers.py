def classify(number):
  if number <= 0:
    raise ValueError('Bad input')
  aliquot = sum(i for i in range(1, number) if number % i == 0)
  if aliquot == number:
    return 'perfect'
  elif aliquot > number:
    return 'abundant'
  else:
    return 'deficient'


# vim:ts=2:sw=2:expandtab
