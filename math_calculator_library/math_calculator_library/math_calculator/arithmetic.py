from .utils import validate_number, validate_list, check_not_zero, round_answer

def add(a, b):
    return validate_number(a, "a") + validate_number(b, "b")

def subtract(a, b):
    return validate_number(a, "a") - validate_number(b, "b")

def multiply(a, b):
    return validate_number(a, "a") * validate_number(b, "b")

def divide(a, b):
    a, b = validate_number(a, "a"), validate_number(b, "b")
    check_not_zero(b, "b")
    return round_answer(a / b)

def average(values):
    values = validate_list(values)
    return round_answer(sum(values) / len(values))

def remainder(a, b):
    a, b = validate_number(a, "a"), validate_number(b, "b")
    check_not_zero(b, "b")
    return a % b
