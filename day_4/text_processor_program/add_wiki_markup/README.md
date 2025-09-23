Here’s a detailed explanation of how to add and customize wiki markup bullets—covering basic lists, nesting, advanced options, common mistakes, and special features.

***

### 1. Basic Bulleted (Unordered) Lists

- **Syntax:** Start each line with an asterisk (`*`) directly against the left margin (no spaces before it).
- **Usage:** Each asterisk makes a new bullet.

**Example:**
```
* Bullet item one
* Bullet item two
* Bullet item three
```
- Renders as:
  - Bullet item one
  - Bullet item two
  - Bullet item three

- Add more asterisks with each new level for deeper nesting.

***

### 2. Nested Bulleted and Numbered Lists

- **Nesting Bullets:** Add an extra asterisk for each deeper level.
- **Mixing:** You can mix numbers (`#`) for ordered lists and asterisks for unordered lists.

**Nested Example:**
```
* Main bullet
** Sub-bullet level 2
*** Sub-bullet level 3
* Next main bullet
```

**Mixed Example:**
```
# First numbered item
#* Bullet under numbered item
#* Another bullet under numbered item
# Second numbered item
```

- Renders as nested bullets or mixed bullets and numbers.

***

### 3. Ordered (Numbered) Lists

- **Syntax:** Use `#` for each item, with one hash per level.
- **Nesting:** More `#` adds numbered sub-levels.

**Example:**
```
# Numbered item one
# Numbered item two
## Sub-numbered item 2.1
# Numbered item three
```

- Renders as:
  1. Numbered item one
  2. Numbered item two
      1. Sub-numbered item 2.1
  3. Numbered item three

[2]

***

### 4. Description (Definition) Lists

- **Syntax:** Use semicolons (`;`) for terms and colons (`:`) for definitions.

**Example:**
```
; Term 1 : Description for Term 1
; Term 2 : Description for Term 2
```
- Renders as:
  - **Term 1** Description for Term 1
  - **Term 2** Description for Term 2

- Good for glossaries or association lists.

***

### 5. Advanced Features and Formatting

#### a. Paragraphs and Blocks Inside Items  
- For multiple paragraphs in a bullet, use HTML tags (`<p>...</p>`) within the bullet markup.
- For line breaks inside an item (not a new bullet), use `<br />`.

**Example:**
```
* First bullet.<br />Second line in the same bullet.
* Bullet with a paragraph.<p>Second paragraph.</p>
```

#### b. Blockquotes or Code Blocks
- Use `<blockquote>` or `<pre>` tags within list items to add quoted or preformatted text.

#### c. Multi-column Lists
- Use templates like `{{columns-list| * item 1 * item 2 ...}}` for multi-column layouts.

#### d. Continuing List Items  
- Lists can’t be “continued” after nested lists using only markup; for continual flow, HTML tags or templates may be required.

***

### 6. Common Mistakes to Avoid

- **No Blank Lines:** Blank lines break a list and start a new one—never add blank lines between list items.
- **No Starting Spaces:** The first character must be `*` or `#` without any leading spaces.
- **Consistent Markup:** Each line in the list must start the same way.

**Wrong Example:**
```
* First bullet

* Second bullet
```
(This will create two separate single-item lists.)

***

### 7. More Customization

- **Specifying Start Numbers:** Use `{{ordered list|start=5|Item 1|Item 2}}` for custom start numbers.
- **Change List Marker Type (CSS):** With advanced templates or CSS, you can alter bullet/number styles.
- **Tables for Alignment or Sorting:** Use tables for more complex item alignment.

***

### 8. Special Horizontal or Inline Lists

- For short, inline lists:  
  _*Example:*_ `''My list:'' item 1, item 2, item 3`
