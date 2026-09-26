def percentage_of(percent, number):
    return round((percent / 100) * number, 2)

def percentage_change(old_value, new_value):
    if old_value == 0:
        raise ZeroDivisionError("Old value cannot be zero.")
    return round(((new_value - old_value) / old_value) * 100, 2)

def increase_by_percentage(number, percent):
    return round(number * (1 + percent / 100), 2)

def decrease_by_percentage(number, percent):
    return round(number * (1 - percent / 100), 2)
