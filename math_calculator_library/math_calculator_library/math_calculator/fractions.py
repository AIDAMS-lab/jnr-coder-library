from fractions import Fraction

def _fraction(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return Fraction(numerator, denominator)

def simplify_fraction(numerator, denominator):
    return _fraction(numerator, denominator)

def add_fractions(n1, d1, n2, d2):
    return _fraction(n1, d1) + _fraction(n2, d2)

def subtract_fractions(n1, d1, n2, d2):
    return _fraction(n1, d1) - _fraction(n2, d2)

def multiply_fractions(n1, d1, n2, d2):
    return _fraction(n1, d1) * _fraction(n2, d2)

def divide_fractions(n1, d1, n2, d2):
    first, second = _fraction(n1, d1), _fraction(n2, d2)
    if second == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first / second
