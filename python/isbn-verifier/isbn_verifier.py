from functools import reduce

reduction = lambda count, pair: count + pair[0] * (10 - pair[1])


def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    nums = list(isbn)
    # The last character only can be 'X'. Map 'X' => 10
    if nums[-1] == 'X':
        nums[-1] = '10'
    if not all(num.isdigit() for num in nums):
        return False
    ints = (int(num) for num in nums)

    count = sum((10 - i) * num for i, num in enumerate(ints))
    # count = reduce(reduction, zip(ints, range(10)), 0)
    return count % 11 == 0
