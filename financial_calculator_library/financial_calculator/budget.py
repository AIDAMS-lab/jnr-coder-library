"""Personal budget calculations."""

from .utils import validate_number, validate_positive, round_money


def total_expenses(expenses):
    """Add all expense values together."""
    if not isinstance(expenses, (list, tuple)):
        raise TypeError("expenses must be a list or tuple.")
    return round_money(sum(validate_number(x, "expense") for x in expenses))


def remaining_money(income, expenses):
    """Return income left after expenses."""
    income = validate_number(income, "income")
    total = total_expenses(expenses)
    return round_money(income - total)


def expense_percentage(income, expenses):
    """Return expenses as a percentage of income."""
    income = validate_positive(income, "income")
    total = total_expenses(expenses)
    return round_money((total / income) * 100)


def budget_summary(income, expenses):
    """Return a simple budget summary as a dictionary."""
    income = validate_number(income, "income")
    total = total_expenses(expenses)
    return {
        "income": round_money(income),
        "total_expenses": total,
        "remaining": round_money(income - total),
        "expense_percentage": round_money((total / income) * 100) if income else 0.0,
    }
