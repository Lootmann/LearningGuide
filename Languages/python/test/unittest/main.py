# main.py
import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Point"):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other: "Point"):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other: "Point"):
        # inner product
        return self.x * other.x + self.y * other.y

    def dist(self, other: "Point") -> float:
        # Euclid Distance
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def __str__(self):
        return f"({self.x}, {self.y})"
