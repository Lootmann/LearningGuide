import re


def cipher_text(plain_text: str) -> str:
    # cleaned text - remove spaces, punctuations and lowered
    plain_text = re.sub(r"[^\w]", "", plain_text.lower())

    # validation
    if plain_text == "" or len(plain_text) == 1:
        return plain_text

    # calc row, col
    row, col = 1, 1
    while True:
        if row * col >= len(plain_text):
            if col >= row and col - row <= 1:
                break

        if row == col:
            col += 1
        else:
            row += 1

    splitted = [plain_text[col * i : col * (i + 1)] for i in range(row)]

    # padding white space
    if len(splitted[-1]) != col:
        splitted[-1] += " " * (col - len(splitted[-1]))

    # concat string by vertically
    cipher = []
    for col in range(col):
        col_str = []
        for _, line in enumerate(splitted):
            col_str.append(line[col])
        cipher.append("".join(col_str))

    # merge splitted
    return " ".join(cipher)
