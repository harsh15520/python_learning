# Factorial in Python: Basic to Advanced

Let's explore several ways to compute the factorial of a number in Python, from basic loops to recursion and built-in functions. Each method has its own strengths and is useful for different scenarios.

***

## 1. **Iterative Approach (for loop)**
This is the most common and beginner-friendly way:
```python
def factorial_for(n):
    """Calculates factorial using a for loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
- **Pros:** Simple, fast, and works for large numbers.
- **Usage:**
  ```python
  print(factorial_for(5))  # Output: 120
  ```

***

## 2. **Iterative Approach (while loop)**
You can also use a while loop:
```python
def factorial_while(n):
    """Calculates factorial using a while loop."""
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
```
- **Usage:**
  ```python
  print(factorial_while(5))  # Output: 120
  ```

***

## 3. **Recursive Approach**
A recursive function calls itself until it reaches the base case:
```python
def factorial_recursive(n):
    """Calculates factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
```
- **Pros:** Elegant and matches the mathematical definition.
- **Cons:** Not recommended for very large numbers (risk of stack overflow).
- **Usage:**
  ```python
  print(factorial_recursive(5))  # Output: 120
  ```

***

## 4. **Using Python's Built-in Function**
The `math` module provides a fast, reliable factorial function:
```python
import math
print(math.factorial(5))  # Output: 120
```
- **Pros:** Fast, handles large numbers, and raises errors for invalid input.[6][7]

***

## 5. **Using NumPy (for advanced users)**
If you're working with arrays or scientific computing:
```python
import numpy as np
n = 5
print(np.prod(range(1, n + 1)))  # Output: 120
```
- **Pros:** Useful for vectorized operations and large datasets.[1]

***

## 6. **Prime Factorization (rarely used)**
This is a more mathematical approach, mainly for learning or optimization in special cases:
```python
def primeFactors(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def factorial_prime(n):
    result = 1
    for i in range(2, n + 1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result
```
- **Usage:**
  ```python
  print(factorial_prime(5))  # Output: 120
  ```

***

## **Quick Review**
- **Iterative (for/while):** Best for most cases.
- **Recursive:** Elegant, but not for very large n.
- **math.factorial():** Fastest and safest for production.
- **NumPy:** For scientific computing.
- **Prime factorization:** For special mathematical needs.
