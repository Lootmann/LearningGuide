def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    divs = set()
    for n in range(1, int(number**0.5) + 1):
        if number % n == 0:
            divs.add(n)
            if n != 1:
                divs.add(number // n)

    total = sum(divs)

    if total == number:
        return "perfect"

    elif total > number:
        return "abundant"

    else:
        return "deficient"
