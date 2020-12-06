DAY = 24 * 60

class Clock:
  def __init__(self, hour, minute):
    self._min = (hour * 60 + minute) % DAY

  def __repr__(self):
    return '%02d:%02d' % (self._min // 60, self._min % 60)

  def __eq__(self, other):
    return self._min == other._min

  def __add__(self, minutes):
    return Clock(0, self._min + minutes)

  def __sub__(self, minutes):
    return Clock(0, self._min - minutes)


# vim:ts=2:sw=2:expandtab
