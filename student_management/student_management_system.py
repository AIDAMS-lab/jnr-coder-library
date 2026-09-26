"""
STUDENT MANAGEMENT SYSTEM
==========================
A simple, beginner-friendly program to manage student records.

Features:
    1. Add a new student
    2. View all students
    3. Search for a student
    4. Update a student's details
    5. Delete a student
    6. Save records to a file (students.txt)
    7. Load records from a file (students.txt)
    8. Exit

How it works:
    - Every student is stored as a dictionary, e.g.:
        {"id": 1, "name": "Ama Owusu", "age": 20, "course": "Computer Science", "grade": "A"}
    - All students are kept in one big list called `students`.
    - The program keeps running in a loop, showing a menu, until you choose "Exit".
"""

# This is the file where student records will be saved/loaded.
DATA_FILE = "students.txt"

# The character we use to separate fields when saving a student to a text line.
SEPARATOR = "|"


# Set up the main data storage

# `students` is a list that holds every student record (as a dictionary).
# `next_id` keeps track of the next unique ID to give a new student.
students = []
next_id = 1



# Functions for each feature of the system

def add_student():
    """Ask the user for details and add a new student to the list."""
    global next_id  # we need to update the shared next_id counter

    print("\n--- Add New Student ---")
    name = input("Enter student's full name: ").strip()

    # this code is to make sure the name isn't left blank
    if name == "":
        print("Name cannot be empty. Student was not added.")
        return

    age = input("Enter student's age: ").strip()
    course = input("Enter student's course: ").strip()
    grade = input("Enter student's grade (e.g. A, B, C): ").strip()

    # add a new student record as adictionary to the students list
    new_student = {
        "id": next_id,
        "name": name,
        "age": age,
        "course": course,
        "grade": grade,
    }

    students.append(new_student)   # add the new student to our list
    print(f"Student '{name}' added successfully with ID {next_id}.")

    next_id += 1  # increase the counter so the next student gets a new unique ID


def view_students():
    """Display all students currently stored."""
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students found. Add a student first.")
        return

    # Print a simple table-like layout
    print(f"{'ID':<5}{'Name':<20}{'Age':<6}{'Course':<20}{'Grade':<6}")
    print("-" * 57)
    for student in students:
        print(f"{student['id']:<5}{student['name']:<20}{student['age']:<6}"
              f"{student['course']:<20}{student['grade']:<6}")
        

# find a student by their id.

def find_student_by_id(student_id):
    """
        Helper function: search the list and return the student with a matching ID.
    """

    # # Returns the student dictionary if found, otherwise returns None.
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def search_student():
    """Search for a student by their ID or name."""
    print("\n--- Search Student ---")
    keyword = input("Enter student ID or name to search: ").strip()

    found_any = False

    for student in students:
        # Match either by exact ID or by a partial, case-insensitive name match
        if str(student["id"]) == keyword or keyword.lower() in student["name"].lower():
            print(f"Found -> ID: {student['id']}, Name: {student['name']}, "
                  f"Age: {student['age']}, Course: {student['course']}, Grade: {student['grade']}")
            found_any = True

    if not found_any:
        print("No matching student found.")


def update_student():
    """Update the details of an existing student."""
    print("\n--- Update Student ---")
    try:
        student_id = int(input("Enter the ID of the student to update: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    student = find_student_by_id(student_id)

    if student is None:
        print("No student found with that ID.")
        return

    print(f"Updating student: {student['name']} (leave a field blank to keep it unchanged)")

    new_name = input(f"New name [{student['name']}]: ").strip()
    new_age = input(f"New age [{student['age']}]: ").strip()
    new_course = input(f"New course [{student['course']}]: ").strip()
    new_grade = input(f"New grade [{student['grade']}]: ").strip()

    # Only overwrite a field if the user actually typed something
    if new_name != "":
        student["name"] = new_name
    if new_age != "":
        student["age"] = new_age
    if new_course != "":
        student["course"] = new_course
    if new_grade != "":
        student["grade"] = new_grade

    print("Student updated successfully.")


def delete_student():
    """Remove a student from the list using their ID."""
    print("\n--- Delete Student ---")
    try:
        student_id = int(input("Enter the ID of the student to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    student = find_student_by_id(student_id)

    if student is None:
        print("No student found with that ID.")
        return

    students.remove(student)
    print(f"Student '{student['name']}' (ID {student_id}) has been deleted.")


def save_students():
    """Save the current list of students to a plain text file.

    Each student becomes one line, with fields separated by SEPARATOR ("|"):
        1|Ama Owusu|20|Computer Science|A
        2|Kofi Mensah|22|Finance|B

    This avoids needing the json module - it's just plain text we build ourselves.
    """
    # "w" mode creates the file if it doesn't exist, or overwrites it if it does.
    file = open(DATA_FILE, "w")

    for student in students:
        line = SEPARATOR.join([
            str(student["id"]),
            student["name"],
            str(student["age"]),
            student["course"],
            student["grade"],
        ])
        file.write(line + "\n")  # "\n" moves to the next line for the next student

    file.close()
    print(f"Saved {len(students)} student record(s) to '{DATA_FILE}'.")


def load_students():
    """Load student records from the plain text file, if it exists.

    We use try/except instead of the os module to check whether the file
    exists: if open() fails because the file isn't there, Python raises
    FileNotFoundError, and we handle that gracefully below.
    """
    global students, next_id

    try:
        file = open(DATA_FILE, "r")
    except FileNotFoundError:
        print(f"No saved file found ('{DATA_FILE}'). Starting with an empty list.")
        return

    loaded_students = []

    for line in file:
        line = line.strip()  # remove the trailing "\n" and any extra spaces

        if line == "":
            continue  # skip any blank lines

        # Split the line back into its 5 fields using the same separator we saved with
        parts = line.split(SEPARATOR)
        if len(parts) != 5:
            continue  # skip any malformed/corrupted lines

        student = {
            "id": int(parts[0]),
            "name": parts[1],
            "age": parts[2],
            "course": parts[3],
            "grade": parts[4],
        }
        loaded_students.append(student)

    file.close()

    students = loaded_students

    # Recalculate next_id so new students don't reuse an existing ID
    if students:
        highest_id = students[0]["id"]
        for student in students:
            if student["id"] > highest_id:
                highest_id = student["id"]
        next_id = highest_id + 1
    else:
        next_id = 1

    print(f"Loaded {len(students)} student record(s) from '{DATA_FILE}'.")


## # This function displays the main menu options for the user to choose from
def show_menu():
    """Print the list of options available to the user."""
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update a student's details")
    print("5. Delete a student")
    print("6. Save records to file")
    print("7. Load records from file")
    print("8. Exit")


def main():
    """Run the program: show the menu repeatedly until the user chooses to exit."""

    # Try to load any previously saved data automatically when the program starts
    load_students()

    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_students()
        elif choice == "7":
            load_students()
        elif choice == "8":
            print("Goodbye!")
            break  # this stops the while loop and ends the program
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


# the condition below checks whether this file is being run directly and not imported from another file or program
# so it runs the codes directly from this main file. 
if __name__ == "__main__":
    main()