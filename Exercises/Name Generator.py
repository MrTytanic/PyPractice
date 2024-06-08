# name generator using random functions and dictionaries
import random

first_names = ["Abraham", "Ronald", "Donald", "Joseph", "Theodore", "George", "Dwight"]
last_names = ["Lincoln", "Reagan", "Trump", "Biden", "Roosevelt", "Washington", "Eisenhower"]

fn_chosen = random.choice(first_names)
ln_chosen = random.choice(last_names)
print(fn_chosen, ln_chosen)