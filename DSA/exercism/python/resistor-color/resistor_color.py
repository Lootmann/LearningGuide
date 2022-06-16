""" resistor_color.py

Implement a function to create a helpful program
so that you don't have to remember the values of the bands.
"""
from typing import List


def color_code(color: str) -> int:
    """color_code

    Args:
        color (str): color name

    Returns:
        int: color code
    """
    if color == "black":
        return 0
    if color == "brown":
        return 1
    if color == "red":
        return 2
    if color == "orange":
        return 3
    if color == "yellow":
        return 4
    if color == "green":
        return 5
    if color == "blue":
        return 6
    if color == "violet":
        return 7
    if color == "grey":
        return 8
    if color == "white":
        return 9
    return -1


def colors() -> List[str]:
    """colors()

    Returns:
        List[str]: list of color_codes
    """
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
