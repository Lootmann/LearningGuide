from typing import List, Tuple

Factor = Tuple[int, List[List[int]]]


def create_iterable(num: int, small: int, large: int) -> List[List[int]]:
    print(num, small, large)

    result = []

    i = 1
    while i * i <= num:
        div, mod = divmod(num, i)
        if mod == 0 and (small <= div <= large) and (small <= num // div <= large):
            result.append([div, num // div])
        i += 1

    return result


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def largest(min_factor=0, max_factor=0):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    max_product = -1
    factor_list = []

    for left_factor in range(max_factor, min_factor - 1, -1):
        for right_factor in range(max_factor, left_factor - 1, -1):
            next_product = left_factor * right_factor

            if max_product < next_product:
                if is_palindrome(next_product):
                    max_product = next_product
                    factor_list = []

            if max_product == next_product:
                factor_list.append([left_factor, right_factor])

            if max_product > next_product:
                break

    if factor_list == []:
        return (None, [])

    return (max_product, factor_list)


def smallest(min_factor: int, max_factor: int) -> Factor:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    for n1 in range(min_factor, max_factor + 1):
        for n2 in range(min_factor, max_factor + 1):
            if is_palindrome(n1 * n2):
                return (n1 * n2, create_iterable(n1 * n2, min_factor, max_factor))

    return (None, [])
