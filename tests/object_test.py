import unittest
from physics.objects import Object, Circle


class ObjectTest(unittest.TestCase):
    def invalidInputs(self):
        self.assertEqual(1, 2)


if __name__ == "__main__":
    unittest.main()
