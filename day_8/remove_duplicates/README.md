## 1. **Using `set()` (Order Not Preserved)**
- **How it works:** Convert the list to a set (which only keeps unique elements), then back to a list.
- **Pros:** Fast and concise, especially for large lists.
- **Cons:** The original order of elements is lost.

**Example:**
```python
my_list = ['a', 'b', 'a', 'c', 'c']
unique_list = list(set(my_list))
print(unique_list)  # Output might be ['c', 'a', 'b'] or another order
```
- **Best for:** When you only care about unique items and order doesn't matter.

***

## 2. **Using a Loop to Preserve Order**
- **How it works:** Iterate through the list, adding each item to a new list only if it hasn't been added before.
- **Pros:** Preserves the original order of elements.
- **Cons:** Slower for large lists, since `in` checks get slower as the list grows.

**Example:**
```python
my_list = ['a', 'b', 'a', 'c', 'c']
unique_ordered_list = []
for item in my_list:
    if item not in unique_ordered_list:
        unique_ordered_list.append(item)
print(unique_ordered_list)  # Output: ['a', 'b', 'c']
```
- **Best for:** When you need to keep the original order of items.

***
## 3. Removing Duplicates with `dict.fromkeys()` in Python

The `dict.fromkeys()` method is a powerful and efficient way to remove duplicates from a list **while preserving the original order** of elements. This approach is widely used in modern Python (3.7+), where dictionaries maintain insertion order by default.

### **How It Works**
- When you call `dict.fromkeys(my_list)`, Python creates a dictionary where each unique item in `my_list` becomes a key.
- Dictionaries cannot have duplicate keys, so any repeated items are automatically discarded.
- Since Python 3.7, dictionaries remember the order in which keys are added, so the order of first appearances is preserved.
- Finally, you convert the dictionary's keys back into a list using `list()`.

**Example:**
```python
my_list = ['a', 'b', 'a', 'c', 'c']
unique_list = list(dict.fromkeys(my_list))
print(unique_list)  # Output: ['a', 'b', 'c']
```

### **Step-by-Step Explanation**
1. **Original List:**
   ```python
   my_list = ['a', 'b', 'a', 'c', 'c']
   ```
2. **Create Dictionary from Keys:**
   ```python
   temp_dict = dict.fromkeys(my_list)
   # temp_dict is {'a': None, 'b': None, 'c': None}
   ```
3. **Convert Keys Back to List:**
   ```python
   unique_list = list(temp_dict)
   # unique_list is ['a', 'b', 'c']
   ```

### **Why Use This Method?**
- **Order is preserved:** The first occurrence of each item is kept, later duplicates are ignored.[1][3][6][7][8]
- **Efficient:** Much faster than looping with `if item not in ...` for large lists.
- **Concise:** One line of code.

### **Comparison with `set()`**
- `set(my_list)` removes duplicates but does **not** preserve order (the result may be jumbled).
- `dict.fromkeys(my_list)` removes duplicates **and** keeps the original order.

**Example:**
```python
a = [1, 16, 2, 3, 4, 5, 6, 8, 10, 3, 9, 15, 7]
print(list(set(a)))              # Order not preserved
print(list(dict.fromkeys(a)))    # Order preserved
```

### **When to Use**
- Use `list(dict.fromkeys(my_list))` when you want to remove duplicates **and** keep the order of the first appearance of each item.
- For large lists where order matters, this is the most Pythonic and efficient solution.

### **Limitations**
- Only works for hashable (immutable) items (e.g., numbers, strings, tuples). Lists or other mutable types in the list will cause a `TypeError`.
- Slightly less intuitive for beginners, but very common in professional Python code.

***
**Summary:**
- `list(dict.fromkeys(my_list))` is the go-to method for removing duplicates from a list while preserving order in Python 3.7+.
- It's fast, concise, and widely used in real-world codebases.

- **Best for:** When you want both efficiency and order preservation.

***

## **Summary Table**
| Method                | Order Preserved? | Performance         | Example Code                        |
|-----------------------|:---------------:|--------------------|-------------------------------------|
| `list(set(lst))`      | No              | Fast               | `list(set(my_list))`                |
| Loop + `append()`     | Yes             | Slower for big lists| See loop example above              |
| `list(dict.fromkeys())`| Yes            | Fast for big lists | `list(dict.fromkeys(my_list))`      |

***

## **Key Takeaways**
- Use `set()` for quick deduplication when order doesn't matter.
- Use a loop or `dict.fromkeys()` when you need to keep the original order.
- For large lists where order matters, `dict.fromkeys()` is usually the best choice.
