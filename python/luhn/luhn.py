class Luhn:
  def __init__(self, card_num):
    self._num = card_num.replace(' ', '')

  def valid(self):
    num = self._num
    # Input must be longer than 1 char.
    if len(num) <= 1:
      return False
    # Input must only contain digits.
    if not num.isnumeric():
      return False
    # Add all the odd-positioned numbers.
    total = sum(int(n) for n in num[-1::-2])
    # Double and maybe subtract 9 from the even-positioned numbers.
    for n in num[-2::-2]:
      n = 2 * int(n)
      total += n if n < 9 else n - 9
    return total % 10 == 0


# vim:ts=2:sw=2:expandtab
