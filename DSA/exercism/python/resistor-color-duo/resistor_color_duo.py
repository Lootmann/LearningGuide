"""resistor_color_duo.py

In this exercise
you are going to create a helpful program
so that you don't have to remember the values of the bands.
"""

from typing import List


def color(color_name: str) -> int:
    """color()

    Args:
        color_name (str): color name

    Returns:
        int: color code
    """
    if color_name == "black":
        return 0
    if color_name == "brown":
        return 1
    if color_name == "red":
        return 2
    if color_name == "orange":
        return 3
    if color_name == "yellow":
        return 4
    if color_name == "green":
        return 5
    if color_name == "blue":
        return 6
    if color_name == "violet":
        return 7
    if color_name == "grey":
        return 8
    # white
    return 9


def value(colors: List[str]) -> int:
    """value

    Args:
        colors (List[str]): list of color names

    Returns:
        int: color name bands
    """
    return 10 * color(colors[0]) + color(colors[1])
