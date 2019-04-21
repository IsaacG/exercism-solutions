class Phone(object):
  def __init__(self, num):
    # Ignore all non-digits.
    digits = ''.join([i for i in num if i.isdigit()])

    # For an 11-digit with country code, drop the country code.
    if len(digits) == 11 and digits.startswith('1'):
      digits = digits[1:]
    self.number = digits
    self.validate()

  def validate(self):
    if len(self.number) != 10:
      raise ValueError('Invalid number')

    for invalid in ('0', '1'):
      for check in (self.area_code, self.exchange):
        if check.startswith(invalid):
          raise ValueError('Invalid number')

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
    return '(%s) %s-%s' % (self.number[0:3], self.number[3:6], self.number[6:10])

        
# vim:ts=2:sw=2:expandtab
