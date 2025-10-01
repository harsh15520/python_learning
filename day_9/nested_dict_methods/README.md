# Python Dictionary Methods and Nested Dictionaries

Let's break down the most important **dictionary methods** in Python and how to work with **nested dictionaries**. These tools help you efficiently store, access, and manipulate complex data structures.

***

## 1. **Accessing Data**
- **`get(key, default=None)`**: Safely retrieves a value for a key. Returns `default` (or `None`) if the key doesn't exist, avoiding `KeyError`.
  ```python
  picnic = {'apples': 5, 'cups': 2}
  print(picnic.get('eggs', 0))  # 0
  print(picnic.get('apples', 0))  # 5
  ```
- **`keys()`**, **`values()`**, **`items()`**: Return dynamic views of the dictionary's keys, values, or key-value pairs (as tuples). Useful for iteration and inspection.
  ```python
  spam = {'color': 'red', 'age': 42}
  print(list(spam.keys()))    # ['color', 'age']
  print(list(spam.values()))  # ['red', 42]
  print(list(spam.items()))   # [('color', 'red'), ('age', 42)]
  for k, v in spam.items():
      print(f"Key: {k}, Value: {v}")
  ```

***
# Python Dictionary `update()` Method: Adding and Updating Data

The `update()` method is a powerful way to add new key-value pairs to a dictionary or update the values of existing keys. It works with another dictionary, an iterable of key-value pairs (like a list of tuples), or keyword arguments.

***

## **How `update()` Works**
- **If the key exists:** The value is updated (overwritten) with the new value.
- **If the key does not exist:** The key-value pair is added to the dictionary.
- **No return value:** The method modifies the dictionary in place and returns `None`.

***

## **Syntax**
```python
dict.update([other])
```
- `other` can be a dictionary, an iterable of key-value pairs, or keyword arguments.

***

## **Examples**

### 1. **Update with Another Dictionary**
```python
d1 = {'A': 'Geeks', 'B': 'For'}
d2 = {'B': 'Geeks', 'C': 'Python'}
d1.update(d2)
print(d1)  # {'A': 'Geeks', 'B': 'Geeks', 'C': 'Python'}
```
- The value for `'B'` is updated, and `'C'` is added.

### 2. **Update with Keyword Arguments**
```python
d1 = {'A': 'Geeks'}
d1.update(B='For', C='Geeks')
print(d1)  # {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
```

### 3. **Update with Iterable of Tuples**
```python
dictionary = {'x': 2}
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)  # {'x': 2, 'y': 3, 'z': 0}
```

### 4. **Add New Key or Update Existing Key**
```python
site = {'Website': 'DigitalOcean', 'Tutorial': 'How To Add to a Python Dictionary'}
site.update({'Author': 'Sammy Shark'})  # Adds new key
site.update({'Tutorial': 'Updated Tutorial'})  # Updates existing key
print(site)
# {'Website': 'DigitalOcean', 'Tutorial': 'Updated Tutorial', 'Author': 'Sammy Shark'}
```

***

## **Best Practices and Use Cases**
- Use `update()` to merge two dictionaries or add multiple key-value pairs at once.
- Use keyword arguments for simple string keys.
- Use an iterable of tuples for dynamic or programmatic updates.
- Remember: If a key exists, its value will be overwritten.

***

## **Quick Review Questions**
- What happens if you use `update()` with a key that already exists?
- How can you add multiple new keys to a dictionary in one line?
- What types of objects can you pass to `update()`?

Try using `update()` in your own code to practice adding and updating dictionary entries!

***

## 3. **Removing Data**
- **`pop(key[, default])`**: Removes the specified key and returns its value. If the key is missing, returns `default` or raises `KeyError`.
  ```python
  d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
  d.pop('Age')
  print(d)  # {'Name': 'Ram', 'Country': 'India'}
  ```
- **`popitem()`**: Removes and returns the last inserted key-value pair as a tuple.
  ```python
  val = d.popitem()
  print(val)  # ('Country', 'India')
  ```
- **`clear()`**: Removes all items from the dictionary.
  ```python
  d.clear()
  print(d)  # {}
  ```

***

## 4. **Creating Nested Dictionaries**
- **Directly with curly braces:**
  ```python
  myfamily = {
      "child1": {"name": "Emil", "year": 2004},
      "child2": {"name": "Tobias", "year": 2007},
      "child3": {"name": "Linus", "year": 2011}
  }
  ```
- **By combining separate dictionaries:**
  ```python
  child1 = {"name": "Emil", "year": 2004}
  child2 = {"name": "Tobias", "year": 2007}
  child3 = {"name": "Linus", "year": 2011}
  myfamily = {"child1": child1, "child2": child2, "child3": child3}
  ```
- **Using the `dict()` constructor and `zip()`:**
  ```python
  IDs = ['emp1','emp2','emp3']
  EmpInfo = [
      {'name': 'Bob', 'job': 'Mgr'},
      {'name': 'Kim', 'job': 'Dev'},
      {'name': 'Sam', 'job': 'Dev'}
  ]
  D = dict(zip(IDs, EmpInfo))
  # {'emp1': {'name': 'Bob', 'job': 'Mgr'}, ...}
  ```
- **With default values using `fromkeys()`:**
  ```python
  IDs = ['emp1','emp2','emp3']
  Defaults = {'name': '', 'job': ''}
  D = dict.fromkeys(IDs, Defaults)
  # All keys share the same Defaults dict
  ```

***

## 4.1. **Accessing Elements in Nested Dictionaries**
- **Chain keys with square brackets:**
  ```python
  print(myfamily["child2"]["name"])  # Output: Tobias
  print(D['emp1']['name'])              # Output: Bob
  ```
- **Using `.get()` for safer access:**
  ```python
  print(D['emp1'].get('salary'))  # Output: None (no error)
  ```
- **Caution:** If you try to access a missing key directly, you'll get a `KeyError`.

***

## 4.2 **Adding and Updating Elements**
- **Add a new key-value pair to an inner dictionary:**
  ```python
  person = {'employee1': {'name': 'Janice', 'age': 25}}
  person['employee1']['department'] = 'HR'
  # Now: {'employee1': {'name': 'Janice', 'age': 25, 'department': 'HR'}}
  ```
- **Add a new inner dictionary:**
  ```python
  person['employee2'] = {'name': 'Jake', 'age': 30, 'department': 'IT'}
  ```

***

## 4.3 **Iterating Through Nested Dictionaries**
- **Loop through outer and inner dictionaries:**
  ```python
  for outer_key, inner_dict in myfamily.items():
      print(outer_key)
      for inner_key, value in inner_dict.items():
          print(f"  {inner_key}: {value}")
  # Output:
  # child1
  #   name: Emil
  #   year: 2004
  # ...
  ```
- **Example with IDs and info:**
  ```python
  people = {
      1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
      2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}
  }
  for p_id, p_info in people.items():
      print(f"Person ID: {p_id}")
      for key in p_info:
          print(f"  {key}: {p_info[key]}")
  ```

***

## 4.4 **Common Pitfalls and Tips**
- **Shared default values:** If you use `fromkeys()` with a mutable default (like a dict), all keys share the same object. Changing one changes all.
- **Use `.get()` for safe access:** Prevents crashes if a key is missing.
- **Nested loops:** Use `.items()` to iterate through both levels.

***

## **Quick Practice**
- Try creating a nested dictionary for students and their grades.
- Practice adding a new field to an inner dictionary.
- Write a loop to print all students and their details.
  

***

## **Summary Table: Key Dictionary Methods**
| Method         | Purpose                                      |
|----------------|----------------------------------------------|
| `get()`        | Safe value access, avoids KeyError            |
| `keys()`       | View of all keys                             |
| `values()`     | View of all values                           |
| `items()`      | View of all key-value pairs                  |
| `update()`     | Merge or add key-value pairs                 |
| `setdefault()` | Insert key with default if missing           |
| `pop()`        | Remove and return value by key               |
| `popitem()`    | Remove and return last key-value pair        |
| `clear()`      | Remove all items                             |

***

**Key Takeaways:**
- Use dictionary methods for safe, efficient data access and manipulation.
- Nested dictionaries are powerful for modeling real-world, hierarchical data.
- Use `.get()` and `.setdefault()` to avoid errors and write concise code.
- Iterating with `.items()` is essential for traversing nested structures.
