"""Loan calculations."""

from .utils import validate_number, validate_positive, round_money


def monthly_payment(principal, annual_rate, years):
    """Calculate a fixed monthly loan payment."""
    principal = validate_positive(principal, "principal")
    annual_rate = validate_number(annual_rate, "annual_rate")
    years = validate_positive(years, "years")

    months = years * 12
    if annual_rate == 0:
        return round_money(principal / months)

    monthly_rate = annual_rate / 100 / 12
    payment = principal * monthly_rate * (1 + monthly_rate) ** months
    payment /= (1 + monthly_rate) ** months - 1
    return round_money(payment)


def total_loan_payment(principal, annual_rate, years):
    """Calculate the total amount paid over the loan."""
    return round_money(monthly_payment(principal, annual_rate, years) * years * 12)


def total_loan_interest(principal, annual_rate, years):
    """Calculate total interest paid on the loan."""
    return round_money(total_loan_payment(principal, annual_rate, years) - principal)
