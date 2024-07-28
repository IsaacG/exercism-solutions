"""Score a game of Yacht."""
import collections


def sum_count(count: collections.Counter) -> int:
    return sum(val * num for val, num in count.items())


def face(val: int, count: collections.Counter) -> int:
    return val * count[val]


CATEGORIES = [
    ("ONES", None, lambda count: face(1, count)),
    ("TWOS", None, lambda count: face(2, count)),
    ("THREES", None, lambda count: face(3, count)),
    ("FOURS", None, lambda count: face(4, count)),
    ("FIVES", None, lambda count: face(5, count)),
    ("SIXES", None, lambda count: face(6, count)),
    ("LITTLE_STRAIGHT", (lambda count: set(count) == {1, 2, 3, 4, 5}), 30),
    ("BIG_STRAIGHT", (lambda count: set(count) == {2, 3, 4, 5, 6}), 30),
    ("FULL_HOUSE", (lambda count: set(count.values()) == {2, 3}), sum_count),
    (
        "FOUR_OF_A_KIND",
        (lambda count: count.most_common(1)[0][1] >= 4),
        (lambda count: 4 * count.most_common(1)[0][0]),
    ),
    ("YACHT", (lambda count: len(set(count)) == 1), 50),
    ("CHOICE", None, sum_count),
]
for name, condition, value in CATEGORIES:
    globals()[name] = (condition, value)


def score(dice: list[int], category) -> int:
    """Return the score of a "hand" in Yacht."""
    counter = collections.Counter(dice)
    condition, value = category
    if condition is None or condition(counter):
        return value(counter) if callable(value) else value
    return 0
