import enum

class Colors(enum.IntEnum):
  black = 0
  brown = 1
  red = 2
  orange = 3
  yellow = 4
  green = 5
  blue = 6
  violet = 7
  grey = 8
  white = 9


def color_code(color):
  return Colors[color].value


def value(colors):
  val = 0
  for c in colors[:2]:
    val = val * 10 + color_code(c)
  return val


# vim:ts=2:sw=2:expandtab
