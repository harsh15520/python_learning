## 1. **Boolean Values and Operators**
- **Boolean values**: `True` and `False` (must be capitalized)
- **Comparison operators** (evaluate to Boolean):
  - `==` (equal to)
  - `!=` (not equal to)
  - `<`, `>`, `<=`, `>=` (less/greater than, etc.)
- **Logical operators**:
  - `and`: Both conditions must be `True`
  - `or`: At least one condition must be `True`
  - `not`: Inverts the Boolean value

***

## 2. **if, elif, else Statements**

### **if statement**
Executes a block if the condition is `True`.
```python
age = 20
if age >= 18:
    print("Eligible to vote.")
```

### **if-else statement**
Provides an alternative if the condition is `False`.
```python
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
```

### **if-elif-else statement**
Checks multiple conditions in order.
```python
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
```
- Only the first `True` condition's block runs; others are skipped.

***

## 3. **Logical Operators in Conditions**

- **and**: `if a > 0 and a % 2 == 0:` (True if both are true)
- **or**: `if a < 0 or a > 100:` (True if at least one is true)
- **not**: `if not name:` (True if `name` is falsy, e.g., empty string)

***

## 4. **Ternary (One-Line) If-Else**
A compact way to assign or print based on a condition:
```python
result = "Pass" if marks >= 40 else "Fail"
print(result)
```

***

## 5. **Nested if Statements**
You can put an `if` inside another `if` or `else` block:
```python
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
```

***

## 6. **Truthy and Falsy Values**
- **Falsy**: `0`, `0.0`, `None`, `''`, `[]`, `{}` (evaluated as `False`)
- **Truthy**: Any other value (non-zero, non-empty)

Example:
```python
name = ''
while not name:
    print('Enter your name:')
    name = input()
```

***

## 7. **Practice**
Try writing a condition that checks if a number is both positive and a multiple of 5:
```python
number = int(input("Enter a number: "))
if number > 0 and number % 5 == 0:
    print("The number is positive and a multiple of 5.")
else:
    print("The number does not meet both conditions.")
```

***

**Summary:**
- Use `if`, `elif`, `else` to control program flow based on conditions.
- Combine conditions with `and`, `or`, `not`.
- Use truthy/falsy values for concise checks.
- Ternary expressions allow one-line decisions.

