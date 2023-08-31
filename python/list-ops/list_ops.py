import typing

S = typing.TypeVar("S")
T = typing.TypeVar("T")

def append(list1: list[T], list2: list[T]) -> list[T]:
    return list1 + list2


def concat(lists: list[list[T]]) -> list[T]:
    result = []
    for l in lists:
        result.extend(l)
    return result


def filter(function: typing.Callable[[T], bool], a_list: list[T]) -> list[T]:
    return [i for i in a_list if function(i)]


def length(a_list: list[T]) -> int:
    return sum(1 for _ in a_list)


def map(function: typing.Callable[[S], T], a_list: list[S]) -> list[T]:
    return [function(i) for i in a_list]


def foldl(function: typing.Callable[[T, S], T], a_list: list[S], initial: T) -> T:
    result = initial
    for i in a_list:
        result = function(result, i)
    return result


def foldr(function: typing.Callable[[T, S], T], a_list: list[S], initial: T) -> T:
    return foldl(function, reverse(a_list), initial)


def reverse(a_list: list[T]) -> list[T]:
    return list(reversed(a_list))
