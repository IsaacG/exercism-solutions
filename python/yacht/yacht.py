"""Score a game of Yacht."""
import collections
import typing


ONES = lambda count: 1 * count[1]
TWOS = lambda count: 2 * count[2]
THREES = lambda count: 3 * count[3]
FOURS = lambda count: 4 * count[4]
FIVES = lambda count: 5 * count[5]
SIXES = lambda count: 6 * count[6]
LITTLE_STRAIGHT = lambda count: 30 if set(count) == {1, 2, 3, 4, 5} else 0
BIG_STRAIGHT = lambda count: 30 if set(count) == {2, 3, 4, 5, 6} else 0
FULL_HOUSE = lambda count: CHOICE(count) if set(count.values()) == {2, 3} else 0
FOUR_OF_A_KIND = lambda count: 4 * count.most_common(1)[0][0] if count.most_common(1)[0][1] >= 4 else 0
YACHT = lambda count: 50 if len(set(count)) == 1 else 0
CHOICE = lambda count: sum(face * times for face, times in count.items())


def score(dice: list[int], category: typing.Callable[[dict[int, int]], int]) -> int:
    """Return the score of a "hand" in Yacht."""
    return category(collections.Counter(dice))

# vim:ts=4:sw=4:expandtab
