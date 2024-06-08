# Resturant Menu

entree = {"steak": 43.00,
          "salad": 15.00,
          "shrimp": 35.00,
          "lobster": 50.00,
          "pasta": 30.00}

beverage = {"water": 5.00,
            "soda": 6.00,
            "wine": 12.00}

tax_rate = 0.06
bill = []
total = 0

# menu
while True:
    menu_prompt = input("Waiter: Would you like to see our menu?: ")
    if menu_prompt.lower() == "yes":
        print("Okay, here is a list of our items and their prices")
        # Combine entrees and beverages into a single dictionary for display
        full_menu = {**entree, **beverage}
        menu_items = [f"{item}: ${price:.2f}" for item, price in full_menu.items()]
        menu_string = ", ".join(menu_items) + "."
        print(menu_string)
        break
    elif menu_prompt.lower() == "no":
        print("Sir you need the menu to order but okay...")
        break
    else:
        print("Sir I cannot understand what you are saying...")

# ordering items
while True:
    order_prompt = input("Waiter: What would you like to order? (Type 'done' to finish): ").lower()
    if order_prompt == "done":
        break
    elif order_prompt in full_menu:
        bill.append(order_prompt)
        total += full_menu[order_prompt]
        print(f"{order_prompt.capitalize()} added to your bill. Current total (without tax): ${total:.2f}")
    else:
        print("That item is not on the menu, please order again.")

# calcultate total
tax = total * tax_rate
total_with_tax = total + tax

print("\nYour final bill:")
for item in bill:
    print(f"{item.capitalize()}: ${full_menu[item]:.2f}")
print(f"Subtotal: ${total:.2f}")
print(f"Tax (6%): ${tax:.2f}")
print(f"Total: ${total_with_tax:.2f}")
