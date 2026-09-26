"""
FINANCE MANAGEMENT SYSTEM
==========================
A simple, beginner-friendly program to manage accounts and transactions.

Features:
    1. Create a new account
    2. View all accounts
    3. Deposit money into an account
    4. Withdraw money from an account
    5. Transfer money between two accounts
    6. View transaction history
    7. Save records to a file (finance.txt)
    8. Load records from a file (finance.txt)
    9. Exit

How it works:
    - Every account is stored as a dictionary, e.g.:
        {"id": 1, "name": "Checking", "balance": 100.0}
    - Every transaction is stored as a dictionary, e.g.:
        {"id": 1, "account_id": 1, "type": "deposit", "amount": 50.0, "note": "salary"}
    - Accounts are kept in one list called `accounts`.
    - Transactions are kept in one list called `transactions` (this is the "history").
    - The program keeps running in a loop, showing a menu, until you choose "Exit".

This program uses ONLY plain Python - no imports of any kind.
    - Saving/loading uses plain text (one record per line, fields separated by "|"),
      instead of the json module.
    - Checking if the save file exists is done with try/except instead of the os module.

Just run:  python finance_system.py
"""

# This is the file where account and transaction records will be saved/loaded.
DATA_FILE = "finance.txt"

# The character we use to separate fields when saving a record to a text line.
SEPARATOR = "|"


# --------------------------------------------------------------------------
# STEP 1: Set up the main data storage
# --------------------------------------------------------------------------
# `accounts` holds every account (as a dictionary).
# `transactions` holds every deposit/withdrawal/transfer ever made (the ledger).
# `next_account_id` and `next_txn_id` keep track of the next unique IDs to hand out.
accounts = []
transactions = []
next_account_id = 1
next_txn_id = 1


# --------------------------------------------------------------------------
# STEP 2: Helper functions
# --------------------------------------------------------------------------

def find_account_by_id(account_id):
    """Search the accounts list and return the account with a matching ID.

    Returns the account dictionary if found, otherwise returns None.
    """
    for account in accounts:
        if account["id"] == account_id:
            return account
    return None


def record_transaction(account_id, txn_type, amount, note):
    """Create a new transaction record and add it to the transactions list.

    txn_type should be one of: "deposit", "withdrawal", "transfer_out", "transfer_in".
    This keeps a full history of everything that happens to every account.
    """
    global next_txn_id

    txn = {
        "id": next_txn_id,
        "account_id": account_id,
        "type": txn_type,
        "amount": amount,
        "note": note,
    }
    transactions.append(txn)
    next_txn_id += 1


def ask_for_amount(prompt_text):
    """Ask the user to type in a positive number and keep asking until they do.

    Returns the amount as a float, or None if the user typed something invalid.
    """
    raw_value = input(prompt_text).strip()

    try:
        amount = float(raw_value)
    except ValueError:
        print("That's not a valid number.")
        return None

    if amount <= 0:
        print("Amount must be greater than zero.")
        return None

    return amount


# --------------------------------------------------------------------------
# STEP 3: Functions for each feature of the system
# --------------------------------------------------------------------------

def create_account():
    """Ask the user for details and create a new account."""
    global next_account_id

    print("\n--- Create New Account ---")
    name = input("Enter account name (e.g. Checking, Savings): ").strip()

    if name == "":
        print("Account name cannot be empty. Account was not created.")
        return

    opening_balance = input("Enter opening balance (or press Enter for 0): ").strip()

    if opening_balance == "":
        opening_balance = 0.0
    else:
        try:
            opening_balance = float(opening_balance)
        except ValueError:
            print("Invalid amount. Account was not created.")
            return

        if opening_balance < 0:
            print("Opening balance cannot be negative. Account was not created.")
            return

    new_account = {
        "id": next_account_id,
        "name": name,
        "balance": opening_balance,
    }

    accounts.append(new_account)
    print(f"Account '{name}' created successfully with ID {next_account_id} "
          f"and balance {opening_balance:.2f}.")

    next_account_id += 1


def view_accounts():
    """Display all accounts and their current balances."""
    print("\n--- All Accounts ---")

    if len(accounts) == 0:
        print("No accounts found. Create an account first.")
        return

    print(f"{'ID':<5}{'Name':<20}{'Balance':<12}")
    print("-" * 37)
    for account in accounts:
        print(f"{account['id']:<5}{account['name']:<20}{account['balance']:<12.2f}")

    total = 0.0
    for account in accounts:
        total = total + account["balance"]
    print("-" * 37)
    print(f"{'TOTAL':<25}{total:<12.2f}")


def deposit_money():
    """Add money to an account."""
    print("\n--- Deposit Money ---")
    try:
        account_id = int(input("Enter account ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    account = find_account_by_id(account_id)
    if account is None:
        print("No account found with that ID.")
        return

    amount = ask_for_amount("Enter amount to deposit: ")
    if amount is None:
        return

    note = input("Enter a note (e.g. 'salary'), or press Enter to skip: ").strip()

    account["balance"] = account["balance"] + amount
    record_transaction(account_id, "deposit", amount, note)

    print(f"Deposited {amount:.2f} into '{account['name']}'. "
          f"New balance: {account['balance']:.2f}")


def withdraw_money():
    """Remove money from an account, as long as there's enough balance."""
    print("\n--- Withdraw Money ---")
    try:
        account_id = int(input("Enter account ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    account = find_account_by_id(account_id)
    if account is None:
        print("No account found with that ID.")
        return

    amount = ask_for_amount("Enter amount to withdraw: ")
    if amount is None:
        return

    if amount > account["balance"]:
        print(f"Cannot withdraw {amount:.2f}. Balance is only {account['balance']:.2f}.")
        return

    note = input("Enter a note (e.g. 'groceries'), or press Enter to skip: ").strip()

    account["balance"] = account["balance"] - amount
    record_transaction(account_id, "withdrawal", amount, note)

    print(f"Withdrew {amount:.2f} from '{account['name']}'. "
          f"New balance: {account['balance']:.2f}")


def transfer_money():
    """Move money from one account to another."""
    print("\n--- Transfer Money ---")
    try:
        from_id = int(input("Enter the FROM account ID: ").strip())
        to_id = int(input("Enter the TO account ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter numbers only.")
        return

    if from_id == to_id:
        print("You can't transfer money to the same account.")
        return

    from_account = find_account_by_id(from_id)
    to_account = find_account_by_id(to_id)

    if from_account is None or to_account is None:
        print("One or both account IDs were not found.")
        return

    amount = ask_for_amount("Enter amount to transfer: ")
    if amount is None:
        return

    if amount > from_account["balance"]:
        print(f"Cannot transfer {amount:.2f}. "
              f"'{from_account['name']}' only has {from_account['balance']:.2f}.")
        return

    note = input("Enter a note, or press Enter to skip: ").strip()

    # Move the money: subtract from one account, add to the other
    from_account["balance"] = from_account["balance"] - amount
    to_account["balance"] = to_account["balance"] + amount

    # Record both sides of the transfer so each account's history makes sense on its own
    record_transaction(from_id, "transfer_out", amount, note)
    record_transaction(to_id, "transfer_in", amount, note)

    print(f"Transferred {amount:.2f} from '{from_account['name']}' to '{to_account['name']}'.")


def view_transaction_history():
    """Display every transaction, optionally filtered to one account."""
    print("\n--- Transaction History ---")

    if len(transactions) == 0:
        print("No transactions yet.")
        return

    filter_choice = input(
        "Press Enter to view ALL transactions, or type an account ID to filter: "
    ).strip()

    print(f"{'TxnID':<8}{'AccID':<8}{'Type':<15}{'Amount':<12}{'Note':<20}")
    print("-" * 63)

    shown_any = False
    for txn in transactions:
        if filter_choice != "" and str(txn["account_id"]) != filter_choice:
            continue  # skip transactions that don't match the filter

        print(f"{txn['id']:<8}{txn['account_id']:<8}{txn['type']:<15}"
              f"{txn['amount']:<12.2f}{txn['note']:<20}")
        shown_any = True

    if not shown_any:
        print("No transactions found for that account ID.")


def save_data():
    """Save all accounts and transactions to a plain text file.

    Each line starts with a tag ("ACCOUNT" or "TXN") so we know what kind of
    record it is when we load the file back later. Fields are separated by
    SEPARATOR ("|"). This avoids needing the json module.

    """
    file = open(DATA_FILE, "w")

    for account in accounts:
        line = SEPARATOR.join([
            "ACCOUNT",
            str(account["id"]),
            account["name"],
            str(account["balance"]),
        ])
        file.write(line + "\n")

    for txn in transactions:
        line = SEPARATOR.join([
            "TXN",
            str(txn["id"]),
            str(txn["account_id"]),
            txn["type"],
            str(txn["amount"]),
            txn["note"],
        ])
        file.write(line + "\n")

    file.close()
    print(f"Saved {len(accounts)} account(s) and {len(transactions)} "
          f"transaction(s) to '{DATA_FILE}'.")


def load_data():
    """Load accounts and transactions back from the plain text file, if it exists.

    We use try/except instead of the os module to check whether the file
    exists: if open() fails because the file isn't there, Python raises
    FileNotFoundError, and we handle that gracefully below.
    """
    global accounts, transactions, next_account_id, next_txn_id

    try:
        file = open(DATA_FILE, "r")
    except FileNotFoundError:
        print(f"No saved file found ('{DATA_FILE}'). Starting with no accounts.")
        return

    loaded_accounts = []
    loaded_transactions = []

    for line in file:
        line = line.strip()
        if line == "":
            continue  # skip blank lines

        parts = line.split(SEPARATOR)

        if parts[0] == "ACCOUNT" and len(parts) == 4:
            account = {
                "id": int(parts[1]),
                "name": parts[2],
                "balance": float(parts[3]),
            }
            loaded_accounts.append(account)

        elif parts[0] == "TXN" and len(parts) == 6:
            txn = {
                "id": int(parts[1]),
                "account_id": int(parts[2]),
                "type": parts[3],
                "amount": float(parts[4]),
                "note": parts[5],
            }
            loaded_transactions.append(txn)

        # any line that doesn't match a known format is silently skipped

    file.close()

    accounts = loaded_accounts
    transactions = loaded_transactions

    # Recalculate the ID counters so new records don't reuse an existing ID
    if accounts:
        highest_account_id = accounts[0]["id"]
        for account in accounts:
            if account["id"] > highest_account_id:
                highest_account_id = account["id"]
        next_account_id = highest_account_id + 1
    else:
        next_account_id = 1

    if transactions:
        highest_txn_id = transactions[0]["id"]
        for txn in transactions:
            if txn["id"] > highest_txn_id:
                highest_txn_id = txn["id"]
        next_txn_id = highest_txn_id + 1
    else:
        next_txn_id = 1

    print(f"Loaded {len(accounts)} account(s) and {len(transactions)} "
          f"transaction(s) from '{DATA_FILE}'.")


# --------------------------------------------------------------------------
# STEP 4: The main menu loop
# --------------------------------------------------------------------------

def show_menu():
    """Print the list of options available to the user."""
    print("\n===== FINANCE MANAGEMENT SYSTEM =====")
    print("1. Create a new account")
    print("2. View all accounts")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer money")
    print("6. View transaction history")
    print("7. Save records to file")
    print("8. Load records from file")
    print("9. Exit")


def main():
    """Run the program: show the menu repeatedly until the user chooses to exit."""

    # Try to load any previously saved data automatically when the program starts
    load_data()

    while True:
        show_menu()
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            transfer_money()
        elif choice == "6":
            view_transaction_history()
        elif choice == "7":
            save_data()
        elif choice == "8":
            load_data()
        elif choice == "9":
            print("Goodbye!")
            break  # this stops the while loop and ends the program
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


# --------------------------------------------------------------------------
# STEP 5: Only run main() if this file is executed directly
# --------------------------------------------------------------------------
# This check means: if someone imports this file into another program instead
# of running it directly, main() won't run automatically.
if __name__ == "__main__":
    main()