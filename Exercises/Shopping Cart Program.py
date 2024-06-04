# Shopping Cart Program - Uses collections 6/3/2024

foods = []
prices = []
subtotal = 0
total = 0

tax = 0
tax_rate = 0.06

while True:
    food = input("Enter a food to buy (q to stop): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print ("----- YOUR CART -----")

for food in foods:
    print(food)

for price in prices:
    subtotal += price
    tax = subtotal * tax_rate
    total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print()
print(f"Your total is: ${total:.2f}")