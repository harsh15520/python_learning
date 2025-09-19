# Exploring Python Data Types and Type Conversion

Let's walk through your breakdown of built-in **Python data types** and how to convert between them, using short sample programs for each. We'll check your understanding step by step.

## 1. Numeric Types: int, float, complex
Numeric types represent whole, decimal, and complex numbers.

```python
# Integer
n = 12
print(type(n))  # <class 'int'>

# Float
f = 3.14
print(type(f))  # <class 'float'>

# Complex
c = 2 + 3j
print(type(c))  # <class 'complex'>
```

**Question:** What is the output of `type(3.0)`?

***

## 2. Sequence Types: str, list, tuple
Sequence types store ordered collections of items.

```python
# String
s = "Hello"
print(type(s))  # <class 'str'>

# List
l = [1, 2, "three"]
print(type(l))  # <class 'list'>

# Tuple
t = (1, 2, 3)
print(type(t))  # <class 'tuple'>
```

How would you make a list that contains both numbers and strings?

***

## 3. Mapping Type: dict
Dictionaries store key-value pairs.

```python
info = {"name": "Alice", "age": 25}
print(type(info))  # <class 'dict'>
```
Try modifying the value for the key "age". What code changes would you make?

***

## 4. Boolean Type: bool
The bool type holds `True` or `False`.

```python
is_valid = True
print(type(is_valid))  # <class 'bool'>
print(is_valid == 1)   # True, since True acts like 1
```
What does `bool(0)` return? What does `bool("hello")` return?

***

## 5. Set Type: set, frozenset
Sets hold unordered, unique items; frozenset is immutable.

```python
s = set([1, 2, 2, 3])
print(s)           # {1, 2, 3}
print(type(s))     # <class 'set'>

fs = frozenset(["A", "B", "C"])
print(type(fs))    # <class 'frozenset'>
```
What happens if you try to add an element to a frozenset?

***

## 6. Binary Types: bytes, bytearray, memoryview

```python
b = b"Python"
print(type(b))   # <class 'bytes'>
ba = bytearray(b)
print(type(ba))  # <class 'bytearray'>
mv = memoryview(b)
print(type(mv))  # <class 'memoryview'>
```

When would you use bytes instead of string?

***

# Type Conversion Examples
Python lets you change the type of a value using constructor functions.

```python
# Convert string to integer
my_str = "123"
my_int = int(my_str)     # 123

# Convert float to integer
my_float = 7.89
my_int2 = int(my_float)  # 7 (decimal part chopped)

# Convert list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# Convert tuple to set
my_tuple2 = ("a", "b", "a")
my_set = set(my_tuple2)  # {'a', 'b'}

# Convert int to string
x = 30
s = str(x)  # "30"
```

**Activity:** Try casting the string "3.14" to a float, then to an int. Can both conversions succeed? What errors do you get?

***

# Quick Review
- **int, float, complex**: for numbers
- **str, list, tuple**: for ordered collections
- **dict**: for mappings
- **bool**: for logic
- **set, frozenset**: for unique collections
