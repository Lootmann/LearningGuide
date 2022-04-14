import math
import unittest
from unittest import TestCase


def circle_area(radius: float) -> float:
    return math.pi * radius**2


class TestLambda(TestCase):
    def test_circle_area(self):
        got = circle_area(3)

        circle_area_λ = lambda radius: math.pi * radius**2
        want = circle_area_λ(3)

        self.assertEqual(got, want)


class TestMap(TestCase):
    def test_map(self):
        got = list(map(lambda x: x**2, range(10)))
        want = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        self.assertListEqual(got, want)


class TestFilter(TestCase):
    def test_filter(self):
        got = list(filter(lambda n: n % 2 == 0, range(10)))
        want = [0, 2, 4, 6, 8]
        self.assertListEqual(got, want)


class TestReduce(TestCase):
    def test_reduce(self):
        from functools import reduce

        got = reduce(lambda a, b: a + b, range(11))
        want = 55
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
