def main():
    n = int(input())

    rows = [list(input()) for _ in range(n)]

    for i in range(n):
        for row, col in zip(range(i + 1, n), range(i + 1, n)):
            if row == 0 or col == 0:
                continue

            top = rows[i][col]
            left = rows[row][i]

            if top == "W" and left == "L":
                continue
            if top == "L" and left == "W":
                continue
            if top == "D" and left == "D":
                continue

            print("incorrect")
            return

    print("correct")


if __name__ == "__main__":
    main()
