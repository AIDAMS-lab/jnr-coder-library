"""Simple terminal application for the financial calculator library."""

from financial_calculator import (
    simple_interest, compound_interest,
    monthly_payment, total_loan_payment, total_loan_interest,
    total_expenses, remaining_money, expense_percentage,
    simple_savings, compound_savings, months_to_goal,
    convert_currency, get_supported_currencies,
)


def number(prompt):
    # Keep asking until the user enters a valid number.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def interest_menu():
    print("\n--- Interest Calculator ---")
    print("1. Simple Interest")
    print("2. Compound Interest")
    choice = input("Choose: ")

    principal = number("Principal: ")
    rate = number("Annual rate (%): ")
    years = number("Years: ")

    if choice == "1":
        interest = simple_interest(principal, rate, years)
        print(f"Interest: {interest:.2f}")
        print(f"Total: {principal + interest:.2f}")
    elif choice == "2":
        interest = compound_interest(principal, rate, years)
        print(f"Compound interest: {interest:.2f}")
        print(f"Total: {principal + interest:.2f}")
    else:
        print("Invalid choice.")


def loan_menu():
    print("\n--- Loan Calculator ---")
    principal = number("Loan amount: ")
    rate = number("Annual interest rate (%): ")
    years = number("Loan period (years): ")

    payment = monthly_payment(principal, rate, years)
    total = total_loan_payment(principal, rate, years)
    interest = total_loan_interest(principal, rate, years)

    print(f"Monthly payment: {payment:.2f}")
    print(f"Total payment: {total:.2f}")
    print(f"Total interest: {interest:.2f}")


def budget_menu():
    print("\n--- Budget Calculator ---")
    income = number("Monthly income: ")
    count = int(number("How many expenses? "))

    expenses = []
    for i in range(count):
        expenses.append(number(f"Expense {i + 1}: "))

    total = total_expenses(expenses)
    remaining = remaining_money(income, expenses)
    percent = expense_percentage(income, expenses)

    print(f"Total expenses: {total:.2f}")
    print(f"Remaining money: {remaining:.2f}")
    print(f"Expense percentage: {percent:.2f}%")


def savings_menu():
    print("\n--- Savings Calculator ---")
    print("1. Simple savings")
    print("2. Compound savings")
    print("3. Months to savings goal")
    choice = input("Choose: ")

    if choice == "1":
        principal = number("Starting savings: ")
        rate = number("Annual rate (%): ")
        years = number("Years: ")
        print(f"Final savings: {simple_savings(principal, rate, years):.2f}")

    elif choice == "2":
        principal = number("Starting savings: ")
        rate = number("Annual rate (%): ")
        years = number("Years: ")
        print(f"Final savings: {compound_savings(principal, rate, years):.2f}")

    elif choice == "3":
        current = number("Current savings: ")
        monthly = number("Monthly saving: ")
        goal = number("Savings goal: ")
        print(f"Months needed: {months_to_goal(current, monthly, goal)}")

    else:
        print("Invalid choice.")


def currency_menu():
    print("\n--- Currency Calculator ---")
    print("Supported:", ", ".join(get_supported_currencies()))

    amount = number("Amount: ")
    source = input("From currency: ")
    target = input("To currency: ")

    try:
        result = convert_currency(amount, source, target)
        print(f"{amount:.2f} {source.upper()} = {result:.2f} {target.upper()}")
    except ValueError as error:
        print(error)


def main():
    while True:
        print("\n================================")
        print("       FINANCIAL CALCULATOR")
        print("================================")
        print("1. Interest")
        print("2. Loans")
        print("3. Budget")
        print("4. Savings")
        print("5. Currency")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                interest_menu()
            elif choice == "2":
                loan_menu()
            elif choice == "3":
                budget_menu()
            elif choice == "4":
                savings_menu()
            elif choice == "5":
                currency_menu()
            elif choice == "6":
                print("Thank you for using the calculator!")
                break
            else:
                print("Invalid choice.")
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
