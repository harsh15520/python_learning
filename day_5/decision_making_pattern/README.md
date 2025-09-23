## 1. **Simple `if` Statement**
- **Pattern:** Execute code only if a condition is true.
- **Example:**
  ```python
  if temperature > 30:
      print("It's hot today.")
  ```

***

## 2. **`if-else` Statement**
- **Pattern:** Choose between two paths based on a condition.
- **Example:**
  ```python
  if score >= 50:
      print("Pass")
  else:
      print("Fail")
  ```

***

## 3. **`if-elif-else` Chain**
- **Pattern:** Check multiple conditions in order; only the first true block runs.
- **Example:**
  ```python
  if age < 13:
      print("Child")
  elif age < 20:
      print("Teenager")
  elif age < 65:
      print("Adult")
  else:
      print("Senior")
  ```

***

## 4. **Nested Conditionals**
- **Pattern:** Place one conditional inside another for multi-level decisions.
- **Example:**
  ```python
  if user_logged_in:
      if user_is_admin:
          print("Welcome, admin!")
      else:
          print("Welcome, user!")
  else:
      print("Please log in.")
  ```

***

## 5. **Ternary Operator (Conditional Expression)**
- **Pattern:** One-line decision for simple cases.
- **Example:**
  ```python
  status = "Adult" if age >= 18 else "Minor"
  print(status)
  ```

***

## 6. **Logical Operators in Conditions**
- **Pattern:** Combine multiple conditions using `and`, `or`, `not`.
- **Example:**
  ```python
  if is_weekend or is_holiday:
      print("No school today!")
  if age > 18 and has_license:
      print("Can drive.")
  if not name:
      print("Name is required.")
  ```

***

## 7. **Best Practices**
- Use `if-elif-else` to avoid deep nesting.
- Order conditions from most specific to most general.
- Prefer built-in methods (like `startswith()`) for simple checks.
- Use logical operators to simplify compound conditions.
- Leverage truthy/falsy values for concise code.

***

**Summary:**
- Decision-making patterns in Python include simple `if`, `if-else`, `if-elif-else` chains, nested conditionals, ternary operators, and logical operators.
- These patterns help your code make choices and follow different paths based on data and user input.
