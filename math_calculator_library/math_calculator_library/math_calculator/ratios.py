from math import gcd

def simplify_ratio(a, b):
    if a == 0 and b == 0:
        raise ValueError("Both ratio values cannot be zero.")
    divisor = gcd(int(abs(a)), int(abs(b)))
    return (int(a / divisor), int(b / divisor))

def divide_in_ratio(amount, first_part, second_part):
    if first_part < 0 or second_part < 0:
        raise ValueError("Ratio parts cannot be negative.")
    total = first_part + second_part
    if total == 0:
        raise ValueError("Ratio cannot be 0:0.")
    return (round(amount * first_part / total, 2),
            round(amount * second_part / total, 2))
