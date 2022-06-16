""" ispangram.py
A pangram is a sentence using every letter of the alphabet at least once.

You should Implement this function named 'is_pangra'
"""
import string


def is_pangram(sentence: str) -> bool:
    """check 'sentence' is pangram
    The UnReadable oneliner. this has few bugs I think.

    :param sentence: str
    :return: bool
    """
    return set(map(lambda x: x.lower(), list(sentence))) >= set(string.ascii_lowercase)
