# Infinite Loops in Python: Common Pitfalls and Best Practices

Infinite loops are a powerful tool in Python, but they can easily become a source of bugs if not handled carefully. Let's break down the main pitfalls and how to avoid them.

## 1. **The `while True` Loop**
- **Pattern:**
  ```python
  while True:
      # code
      if exit_condition:
          break
  ```
- **Pitfall:** If the `break` statement is missing or unreachable, the loop will run forever.[1][2][5]
- **Example:**
  ```python
  while True:
      name = input('Type your name: ')
      if name == 'your name':
          break
  print('Thank you!')
  ```
  If the user never types 'your name', the loop never ends.

## 2. **Unreachable `break` Due to Logic**
- If a `continue` statement is used before the `break`, the loop may never reach the exit condition.
- **Example:**
  ```python
  while True:
      name = input('Who are you? ')
      if name != 'Joe':
          continue  # Skips password check
      password = input('Password: ')
      if password == 'swordfish':
          break
  print('Access granted.')
  ```
  Here, only 'Joe' can reach the password check and break out. Any other input causes the loop to restart.

## 3. **Condition Variable Not Updated**
- If your loop relies on a variable to end, but you forget to update it, the loop runs forever.
- **Example:**
  ```python
  spam = 0
  while spam < 5:
      print('Hello, world.')
      # spam = spam + 1  # If missing, loop is infinite
  ```
  Always ensure your condition variable changes so the loop can end.[3][5]

## 4. **Recursive Infinite Loops**
- Recursive functions without a base case can act like infinite loops, eventually causing a crash or `RecursionError`.
- Always include a clear exit condition in recursive functions.

## 5. **How to Stop an Infinite Loop**
- If you get stuck in an infinite loop during development, press **Ctrl+C** in your terminal to force-stop the program.[5][3]
