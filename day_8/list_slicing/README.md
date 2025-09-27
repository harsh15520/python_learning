## 1. List Creation

- **Using square brackets:**
  ```python
  empty_list = []
  numbers = [1, 2, 3, 4, 5]
  mixed_list = ['hello', 3.1415, True, None, 42]
  ```
- **Using the `list()` constructor:**
  ```python
  my_tuple = ('cat', 'dog', 5)
  my_list = list(my_tuple)  # ['cat', 'dog', 5]
  char_list = list('hello') # ['h', 'e', 'l', 'l', 'o']
  ```
- **Using list comprehensions:**
  ```python
  squares = [x**2 for x in range(10)]  # [0, 1, 4, ..., 81]
  vec = [-4, -2, 0, 2, 4]
  doubled = [x*2 for x in vec]         # [-8, -4, 0, 4, 8]
  positives = [x for x in vec if x >= 0]  # [0, 2, 4]
  ```

***
## 2. List Indexing

- **Positive indexing (starts at 0):**
  ```python
  spam = ['cat', 'bat', 'rat', 'elephant']
  print(spam[0])  # 'cat'
  print(spam[2])  # 'rat'
  ```
- **Negative indexing (from the end):**
  ```python
  print(spam[-1])  # 'elephant'
  print(spam[-3])  # 'bat'
  ```
- **Nested lists:**
  ```python
  spam = [['cat', 'bat'], [10, 20, 30]]
  print(spam[0][1])  # 'bat'
  print(spam[1][2])  # 30
  ```

***

## 3. List Slicing

- **Basic slicing:**
  ```python
  spam = ['cat', 'bat', 'rat', 'elephant']
  print(spam[1:3])  # ['bat', 'rat']
  ```
- **Omitting start or stop:**
  ```python
  print(spam[:2])   # ['cat', 'bat']
  print(spam[1:])   # ['bat', 'rat', 'elephant']
  print(spam[:])    # ['cat', 'bat', 'rat', 'elephant'] (shallow copy)
  ```
- **Slicing with a step:**
  ```python
  numbers = list(range(10))
  print(numbers[0:10:2])  # [0, 2, 4, 6, 8]
  print(numbers[::-1])    # [9, 8, 7, ..., 0] (reversed)
  ```

***

## 4. Common List Methods

- `append(x)`: Add an item to the end of the list.
- `extend(iterable)`: Add all items from another iterable.
- `insert(i, x)`: Insert an item at a given position.
- `remove(x)`: Remove the first occurrence of x.
- `pop([i])`: Remove and return item at position i (default last).
- `clear()`: Remove all items from the list.
- `index(x)`: Return the index of the first occurrence of x.
- `count(x)`: Return the number of times x appears.
- `sort()`: Sort the list in place.
- `reverse()`: Reverse the list in place.
- `copy()`: Return a shallow copy of the list.

**Example:**
```python
a = [1, 2, 3]
a.append(4)        # [1, 2, 3, 4]
a.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
a.insert(2, 99)    # [1, 2, 99, 3, 4, 5, 6]
a.remove(99)       # [1, 2, 3, 4, 5, 6]
a.pop()            # [1, 2, 3, 4, 5]
a.sort()           # [1, 2, 3, 4, 5]
a.reverse()        # [5, 4, 3, 2, 1]
```

***
## Shallow Copy vs. Deep Copy in Python

Understanding the difference between **shallow copy** and **deep copy** is crucial when working with lists or other complex objects in Python, especially if they contain nested mutable elements like other lists or dictionaries.

***

### **Shallow Copy**
- **What it does:** Creates a new outer object (like a list), but the elements inside are *references* to the same objects as in the original. No nested objects are copied—just their references.
- **How to make one:** Use `a[:]`, `a.copy()`, or `copy.copy(a)`.
- **Effect:**
  - Changes to the *outer* list (like adding/removing elements) do **not** affect the original.
  - Changes to *nested* mutable elements (like modifying a sublist or dictionary) **do** affect both the original and the copy, since they point to the same objects.

**Example:**
```python
import copy
origin = [[1, 2], [3, 4]]
shallow_copy = copy.copy(origin)
shallow_copy[0][0] = 99
print(origin)        # [[99, 2], [3, 4]]
print(shallow_copy)  # [[99, 2], [3, 4]]
```
- Modifying a nested element in `shallow_copy` also changes it in `origin`.

***

### **Deep Copy**
- **What it does:** Recursively copies *all* nested objects, so the new object is completely independent of the original.
- **How to make one:** Use `copy.deepcopy(a)`.
- **Effect:**
  - Changes to any part of the deep copy (outer or nested) do **not** affect the original, and vice versa.

**Example:**
```python
import copy
origin = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(origin)
deep_copy[0][0] = 99
print(origin)    # [[1, 2], [3, 4]]
print(deep_copy) # [[99, 2], [3, 4]]
```
- Modifying a nested element in `deep_copy` does **not** change `origin`.

***

### **Summary Table**
| Copy Type     | Outer Object | Nested Objects | Changes to Nested Affect Original? |
|---------------|--------------|---------------|------------------------------------|
| Shallow Copy  | New          | Shared        | Yes                                |
| Deep Copy     | New          | New           | No                                 |

***

### **When to Use Which?**
- Use **shallow copy** when you want a new container but are okay with sharing the inner objects (e.g., for performance or when you don't plan to mutate nested data).
- Use **deep copy** when you need a completely independent copy, including all nested data structures.

If you want to see more real-world examples or practice with nested lists, let me know!

## **Quick Practice**
- Try creating a list of the first 10 even numbers using a list comprehension.
- Use slicing to get the last three elements of a list.
- Use `append()` and `pop()` to add and remove elements from a list.
