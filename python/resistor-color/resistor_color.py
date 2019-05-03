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


def colors():
    return list(Colors.__members__.keys())


# vim:ts=2:sw=2:expandtab
