"""Financial calculator."""

from .interest import simple_interest, compound_interest, total_amount
from .loans import monthly_payment, total_loan_payment, total_loan_interest
from .budget import total_expenses, remaining_money, expense_percentage, budget_summary
from .savings import simple_savings, compound_savings, months_to_goal
from .currency import convert_currency, set_exchange_rate, get_supported_currencies

__all__ = [
    "simple_interest", "compound_interest", "total_amount",
    "monthly_payment", "total_loan_payment", "total_loan_interest",
    "total_expenses", "remaining_money", "expense_percentage", "budget_summary",
    "simple_savings", "compound_savings", "months_to_goal",
    "convert_currency", "set_exchange_rate", "get_supported_currencies",
]
