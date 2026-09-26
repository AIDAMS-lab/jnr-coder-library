import math

def solve_linear(a, b):
    # Solves ax + b = 0.
    if a == 0:
        if b == 0:
            return "All real numbers are solutions."
        return "No solution."
    return round(-b / a, 2)

def solve_quadratic(a, b, c):
    # Solves ax² + bx + c = 0.
    if a == 0:
        return solve_linear(b, c)
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No real solutions."
    if discriminant == 0:
        return round(-b / (2 * a), 2)
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return (round(x1, 2), round(x2, 2))
