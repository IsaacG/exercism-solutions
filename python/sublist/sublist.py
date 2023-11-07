import enum

class Results(enum.Enum):
    SUBLIST = 0
    SUPERLIST = 1
    EQUAL = 2
    UNEQUAL = 3


# Possible sublist categories.
# Change the values as you see fit.
for result in Results:
    globals()[result.name] = result


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    r = SUBLIST
    if len(list_one) > len(list_two):
        list_one, list_two = list_two, list_one
        r = SUPERLIST

    for i in range(len(list_two) - len(list_one) + 1):
        if list_one == list_two[i:i + len(list_one)]:
            return r

    return UNEQUAL
