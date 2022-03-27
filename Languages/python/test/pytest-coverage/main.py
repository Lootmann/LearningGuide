def is_big(num: int) -> bool:
    return num > 10


def add(x: int, y: int) -> int:
    total = x + y
    if is_big(total):
        return 0
    return total


def sub(x: int, y: int) -> int:
    return x - y


def mul(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> int:
    if y == 0:
        return 0
    return x // y
