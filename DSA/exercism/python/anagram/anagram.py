""" find_anagrams

Find anagrams.
"""
from typing import List


def is_anagrams(word: str, candidate: str) -> bool:
    """is_anagrams

    :param word: str
    :return: bool - return True when word is anagram
    """
    return word.lower() != candidate.lower() and sorted(list(word.lower())) == sorted(
        list(candidate.lower())
    )


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """find_anagrams

    :param word: str
    :return:
    """
    anagrams = []

    for candidate in candidates:
        if is_anagrams(word, candidate):
            anagrams.append(candidate)

    return anagrams
