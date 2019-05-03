import collections

def count(dice):
  c = collections.defaultdict(int)
  for i in dice:
    c[i] += 1
  return c

_NUM = lambda d, n: sum([i for i in d if i == n])
ONES = lambda d: _NUM(d, 1)
TWOS = lambda d: _NUM(d, 2)
THREES = lambda d: _NUM(d, 3)
FOURS = lambda d: _NUM(d, 4)
FIVES = lambda d: _NUM(d, 5)
SIXES = lambda d: _NUM(d, 6)
LITTLE_STRAIGHT = lambda d: 30 if set(d) == {1, 2, 3, 4, 5} else 0
BIG_STRAIGHT = lambda d: 30 if set(d) == {2, 3, 4, 5, 6} else 0
FULL_HOUSE = lambda d: sum(d) if set(count(d).values()) == {2, 3} else 0
FOUR_OF_A_KIND = lambda d: sum([n for n, c in count(d).items() if c >= 4]) * 4
YACHT = lambda d: 50 if len(set(d)) == 1 else 0
CHOICE = lambda d: sum(d)


def score(dice, category):
    return category(dice)

# vim:ts=2:sw=2:expandtab
