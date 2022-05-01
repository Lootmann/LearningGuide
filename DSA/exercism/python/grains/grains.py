"""Caluculate grains"""


def square(number: int) -> int:
    """square number

    Args:
        number: int - num of grains
    Returns:
        int - number * number
    Exceptions:
        raise Exception when number < number or 64 < number
    """
    if number < 1 or 64 < number:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    """total num of grains

    Args:
        None
    Returns:
        int - sum squares of num of grains

        2**1 + 2**2 + 2**3 + ... + 2**63

        00000000001(2)
        00000000010(2)
        00000000100(2)
        ...
        10000000000(2)
        -----------
        11111111111(2) means 100000000000 - 1 = 2**64 - 1

    """
    return 2**64 - 1
