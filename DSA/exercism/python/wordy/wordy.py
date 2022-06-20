"""wordy.py

Parse and evaluate simple math word problems returning the answer as an integer.
"""


def is_operation(token: str) -> bool:
    """is_operation

    :param token: - str
    :return: bool
    """
    return token in ("plus", "minus", "multiplied", "divided")


def convert(left: str, op: str, right: str) -> int:
    """convert

    :param left:  - str: operand
    :param op:    - str: operation
    :param right: - str: operand
    :return: - int
    """
    if not is_operation(op):
        raise ValueError("syntax error")

    try:
        int(left)
        int(right)
    except:
        raise ValueError("syntax error")

    if op == "plus":
        return int(left) + int(right)

    if op == "minus":
        return int(left) - int(right)

    if op == "multiplied":
        return int(left) * int(right)

    if op == "divided":
        return int(left) // int(right)

    return -9999


def calc(tokens: list) -> int:
    """calc simple math expression

    e.g.)
    1
    1 plus 1
    1 multiplied 2 multiplied 4

    valid tokens should be odd number of strings.

    :params tokens: list
    :return: int
    """
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")

    if len(tokens) == 1:
        return int(tokens[0])

    total = 0

    for i in range(0, (len(tokens) + 2) // 2, 2):
        if i == 0:
            total += convert(tokens[i], tokens[i + 1], tokens[i + 2])
        else:
            total = convert(str(total), tokens[i + 1], tokens[i + 2])

    return total


def answer(question: str) -> int:
    """answer

    :param question: str
    :return: int
    """
    question = question.strip("?")
    chunks = question.split(" ")[2:]

    convert = []

    # validation
    if len(chunks) == 0:
        raise ValueError("syntax error")

    for chunk in chunks:
        if is_operation(chunk):
            convert.append(chunk)
        elif chunk == "by":
            pass
        else:
            try:
                convert.append(int(chunk))
            except:
                raise ValueError("unknown operation")

    return calc(convert)
