### **How the Problem Happens**

Consider this code:
```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```
Instead of resulting in ``, ``, and ``, the output is:
```
[1]
[1, 2]
[1, 2, 3]
```
The list `L` is created only **once** and every call to `f` adds to the same list, so its contents persist (and grow) as the function is called repeatedly.

***

### **Why?**
- **Mutable types** (lists, dicts, sets, custom classes) can be changed in place and so any change inside the function is visible in every call.
- **Immutable types** (numbers, strings, tuples, None, etc.) do *not* have this problem because their values can't change after they are created.
- **Default values** for parameters are evaluated only once: when the function is defined—not each time the function is called.

***

### **Best Practice: Use `None` as Default**
The standard remedy is to use `None` as a sentinel value, then instantiate the mutable object inside the function each time:
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [2]
print(f(3))  # [3]
```
Each call that omits `L` now gets a **fresh new list**.

***

### **Deliberate Use: Caching and Memoization**
This "footgun" can actually be beneficial when you *want* persistent storage between calls—such as a cache or memoization pattern:
```python
def expensive_function(arg1, arg2, *, _cache={}):
    if (arg1, arg2) in _cache:
        return _cache[(arg1, arg2)]
    # compute result...
    result = ...
    _cache[(arg1, arg2)] = result
    return result
```
Here, the default `_cache` dictionary **should** be shared between calls to store cached results.

***

### **Summary Table: Safe vs. Unsafe Defaults**

| Data Type          | Is it safe as default? | Why?                                                                      |
|--------------------|:---------------------:|---------------------------------------------------------------------------|
| `int`, `str`, `()` | Yes                  | Each call uses an immutable, can’t be changed after creation.             |
| `[]`, `{}`         | No                   | Mutable, changes persist across function calls.                           |
| `None`             | Yes (with check)     | Can serve as a unique sentinel value; always assign a new object if None. |

***

Following this pattern avoids subtle bugs and makes function behavior predictable and safe.Using a mutable object like a list or dictionary as a default argument in Python functions is a well-known pitfall because the default object is created **once at function definition**, not each time the function is called. When the mutable argument is modified, that change persists for future calls, which can lead to extremely confusing bugs and is generally considered bad practice.

**Example of the Pitfall:**
```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # Output: [1]
print(f(2))  # Output: [1, 2]
print(f(3))  # Output: [1, 2, 3]
```
All calls share the same list object, so new values accumulate, instead of seeing ``, ``, `` as the output.

**Why does this happen?**
- Default arguments are only evaluated **once**, when the function is defined, not each time the function is called.
- Mutable objects (lists, dicts, sets) allow changes that persist between calls; immutable objects (tuples, numbers, strings) do not have this problem.

**The Correct Approach: Use `None` as default**
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))  # Output: [1]
print(f(2))  # Output: [2]
print(f(3))  # Output: [3]
```
This way, each call gets its own fresh list unless one is explicitly provided.

**When is it useful?**
- This behavior is sometimes used intentionally, such as using a dictionary as a function-local cache for memoization, where shared state across calls is desired.
- However, for routine tasks, always use `None` (or another immutable) as the default to avoid hard-to-debug bugs in your code.
