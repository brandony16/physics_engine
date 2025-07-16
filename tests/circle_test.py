import unittest
from physics.objects.Circle import Circle


class CircleTest(unittest.TestCase):
    # Mass, position, and velocity are tested in the specific object test
    def setUp(self):
        self.m = 1
        self.p = [3, 2]

    # ----- INVALID INPUTS -----
    def test_invalid_radius(self):
        with self.assertRaises(TypeError) as e:
            Circle(self.m, [3, 5], self.p)
        self.assertEqual(str(e.exception), "Radius must be a number")

        with self.assertRaises(ValueError) as e:
            Circle(self.m, -2, self.p)
        self.assertEqual(str(e.exception), "Radius must be positive")

    # ----- VALID INPUTS -----
    def test_int_radius(self):
        circle = Circle(self.m, 2, self.p)

    def test_float_radius(self):
        circle = Circle(self.m, 2.5, self.p)

    # Currently 0 is allowed so point masses can exist
    def test_zero_radius(self):
        circle = Circle(self.m, 0, self.p)


if __name__ == "__main__":
    unittest.main()
