MASK = 0b_0111_1111
MSB = 0b_1000_0000


def encode(numbers: list) -> list:
    print("MSB :", MSB)

    bits = []
    for number in numbers[::-1]:
        msb = 0
        while True:
            bits.insert(0, (number & MASK) | msb)
            msb = MSB
            number >>= 7
            if number == 0:
                break

    return bits


def decode(bytes_: list) -> list:
    res = []

    bytes = 0
    for b in bytes_:
        bytes = (bytes << 7) + (b & MASK)
        if b & MSB == 0:
            res.append(bytes)
            bytes = 0
    else:
        if b & MSB != 0:  # type: ignore
            raise ValueError("incomplete sequence")

    return res
