def append(list1: list, list2: list) -> list:
    for num in list2:
        list1.append(num)
    return list1


def concat(lists: list) -> list:
    res = []
    for obj in lists:
        if type(obj) is list:
            for elem in obj:
                res.append(elem)
        else:
            res.append(obj)

    return res


def filter(func, lst: list):
    result = []
    for num in lst:
        if func(num):
            result.append(num)
    return result


def length(lst: list):
    return len(lst)


def map(function, list: list) -> list:
    return [function(num) for num in list]


def foldl(function, lst, initial):
    for num in lst:
        initial = function(num, initial)
    return initial


def foldr(function, lst, initial):
    for elem in reversed(lst):
        initial = function(elem, initial)
    return initial


def reverse(lst: list) -> list:
    return lst[::-1]
