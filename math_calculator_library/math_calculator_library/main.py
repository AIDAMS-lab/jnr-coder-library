from math_calculator import add, subtract, multiply, divide, percentage_of, square, square_root, solve_linear, rectangle_area, mean, median, mode, cm_to_m, celsius_to_fahrenheit

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def arithmetic_menu():
    print("\n--- Basic Arithmetic ---")
    a, b = number("First number: "), number("Second number: ")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Choose: ")
    try:
        answers = {"1": add(a,b), "2": subtract(a,b), "3": multiply(a,b), "4": divide(a,b)}
        print("Answer:", answers.get(choice, "Invalid choice."))
    except ZeroDivisionError as error:
        print("Error:", error)

def percentage_menu():
    print("\n--- Percentage ---")
    print("Answer:", percentage_of(number("Percentage: "), number("Number: ")))

def powers_menu():
    print("\n--- Powers and Roots ---")
    value = number("Number: ")
    choice = input("1. Square\n2. Square root\nChoose: ")
    try:
        print("Answer:", square(value) if choice == "1" else square_root(value) if choice == "2" else "Invalid choice.")
    except ValueError as error:
        print("Error:", error)

def algebra_menu():
    print("\n--- Linear Algebra ---")
    print("Solves ax + b = 0")
    print("x =", solve_linear(number("a: "), number("b: ")))

def geometry_menu():
    print("\n--- Geometry ---")
    choice = input("1. Rectangle area\n2. Square area\nChoose: ")
    if choice == "1":
        print("Area:", rectangle_area(number("Length: "), number("Width: ")))
    elif choice == "2":
        side = number("Side: ")
        print("Area:", side ** 2)
    else:
        print("Invalid choice.")

def statistics_menu():
    try:
        values = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
        print("Mean:", mean(values))
        print("Median:", median(values))
        print("Mode:", mode(values))
    except ValueError as error:
        print("Error:", error)

def conversion_menu():
    choice = input("1. Centimetres to metres\n2. Celsius to Fahrenheit\nChoose: ")
    value = number("Value: ")
    if choice == "1":
        print("Answer:", cm_to_m(value), "m")
    elif choice == "2":
        print("Answer:", celsius_to_fahrenheit(value), "°F")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\n===================================")
        print("       MATHEMATICS CALCULATOR")
        print("===================================")
        print("1. Basic Arithmetic")
        print("2. Percentages")
        print("3. Powers and Roots")
        print("4. Algebra")
        print("5. Geometry")
        print("6. Statistics")
        print("7. Unit Conversion")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == "1": arithmetic_menu()
        elif choice == "2": percentage_menu()
        elif choice == "3": powers_menu()
        elif choice == "4": algebra_menu()
        elif choice == "5": geometry_menu()
        elif choice == "6": statistics_menu()
        elif choice == "7": conversion_menu()
        elif choice == "8":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
