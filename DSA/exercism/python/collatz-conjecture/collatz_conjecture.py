def steps(number: int) -> int:
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    cnt = 0

    while number > 1:
        cnt += 1
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1

    return cnt
