import math

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return round(math.pi * radius ** 2, 2)

def circle_circumference(radius):
    return round(2 * math.pi * radius, 2)

def cube_volume(side):
    return side ** 3

def cuboid_volume(length, width, height):
    return length * width * height

def cylinder_volume(radius, height):
    return round(math.pi * radius ** 2 * height, 2)

def sphere_volume(radius):
    return round((4 / 3) * math.pi * radius ** 3, 2)
