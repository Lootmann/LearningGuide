def is_rectangles(strings: list, r: int, c: int, r_i: int, c_i: int) -> bool:
    for col in range(c, c_i + 1):
        if strings[r][col] in ("|", " "):
            return False
        if strings[r_i][col] in ("|", " "):
            return False

    for row in range(r, r_i + 1):
        if strings[row][c] in ("-", " "):
            return False
        if strings[row][c_i] in ("-", " "):
            return False

    return True


def rectangles(strings: list) -> int:
    if len(strings) <= 1:
        return 0

    col_max = len(strings[0])
    row_max = len(strings)

    plus_indexes = []

    for row, line in enumerate(strings):
        for col, ch in enumerate(line):
            if ch == "+":
                plus_indexes.append((row, col))

    cnt = 0
    for row, col in plus_indexes:
        for col_i in range(col + 1, col_max):
            if strings[row][col_i] == "+":
                for row_i in range(row + 1, row_max):
                    if strings[row_i][col] == "+" and strings[row_i][col_i] == "+":
                        if is_rectangles(strings, row, col, row_i, col_i):
                            cnt += 1

    return cnt
