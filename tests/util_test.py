import unittest
import numpy as np
from physics.utils import get_distance
from physics.objects.Object import Object


class getDistanceTest(unittest.TestCase):
    def test_basic_x_dist(self):
        obj = Object(1, [0, 0])
        obj2 = Object(1, [5, 0])

        dist = get_distance(obj, obj2)

        # dx = 5, dy = 0
        self.assertAlmostEqual(dist, 5)

    def test_basic_y_dist(self):
        obj = Object(1, [0, 0])
        obj2 = Object(1, [0, 5])

        dist = get_distance(obj, obj2)

        # dx = 0, dy = 5
        self.assertAlmostEqual(dist, 5)

    def test_x_and_y_diff_1(self):
        obj = Object(1, [4, 0])
        obj2 = Object(1, [0, 3])

        dist = get_distance(obj, obj2)

        # 3, 4, 5 triangle
        self.assertAlmostEqual(dist, 5)

    def test_x_and_y_diff_2(self):
        obj = Object(1, [-10, 0])
        obj2 = Object(1, [5, -6])

        dist = get_distance(obj, obj2)

        # dx = 15, dy = 6
        expected = np.sqrt(225 + 36)

        self.assertAlmostEqual(dist, expected)

    def test_x_and_y_diff_3(self):
        obj = Object(1, [1, -1])
        obj2 = Object(1, [0, -2])

        dist = get_distance(obj, obj2)

        # dx = 1, dy = 1
        expected = np.sqrt(2)

        self.assertAlmostEqual(dist, expected)


if __name__ == "__main__":
    unittest.main()
