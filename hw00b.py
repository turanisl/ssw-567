import unittest

def classify_triangle(a, b, c):

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


class TriangleTest(unittest.TestCase):

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
        self.assertEqual(classify_triangle(5, 4, 3), "Scalene and Right")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral and Not Right")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)