"""rail_fence_cipher.py

Implement encoding and decoding for the rail fence cipher.
"""


class Counter:
    def __init__(self, rail: int):
        self.rail = rail - 1
        self.cnt = -1
        self.is_increase = True

    def next(self) -> int:
        if self.is_increase:
            if self.cnt >= self.rail:
                self.cnt -= 1
                self.is_increase = False
            else:
                self.cnt += 1
        else:
            if self.cnt == 0:
                self.cnt += 1
                self.is_increase = True
            else:
                self.cnt -= 1

        return self.cnt

    def current(self) -> int:
        return self.cnt


def encode(message: str, rails: int) -> str:
    c = Counter(rail=rails)
    result = [""] * rails

    for ch in message:
        result[c.next()] += ch

    return "".join(result)


def rail_number(pos: int, rails: int) -> int:
    pos = pos % (rails * 2 - 2)
    if pos < rails:
        return pos
    else:
        return 2 * rails - pos - 2


def decode(encoded_message: str, rails: int) -> str:
    size = len(encoded_message)
    result = ["" for _ in range(size)]
    idx = 0

    for i in range(rails):
        for j in range(size):
            if i == rail_number(j, rails):
                result[j] = encoded_message[idx]
                idx += 1

    return "".join(result)
