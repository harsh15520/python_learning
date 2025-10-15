# Python Sets: Unique Elements and Set Operations - Complete Guide

## **What Makes Sets Unique**

Python sets are **unordered collections that store only unique elements**. This fundamental property makes them exceptionally useful for removing duplicates and performing mathematical set operations efficiently.

### **Key Characteristics**
1. **No Duplicates:** Sets automatically remove duplicate values
2. **Unordered:** Elements have no fixed position or index
3. **Mutable:** You can add/remove elements (but the elements themselves must be immutable/hashable)
4. **Hashable Elements Only:** Can contain numbers, strings, tuples (not lists, dicts, or other sets)

```python
# Automatic duplicate removal
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# Convert list to remove duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
unique = set(my_list)  # {1, 2, 3, 4, 5}
```

***

## **Creating Sets**

```python
# Curly braces
s = {1, 2, 3}

# set() constructor
s = set([1, 2, 3])

# Empty set (must use set(), not {})
empty = set()

# From string
chars = set("hello")  # {'h', 'e', 'l', 'o'}

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

***

## **Complete Set Operations**

### **1. Union (|)** - All elements from both sets
Combines all unique elements from multiple sets.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Operator
print(A | B)  # {1, 2, 3, 4, 5, 6}

# Method (accepts any iterable)
print(A.union(B))  # {1, 2, 3, 4, 5, 6}
print(A.union([5, 6, 7]))  # Works with lists too
```

### **2. Intersection (&)** - Common elements only
Returns elements that exist in all sets.

```python
print(A & B)  # {3, 4}
print(A.intersection(B))  # {3, 4}

# Multiple sets
C = {3, 6, 7}
print(A & B & C)  # {3}
```

### **3. Difference (-)** - Elements in first but not in second
Returns elements from the first set that aren't in the other(s).

```python
print(A - B)  # {1, 2}
print(B - A)  # {5, 6}
print(A.difference(B))  # {1, 2}
```

### **4. Symmetric Difference (^)** - Elements in either but not both
Returns elements that are in exactly one of the sets.

```python
print(A ^ B)  # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
```

### **5. Subset/Superset Tests**
```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print(A <= B)  # True (A is subset of B)
print(A < B)   # True (A is proper subset)
print(B >= A)  # True (B is superset of A)
print(B > A)   # True (B is proper superset)
print(A.issubset(B))  # True
print(B.issuperset(A))  # True
```

### **6. Disjoint Test**
```python
A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))  # True (no common elements)
```

***

## **Set Operations Summary Table**

| Operation | Operator | Method | Returns |
|-----------|----------|--------|---------|
| Union | `A \| B` | `A.union(B)` | All elements from both |
| Intersection | `A & B` | `A.intersection(B)` | Common elements |
| Difference | `A - B` | `A.difference(B)` | Elements in A not in B |
| Symmetric Diff | `A ^ B` | `A.symmetric_difference(B)` | Elements in A or B, not both |
| Subset | `A <= B` | `A.issubset(B)` | True if A ⊆ B |
| Superset | `A >= B` | `A.issuperset(B)` | True if A ⊇ B |
| Disjoint | N/A | `A.isdisjoint(B)` | True if A ∩ B = ∅ |

***

## **Modifying Sets**

### **Adding Elements**
```python
s = {1, 2, 3}
s.add(4)              # Add single element
s.update([5, 6, 7])   # Add multiple elements
s |= {8, 9}           # In-place union
```

### **Removing Elements**
```python
s.remove(3)    # Raises KeyError if not found
s.discard(10)  # No error if not found
s.pop()        # Removes arbitrary element
s.clear()      # Removes all elements
```

### **In-Place Operations**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A |= B   # In-place union: A.update(B)
A &= B   # In-place intersection: A.intersection_update(B)
A -= B   # In-place difference: A.difference_update(B)
A ^= B   # In-place symmetric difference
```

***

## **Practical Use Cases**

### **1. Remove Duplicates**
```python
emails = ["alice@example.com", "bob@example.com", "alice@example.com"]
unique_emails = list(set(emails))
```

### **2. Find Common Elements**
```python
course1_students = {"Alice", "Bob", "Charlie"}
course2_students = {"Bob", "Diana", "Charlie"}
both_courses = course1_students & course2_students  # {'Bob', 'Charlie'}
```

### **3. Find Unique to Each Set**
```python
only_course1 = course1_students - course2_students  # {'Alice'}
only_course2 = course2_students - course1_students  # {'Diana'}
```

### **4. Fast Membership Testing**
```python
# O(1) average time complexity
valid_users = {"alice", "bob", "charlie"}
if "alice" in valid_users:  # Very fast
    print("Valid user")
```

### **5. Data Cleaning**
```python
# Remove stopwords
words = ["the", "cat", "and", "the", "dog"]
stopwords = {"the", "and", "or"}
clean_words = set(words) - stopwords  # {'cat', 'dog'}
```

***

## **frozenset: Immutable Sets**

For situations requiring immutable sets (e.g., as dictionary keys):

```python
# Create immutable set
fs = frozenset([1, 2, 3])

# Use as dict key
d = {fs: "immutable set key"}

# Use in another set
s = {frozenset([1, 2]), frozenset([3, 4])}
```

***

## **Important Notes**

1. **Hashability Requirement:** Elements must be immutable (numbers, strings, tuples with immutable contents)
2. **Order Not Guaranteed:** Sets don't maintain insertion order
3. **No Indexing:** Cannot access elements by position: `s[0]` raises TypeError
4. **Operators vs Methods:** Operators require set arguments; methods accept any iterable
5. **Numeric Equality:** `1` and `1.0` are considered equal, only one will appear in set

***

## **Performance Benefits**

Sets are implemented as hash tables, providing:
- **O(1)** average time for membership testing
- **O(1)** average time for adding/removing elements
- Extremely efficient for large collections
- Much faster than lists for membership checks

***
