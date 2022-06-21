"""say.py

Given a number from 0 to 999,999,999,999, spell out that number in English.
"""


def fixed_call(number: int) -> str:
    return {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
        1000000: "million",
        1000000000: "billion",
    }.get(number, "***" * 10)


def three_digit_call(number: int) -> str:
    """convert number to spell out in English
    :param number: int
    :return: str
    """
    if not 0 <= number <= 999:
        raise ValueError("WTF")

    if 0 <= number <= 19:
        return fixed_call(number)

    call = []

    # digit 3
    if number >= 100:
        call.append(fixed_call(number // 100) + " " + fixed_call(100))
        number %= 100

    # digit 2
    if number >= 10:
        # 20 - 99
        call.append(fixed_call(number // 10 * 10))
        number %= 10

        if number != 0:
            call[-1] += "-" + fixed_call(number)

    return " ".join(call)


def digit_split(number: int) -> list:
    digits = ["", "thousand", "million", "billion"]

    result = []

    if number < 1_000:
        result.append((number, digits[0]))

    elif number < 1_000_000:
        result.append((number // 1000, digits[1]))
        result.append((number % 1000, digits[0]))

    elif number < 1_000_000_000:
        result.append((number // 1_000_000, digits[2]))
        number %= 1_000_000
        result.append((number // 1000, digits[1]))
        number %= 1_000
        result.append((number % 1000, digits[0]))

    elif number < 1_000_000_000_000:
        result.append((number // 1_000_000_000, digits[3]))
        number %= 1_000_000_000
        result.append((number // 1_000_000, digits[2]))
        number %= 1_000_000
        result.append((number // 1000, digits[1]))
        number %= 1_000
        result.append((number % 1000, digits[0]))

    else:
        result.append((number // 1_000_000_000_000, digits[3]))

    return result


def say(number: int) -> str:
    """say
    Given a number from 0 to 999,999,999,999 spell out that number in English.

    :param number: int
    :return: str
    """
    # validation
    if number < 0 or 999_999_999_999 < number:
        raise ValueError("input out of range")

    if 0 <= number <= 19:
        return fixed_call(number)

    result = []

    for chunk, digit in digit_split(number):
        if chunk != 0:
            if digit == "":
                result.append(three_digit_call(chunk))
            else:
                result.append(three_digit_call(chunk) + " " + digit)

    return " ".join(result)
