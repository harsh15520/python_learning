# Overview of Python Built-in Data Types

Python organizes data items into **data types**, which determine what operations can be performed and how the data is stored. Since *everything is an object* in Python, data types are classes, and variables are instances of those classes.[1][2][7]

Let's break down the standard built-in types and actively check your understanding as we go!

## Numeric Data Types (int, float, complex)
- **int:** Whole numbers, no decimal (e.g., `42`, `-5`)
- **float:** Numbers with decimals (e.g., `3.14`, `-0.75`)
- **complex:** Numbers with real and imaginary parts (e.g., `2+3j`)

Try: What type do you get if you run `type(2.5)`? Can you explain what `j` means in a complex number?

## Sequence Types (str, list, tuple)
- **str:** Strings, for text—can be created with single, double, or triple quotes (e.g., `'hello'`, `"world"`)
- **list:** Ordered, mutable collections using `[ ]` (e.g., `[1, 2, 3]`)
- **tuple:** Ordered, immutable collections using `( )` (e.g., `(1, 2, 3)`)

Try: Make a list with three different types of elements (number, string, boolean). How do you add an item to a list? Can you change a tuple after creation?

## Mapping Type (dict)
- **dict:** Key-value pairs in `{}`; keys must be unique and immutable.

Example: `{"name": "Alice", "age": 30}`

Try: How would you retrieve the value for the key "name" in the above dict?

## Boolean Type (bool)
- **bool:** Two values only—`True` or `False` (capitalized, no quotes)
- Used for logic and conditionals.

Try: What result do you get from `bool(0)` and `bool("hello")`?

## Set Types (set, frozenset)
- **set:** Unordered, mutable collection of unique elements (e.g., `{1, 2, 3}`)
- **frozenset:** Same as set, but immutable.

Try: What happens if you add the same element twice to a set? Can you explain the difference between set and frozenset?

## Binary Types (bytes, bytearray, memoryview)
- **bytes:** Immutable sequence of bytes (e.g., `b'abc'`)
- **bytearray:** Mutable sequence of bytes
- **memoryview:** Allows access to the memory of other binary objects
