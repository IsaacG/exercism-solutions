def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for l in lists:
        result.extend(l)
    return result


def filter(function, a_list):
    return [i for i in a_list if function(i)]


def length(a_list):
    return len(a_list)


def map(function, a_list):
    return [function(i) for i in a_list]


def foldl(function, a_list, initial):
    result = initial
    for i in a_list:
        result = function(result, i)
    return result


def foldr(function, a_list, initial):
    result = initial
    for i in reversed(a_list):
        result = function(i, result)
    return result


def reverse(a_list):
    return list(reversed(a_list))
