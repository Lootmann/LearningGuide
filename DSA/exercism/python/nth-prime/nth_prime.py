def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    if True in (number == 2, number == 3):
        return True

    if True in (number % 2 == 0, number % 3 == 0):
        return False

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


def prime(number: int) -> int:
    if number == 0:
        raise ValueError("there is no zeroth prime")

    if number == 1:
        return 2

    number -= 1
    num = 3

    while True:
        if is_prime(num):
            number -= 1

        if number == 0:
            break

        num += 2

    return num
