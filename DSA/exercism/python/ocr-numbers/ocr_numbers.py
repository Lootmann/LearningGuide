from typing import List


def grid_to_number(grid: list) -> str:
    """grid_to_number

    grid = [
        " _ ",
        "| |",
        "|_|",
    ]

    return 0

    :param grid: list
    :return: str
    """
    if len(grid) != 4:
        raise ValueError("Number of input lines is not a multiple of four")

    if grid[0] == " _ " and grid[1] == "| |" and grid[2] == "|_|":
        return "0"

    if grid[0] == "   " and grid[1] == "  |" and grid[2] == "  |":
        return "1"

    if grid[0] == " _ " and grid[1] == " _|" and grid[2] == "|_ ":
        return "2"

    if grid[0] == " _ " and grid[1] == " _|" and grid[2] == " _|":
        return "3"

    if grid[0] == "   " and grid[1] == "|_|" and grid[2] == "  |":
        return "4"

    if grid[0] == " _ " and grid[1] == "|_ " and grid[2] == " _|":
        return "5"

    if grid[0] == " _ " and grid[1] == "|_ " and grid[2] == "|_|":
        return "6"

    if grid[0] == " _ " and grid[1] == "  |" and grid[2] == "  |":
        return "7"

    if grid[0] == " _ " and grid[1] == "|_|" and grid[2] == "|_|":
        return "8"

    if grid[0] == " _ " and grid[1] == "|_|" and grid[2] == " _|":
        return "9"

    return "?"


def split_grid(input_grid: list) -> List[List[str]]:
    """split_grid

    input_grid = [
        "    _ ",
        "  | _|",
        "  ||_ ",
        "      ",
    ]

    [
        [ "   ", "  |", "  |", "   ", ],
        [ " _ ", " _|", "|_ ", "   ", ],
    ]

    :param input_grid: List
    :return: List[List]
    """
    res = []
    for line in input_grid:
        row = []
        for i in range((len(line) + 2) // 3):
            row.append(line[3 * i : 3 * (i + 1)])
        res.append(row)
    return res


def join_digits(grid: List) -> List:
    """join_digits

    grid = [
        [ " _ ", " _|", " _|", "   ", ],
        [ " _ ", "| |", "|_|", "   ", ]
    ]

    return "30"

    :param grid: list
    :return: list
    """
    numbers = []
    for i in range(len(grid[0])):
        num = []
        for line in grid:
            num.append(line[i])

        numbers.append(num)

    result = []

    for number in numbers:
        result.append(grid_to_number(number))

    return result


def convert(input_grid: list) -> str:
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    # one char
    if len(input_grid[0]) == 3:
        return grid_to_number(input_grid)

    # vertical splitted
    result = []

    if len(input_grid) > 4:
        grids = []

        for i in range(len(input_grid[0]) // 3):
            row = input_grid[4 * i : 4 * i + 4]
            grids.append(row)

        for grid in grids:
            chunks = []

            for line in grid:
                chunks.append(line)

            got = split_grid(chunks)
            one_line = join_digits(got)

            result.append("".join(one_line))

        return ",".join(result)

    # normal
    got = split_grid(input_grid)
    result = join_digits(got)

    return "".join(result)
