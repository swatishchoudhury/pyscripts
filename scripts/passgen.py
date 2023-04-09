"""
Password Generator - A Python script that generates a random password and saves it to the clipboard.

This script uses the win32clipboard module to save the generated password to the clipboard, making it easy to paste into other applications. The password is generated using a combination of lowercase and uppercase letters, digits, and symbols.

Usage:
python passgen.py
or
Just double click on the passgen.py file, if you have Python installed, and it will be saved to your clipboard.

Note: You can customize the length of the password by changing the length argument in the generate_password function.

This script is open source and available on GitHub at https://github.com/swatishchoudhury/pyscripts.

"""

import win32clipboard
import random
import string


def generate_password(length=16):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    chars = lowercase + uppercase + digits + symbols + symbols
    password = "".join(random.choice(chars) for _ in range(length))
    return password


password = generate_password(16)

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(password)
win32clipboard.CloseClipboard()

# print(f"The generated password is {password}")
print("Password saved to clipboard.")
