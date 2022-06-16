""" score
Write a function that returns the earned points in a single toss of a Darts game.
"""
import math


def score(x: float, y: float) -> int:
    """
    :param x: float - distance from inner point
    :param y: float - distance from inner point

    :return: int - darts score
    """
    eps = 1e-3
    dist = math.sqrt(x**2 + y**2)

    if dist - 1.0 <= eps:
        return 10

    if dist - 5.0 <= eps:
        return 5

    if dist - 10.0 <= eps:
        return 1

    return 0
