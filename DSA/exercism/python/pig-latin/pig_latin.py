""" ./pig_latin.py
"""


def is_vowel(ch: str) -> bool:
    return ch in ("a", "e", "i", "o", "u")


def is_consonant(ch: str) -> bool:
    return not is_vowel(ch)


def is_rule4(word: str) -> bool:
    y_pos = word.find("y")

    if y_pos in (-1, 0):
        return False

    cnt = 0
    for ch in word:
        if is_consonant(ch) and ch != "y":
            cnt += 1
        else:
            break

    return y_pos == cnt


def pignize(word: str) -> str:
    # Rule 1
    if is_vowel(word[0]) or word[:2] in ("xr", "yt"):
        return word + "ay"

    # Rule 3
    if is_consonant(word[0]) and word[1:3] == "qu":
        return word[3:] + word[:3] + "ay"

    if word[0:2] == "qu":
        return word[2:] + word[:2] + "ay"

    # Rule 4
    if is_rule4(word):
        idx = word.index("y")
        return word[idx:] + word[0:idx] + "ay"

    # Rule 2
    if is_consonant(word[0]):
        idx = 0
        for i, ch in enumerate(word):
            if is_consonant(ch):
                idx = i
            else:
                break

        return word[idx + 1 :] + word[0 : idx + 1] + "ay"

    return word


def translate(text: str) -> str:
    converted = []

    for word in text.split():
        converted.append(pignize(word))

    return " ".join(converted)
