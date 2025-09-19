# Python Fundamental Data Types & Variables

Let's break down what you've asked about—**variables, data types (integers, floats, strings, booleans), and naming rules**—with some examples and questions to reinforce your understanding.

## 1. **Variables & Assignment**
Variables in Python store data that can change as your program runs. You create them by *assigning* a value:

```python
spam = 42  # spam is now an integer
```

- You don't declare the type—it changes dynamically:
```python
spam = 42       # int
spam = "eggs"   # now spam is a str!
```

**Check:**
Why do you think Python lets you change a variable's type just by assigning a new value to it? What could be the benefits or risks?

## 2. **Naming Rules**
- Only use letters, digits, underscores.
- Can't start with a digit.
- Case-sensitive!
- Avoid Python keywords as variable names.

```python
my_var = 'ok'   # legal
2myvar = 'bad'  # illegal
```

**Activity:**
Come up with two legal variable names and one illegal one. Can you explain *why* the illegal name is not allowed?

## 3. **Multiple Assignment & Deletion**
Assign multiple variables at once:
```python
a = b = c = 100     # all three get 100
x, y, z = 1, 2.5, "Python" # different types
```
Delete a variable:
```python
del x
```
Trying to use `x` after it's deleted will cause a `NameError`.[1][2]

## 4. **Numeric Data Types**
- **Integers:** Whole numbers, e.g. `42`, `-2`, `0` (`int`)
- **Floats:** Decimals, e.g. `3.14`, `-1.25`, `6.022e23` (`float`)

Arithmetic examples:
```python
x = 10
print(x + 5)  # 15
print(x / 2)  # 5.0 (float result!)
```

## 5. **Strings**
Any text inside quotes is a string:
```python
name = "Alice"
greeting = 'Hello, World!'
```
- *Concatenation:* `"Hi, " + name` results in "Hi, Alice"
- *Replication:* `'Ho! ' * 3` results in "Ho! Ho! Ho! "
- *Length:* `len(greeting)`
- *Immutability:* You can't change `greeting`; you must create a new string.

## 6. **Booleans**
- `True` and `False` (no quotes!)
- Used with comparisons:
```python
is_adult = age > 18   # True if age > 18
```
- `and`, `or`, `not` combine logical statements.
- Truthy/falsy: zero, empty containers, `None`, `False` are "falsy"; everything else is "truthy".

## 7. **Type Conversion**
Use built-in functions:
```python
x = int("57")    # 57
name = str(42)   # "42"
is_ok = bool("Hello")  # True (non-empty string)
```

## Quick Memory Aid
- **int:** Whole numbers
- **float:** Decimals
- **str:** Text
- **bool:** True/False
