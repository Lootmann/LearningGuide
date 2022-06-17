def square_of_sum(number: int):
    total = sum(range(number + 1))
    return total**2


def sum_of_squares(number: int):
    total = 0
    for num in range(number + 1):
        total += num**2
    return total


def difference_of_squares(number: int):
    return square_of_sum(number) - sum_of_squares(number)
