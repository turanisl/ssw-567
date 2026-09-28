"""Classify triangles by side type and whether they are right triangles."""

import unittest


def classify_triangle(a, b, c):
    """return side and right triangle classification"""
    if a == b and b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if (a ** 2 + b ** 2 == c ** 2 or
            a ** 2 + c ** 2 == b ** 2 or
            b ** 2 + c ** 2 == a ** 2):
        return triangle_type + " and Right"

    return triangle_type + " and Not Right"


class TriangleTest(unittest.TestCase): # tests
    """unit tests for triangle classification function"""

    def test_right_triangle(self):
        """test right and non right triangle classifications"""
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
        self.assertEqual(classify_triangle(5, 4, 3), "Scalene and Right")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral and Not Right")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    