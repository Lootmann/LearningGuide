def mul(series: str) -> int:
    res = 1
    for num in series:
        res *= int(num)
    return res


def largest_product(series: str, size: int) -> int:
    """
    size = 3

    0 1 2 3 4 5 6 7 8 9 10
    ----------------------
    1 2 3 4 5 0 5 4 3 2 1
    1 2 3 x x x x x 3 2 1
    """
    if size == 0:
        return 1

    if size < 0:
        raise ValueError("span must not be negative")

    if len(series) < size:
        raise ValueError("span must be smaller than string length")

    if not all([x.isdigit() for x in list(series)]):
        raise ValueError("digits input must only contain digits")

    if len(series) == size:
        return mul(series)

    res = 0
    for i in range(len(series) - size + 1):
        res = max(res, mul(series[i : i + size]))

    return res
