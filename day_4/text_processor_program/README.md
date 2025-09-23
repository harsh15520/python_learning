A **text processor program** in Python is typically a script or application designed to perform various operations on text data, ranging from simple formatting and manipulation to complex pattern matching and extraction. Python's rich set of built-in string methods and specialized modules make it highly effective for such tasks.

Here are several examples and concepts related to Python text processor programs:

### Core String Methods and Modules for Text Processing

Many text processing tasks leverage Python's built-in string methods:
*   **Case Conversion**: Methods like `upper()` and `lower()` convert strings to uppercase or lowercase, respectively.
*   **Whitespace Management**: `strip()`, `lstrip()`, and `rstrip()` remove leading, trailing, or both leading and trailing whitespace (including newlines). `rstrip()` is particularly useful for cleaning lines read from files, similar to Perl's `chomp()`.
*   **Text Justification**: `rjust()`, `ljust()`, and `center()` pad strings with spaces (or a specified character) to align text, often used for tabular data.
*   **Splitting and Joining**:
    *   The `split()` method breaks a string into a list of substrings using a specified delimiter, such as whitespace or newline characters.
    *   The `join()` method concatenates a sequence of strings into a single string, inserting a separator between each element. This is often the most efficient way to build a string from multiple parts, especially in loops.
*   **Replacing Substrings**: The `replace(old, new, count)` method returns a copy of the string with occurrences of `old` replaced by `new`.

### Advanced Text Processing Capabilities

For more complex scenarios, Python offers powerful modules:
*   **Regular Expressions (`re` module)**: For pattern matching beyond simple string methods, the `re` module is essential. It allows:
    *   **Pattern-based Splitting**: `re.split()` can split strings using complex patterns or multiple delimiters.
    *   **Pattern-based Substitution**: `re.sub()` replaces occurrences of a pattern with a specified string or the result of a function.
    *   **Finding All Matches**: `re.findall()` returns all non-overlapping matches of a pattern.
*   **Text Wrapping (`textwrap` module)**: This module provides functions and a `TextWrapper` class for formatting paragraphs of text to fit a given width. Functions include `wrap()` (returns a list of lines), `fill()` (returns a single string with newlines), `shorten()` (collapses and truncates text), `dedent()` (removes common leading whitespace), and `indent()` (adds prefixes to lines).
*   **Unicode Handling (`unicodedata` and encoding support)**: Python 3 uses Unicode for strings. Text processors must handle character encodings correctly, especially when reading from or writing to files. The `unicodedata` module provides tools for normalizing Unicode strings for consistent comparisons.

### Examples of Python Text Processor Programs

Several practical text processing programs are demonstrated in the sources:

1.  **Multi-Clipboard Automatic Messages (`mclip.py`, `mcb.pyw`)**:
    *   This program stores multiple text phrases associated with keywords.
    *   Users can copy a stored phrase to the clipboard by providing its keyword as a command-line argument.
    *   An enhanced version (`mcb.pyw`) uses the `shelve` module to persistently save and load clipboard content, allowing users to save new text, list existing keywords, or delete entries without modifying the script's source code.
    *   It utilizes `sys.argv` for command-line arguments and `pyperclip.copy()`/`pyperclip.paste()` for clipboard interaction.

2.  **Adding Bullets to Wiki Markup (`bulletPointAdder.py`)**:
    *   This script takes text from the clipboard, adds a star (`* `) and a space to the beginning of each line, and then pastes the modified text back to the clipboard.
    *   It achieves this by splitting the clipboard text by newline characters (`text.split('\n')`), iterating through the resulting list to prepend the bullet, and then joining the modified lines back into a single string (`'\n'.join(lines)`).

3.  **Pig Latin Program (`pigLat.py`)**:
    *   Translates English words into Pig Latin based on whether they start with a vowel or a consonant cluster.
    *   The program uses `message.split()` to break the input message into individual words. It identifies and separates non-letter characters at the beginning and end of words using `isalpha()` and string slicing, remembers original casing with `isupper()` and `istitle()`, and converts words to lowercase with `lower()` for translation. Finally, it reassembles the translated words and non-letters using string concatenation and `join()`.

4.  **Phone Number and Email Address Extractor**:
    *   This program searches text copied to the clipboard for phone numbers and email addresses using regular expressions.
    *   It uses `re` module functions to find all matches of predefined phone number and email address patterns and then formats these matches into a single string to be copied back to the clipboard.

### Interacting with Text Files

Python text processor programs frequently interact with files. This involves:
*   **Reading Files**: Using `open()` to get a file object, then `read()` to get the entire content as a single string, or `readlines()` to get a list of strings, one per line. The `pathlib` module also provides `Path.read_text()` for convenience.
*   **Writing Files**: Opening files in write (`'w'`) or append (`'a'`) mode with `open()` and using the `write()` method to save processed strings. `Path.write_text()` offers similar functionality.

### Terminal-based Text Editing

For more interactive, terminal-based text processing, the `curses` module and `curses.textpad` module provide functionality to create applications that can display and edit text within the terminal window. This allows for direct character input and basic text editing features.

Python's string methods are generally faster for simple string operations than regular expressions, as they are often implemented in C. However, the `re` module becomes necessary for searching and replacing complex patterns that cannot be expressed with simple literal strings.
