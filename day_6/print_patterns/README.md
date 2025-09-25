## 1. **Basic Pattern: Square of Stars**

```python
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()
```
- **Outer loop:** Controls rows
- **Inner loop:** Controls columns
- **`end=" "`** keeps stars on the same line

***

## 2. **Right Triangle of Numbers**

```python
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```
**Output for 5 rows:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

***

## 3. **Reverse Number Triangle**

```python
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
```
**Output for 5 rows:**
```
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
```

***

## 4. **Pyramid Pattern of Stars**

```python
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)
```
**Output for 5 rows:**
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

***

## 5. **Custom Grid Pattern (List of Lists)**

You can store a pattern in a grid (list of lists) and print it row by row:

```python
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]
for row in grid:
    for cell in row:
        print(cell, end='')
    print()
```

***

## 6. **Advanced: Custom Number Patterns**

### a) Each row with same number (row value)
```python
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
```
**Output for 5 rows:**
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

### b) Each row with decreasing numbers (n - i)
```python
n = int(input("Enter n: "))
for i in range(n):
    for j in range(i + 1):
        print(n - i, end=" ")
    print()
```
**Output for n=5:**
```
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
```

***

## **Tips for Pattern Printing**
- **Decide rows/columns:** Use `input()` for flexibility.
- **Nested loops:** Outer for rows, inner for columns.
- **String manipulation:** Use `*` for repetition, `+` for concatenation.
- **Grid data:** Use list of lists for custom shapes.
- **Formatting:** Use `end=''` to control line breaks.
