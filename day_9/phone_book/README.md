## **Basic Level: Dictionary Phone Book**

- **Data Structure:** Use a dictionary where the key is the contact name and the value is the phone number.
- **Operations:** Add, look up, update, and delete contacts.

```python
# Basic phone book
phone_book = {}
phone_book['Alice'] = '555-1234'
phone_book['Bob'] = '555-5678'

# Access
print(phone_book['Alice'])  # Output: 555-1234

# Update
phone_book['Alice'] = '555-0000'

# Delete
del phone_book['Bob']

# Check existence
if 'Alice' in phone_book:
    print("Alice is in the phone book.")
```

***

## **Intermediate Level: Interactive Menu System**

- **Features:** Add, search, delete, and display all contacts via a menu.
- **Implementation:** Use input() and a while loop for user interaction.

```python
def display_menu():
    print("\nPhone Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All")
    print("5. Exit")

def main():
    phone_book = {}
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Name: ")
            number = input("Phone: ")
            phone_book[name] = number
            print("Contact added.")
        elif choice == '2':
            name = input("Name to search: ")
            print(phone_book.get(name, "Not found"))
        elif choice == '3':
            name = input("Name to delete: ")
            if name in phone_book:
                del phone_book[name]
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '4':
            for name, number in phone_book.items():
                print(f"{name}: {number}")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

main()
```


***

## **Advanced Level: Parsing and Validating with Regex**

- **Scenario:** Extract contacts from raw text using regular expressions.
- **Example:** Parse lines like `"Ross McFluff: 834.345.1254 155 Elm Street"`.

```python
import re

text = """Ross McFluff: 834.345.1254 155 Elm Street
Heather Albrecht: 548.326.4584 919 Park Place"""

entries = re.split("\n+", text)
parsed = [re.split(":? ", entry, maxsplit=3) for entry in entries]
phone_book = {}
for entry in parsed:
    if len(entry) >= 3:
        name = f"{entry[0]} {entry[1]}"
        phone_book[name] = entry[2]
print(phone_book)
# Output: {'Ross McFluff': '834.345.1254', 'Heather Albrecht': '548.326.4584'}
```

- **Validation:** Use regex to check phone number formats before adding to the phone book.

***

## **Expert Level: Persistence and Extended Features**

- **Persistence:** Save/load the phone book using JSON or the shelve module.
- **Multiple Fields:** Store more details (email, address) using nested dictionaries.
- **GUI/CLI:** Build a graphical or advanced text interface for better usability.
- **Bulk Import:** Parse and import contacts from files or text blocks.

```python
import json

# Save
with open('phonebook.json', 'w') as f:
    json.dump(phone_book, f)

# Load
with open('phonebook.json', 'r') as f:
    phone_book = json.load(f)
```


***

## **Summary Table**

| Level        | Features                                      | Example Use Case                |
|--------------|-----------------------------------------------|---------------------------------|
| Basic        | Dict add, update, delete, lookup              | Small scripts, learning basics  |
| Intermediate | Menu-driven, user input, display all          | CLI tools, practice projects    |
| Advanced     | Regex parsing, validation, bulk import        | Data cleaning, automation       |
| Expert       | File persistence, nested dicts, GUI/CLI       | Real-world apps, large datasets |

***

**Key Takeaways:**  
- Start with a dictionary for simple phone books.
- Add user interaction and validation for practical tools.
- Use regex for parsing and cleaning text data.
- Add persistence and advanced features for real-world use.
