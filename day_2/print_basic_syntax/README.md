The **first "Hello World" program in Python** is one of the simplest programs you can write, using Python's built-in `print()` function to display text on the screen.

## Basic "Hello World" Program

```python
print("Hello, World!")
```

This single line of code will output:
```
Hello, World!
```

The `print()` function is a **built-in function** in Python that tells the program to display something on the screen. The text **"Hello, World!"** is a string (sequence of characters) that must be enclosed in quotation marks.

## Alternative Quote Styles

Python allows you to use different types of quotes to create strings:

```python
# Using single quotes
print('Hello, World!')

# Using double quotes  
print("Hello, World!")

# Using triple quotes
print('''Hello, World!''')
```

All three methods produce the same output.

## How the print() Function Works

The `print()` function follows this basic structure:
- **print()** is the function name, followed by parentheses
- Inside the parentheses, you place the **string** (text) you want to display
- Strings must be enclosed in quotation marks (single, double, or triple)

## Running Your First Program

To run your "Hello World" program:

1. **Create a Python file** (e.g., `hello.py`)
2. **Write the code**: `print("Hello, World!")`
3. **Save the file**
4. **Run it** using: `python hello.py`

## Additional Print Statement Examples

You can expand beyond the basic "Hello World" with these variations:

```python
# Using variables
greeting = "Hello, World!"
print(greeting)

# Printing multiple items
print("Hello", "World!")

# Using f-strings (Python 3.6+)
message = "Hello, World!"
print(f"{message}")

# String concatenation
print("Hello, " + "World!")
```

The "Hello, World!" program serves as a **traditional first program** for beginners learning any programming language, as it demonstrates basic syntax and helps verify that your programming environment is working correctly.
