import unittest
from financial_calculator.loans import monthly_payment, total_loan_payment


class TestLoans(unittest.TestCase):
    def test_zero_interest(self):
        self.assertEqual(monthly_payment(1200, 0, 1), 100.0)

    def test_total_payment(self):
        self.assertEqual(total_loan_payment(1200, 0, 1), 1200.0)


if __name__ == "__main__":
    unittest.main()
