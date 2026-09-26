import unittest
from fractions import Fraction
from math_calculator import *

class TestMathLibrary(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(divide(10, 5), 2)

    def test_fraction(self):
        self.assertEqual(add_fractions(1, 2, 1, 4), Fraction(3, 4))

    def test_percentage(self):
        self.assertEqual(percentage_of(20, 500), 100)

    def test_ratio(self):
        self.assertEqual(simplify_ratio(10, 20), (1, 2))

    def test_powers(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square_root(49), 7)

    def test_algebra(self):
        self.assertEqual(solve_linear(2, -10), 5)
        self.assertEqual(solve_quadratic(1, -5, 6), (3.0, 2.0))

    def test_geometry(self):
        self.assertEqual(rectangle_area(10, 5), 50)
        self.assertEqual(square_area(5), 25)

    def test_statistics(self):
        self.assertEqual(mean([10, 20, 30]), 20)
        self.assertEqual(median([10, 30, 20]), 20)
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_conversion(self):
        self.assertEqual(cm_to_m(100), 1)
        self.assertEqual(kg_to_g(2), 2000)
        self.assertEqual(celsius_to_fahrenheit(0), 32)

if __name__ == "__main__":
    unittest.main()
