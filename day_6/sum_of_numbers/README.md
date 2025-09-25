# Summing Numbers in Python: Basic to Advanced

Let's explore several ways to find the sum of numbers in Python, from simple loops to built-in functions and more advanced techniques.

***

## 1. **Sum of a Pre-defined List**
You can sum the elements of a list using a `for` loop or the built-in `sum()` function.

**Using a for loop:**
```python
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"The sum is: {total}")  # Output: 150
```

**Using `sum()`:**
```python
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(f"The sum is: {total}")  # Output: 150
```
- The `sum()` function is efficient and Pythonic for adding all elements in a list.[1][2][3]

***

## 2. **Sum of Numbers in a Range**
You can sum a sequence of numbers using `range()`:
```python
total = 0
for num in range(101):  # Sums numbers from 0 to 100
    total += num
print(f"The sum from 0 to 100 is: {total}")  # Output: 5050
```
Or, more simply:
```python
print(sum(range(101)))  # Output: 5050
```

***

## 3. **Sum of User-Entered Numbers**
Use a loop to collect numbers from the user, then sum them:
```python
numbers = []
print("Enter numbers to sum. Press Enter on a blank line to finish.")
while True:
    user_input = input("Enter a number: ")
    if user_input == '':
        break
    try:
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number.")
total = sum(numbers)
print(f"The numbers you entered are: {numbers}")
print(f"The sum is: {total}")
```

***

## 4. **Sum Using a Function**
Wrap your logic in a function for reusability:
```python
def sum_numbers(number_list):
    total = 0
    for number in number_list:
        total += number
    return total

my_numbers = [1.5, 2.5, 3.0, 4.5]
result = sum_numbers(my_numbers)
print(f"The sum is: {result}")  # Output: 11.5
```

**Pythonic version:**
```python
def pythonic_sum(number_list):
    return sum(number_list)

my_numbers = [10, -2, 5, 8]
result = pythonic_sum(my_numbers)
print(f"The sum is: {result}")  # Output: 21
```

***

## 5. **Sum of Other Data Structures**
- **Tuple:** `sum((1, 2, 3, 4, 5))` → 15[3]
- **Set:** `sum({1, 2, 3, 4, 5})` → 15[3]
- **Dictionary values:**
  ```python
  my_dict = {'a': 10, 'b': 20, 'c': 30}
  print(sum(my_dict.values()))  # Output: 60
  ```

***

## **Quick Review**
- The built-in `sum()` function is the most efficient and Pythonic way to sum numbers in a list or other iterable.[2][1][3]
- You can use loops for more control or custom logic.
- Functions make your code reusable and clean.
