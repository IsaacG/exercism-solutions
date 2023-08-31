import string


class PhoneNumber(object):
  def __init__(self, num):
    if any(c in num for c in string.ascii_letters):
      raise ValueError('letters not permitted')
    if any(c in num for c in set(string.punctuation) - set("()+-.")):
      raise ValueError('punctuations not permitted')
        

    # Ignore all non-digits.
    digits = ''.join([i for i in num if i.isdigit()])

    if len(digits) > 11:
      raise ValueError('must not be greater than 11 digits')
    # For an 11-digit with country code, drop the country code.
    if len(digits) == 11:
      if digits.startswith('1'):
        digits = digits[1:]
      else:
        raise ValueError('11 digits must start with 1')
    self.number = digits

    if len(self.number) != 10:
      raise ValueError('must not be fewer than 10 digits')

    for num, name in (('0', 'zero'), ('1', 'one')):
      for val, part in ((self.area_code, 'area'), (self.exchange, 'exchange')):
        if val.startswith(num):
          raise ValueError(f'{part} code cannot start with {name}')

  @property
  def area_code(self):
    return self.number[0:3]

  @property
  def exchange(self):
    return self.number[3:6]

  @property
  def subscriber(self):
    return self.number[6:10]

  def pretty(self):
    return '(%s)-%s-%s' % (self.number[0:3], self.number[3:6], self.number[6:10])


# vim:ts=2:sw=2:expandtab
