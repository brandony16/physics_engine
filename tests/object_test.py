import unittest
from physics.objects import Object


class ObjectTest(unittest.TestCase):
    # ----- INVALID INPUTS -----
    def test_invalid_mass(self):
        with self.assertRaises(ValueError) as e:
            Object(-1, [2, 2], [0, 0])
        self.assertEqual(str(e.exception), "Mass must be positive and non-zero")

        with self.assertRaises(TypeError) as e:
            Object("2", [2, 2], [0, 0])
        self.assertEqual(str(e.exception), "Mass must be a number")

    def test_invalid_position(self):
        # Wrong type
        with self.assertRaises(TypeError) as e:
            Object(1, (2, 5), [0, 0])
        self.assertEqual(str(e.exception), "Position must be a list or numpy array")

        # Too many dims
        with self.assertRaises(ValueError) as e:
            Object(1, [0, 0, 0], [0, 0])
        self.assertEqual(str(e.exception), "Position must have exactly two elements")

        # Wrong type within
        with self.assertRaises(TypeError) as e:
            Object(1, [0, "5"], [0, 0])
        self.assertEqual(str(e.exception), "Position must contain only numbers")

    def test_invalid_velocity(self):
        # Wrong type
        with self.assertRaises(TypeError) as e:
            Object(1, [0, 0], "[0, 0]")
        self.assertEqual(str(e.exception), "Velocity must be a list or numpy array")

        # Too many dims
        with self.assertRaises(ValueError) as e:
            Object(1, [0, 0], [7, 4, 2])
        self.assertEqual(str(e.exception), "Velocity must have exactly two elements")

        # Wrong type within
        with self.assertRaises(TypeError) as e:
            Object(1, [0, 0], [[4], 0])
        self.assertEqual(str(e.exception), "Velocity must contain only numbers")

    # ----- VALID INPUTS -----
    def test_int_inputs(self):
        obj = Object(4, [3, 2], [5, 8])

    def test_negative_inputs(self):
        obj = Object(4, [-3, 2], [5, -4])

    def test_float_inputs(self):
        obj = Object(4.3, [2.6, 3.6], [1.6, -5.8])

    def test_mized_inputs(self):
        obj = Object(9.0, [4, -3.7], [-2, 0.1])

    # Add more tests as object gets methods


if __name__ == "__main__":
    unittest.main()
