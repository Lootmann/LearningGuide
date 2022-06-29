def factors(value: int) -> list:
    res = []

    while value % 2 == 0:
        if value % 2 == 0:
            res.append(2)
            value //= 2

    for i in range(3, int(value**0.5) + 1, 2):
        while value % i == 0:
            res.append(i)
            value //= i

    if value != 1:
        res.append(value)

    return res
