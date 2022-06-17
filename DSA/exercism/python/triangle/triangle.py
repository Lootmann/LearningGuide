from typing import List

TriangleSide = List[float]


def is_triangle(sides: TriangleSide) -> bool:
    sides.sort()

    if 0 in sides:
        return False

    if sides[0] + sides[1] < sides[2]:
        return False

    return True


def equilateral(sides: TriangleSide) -> bool:
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides: TriangleSide) -> bool:
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


def scalene(sides: TriangleSide) -> bool:
    if not is_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
