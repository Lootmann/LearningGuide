def slices(series: str, length: int) -> list:
    # validation
    if len(series) == 0:
        raise ValueError("series cannot be empty")

    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    res = []
    for i in range(len(series) - length + 1):
        res.append(series[i : i + length])

    return res
