"""bob.py

Responder to Bob.
"""


def has_letter(string: str) -> bool:
    """is_noletter
    check string has any letter
    letter is any of [a-zA-Z!?] char.

    >>> has_letter("")
    False
    >>> has_letter("?")
    True
    >>> has_letter("!")
    True
    >>> has_letter("     ")
    False
    >>> has_letter("\t\t")
    False

    :param string: str
    :return: bool
    """
    if len(string) == 0:
        return False

    if string[-1] == "?":
        return True

    for char in string:
        if char.isalnum():
            return True

    return False


def is_all_capital(string: str) -> bool:
    """is_capital
    check string is all capital or not

    >>> is_all_capital("A")
    True
    >>> is_all_capital("ABBB")
    True
    >>> is_all_capital("!1!!!!!")
    False
    >>> is_all_capital("??!?!A")
    True

    :param string: str
    :return: bool
    """
    has_any_letter = False
    for char in list(string):
        if char.isalpha():
            has_any_letter = True
            if char.islower():
                return False

    return True and has_any_letter


def response(hey_bob: str) -> str:
    """response
    response to bob

    :param hey_bob: str
    :return: str
    """
    hey_bob = hey_bob.strip()

    if not has_letter(hey_bob):
        return "Fine. Be that way!"

    has_question = hey_bob[-1] == "?"
    is_capital = is_all_capital(hey_bob)

    if is_capital:
        if has_question:
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    if has_question:
        return "Sure."

    return "Whatever."


if __name__ == "__main__":
    import doctest

    doctest.testmod()
