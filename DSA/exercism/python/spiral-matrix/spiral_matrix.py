"""spiral_matrix.py

Give the size, return a square matrix of numbers in spiral order.
"""


def spiral_matrix(size: int) -> list:
    matrix = [[0] * size for _ in range(size)]

    if size == 0:
        return matrix

    x, y = 0, 0

    x_low_lim = 0
    x_upp_lim = size - 1
    y_low_lim = 1
    y_upp_lim = size - 1

    # O(size^2)
    number = 1
    matrix[y][x] = number

    loop_count = 2 * size

    while True:
        # x++
        while x < x_upp_lim:
            matrix[y][x] = number
            number += 1
            x += 1
        x_upp_lim -= 1
        loop_count -= 1
        if loop_count == 0:
            break

        # y++
        while y < y_upp_lim:
            matrix[y][x] = number
            number += 1
            y += 1
        y_upp_lim -= 1
        loop_count -= 1
        if loop_count == 0:
            break

        # x--
        while x_low_lim < x:
            matrix[y][x] = number
            number += 1
            x -= 1
        x_low_lim += 1
        loop_count -= 1
        if loop_count == 0:
            break

        # y--
        while y_low_lim < y:
            matrix[y][x] = number
            number += 1
            y -= 1
        y_low_lim += 1
        loop_count -= 1
        if loop_count == 0:
            break

    matrix[y][x] = number

    return matrix
