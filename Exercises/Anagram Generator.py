import random

while True:
    # User input
    user_input = input("What word/phrase would you like to become an anagram?: ")

    # remove non-letters
    filtered_input = [char for char in user_input if char.isalpha()]

    # shuffle and create anagram
    random.shuffle(filtered_input)
    anagram = ''.join(filtered_input)
    print("Anagram:", anagram)