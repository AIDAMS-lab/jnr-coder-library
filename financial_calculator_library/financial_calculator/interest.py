"""Interest calculations."""

from .utils import validate_number, validate_positive, round_money


def simple_interest(principal, rate, time):
    """Return simple interest: P * R * T / 100."""
    principal = validate_positive(principal, "principal")
    rate = validate_number(rate, "rate")
    time = validate_positive(time, "time")
    return round_money(principal * rate * time / 100)


def total_amount(principal, interest):
    """Return principal plus interest."""
    principal = validate_number(principal, "principal")
    interest = validate_number(interest, "interest")
    return round_money(principal + interest)


def compound_interest(principal, rate, time, compounds_per_year=1):
    """Return compound interest earned."""
    principal = validate_positive(principal, "principal")
    rate = validate_number(rate, "rate")
    time = validate_positive(time, "time")
    compounds_per_year = validate_positive(compounds_per_year, "compounds_per_year")

    amount = principal * (1 + rate / (100 * compounds_per_year)) ** (
        compounds_per_year * time
    )
    return round_money(amount - principal)
