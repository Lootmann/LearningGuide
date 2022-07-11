"""affine_cipher.py
Create an implementation of the affine cipher,
an ancient encryption system created in the Middle East.
"""
from string import digits


def idx(char: str) -> int:
    return ord(char) - ord("a")


def m() -> int:
    return ord("z") - ord("a")


def validation(a: int) -> None:
    num = 26
    idx = 2
    primes = set()

    while num >= idx:
        if num % idx == 0:
            primes.add(idx)
            num //= idx
        else:
            idx += 1

    idx = 2
    while a >= idx:
        if a % idx == 0:
            if idx in primes:
                raise ValueError("a and m must be coprime.")
            a //= idx
        else:
            idx += 1


def is_digit(ch: str) -> bool:
    return ch in set(digits)


def encode(plain_text: str, a: int, b: int) -> str:
    """
    E(x) = (ai + b) mod m
    """

    def E(a, ch, b, m) -> int:
        letter_index = ord(ch) - ord("a")
        return (a * letter_index + b) % m + ord("a")

    validation(a)

    res = ""
    for ch in plain_text:
        if ch.isalpha():
            x = chr(E(a, ch.lower(), b, 26))
            res += x
        elif is_digit(ch):
            res += ch

    r = range((len(res) + 4) // 5)
    return " ".join([res[5 * i : 5 * i + 5] for i in r])


def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


def mmi(a: int, m: int) -> int:
    d, x, _ = extgcd(a, m)
    if d != 1:
        return -1
    return x % m


def decode(ciphered_text: str, a: int, b: int) -> str:
    """
    D(y) = (a^-1)(y - b) mod m
    """

    def D(a_inverse, y, b, m) -> int:
        """
        D(y) = (a^-1)(y - b) mod m
        """
        return a_inverse * (y - b) % m + ord("a")

    validation(a)

    res = []
    for ch in ciphered_text:
        if ch.isalpha():
            a_inverse = mmi(a, 26)
            x = D(a_inverse, ord(ch) - ord("a"), b, 26)
            res.append(chr(x))
        elif "0" <= ch <= "9":
            res.append(ch)
        else:
            pass

    return "".join(res)
