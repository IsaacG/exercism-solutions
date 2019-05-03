def square_of_sum(count):
    return sum(range(count + 1)) ** 2


def sum_of_squares(count):
    return sum(map(lambda x: x ** 2, range(count + 1)))
    # return sum([x ** 2 for x in range(count + 1)])


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)

# vim:ts=2:sw=2:expandtab
