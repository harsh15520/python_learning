## Accessing Docstrings in Python

**Docstrings** are special string literals used to document functions, classes, and modules. They are not ignored by the interpreter and can be accessed at runtime, making them a powerful tool for code clarity and maintainability.

### How to Access Docstrings

- **Using `__doc__` attribute:**
  - Returns the docstring as a string.
  - Example:
    ```python
    def power(a: int, b: int) -> int:
        """
        Raises a number to a power.

        Args:
            a (int): The base number.
            b (int): The exponent.

        Returns:
            int: The result of a raised to the power b.
        """
        return a ** b

    print(power.__doc__)
    ```
  - Output:
    ```
    Raises a number to a power.

    Args:
        a (int): The base number.
        b (int): The exponent.

    Returns:
        int: The result of a raised to the power b.
    ```

- **Using `help()` function:**
  - Displays the docstring in a structured, interactive format, including the function signature and more details.
  - Example:
    ```python
    help(power)
    ```
  - Output (truncated for clarity):
    ```
    Help on function power in module __main__:
    power(a: int, b: int) -> int
        Raises a number to a power.

        Args:
            a (int): The base number.
            b (int): The exponent.

        Returns:
            int: The result of a raised to the power b.
    ```
## Why Use Type Hints and Comments in Python?

### **Type Hints**
Type hints (like `a: int, b: int -> int`) clarify what types your function expects and returns. They act as a form of documentation, making your code easier to read and understand for both humans and tools.[2][5][6]

**Benefits:**
- **Improved readability:** Type hints show at a glance what types are expected, making code easier to follow.[5][7][2]
- **Error detection:** Static analysis tools (like `mypy` or `pyright`) use type hints to catch type-related bugs before runtime.[6][8][2]
- **Better IDE support:** Many editors use type hints for code completion, navigation, and refactoring.[8][9][2]
- **Facilitates teamwork:** In large projects, type hints help developers understand data flow and function contracts.[2][5]

**Limitations:**
- **Not enforced at runtime:** Type hints are only hints; Python does not raise errors if types don't match.[3][7][2]
- **May be overkill for small scripts:** For simple code, type hints can add unnecessary complexity.[6][2]

**Example:**
```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

### **Comments**
Comments (`# ...`) inside functions explain complex or non-obvious logic. While docstrings describe *what* a function does, comments clarify *how* it works.

**Benefits:**
- **Clarify tricky code:** Comments help others (and your future self) understand why certain steps are taken.
- **Document business logic:** Useful for explaining algorithms, edge cases, or temporary code sections.

**Example:**
```python
def factorial(n: int) -> int:
    """Returns the factorial of n."""
    result = 1
    # Loop from 1 to n, multiplying result by each number
    for i in range(1, n + 1):
        result *= i
    return result
```

### **Summary**
- **Type hints** make code more readable, help catch errors early, and improve tooling, but are not enforced at runtime.[5][2][6]
- **Comments** explain the reasoning behind code, especially for complex logic.
- **Docstrings** describe what a function does; **comments** explain how it does it.
