def cm_to_m(cm):
    return cm / 100

def m_to_cm(m):
    return m * 100

def km_to_m(km):
    return km * 1000

def kg_to_g(kg):
    return kg * 1000

def g_to_kg(g):
    return g / 1000

def minutes_to_hours(minutes):
    return minutes / 60

def hours_to_minutes(hours):
    return hours * 60

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)
