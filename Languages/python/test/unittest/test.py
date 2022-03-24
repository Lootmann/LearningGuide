# test.py
import math
import unittest

from main import Point


class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point(1, 2)
        self.assertEqual(str(p), "(1, 2)")

    def test_add(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertEqual(str(p1 + p2), "(3, 5)")

    def test_sub(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertEqual(str(p1 - p2), "(-1, -1)")

    def test_mul_inner_product(self):
        p1 = Point(3, 2)
        p2 = Point(2, 1)
        self.assertEqual(p1 * p2, 8)

    def test_dist_euclid_distance(self):
        p1 = Point(0, 0)
        p2 = Point(1, 1)
        self.assertAlmostEqual(p1.dist(p2), 1.41421356, places=8)

    def test_dist_euclid_distance1(self):
        p1 = Point(0, 0)
        p2 = Point(2, 2)
        self.assertAlmostEqual(p1.dist(p2), 2.828427124, places=8)


if __name__ == "__main__":
    unittest.main()
