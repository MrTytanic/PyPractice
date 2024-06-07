# Resturant Menu - A humours interactive "game" that utilizes dictionaries

entree = {"steak": 43.00,
        "salad": 15.00,
        "shrimp": 35.000,
        "lobster": 50.00,
        "pasta": 30.00}

beverage = {"water": 5.00,
            "soda": 6.00,
            "wine": 12.00}

bill = []
total = 0

# prompt the user to use the menu
menu_prompt = input("Waiter: Would you like to see our menu?: ")
if menu_prompt == "yes":
    print("Okay, here is a list of our items and their prices")
    print(entree)
elif menu_prompt == "no":
    print("Sir you need the menu to order but okay...")
    input("What would you like to order?: ")
else:
    print("Sir I cannot understand what you are saying...")
