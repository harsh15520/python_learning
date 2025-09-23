## Basic Concepts

### 1. **What Is Extraction?**
Extraction is identifying and retrieving specific patterns of text from data. Here, the goal is to find phone numbers and email addresses hidden within text.

### 2. **Regular Expressions (Regex) Basics**
- Regex is a language for specifying search patterns.  
- Key constructs:
  - **Literals:** Exact characters to match (e.g., `abc` matches “abc”).
  - **Character classes:** Sets of possible characters, e.g. `[0-9]` or `[aeiou]`.
  - **Quantifiers:** How many times a pattern may repeat, e.g. `*` (0+), `+` (1+), `{2,4}` (between 2 and 4).
  - **Anchors:** Define start/end positions like `^` (start) and `$` (end).
  - **Groups:** Parentheses to group sub-patterns and capture matches.
  - **Alternation:** The OR operator `|` matches alternatives.

### 3. **Simple Regex for Phone Numbers**
- Digits only pattern: `\d{10}` (matches 10 consecutive digits).
- Common phone formatting includes separators: space, hyphen, or dots.
- Area code parentheses: `(\d{3})` or `$$\d{3}$$`.
- Sample pattern:  
  `($$\d{3}$$|\d{3})?[\s.-]?\d{3}[\s.-]\d{4}`  
  Matches optional area code, separators, and number groups.

### 4. **Simple Regex for Emails**
- Basic pattern: username part, `@`, domain part, dot extension.
- Example:  
  `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
- Username allows letters, digits, dots, underscores, etc.
- Domain includes letters, digits, hyphens, multiple subdomains possible.

***

## Intermediate Concepts

### 1. **Verbose Mode**
- Use verbose flag to structure complex regex with whitespace and comments for readability.
- Example:
  ```python
  re.compile(r'''
    pattern details
  ''', re.VERBOSE)
  ```

### 2. **Capture Groups & Extraction**
- Parentheses capture parts of matches for further processing.
- Enables extracting just phone numbers or emails from surrounding text.

### 3. **Flexible Patterns**
- Handling extensions for phones: `(ext|x|extension)?\s*\d+`
- Optional country codes: `(\+\d{1,2}\s)?`
- More complex email validations for subdomains and new TLDs.

### 4. **Handling Multiple Matches**
- Use `re.findall()` to extract all matching substrings, not just one.

***

## Advanced Concepts

### 1. **Unicode & Internationalization**
- Support numbers with international prefixes `+\d+`
- Support email unicode characters in username and domain (IDN).

### 2. **Performance Tuning**
- Regex can be slow on very large texts or with complex patterns.
- Use atomic groups or possessive quantifiers (in some engines).
- Optimize pattern order to reduce backtracking.

### 3. **Context Awareness**
- Extract with context rules (e.g., ignore numbers in dates or IDs).
- Use lookarounds to assert conditions without capturing.

### 4. **Data Cleaning Post-Extraction**
- Normalize phone numbers (remove spaces, add country code).
- Validate email formats further using domain checks or SMTP verification.

### 5. **Security Considerations**
- Carefully sanitize extracted data to avoid injection or misuse.
- Avoid regex denial of service by limiting input sizes.

***

## Practical Workflow Summary

1. **Design regex patterns** for phone numbers and email addresses.
2. **Read input text** (from clipboard, files, or network).
3. **Find all matches** using `re.findall()` or similar functions.
4. **Post-process matches** for format normalization and validation.
5. **Output or store extracted contacts** for further use.

***

### Useful Python Tools

- `re` module for regex operations.
- `pyperclip` to interface with clipboard.
- Libraries like `phonenumbers` for advanced phone parsing.
- Email validation packages for comprehensive checks.
