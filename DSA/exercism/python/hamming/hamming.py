def distance(strand_a: str, strand_b: str) -> int:
    """distance
    calc hamming distance

    :param strand_a: str
    :param strand_b: str
    :return: int - a num of hamming distance.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    cnt = 0

    for i, ch in enumerate(strand_a):
        if ch != strand_b[i]:
            cnt += 1

    return cnt
