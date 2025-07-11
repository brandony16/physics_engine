import unittest
from physics.objects import Circle


class ObjectTest(unittest.TestCase):
    # Mass, position, and velocity are tested in object_test
    def setUp(self):
        self.m = 1
        self.p = [3, 2]
        self.v = [1, 0]

    # ----- INVALID INPUTS -----
    def test_invalid_radius(self):
        with self.assertRaises(TypeError) as e:
            Circle(self.m, self.p, self.v, [3, 5])
        self.assertEqual(str(e.exception), "Radius must be a number")

        with self.assertRaises(ValueError) as e:
            Circle(self.m, self.p, self.v, -2)
        self.assertEqual(str(e.exception), "Radius must be positive")

    # ----- VALID INPUTS -----
    def test_int_radius(self):
        circle = Circle(self.m, self.p, self.v, 2)

    def test_float_radius(self):
        circle = Circle(self.m, self.p, self.v, 2.5)

    # Currently 0 is allowed so point masses can exist
    def test_zero_radius(self):
        circle = Circle(self.m, self.p, self.v, 0)


if __name__ == "__main__":
    unittest.main()
