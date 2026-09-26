import unittest
from financial_calculator.budget import total_expenses, remaining_money


class TestBudget(unittest.TestCase):
    def test_total_expenses(self):
        self.assertEqual(total_expenses([100, 200, 50]), 350.0)

    def test_remaining_money(self):
        self.assertEqual(remaining_money(1000, [100, 200]), 700.0)


if __name__ == "__main__":
    unittest.main()
