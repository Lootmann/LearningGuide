def is_prime(num: int) -> bool:
    if num in (2, 3):
        return True

    if num == 1:
        return False

    if 0 in (num % 2, num % 3):
        return False

    for n in range(3, int(num**0.5) + 1, 2):
        if num % n == 0:
            return False

    return True


def primes(limit: int) -> list:
    """primes

    Find primes

    NOTE:
        Where does this code use the sieve of Eratosthenes?

    :param int: limit
    :return: list - a lists of primes
    """
    res = []

    if limit <= 1:
        return res

    for num in range(1, limit + 1):
        if is_prime(num):
            res.append(num)

    return res
