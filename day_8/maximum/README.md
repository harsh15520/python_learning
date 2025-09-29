# Finding the Maximum Value in a List (Without `max()`)

## **Approach 1: Using a For Loop**
This is the most common and beginner-friendly way. You:
- Assume the first element is the maximum.
- Loop through the rest, updating your maximum if you find a bigger value.

```python
def find_max_with_for_loop(numbers: list[int | float]) -> int | float:
    """
    Finds the maximum value in a list using a for loop.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
```

**Example:**
```python
my_numbers = [10, 24, 76, 23, 12]
maximum = find_max_with_for_loop(my_numbers)
print(f"The maximum value is: {maximum}")  # Output: 76
```

***

## **Approach 2: Using a While Loop**
This method is similar, but you manage the index manually.

```python
def find_max_with_while_loop(numbers: list[int | float]) -> int | float:
    """
    Finds the maximum value in a list using a while loop.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")
    max_value = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] > max_value:
            max_value = numbers[index]
        index += 1
    return max_value
```

**Example:**
```python
my_numbers = [10, 24, 76, 23, 12]
maximum_while = find_max_with_while_loop(my_numbers)
print(f"The maximum value (using while) is: {maximum_while}")  # Output: 76
```

***

## **Other Approaches (for practice)**
- **Sorting:** `sorted(my_list)[-1]` (not recommended for large lists, as it’s less efficient than a loop)[1][2][3]
- **Reduce:** `from functools import reduce; reduce(lambda x, y: x if x > y else y, my_list)`[2]

***

## **Quick Review**
- Why do we start with the first element as the initial maximum?
- What happens if the list is empty?
- How would you modify these functions to also return the index of the maximum value?
