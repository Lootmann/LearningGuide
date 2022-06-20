"""./isogram.py
Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase
without a repeating letter,
however spaces and hyphens are allowed to appear multiple times.
"""


def is_isogram(string: str) -> bool:
    """is_isogram

    :param string: str
    :return: bool - str is isogram
    """
    string = string.lower()
    string = string.replace("-", "").replace(" ", "")
    print(string)

    return len(string) == len(set(string))
