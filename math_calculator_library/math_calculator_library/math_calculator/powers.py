import math

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def power(base, exponent):
    return base ** exponent

def square_root(number):
    if number < 0:
        raise ValueError("Cannot find the real square root of a negative number.")
    return round(math.sqrt(number), 2)

def cube_root(number):
    if number < 0:
        return round(-((-number) ** (1 / 3)), 2)
    return round(number ** (1 / 3), 2)
