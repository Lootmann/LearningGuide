from string import ascii_uppercase


def rows(letter):
    letters = list(ascii_uppercase)
    count = letters.index(letter)
    countrow = 0
    rows = []

    for irow in range(0, count * 2 + 1):
        row = []

        for i in range(0, count * 2 + 1):
            # left , right
            if i == count - countrow or i == count + countrow:
                row.append(letters[countrow])
            else:
                row.append(" ")

        rows.append("".join(row))

        if irow < count:
            countrow = countrow + 1

        elif irow >= count:
            countrow = countrow - 1

    return rows
