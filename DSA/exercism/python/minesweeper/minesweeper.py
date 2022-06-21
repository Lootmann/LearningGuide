def count_mine(y: int, x: int, field: list) -> str:
    y_lim = len(field)
    x_lim = len(field[0])

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0

    for (yi, xi) in zip(dy, dx):
        cur_y = y + yi
        cur_x = x + xi

        if 0 <= cur_y < y_lim and 0 <= cur_x < x_lim:
            if field[cur_y][cur_x] == "*":
                cnt += 1

    if cnt == 0:
        return " "

    return str(cnt)


def annotate(minefield: list) -> list:
    # minefield validation
    if minefield == []:
        return []

    if len(set([len(row) for row in minefield])) != 1:
        raise ValueError("The board is invalid with current input.")

    result = []

    for y, row in enumerate(minefield):
        row_result = []

        for x, cell in enumerate(row):
            if cell == " ":
                row_result.append(count_mine(y, x, minefield))
            elif cell == "*":
                row_result.append("*")
            else:
                raise ValueError("The board is invalid with current input.")

        result.append("".join(row_result))

    return result
