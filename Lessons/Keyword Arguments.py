# keyword arguments = an argument preceded by an identifier

for number in range(1, 11):
    print(number, end=" ")
print()
print("1", "2", "3", "4", "5", sep="-")

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="John", first="James")