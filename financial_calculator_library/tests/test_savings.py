import unittest
from financial_calculator.savings import simple_savings, months_to_goal


class TestSavings(unittest.TestCase):
    def test_simple_savings(self):
        self.assertEqual(simple_savings(1000, 10, 2), 1200.0)

    def test_months_to_goal(self):
        self.assertEqual(months_to_goal(1000, 500, 2500), 3)


if __name__ == "__main__":
    unittest.main()
