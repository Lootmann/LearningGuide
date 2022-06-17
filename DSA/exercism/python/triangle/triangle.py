from typing import List

TriangleSide = List[float]


def is_valid_triangle(func):
    def inner(sides: TriangleSide) -> bool:
        return sum(sides) > 2 * max(sides) and func(sides)

    return inner


@is_valid_triangle
def equilateral(sides: TriangleSide) -> bool:
    return sides[0] == sides[1] and sides[1] == sides[2]


@is_valid_triangle
def isosceles(sides: TriangleSide) -> bool:
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


@is_valid_triangle
def scalene(sides: TriangleSide) -> bool:
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
