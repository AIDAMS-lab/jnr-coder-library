def validate_number(value, name="value"):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    return float(value)

def validate_list(values, name="values"):
    if not isinstance(values, (list, tuple)) or not values:
        raise ValueError(f"{name} must contain at least one number.")
    for value in values:
        validate_number(value, name)
    return values

def check_not_zero(value, name="value"):
    if value == 0:
        raise ZeroDivisionError(f"{name} cannot be zero.")

def round_answer(value, digits=2):
    return round(float(value), digits)
