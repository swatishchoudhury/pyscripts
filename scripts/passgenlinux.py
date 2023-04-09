"""
Password Generator - A Python script that generates a random password and saves it to the clipboard.

This script uses the xclip command-line tool to save the generated password to the clipboard, making it easy to paste into other applications. The password is generated using a combination of lowercase and uppercase letters, digits, and symbols.

Usage:
python passgenlinux.py

Note: You can customize the length of the password by changing the length argument in the generate_password function.

This script is open source and available on GitHub at https://github.com/swatishchoudhury/pyscripts.

"""
import random
import string
import subprocess


def generate_password(length=16):
    """Generate a random password with specified length."""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    chars = lowercase + uppercase + digits + symbols
    password = "".join(random.choice(chars) for _ in range(length))
    return password


password = generate_password(16)

proc = subprocess.Popen(["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE)
proc.communicate(input=password.encode())

print("Password saved to clipboard.")
