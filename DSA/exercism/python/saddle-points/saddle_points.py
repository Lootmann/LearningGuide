def saddle_points(matrix: list) -> list:
    # validation
    if len(matrix) == 0:
        return []

    lengths = set()
    for row in matrix:
        lengths.add(len(row))

    if len(lengths) != 1:
        raise ValueError("irregular matrix")

    row_maxs = []
    for row in matrix:
        row_maxs.append(max(row))

    col_mins = []
    for i in range(len(matrix[0])):
        col_min = 99
        for j in range(len(matrix)):
            col_min = min(col_min, matrix[j][i])
        col_mins.append(col_min)

    result = []

    for r, row_max in enumerate(row_maxs):
        for c, col_min in enumerate(col_mins):
            if row_max == col_min:
                result.append({"row": r + 1, "column": c + 1})

    return result
