# Python Variable Scope: Local vs Global

Understanding **variable scope** in Python is crucial for writing clear, bug-free code. Let's break down the main types of scope, how they interact, and how they relate to function parameters and default values.

***

## 1. **Local Scope**
- **Definition:** A variable assigned inside a function is *local* to that function. It only exists while the function runs and can't be accessed outside it.
- **Example:**
  ```python
  def greet():
      message = 'Hello'
      print('Local:', message)
  greet()
  print(message)  # Error: message is not defined
  ```
- **Key Point:** Local variables are created when the function is called and destroyed when it ends.

***

## 2. **Global Scope**
- **Definition:** A variable assigned outside any function is *global*. It can be accessed from anywhere in the program, including inside functions (unless shadowed by a local variable of the same name).
- **Example:**
  ```python
  message = 'Hello'
  def greet():
      print('Inside function:', message)
  greet()
  print('Outside function:', message)
  ```
- **Key Point:** Global variables persist for the entire program and are accessible from any scope.

***

## 3. **Scope Resolution Rules**
- If you assign to a variable inside a function, Python treats it as *local* by default—even if a global variable with the same name exists.
- If you only *read* a variable inside a function (and don't assign to it), Python will use the global variable.
- To modify a global variable inside a function, use the `global` keyword:
  ```python
  a = 1
  def h():
      global a
      a = 3
  h()
  print(a)  # 3
  ```
## 4. **The `nonlocal` Keyword in Python**
- The `nonlocal` keyword is used **inside nested functions** to modify a variable from the nearest enclosing (but non-global) scope.
- This is useful when you want an inner function to update a variable defined in its outer function, rather than creating a new local variable or modifying a global one.

**Example:**
```python
def outer():
    message = "Hello"
    def inner():
        nonlocal message  # Refers to 'message' in outer()
        message = "Hello, Python!"
        print("Inside inner:", message)
    inner()
    print("Inside outer:", message)
outer()
```
**Output:**
```
Inside inner: Hello, Python!
Inside outer: Hello, Python!
```
- Here, `nonlocal message` allows the inner function to modify `message` from the outer function, not create a new local variable.

**Scope Comparison:**
| Keyword   | Scope affected         | Can modify local? | Can modify global? |
|-----------|-----------------------|-------------------|--------------------|
| nonlocal  | Enclosing function    | Yes               | No                 |
| global    | Global                | No                | Yes                |

## 5. **Default Parameters and Scope**
- **Default parameter values** are evaluated **once at function definition time**, not each time the function is called.
- If a default value refers to a global variable, it uses the value at the moment the function is defined, not when it is called.

**Example:**
```python
i = 5
def f(arg=i):
    print(arg)
i = 6
f()  # Prints 5, not 6
```
- The default value for `arg` was set to `5` when the function was defined. Changing `i` later does not affect the default.

## 6. **Mutable Default Pitfall**
- If the default is a mutable object (like a list or dictionary), it is **shared across all calls** that use the default, which can lead to persistent changes and bugs.
- **Best practice:** Use `None` as the default and create a new object inside the function if needed.

**Example:**
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
- This ensures each call gets a fresh list unless one is explicitly provided.

***
**Summary:**
- Use `nonlocal` to modify variables in the nearest enclosing function scope (not global).
- Default parameter values are set at function definition, not at call time.
- Avoid mutable objects as default parameters; use `None` and create new objects inside the function.
