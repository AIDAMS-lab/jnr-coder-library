"""Small examples showing how to use the library."""

from financial_calculator import (
    simple_interest,
    monthly_payment,
    budget_summary,
    compound_savings,
    convert_currency,
)

print("Simple interest:", simple_interest(1000, 10, 2))
print("Monthly loan payment:", monthly_payment(10000, 10, 2))
print("Budget:", budget_summary(5000, [1500, 800, 500, 300]))
print("Compound savings:", compound_savings(2000, 5, 3))
print("100 GHS in USD:", convert_currency(100, "GHS", "USD"))
