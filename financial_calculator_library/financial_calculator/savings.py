"""Savings calculations."""

from .utils import validate_number, validate_positive, round_money


def simple_savings(principal, rate, years):
    """Return savings growth using simple interest."""
    principal = validate_positive(principal, "principal")
    rate = validate_number(rate, "rate")
    years = validate_positive(years, "years")
    return round_money(principal + (principal * rate * years / 100))


def compound_savings(principal, rate, years, compounds_per_year=12):
    """Return the final balance using compound growth."""
    principal = validate_positive(principal, "principal")
    rate = validate_number(rate, "rate")
    years = validate_positive(years, "years")
    compounds_per_year = validate_positive(compounds_per_year, "compounds_per_year")

    return round_money(
        principal * (1 + rate / (100 * compounds_per_year))
        ** (compounds_per_year * years)
    )


def months_to_goal(current_savings, monthly_saving, goal):
    """Return whole months needed to reach a goal without interest."""
    current_savings = validate_number(current_savings, "current_savings")
    monthly_saving = validate_positive(monthly_saving, "monthly_saving")
    goal = validate_positive(goal, "goal")

    if current_savings >= goal:
        return 0

    remaining = goal - current_savings
    months = int((remaining + monthly_saving - 1) // monthly_saving)
    return months
