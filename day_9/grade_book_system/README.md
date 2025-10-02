## 1. **Core Data Structure**
- The grade book is a dictionary where each key is a student name (string), and each value is another dictionary (the student's record).
- Each student's record is a dictionary mapping subject names (strings) to a list of grades (numbers).

**Example:**
```python
grade_book = {
    'Alice': {'Math': [90, 85], 'Science': [88]},
    'Bob': {'Math': [75], 'History': [80, 82]}
}
```

***

## 2. **Functions for System Operations**

### Add a New Student
```python
def add_student(grade_book, student_name):
    """Adds a new student to the grade book if they don't already exist."""
    if student_name not in grade_book:
        grade_book[student_name] = {}
        print(f"Student '{student_name}' has been added.")
    else:
        print(f"Student '{student_name}' already exists.")
    return grade_book
```

### Add a Grade for a Student
```python
def add_grade(grade_book, student_name, subject, grade):
    """Adds a grade to a student's record for a specific subject."""
    try:
        grade = float(grade)
        if not (0 <= grade <= 100):
            print("Error: Grade must be between 0 and 100.")
            return grade_book
    except ValueError:
        print("Error: Invalid grade. Please enter a numeric value.")
        return grade_book

    if student_name in grade_book:
        student_record = grade_book[student_name]
        student_record.setdefault(subject, []).append(grade)
        print(f"Added grade {grade} for {student_name} in {subject}.")
    else:
        print(f"Error: Student '{student_name}' not found.")
    return grade_book
```

### Calculate Average Grade
```python
def calculate_average(student_record, subject=None):
    """Calculates the average for a specific subject or all subjects."""
    if subject:
        if subject in student_record:
            grades = student_record[subject]
            return sum(grades) / len(grades) if grades else 0.0
        else:
            return 0.0
    else:
        all_grades = []
        for grades in student_record.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0.0
```

### Display Student Report Card
```python
def display_report_card(grade_book, student_name):
    """Displays a formatted report card for a student."""
    if student_name not in grade_book:
        print(f"Error: Student '{student_name}' not found.")
        return

    print(f"\n--- Report Card for {student_name} ---")
    student_record = grade_book[student_name]

    if not student_record:
        print("No grades recorded yet.")
        print("---------------------------------")
        return

    for subject, grades in student_record.items():
        average = calculate_average(student_record, subject)
        grades_str = ", ".join(map(str, grades))
        print(f"  Subject: {subject}")
        print(f"    Grades: {grades_str}")
        print(f"    Average: {average:.2f}")

    overall_average = calculate_average(student_record)
    print(f"\n  Overall Average: {overall_average:.2f}")
    print("---------------------------------")
```

***

## 3. **Main Program Loop (User Interface)**
```python
def main():
    """The main function to run the grade book system."""
    grade_book = {}
    while True:
        print("\n--- Student Grade Book Menu ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Display Report Card")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            name = input("Enter student's name: ")
            grade_book = add_student(grade_book, name)
        elif choice == '2':
            name = input("Enter student's name: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            grade_book = add_grade(grade_book, name, subject, grade)
        elif choice == '3':
            name = input("Enter student's name: ")
            display_report_card(grade_book, name)
        elif choice == '4':
            print("Exiting the grade book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
```

***

## **Key Concepts Practiced**
- **Dictionaries & Nested Dictionaries:** For structured, efficient data storage.
- **Functions:** For modular, reusable code.
- **Loops & Conditionals:** For user interaction and data processing.
- **Error Handling:** To prevent crashes and guide the user.
- **String Manipulation:** For clear, formatted output.

***

**Try extending this system:**
- Add the ability to remove students or subjects.
- Calculate and display letter grades.
- Save/load the grade book to a file for persistence.
