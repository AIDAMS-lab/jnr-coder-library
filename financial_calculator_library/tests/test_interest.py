import unittest
from financial_calculator.interest import simple_interest, compound_interest


class TestInterest(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(simple_interest(1000, 10, 2), 200.0)

    def test_compound_interest(self):
        self.assertAlmostEqual(compound_interest(1000, 10, 2), 210.0, places=2)


if __name__ == "__main__":
    unittest.main()
