import unittest
from physics.collisions.shape_collisions import circle_circle_collision
from physics.objects.Circle import Circle


class CircleCircleCollisionTest(unittest.TestCase):
    def test_not_colliding(self):
        c1 = Circle(1.0, 1.0, [0, 0])
        c2 = Circle(1.0, 1.0, [0, 5])

        self.assertFalse(circle_circle_collision(c1, c2))

    def test_colliding_same_pos(self):
        c1 = Circle(1.0, 1.0, [0, 3])
        c2 = Circle(1.0, 1.0, [0, 3])

        self.assertTrue(circle_circle_collision(c1, c2))

    def test_colliding_diff_pos(self):
        c1 = Circle(1.0, 1.0, [0, 2.5])
        c2 = Circle(1.0, 1.0, [0, 3])

        self.assertTrue(circle_circle_collision(c1, c2))

    def test_not_colliding_touching_exact(self):
        c1 = Circle(1.0, 1.0, [0, 1])
        c2 = Circle(1.0, 1.0, [0, 3])

        self.assertFalse(circle_circle_collision(c1, c2))


if __name__ == "__main__":
    unittest.main()
