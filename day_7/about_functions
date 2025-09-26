# Defining Functions, Parameters, and Return Statements in Python

Let's break down how to define and use functions in Python, including parameters, arguments, and return values.

***

## 1. **Function Definition**
- Use the `def` keyword, followed by the function name and parentheses (with optional parameters).
- The function body is indented.
- An optional docstring (triple-quoted string) can describe the function's purpose.
- The `return` statement sends a value back to the caller (optional).

**Example:**
```python
def greet():
    """Prints a welcome message."""
    print("Welcome to Python!")

greet()  # Function call
```

***

## 2. **Parameters and Arguments**
- **Parameters** are variables in the function definition.
- **Arguments** are the actual values you pass when calling the function.

**Positional Arguments:**
```python
def say_hello(name):
    print('Hello, ' + name)

say_hello('Al')  # 'Al' is the argument
```

**Keyword Arguments:**
```python
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')
```

**Default Arguments:**
```python
def my_fun(x, y=50):
    print("x:", x)
    print("y:", y)

my_fun(10)  # y defaults to 50
```

**Mutable Default Pitfall:**
Avoid using mutable objects (like lists) as default values.
```python

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

**Arbitrary Argument Lists:**
- `*args` collects extra positional arguments as a tuple.
- `**kwargs` collects extra keyword arguments as a dictionary.
```python
def my_fun(*args):
    for arg in args:
        print(arg)

my_fun('Hello', 'World')
```

***

## 3. **Return Statements**
- `return` exits the function and optionally sends a value back.
- If omitted, the function returns `None` by default.
- Multiple values separated by commas are returned as a tuple.

**Example:**
```python
def square_value(num):
    """Returns the square of the number."""
    return num ** 2

print(square_value(2))   # Output: 4
print(square_value(-4))  # Output: 16
```

***
