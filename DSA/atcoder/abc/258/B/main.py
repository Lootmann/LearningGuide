def main():
    n = int(input())
    matrix = []

    for _ in range(n):
        line = input()
        matrix.append(list(line + line))

    matrix += matrix[0 : len(matrix)]

    ans = 0

    row_range = len(matrix)
    col_range = len(matrix[0])

    # horizontal
    for row in range(row_range):
        for col in range(col_range - n + 1):
            line = matrix[row][col : col + n]
            ans = max(ans, int("".join(line[::-1])))
            ans = max(ans, int("".join(line)))

    # vertical
    for col in range(col_range):
        for row in range(row_range - n + 1):
            line = [matrix[row + i][col] for i in range(n)]
            ans = max(ans, int("".join(line)))
            ans = max(ans, int("".join(line[::-1])))

    # diagonal
    ## top-left bottom-right
    for row in range(row_range - n + 1):
        for col in range(col_range - n + 1):
            line = [matrix[row + i][col + i] for i in range(n)]
            ans = max(ans, int("".join(line)))
            ans = max(ans, int("".join(line[::-1])))

    ## top-right bottom-left
    for row in range(n, row_range):
        for col in range(col_range - n + 1):
            line = [matrix[row - i][col + i] for i in range(n)]
            ans = max(ans, int("".join(line)))
            ans = max(ans, int("".join(line[::-1])))

    print(ans)


if __name__ == "__main__":
    main()
