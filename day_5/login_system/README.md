# Login System: Basic to Advanced

Let's build your understanding of a login system in Python, step by step.

***

## 1. **Basic Login System**
Checks a single username and password (hardcoded).

```python
stored_username = "user1"
stored_password = "pass123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Login successful!")
else:
    print("Login failed.")
```
- **Simple check:** Only one user, no security features.

***

## 2. **Intermediate Login System**
Supports multiple users using a dictionary.

```python
users = {
    "user1": "pass123",
    "admin": "adminpass",
    "guest": "guestpass"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Login failed.")
```
- **Multiple users:** Checks if username exists and password matches.

***

## 3. **Advanced Login System**
Adds features like limited attempts, password masking, and user registration.

### **A. Limited Attempts**
```python
users = {"user1": "pass123"}
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Login failed. Attempts left: {attempts}")
if attempts == 0:
    print("Account locked.")
```

### **B. Password Masking**
Use the `getpass` module to hide password input (works in terminal):
```python
import getpass
password = getpass.getpass("Enter password: ")
```

### **C. User Registration**
Allow new users to sign up:
```python
users = {}
choice = input("Type 'login' or 'register': ")
if choice == "register":
    new_user = input("Choose a username: ")
    new_pass = input("Choose a password: ")
    users[new_user] = new_pass
    print("Registration successful!")
elif choice == "login":
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Login failed.")
```

***

## **Summary Table**
| Level         | Features                                 |
|---------------|------------------------------------------|
| Basic         | Single user, hardcoded credentials       |
| Intermediate  | Multiple users, dictionary lookup        |
| Advanced      | Limited attempts, password masking, registration |
