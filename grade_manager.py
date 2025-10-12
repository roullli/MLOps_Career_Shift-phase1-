from pathlib import Path

students_dict: dict[str, int] = {}


def add_student():
    """Add or update a student with input validation."""
    student_name = input("Enter the student's name (in alphabet): ").strip()
    student_grade = input("enter the grade (in digits): ").strip()
    try:
        student_grade = int(student_grade)
        if not 0 <= student_grade <= 100:
            raise ValueError("Enter the grade correctly(0-100)")
    except ValueError as e:
        print(f"Invalid grade:{e}")
        return

    students_dict[student_name] = student_grade
    print(f"Added: {student_name} -> {student_grade}")


def update_grade():
    """Update an existing student's grade (reuses the add flow)."""
    student_name = input(
        "Enter the name of the student which you want to update the grade for: "
    ).strip()
    if student_name not in students_dict:
        print(f"Student '{student_name}' not found.")
        return
    # Reuse validation
    new_grade = input("Enter updated grade: ").strip()
    try:
        new_grade = int(new_grade)
        if not 0 <= new_grade <= 100:
            raise ValueError("Enter the grade correctly(0-100)")
    except ValueError as e:
        print(f"Invalid grade:{e}")
        return
    students_dict[student_name] = new_grade
    print(f"Updated: {student_name} -> {new_grade}")


def average_grade():
    """Print the average grade with two decimal places."""
    if not students_dict:
        print("There is no student added yet!")
        return
    try:
        students_grades = [int(x) for x in list(students_dict.values())]
        print(f"Average grade: {sum(students_grades) / len(students_grades)}")
    except Exception as e:
        print(f"Could not compute average: {e}")


def save_to_file() -> None:
    """Save all students to files/grades.txt (one line per record)."""
    path = Path("files/grades.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:

        with path.open("w", encoding="utf-8") as file:
            for name, grade in students_dict.items():
                file.write(f"{name}: {grade}\n")
        print(f"Saved {len(students_dict)} records to {path}")

    except OSError as e:
        print(f"File error: {e}")


def load_from_file():
    """Load students from files/grades.txt, replacing the current dict."""
    path = Path("files/grades.txt")
    try:
        loaded: dict[str, int] = {}
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                # Strip whitespace and split the line into name and grade
                line = line.strip()
                if not line:
                    continue
                if ":" not in line:
                    print(f"skipping malformed line: {line}")
                    continue
                name, gradestr = line.split(":", 1)
                name = name.strip()
                grade = int(gradestr.strip())
                if not 0 <= grade <= 100:
                    print(f"Skipping out-of-range grade for {name}: {grade}")
                    continue
                loaded[name] = grade
        students_dict.clear()
        students_dict.update(loaded)
        print(f"Loaded {len(students_dict)} records from {path}")
    except FileNotFoundError:
        print("No saved file found yet. Try 'Save all data to file' first.")
    except (OSError, ValueError) as e:
        print(f"Error reading file: {e}")


def list_students() -> None:
    """List all students sorted by grade descending."""
    if not students_dict:
        print("No students.")
        return
    print("Students (highest grade first):")
    for name, grade in sorted(students_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"  {name}: {grade}")


def app():
    while True:
        choice = input(
            "\nSelect:\n"
            " 1. Add student and grade\n"
            " 2. Update a grade\n"
            " 3. Calculate average grade\n"
            " 4. Save all data to file\n"
            " 5. Load data from file\n"
            " 6. List all students\n"
            " 0. Exit\n"
            "Enter your choice (0-6): "
        ).strip()

        if int(choice) == 1:
            add_student()

        elif int(choice) == 2:
            update_grade()

        elif int(choice) == 3:
            average_grade()

        elif int(choice) == 4:
            save_to_file()

        elif int(choice) == 5:
            load_from_file()

        elif int(choice) == 6:
            list_students()

        elif int(choice) == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter again")


if __name__ == "__main__":
    app()