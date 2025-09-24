### Python Loop Control Statements: `break`, `continue`, and `pass`

Loop control statements let you change the normal flow of a loop. Let's break down each one with clear examples and explanations.

***

#### **1. `break` Statement**
- **Purpose:** Immediately exits the innermost loop (for or while) when a certain condition is met.
- **Common use:** To stop a loop early, such as when a search is successful or an error is found.

**Example (for loop):**
```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)
```
**Output:**
```
0
1
2
3
4
```

**Example (while loop):**
```python
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
```
**Output:**
```
0
1
2
3
4
```

***

#### **2. `continue` Statement**
- **Purpose:** Skips the rest of the current loop iteration and jumps to the next iteration.
- **Common use:** To ignore certain values or conditions without stopping the loop.

**Example (for loop):**
```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```
**Output:**
```
1
3
5
7
9
```

**Example (while loop):**
```python
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
```
**Output:**
```
1
3
5
7
9
```

***

#### **3. `pass` Statement**
- **Purpose:** Does nothing; acts as a placeholder where code is required syntactically but you don't want to execute anything yet.
- **Common use:** Empty function, class, or loop bodies during development.

**Example:**
```python
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    print(i)
```
**Output:**
```
0
1
2
3
4
```

***

#### **Quick Review**
- **`break`**: Exits the loop immediately.
- **`continue`**: Skips to the next iteration.
- **`pass`**: Does nothing (placeholder).

**Try this:**
- Write a loop that prints numbers 0 to 9, but skips 4 and stops entirely if it reaches 7. What do you expect the output to be?
