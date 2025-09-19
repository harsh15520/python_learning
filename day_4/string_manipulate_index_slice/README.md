# Python Strings: Core Concepts & Operations

## 1. **String Basics**
- **Strings** represent sequences of Unicode characters (letters, digits, symbols).
- *Creation*: Use single `'...'`, double `"..."`, or triple quotes (`'''...'''`, `"""..."``).[2][8]
- Python has no separate "char" type; a one-character string is just a string of length one.

## 2. **Immutability**
- Strings are **immutable**: once created, their contents cannot be changed.
- To "modify" a string, create a new one (e.g., using slicing and concatenation).
- Example:
  ```python
  name = "Zophie a cat"
  new_name = name[:7] + "the" + name[8:]  # 'Zophie the cat'
  ```

## 3. **Indexing**
- Access individual characters using zero-based indices:
  ```python
  s = "GeeksforGeeks"
  print(s[0])    # 'G' (first character)
  print(s[1])    # 'e' (second character)
  print(s[-1])   # 's' (last character)
  print(s[-10])  # 'k' (tenth from end)
  ```
- Negative indices count from the end (`-1` is last character).
- Out-of-range index → IndexError.

## 4. **Slicing**
- Extract substrings with `s[start:stop]` (stop exclusive).
- Omitted indices have defaults: `s[:n]` starts at 0, `s[n:]` ends at the last character.
- Slicing with steps: `s[start:stop:step]` — `s[::-1]` reverses the string.
- Out-of-range slices return empty string or part of the string (no error).[5][2]

## 5. **String Manipulation**
- Concatenation: `s1 + s2` joins strings.
- Replication: `s * 3` repeats a string 3 times.
- Example:
  ```python
  s1 = "Hello"
  s2 = "World"
  s3 = s1 + " " + s2
  print(s3)       # 'Hello World'
  print(s1 * 3)   # 'HelloHelloHello'
  ```

## 6. **Built-in String Methods**
**All methods return new strings (do not change the original):**[1]
- `.upper()`, `.lower()`: Change case.
- `.strip()`, `.lstrip()`, `.rstrip()`: Remove whitespace (or chosen characters).
- `.replace(old, new, count)`: Replace substrings.
- `.split(sep)`: Split into a list on a delimiter.
- `.join(list_of_strings)`: Efficiently join many strings (use on separator). Example: `', '.join(['a', 'b', 'c'])` → 'a, b, c'.[4]
- `.startswith()`, `.endswith()`: Check beginnings and endings.
- `.find(sub)`, `.index(sub)`: Search for substring.
- `.capitalize()`, `.title()`: Adjust capitalization.
- `.zfill(width)`: Pads string with zeros on the left.
- New in 3.9+: `.removeprefix(prefix)`, `.removesuffix(suffix)`.

## 7. **Editing Characters (Advanced)**
- Since strings are immutable, convert to a list to make many character changes:
  ```python
  word = "elephant"
  chars = list(word)
  chars[0] = 'E'      # Change first letter
  chars.append('!')   # Add an exclamation mark
  word_modified = "".join(chars)
  print(word_modified)  # 'Elephant!'
  ```

## 8. **String Formatting**
- **F-strings** (Python 3.6+):
  ```python
  name = "Alice"
  print(f"Hello, {name}!")
  ```
- **str.format():**
  ```python
  print("Hello, {}!".format(name))
  ```
- **% formatting** is older (discouraged now).

## 9. **Membership, Length & Iteration**
- `'a' in s` checks for substring presence.
- `len(s)` gives string length.
- Use `for c in s` to iterate through characters.

## 10. **Practical Usage & Recap**
- Strings: write messages, store input, manipulate text.
- Immutability: always make new strings for "changed" versions.
- Master string methods—they're fast and make code much clearer than manual loops/regex for basic tasks.
