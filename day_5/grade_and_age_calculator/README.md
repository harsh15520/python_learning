## 1. **Basic Grade Calculator**
A simple program assigns a grade based on a single `if-else` statement:

```python
mark = int(input("Enter your mark: "))
if mark >= 50:
    print("Pass")
else:
    print("Fail")
```
- **Checks one condition:** pass or fail.

***

## 2. **Intermediate Grade Calculator**
Use an `if-elif-else` chain to assign letter grades:

```python
mark = int(input("Enter your mark: "))
if mark >= 90:
    print("A")
elif mark >= 80:
    print("B")
elif mark >= 70:
    print("C")
elif mark >= 60:
    print("D")
else:
    print("F")
```
- **Multiple conditions:** more detailed grading.

***

## 3. **Advanced Grade Calculator**
Add input validation and error handling:

```python
try:
    mark = int(input("Enter your mark (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid mark.")
    elif mark >= 90:
        print("A")
    elif mark >= 80:
        print("B")
    elif mark >= 70:
        print("C")
    elif mark >= 60:
        print("D")
    else:
        print("F")
except ValueError:
    print("Please enter a valid number.")
```
- **Handles errors and invalid input.**

***

## 4. **Basic Age Classifier**
Classifies age with a simple `if-else`:

```python
age = int(input("Enter your age: "))
if age < 18:
    print("Minor")
else:
    print("Adult")
```
- **Simple two-category classification.**

***

## 5. **Intermediate Age Classifier**
Use `if-elif-else` for more categories:

```python
age = int(input("Enter your age: "))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```
- **Multiple age groups.**

***

## 6. **Advanced Age Classifier (Nested Conditionals)**
Add a nested check for club membership among seniors:

```python
try:
    age = int(input("Enter your age: "))
    is_member = True  # or False
    if age < 0:
        print("Invalid age.")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age < 65:
        print("Adult")
    else:
        if is_member:
            print("Senior Club Member")
        else:
            print("Senior")
except ValueError:
    print("Please enter a valid number.")
```
- **Nested conditional:** checks for membership only if age is 65 or above.
- **Error handling:** for invalid input.

***

## **Summary Table**
| Level         | Grade Calculator Features         | Age Classifier Features           |
|--------------|-----------------------------------|-----------------------------------|
| Basic        | Pass/Fail                         | Minor/Adult                       |
| Intermediate | Letter grades (A-F)               | Child/Teenager/Adult/Senior       |
| Advanced     | Input validation, error handling  | Nested club member check, errors  |

***
