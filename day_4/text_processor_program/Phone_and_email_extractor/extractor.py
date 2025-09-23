import re
import pyperclip

# Define regex pattern for phone numbers (US-style example)
phone_pattern = re.compile(r'''
    (
        (\+?\d{1,3}[\s-])?             # Optional country code
        (\(?\d{3}\)?[\s.-]?)           # Area code with optional parentheses
        \d{3}                          # First 3 digits
        [\s.-]?                       # Separator
        \d{4}                          # Last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # Optional extension
    )
''', re.VERBOSE)

# Define regex pattern for emails
email_pattern = re.compile(r'''
    (
        [a-zA-Z0-9._%+-]+           # Username
        @
        [a-zA-Z0-9.-]+              # Domain
        \.[a-zA-Z]{2,}              # Extension
    )
''', re.VERBOSE)

# Get text from clipboard
text = pyperclip.paste()

# Find all phone numbers and emails in the text
phones = phone_pattern.findall(text)
emails = email_pattern.findall(text)

# Extract full phone numbers from groups
phone_numbers = [match[0] for match in phones]

# Combine results
results = phone_numbers + emails

if results:
    # Copy results to clipboard as newline separated string
    pyperclip.copy('\n'.join(results))
    print("Phone numbers and emails copied to clipboard:")
    print('\n'.join(results))
else:
    print("No phone numbers or emails found.")
