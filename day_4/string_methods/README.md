# Python String Methods & Formatting Overview

Python's built-in string methods make manipulation easy, **efficient**, and readable. All are immutable: methods return a *new* string; the original isn’t changed.

## **Common String Methods**

**1. Case Transformation:**
- `upper()`: all uppercase
- `lower()`: all lowercase
- `casefold()`: aggressive lowercasing (best for international/insensitive compares)
- `isupper()`, `islower()`: tests if all letters are upper/lower

**2. Splitting & Joining:**
- `split()`: splits string into list by delimiter (default: whitespace). `maxsplit` limits splits.
- Example:
  ```python
  s = "My name is Simon"
  print(s.split())  # ['My', 'name', 'is', 'Simon']
  print(s.split('a'))  # ['My n', 'me is Simon']
  ```
- `join()`: joins iterable of strings, placing the separator between.
  ```python
  words = ["apple", "banana", "cherry"]
  print(", ".join(words))  # apple, banana, cherry
  ```

**3. Slicing & Indexing:**
- Slicing: `s[start:stop]` (stop not included), steps: `s[::-1]` reverses
- Indexing: `s`, `s[-1]`, only integer indices

**4. Other Useful Methods:**
- `strip()`, `lstrip()`, `rstrip()`: remove whitespace or specified chars from ends
- `replace(old, new, count=None)`: replace appearances of substring
- `startswith(prefix)`, `endswith(suffix)`: True/False for checks at string's ends
- `len(s)`: number of characters
- `format()`: basic formatting (see below)

## **String Formatting**
Python offers several ways to insert variables/expressions into strings:

### **Formatted String Literals (f-strings) — Best Practice for New Code (Python 3.6+)**
- Prefix string with `f`, use `{}` for variables/expressions
- Example:
  ```python
  name = "Alice"
  age = 25
  print(f"My name is {name} and I am {age} years old.")
  price = 49.99
  print(f"Price is {price:.2f} dollars")  # modifiers like .2f for float
  ```
- **Benefits:** Fast, readable, supports complex expressions and formatting in-place[1][2][3][4][5][7]

### **str.format() Method — Flexible & Older**
- Uses `{}` placeholders, filled by `.format()` arguments
- Example:
  ```python
  print("My name is {} and I am {} years old.".format(name, age))
  print("Price is {:.2f} dollars".format(price))
  ```
- Can use dictionary unpacking: `"Name: {name}, Age: {age}".format(**person_dict)`

### **% Operator — Oldest, Discouraged for New Code**
- C-like syntax; less readable, quirks with tuples/dicts
- Example:
  ```python
  print("My name is %s and I am %d years old." % (name, age))
  ```

## **Immutability Recap**
- Methods return new strings; direct modifications aren't allowed.
- To "change" a string, reassign: `s = s.upper()`
