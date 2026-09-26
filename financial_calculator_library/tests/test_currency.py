import unittest
from financial_calculator.currency import convert_currency


class TestCurrency(unittest.TestCase):
    def test_same_currency(self):
        self.assertEqual(convert_currency(100, "GHS", "GHS"), 100.0)

    def test_conversion(self):
        self.assertAlmostEqual(convert_currency(100, "GHS", "USD"), 6.7, places=2)


if __name__ == "__main__":
    unittest.main()
