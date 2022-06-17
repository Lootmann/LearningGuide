""" ./matching_brackets.py
ordinary stack computations
"""


def is_paired(input_string: str) -> bool:
    """is_paired
    Are input_string brackets valid pairs?

    :param input_string: str
    :return: bool
    """

    stack = []

    for ch in input_string:
        if ch in {"(", "{", "["}:
            stack.append(ch)

        elif ch in {")", "}", "]"}:
            if len(stack) == 0:
                return False

            top = stack.pop()

            if not top == "(" and ch == ")":
                return False

            if not top == "{" and ch == "}":
                return False

            if not top == "[" and ch == "]":
                return False

    return len(stack) == 0
