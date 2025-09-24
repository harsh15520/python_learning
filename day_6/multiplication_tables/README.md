## 1. **Basic: Table for a Single Number**

**Using a for loop:**
```python
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```
- This prints the multiplication table for the chosen number from 1 to 10.[1][6][8]

**Using a while loop:**
```python
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
```
- Both methods give the same result; choose whichever loop you prefer.[4][5][6]

***

## 2. **Custom Range Table**
You can let the user choose the range:
```python
number = int(input("Enter the multiplier: "))
end = int(input("Enter the range end: "))
for i in range(1, end + 1):
    print(f"{number} x {i} = {number * i}")
```
- This prints the table up to any number you want.[9]

***

## 3. **Advanced: Tables for Multiple Numbers (Nested Loops)**

**Full tables from 1 to 10:**
```python
for i in range(1, 11):
    print(f"Multiplication table of: {i}")
    for j in range(1, 11):
        print(f" {i} x {j} = {i * j}")
    print()  # Blank line between tables
```
- This prints each table from 1 to 10, one after another.[6][7][8]

**Tabular format with headers:**
```python
print("   ", end='')
for header in range(1, 11):
    print(f"{header:2}", end=' ')
print()  # Header row
print("   " + ("--- " * 10))
for i in range(1, 11):
    print(f"{i:2} | ", end='')
    for j in range(1, 11):
        print(f"{i*j:2}", end=' ')
    print()
```
- This creates a grid-style multiplication table, making it easy to see all products at a glance.[7]

***

## 4. **Using Nested While Loops**
```python
row = 1
while row <= 10:
    col = 1
    while col <= 10:
        print(f"{row} x {col} = {row * col}", end="\t")
        col += 1
    print()
    row += 1
```
- This also prints a full multiplication table, row by row.[9]

***
