# Quiz game using 2D Collections

import random
score = 0

# list of countries that are randomly chosen
europe = ["Germany", "Italy", "France", "The United Kingdom", "Serbia"]
americas = ["The United States", "Mexico", "Canada", "El Salvador", "Panama"]
middle_east = ["Iraq", "Saudi Arabia", "Lebanon", "Jordan"]
asia = ["China", "Japan", "North Korea", "South Korea"]
africa = ["Gabon", "Chad", "Liberia", "Morocco", "Algeria", "Zimbabwe"]

# list of answers for each continent
europe_answer = ["Berlin", "Rome", "Paris", "London", "Belgrade"]
americas_answer = ["Washington D.C.", "Mexico City", "Ottawa", "San Salvador", "Panama City"]
middle_east_answer = ["Baghdad", "Riyadh", "Beirut", "Amman"]
asia_answer = ["Beijing", "Tokyo", "Pyongyang", "Seoul"]
africa_answer = ["Libreville", "N'Djamena", "Monrovia", "Rabat", "Algiers", "Harare"]

# dictionary for country-capital mappings
country_to_capital = {}

# populate the dictionary
for continent, countries, capitals in zip(
    ["Europe", "Americas", "Middle East", "Asia", "Africa"],
    [europe, americas, middle_east, asia, africa],
    [europe_answer, americas_answer, middle_east_answer, asia_answer, africa_answer]
):
    for country, capital in zip(countries, capitals):
        country_to_capital[country] = capital

# continent selector
while True:
    continent = input("What continent?: ").strip().lower()

    if continent == 'europe':
        selected_country = random.choice(europe)
    elif continent in ['america', 'americas']:
        selected_country = random.choice(americas)
    elif continent in ['middle east', 'middle-east']:
        selected_country = random.choice(middle_east)
    elif continent == 'asia':
        selected_country = random.choice(asia)
    elif continent == 'africa':
        selected_country = random.choice(africa)
    else:
        print("That is an invalid input!")
        continue

    correct_answer = country_to_capital[selected_country]
    user_answer = input(f"What is the capital of {selected_country}? ").strip()

    if user_answer.lower() == correct_answer.lower():
        score += 1
        if score == 1:
            print ("Correct! You now have 1 point!")
        else:
            print(f"Correct! You now have {score} points!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")