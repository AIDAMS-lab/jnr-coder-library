"""Small helper functions used by the library."""

def validate_number(value, name="value", allow_zero=True):
    # Make sure the value is a number.
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    # Most financial values should not be negative.
    if value < 0 or (not allow_zero and value == 0):
        raise ValueError(f"{name} must be {'greater than 0' if not allow_zero else '0 or greater'}.")
    return float(value)


def validate_positive(value, name="value"):
    return validate_number(value, name, allow_zero=False)


def round_money(value):
    # Money is normally shown with two decimal places.
    return round(float(value), 2)


def format_money(value, symbol=""):
    return f"{symbol}{round_money(value):,.2f}"
