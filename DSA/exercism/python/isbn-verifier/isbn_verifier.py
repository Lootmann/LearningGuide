import re


def is_valid(isbn: str) -> bool:
    """is_valid

    :param isbn: str
    :return: bool - return True if isbn is True
    """
    # strip '-'
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    total = 0

    # TODO: repcae Regex re.search or re.match
    for weight, ch in enumerate(isbn):
        if ch == "X":
            total += 10
        elif "0" <= ch <= "9":
            total += int(ch) * (10 - weight)
        else:
            return False

    return total % 11 == 0
