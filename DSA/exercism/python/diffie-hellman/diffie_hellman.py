import random


def is_prime(num: int) -> bool:
    if num in (2, 3):
        return True

    if 0 in (num % 2, num % 3):
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def private_key(p: int) -> int:
    """private_key

    return prime number which 1 < private_key(p) < p
    """
    # easy randomize
    start = random.randint(1, p)

    for num in range(start, p + 1):
        if is_prime(num):
            return num

    return -1


def public_key(p: int, g: int, private: int) -> int:
    """gen public_key

    s = B ** a mod p
    """
    if p == g:
        private = private_key(private)
    return (g**private) % p


def secret(p: int, public: int, private: int) -> int:
    """gen secret

    s = A ** b mod p
    """
    return (public**private) % p
