## 1. `append()`
- **Purpose:** Adds a single item to the end of the list.
- **Syntax:** `list.append(x)`
- **Usage:** Ideal for adding items one by one, especially in a loop.
- **Example:**
  ```python
  spam = ['cat', 'dog', 'bat']
  spam.append('moose')
  # Result: ['cat', 'dog', 'bat', 'moose']
  ```

***

## 2. `extend()`
- **Purpose:** Adds each element of another iterable (like a list, tuple, string) to the end of your list.
- **Syntax:** `list.extend(iterable)`
- **Usage:** Use when you want to merge two lists or add multiple items at once.
- **Example:**
  ```python
  a = [1, 2, 3]
  a.extend([4, 5])
  # Result: [1, 2, 3, 4, 5]
  ```
- **Difference from `append()`:** `append()` would add the entire list as a single element: `[1, 2, 3, ]`.

***

## 3. `pop()`
- **Purpose:** Removes and returns the item at a specified index (or the last item by default).
- **Syntax:** `list.pop([i])`
- **Usage:** Useful for stack-like operations (last-in, first-out) or removing and using an element.
- **Example:**
  ```python
  stack = [1, 2, 3]
  last_item = stack.pop()
  # last_item is 3, stack is now [1, 2]
  second_item = stack.pop(0)
  # second_item is 1, stack is now [2]
  ```

***

## 4. Python List `remove()` Method

The `remove()` method is used to delete the **first occurrence** of a specified value from a list. It modifies the list in place and does **not** return a value (returns `None`).

### **Syntax**
```python
list.remove(x)
```
- `x`: The value you want to remove (can be a string, number, list, etc.)

### **How It Works**
- Scans the list from left to right.
- Removes the first item that matches the specified value.
- If the value is not found, it raises a `ValueError`.

### **Examples**
```python
fruits = ['apple', 'banana', 'cherry', 'banana', 'kiwi']
fruits.remove('banana')
print(fruits)  # ['apple', 'cherry', 'banana', 'kiwi']
```
- Only the **first** 'banana' is removed.

#### **Removing Multiple Values**
To remove all occurrences, you can use a loop or list comprehension:
```python
while 'banana' in fruits:
    fruits.remove('banana')
# or
fruits = [x for x in fruits if x != 'banana']
```

#### **Error Handling**
If the value is not present:
```python
try:
    fruits.remove('orange')
except ValueError:
    print("Value not found in list.")
```

### **Key Points**
- Removes by value, **not** by index.
- Only the first matching value is removed.
- Raises `ValueError` if the value is not found.
- Does **not** return the removed value; returns `None`.
  
## 5. `sort()`
- **Purpose:** Sorts the list in ascending order (default) or descending order with `reverse=True`.
- **Syntax:** `list.sort(key=None, reverse=False)`
- **Usage:** Use for organizing lists of numbers or strings.
- **Example:**
  ```python
  nums = [5, 2, 3, 1, 4]
  nums.sort()
  # Result: [1, 2, 3, 4, 5]
  nums.sort(reverse=True)
  # Result: [5, 4, 3, 2, 1]
  names = ['Alice', 'bob', 'Carol']
  names.sort(key=str.lower)
  # Result: ['Alice', 'bob', 'Carol']
  ```

***
