Here is a comprehensive overview of **for loops**, the **range() function**, and **while loops** in Python, including common use cases and control statements.

### for Loops

A *for loop* in Python allows iteration over any iterable sequence, such as lists, strings, tuples, dictionaries, or ranges. The loop assigns each element of the sequence to a variable in turn, executing the indented code block for every item.
- **Syntax:**  
  ```python
  for var in iterable:
      # statements
  ```
- **Examples with common iterables:**  
  - **String:**  
    ```python
    s = "Geeks"
    for i in s:
        print(i)
    # Prints: G e e k s (each on a new line)
    ```
  - **List:**  
    ```python
    s = ["Geeks", "for", "Geeks"]
    for i in s:
        print(i)
    # Prints: Geeks for Geeks (each on a new line)
    ```
  - **Dictionary:**  
    ```python
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)
    # Prints: gallahad the pure, robin the brave
    ```

### The range() Function

The `range()` function creates a memory-efficient sequence of numbers, commonly used for index-based iteration with for loops.
- **range(stop):** 0 up to, but not including, stop.
  - Example: `range(5)` → 0, 1, 2, 3, 4
- **range(start, stop):** start up to, but not including, stop.
  - Example: `range(5, 10)` → 5, 6, 7, 8, 9
- **range(start, stop, step):** increment by step.
  - Example: `range(0, 10, 2)` → 0, 2, 4, 6, 8
- **Iterating by index:**  
  ```python
  a = ['Mary', 'had', 'a', 'little', 'lamb']
  for i in range(len(a)):
      print(i, a[i])
  ```
- **More Pythonic:**  
  Use `enumerate()` for both index and item.

### while Loops

A *while loop* keeps executing its body as long as a specified condition remains true. It checks the condition before every iteration.
- **Syntax:**  
  ```python
  while condition:
      # statements
  ```
- **Example:**  
  ```python
  spam = 0
  while spam < 5:
      print('Hello, world.')
      spam = spam + 1
  # Prints 'Hello, world.' five times
  ```

### Loop Control Statements

Both for and while loops support control statements to modify loop flow:
- **break:** Immediately exits the innermost loop.
- **continue:** Skips the rest of the current iteration; resumes with the next loop evaluation.
- **else:** Runs if the loop concludes without being interrupted by `break`.
- **pass:** Null statement, useful as a placeholder.

This explanation covers practical Python loop usage, control techniques, and examples with common iterables and the `range()` function.
