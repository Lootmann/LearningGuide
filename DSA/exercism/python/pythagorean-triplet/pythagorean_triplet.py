def triplets_with_sum(num: int) -> list:
    """
    a + b + c = num
    a^2 + b^2 = c^2

    :param num: int
    :return: list - (a, b, c) and a < b < c
    """
    result = []

    for a in range(0, num // 2):
        if (num**2 - 2 * num * a) % (2 * num - 2 * a) == 0:
            b = (num * num - 2 * num * a) // (2 * num - 2 * a)
            c = num - a - b

            if a * a + b * b == c * c and a < b < c:
                result.append([a, b, c])

    return result
