""" twelve_days.py

Your task in this exercise is to write code that returns the lyrics of the song:
'The Twelve Days of Christmas.'
"""
from typing import List


def format_header(day: int) -> str:
    """format_header

    Args:
        day (int): 1 - 12

    Returns:
        str: a lyrics of header
    """
    header = "On the {} day of Christmas my true love gave to me:"

    if day == 1:
        ordinal = "first"
    elif day == 2:
        ordinal = "second"
    elif day == 3:
        ordinal = "third"
    elif day == 4:
        ordinal = "fourth"
    elif day == 5:
        ordinal = "fifth"
    elif day == 6:
        ordinal = "sixth"
    elif day == 7:
        ordinal = "seventh"
    elif day == 8:
        ordinal = "eighth"
    elif day == 9:
        ordinal = "ninth"
    elif day == 10:
        ordinal = "tenth"
    elif day == 11:
        ordinal = "eleventh"
    else:
        ordinal = "twelfth"

    return header.format(ordinal)


def create_verse(verse_index: int) -> str:
    """create verse

    Args:
        verse_index (int): 1 - 12

    Returns:
        str: verse by days
    """
    header = format_header(verse_index)

    lists = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves,",
        "three French Hens,",
        "four Calling Birds,",
        "five Gold Rings,",
        "six Geese-a-Laying,",
        "seven Swans-a-Swimming,",
        "eight Maids-a-Milking,",
        "nine Ladies Dancing,",
        "ten Lords-a-Leaping,",
        "eleven Pipers Piping,",
        "twelve Drummers Drumming,",
    ]

    result = [header]

    verse_index -= 1

    if verse_index == 0:
        result.append(lists[verse_index])
    else:
        for i in range(verse_index, 0, -1):
            result.append(lists[i])

        result.append("and " + lists[0])

    return " ".join(result)


def recite(start_verse: int, end_verse: int) -> List[str]:
    """recite

    Args:
        start_verse (int): 1 - 12
        end_verse (int): 1 - 12

    Returns:
        List[str]: a list of verses
    """

    result = []

    for i in range(start_verse, end_verse + 1):
        result.append(create_verse(i))

    return result
