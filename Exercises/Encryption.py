# substitution encryption using random characters

import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

# generate key
random.shuffle(key)

# encrypt user input
plain_text = input("What would you like to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"Original message: {plain_text}.")
print(f"Encrypted messaged: {cipher_text}.")

# decrypt user input
cipher_text = input("What would you like to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"Encrypted message: {cipher_text}.")
print(f"Original message: {plain_text}.")