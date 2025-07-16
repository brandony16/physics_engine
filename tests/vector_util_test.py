import unittest
import physics.vector_utils as v
import numpy as np


class VectorUtilTests(unittest.TestCase):
    def test_to_vec(self):
        seq1 = (2, 5)
        seq2 = [3, 8]

        vec1 = v.to_vec(seq1)
        vec2 = v.to_vec(seq2)

        self.assertTrue(isinstance(vec1, np.ndarray))
        self.assertTrue(isinstance(vec2, np.ndarray))

        self.assertTrue(isinstance(vec1[0], float))
        self.assertTrue(isinstance(vec2[0], float))

        self.assertAlmostEqual(vec1[0], 2)
        self.assertAlmostEqual(vec1[1], 5)
        self.assertAlmostEqual(vec2[0], 3)
        self.assertAlmostEqual(vec2[1], 8)

    def test_add(self):
        vec1 = v.to_vec([3, 4])
        vec2 = v.to_vec([6, -8])

        total = v.add(vec1, vec2)

        self.assertAlmostEqual(total[0], 9)
        self.assertAlmostEqual(total[1], -4)

    def test_scale(self):
        vec1 = v.to_vec([-2, 4])

        scale1 = v.scale(vec1, 5)
        scale2 = v.scale(vec1, -1 / 2)

        self.assertAlmostEqual(scale1[0], -10)
        self.assertAlmostEqual(scale1[1], 20)

        self.assertAlmostEqual(scale2[0], 1)
        self.assertAlmostEqual(scale2[1], -2)

    def test_dot(self):
        vec1 = v.to_vec([3, 4])
        vec2 = v.to_vec([6, -8])
        dot = v.dot(vec1, vec2)  # 18 - 32 = -14

        vec3 = v.to_vec([2, 1])
        vec4 = v.to_vec([-1, 2])
        dot2 = v.dot(vec3, vec4)  # -2 + 2 = 0

        self.assertAlmostEqual(dot, -14)
        self.assertAlmostEqual(dot2, 0)

    def test_norm(self):
        vec1 = v.to_vec([3, 4])
        vec2 = v.to_vec([6, -8])
        
        norm = v.norm(vec1)
        norm2 = v.norm(vec2)

        self.assertAlmostEqual(norm, 5)
        self.assertAlmostEqual(norm2, 10)


if __name__ == "__main__":
    unittest.main()
