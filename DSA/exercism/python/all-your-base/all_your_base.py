"""all_your_base.py
Convert a number, represented as a sequence of digits in one base,
to any other base.

Implement general base conversion. Given a number in base **a**,
represented as a sequence of digits, convert it to base **b**.
"""


def rebase(input_base: int, digits: list, output_base: int) -> list:
    """rebase

    :param input_base: int
    :param digits: list
    :param output_base: int

    :return: list
    """
    # validations
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any(map(lambda n: n < 0 or input_base <= n, digits)):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    total = 0
    weight = len(digits) - 1

    # convert input_base to decimal
    for digit in digits:
        total += digit * input_base**weight
        weight -= 1

    weight = 1
    while total > weight * output_base:
        weight *= output_base

    # convert decimal to output_base
    result = []

    while weight > 0:
        result.append(total // weight)
        total %= weight
        weight //= output_base

    return result
