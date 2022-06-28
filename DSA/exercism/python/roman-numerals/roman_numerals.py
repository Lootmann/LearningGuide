""" roman_numerals.py

Write a function to convert from normal numbers to Roman Numerals.
"""
from collections import OrderedDict


def num_to_roman(num: int) -> str:
    """num_to_roman

    :param num: int - decimal number
    :return: str - roman
    """
    d = OrderedDict(
        {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
    )

    res = []
    while num > 0:
        for k, v in d.items():
            if num >= k:
                res.append(v)
                num -= k
                break

    return "".join(res)


def roman(number: int) -> str:
    """roman

    :param number: int
    :return: str - roman number
    """
    digits = []
    for i, ch in enumerate(reversed(str(number))):
        digits.append(int(ch + "0" * i))

    res = []
    for digit in reversed(digits):
        res.append(num_to_roman(digit))

    return "".join(res)
