""" sum_of_multiples.py

Given a number, find the sum of all the unique multiples of particular
numbers up to but not including that number.
"""


def sum_of_multiples(limit, multiples) -> int:
    """sum_of_multiples

    :param limit: int
    :param multiples: List[int]
    :return: int - sum of multiples
    """
    total = set()

    # calc O(N * M)
    for num in range(limit):
        for mul in multiples:
            if mul != 0 and num % mul == 0:
                total.add(num)

    return sum(total)
