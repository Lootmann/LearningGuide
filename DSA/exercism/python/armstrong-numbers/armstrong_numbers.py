""" Armstrong Number

An [Armstrong number](https://en.wikipedia.org/wiki/Narcissistic_number)
is a number that is the sum of its own digits each raised
to the power of the number of digits.
"""
from typing import Generator


def number_digits(number: int) -> int:
    """calc number of digits
    len(str(number)) is same returns I think.

    :param number:int
    :return:  int - number of digits
    """
    cnt = 0
    while number > 0:
        cnt += 1
        number //= 10
    return cnt


def gen(number: int) -> Generator:
    """generate each number
    :param number: int
    :return: int
    """
    while number > 0:
        yield number % 10
        number //= 10


def is_armstrong_number(number: int) -> bool:
    """check an arg named number is Armstrong Number

    :param number: int
    :return: bool
    """
    digits = number_digits(number)
    result = 0

    for num in gen(number):
        result += num**digits

    return number == result
