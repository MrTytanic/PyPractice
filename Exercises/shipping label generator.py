# shipping label generator
def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

# user input
prefix = input("What is the client's prefix (Press enter to leave blank): ").capitalize()
first_name = input("What is the client's first name?: ").capitalize()
last_name = input("What is the client's last name?: ").capitalize()
suffix = input("What is the client's suffix? (Press enter to leave blank): ").capitalize()
address = input("What address?: ")
cities = input("What city?: ").capitalize()
states = input("What state?: ").upper()
zipcode = input("What zipcode?: ")

# name
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name(f"{prefix}", f"{first_name}", f"{last_name}", f"{suffix}")

# address

print_address(street=f"{address}",
              city=f"{cities}",
              state=f"{states}",
              zip=f"{zipcode}"
              )

print(print_address)