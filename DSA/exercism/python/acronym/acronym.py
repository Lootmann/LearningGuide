""" acronym.py

Convert a phrase to its acronym.
"""
import re


def abbreviate(words: str) -> str:
    res = []
    words = re.sub(r"[^a-zA-Z- \']", " ", words)

    for word in re.split(r"[ -]", words):
        if word:
            res.append(word[0])

    return "".join(map(lambda s: s.title()[0], res))
