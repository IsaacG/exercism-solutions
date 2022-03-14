def square(num: int) -> int:
    if not 0 < num <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (num - 1)


def total() -> int:
    return 2 ** 64 - 1
