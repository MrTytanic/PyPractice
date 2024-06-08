# guessing numbers game
import random
import time

low = 1
high = 6
score = 0

# game show host
print("Welcome to the random number game! I am your host, Randy.")
time.sleep(1)
print("I will generate a random number between one to six. You have to guess the number!")
time.sleep(1)

# game loop
while True:
    # Generate random number
    generated_number = random.randint(low, high)
    print("\nReady? Here we go!")

    # guessing
    while True:
        try:
            player_input = int(input("Guess the number and you will get 1 point!: "))

            if player_input == generated_number:
                print("Correct!")
                score += 1
                print(f"Your score is now {score}!")
                break
            else:
                print("WRONG! Guess again...")
        except:
            print("That's an invalid input, silly! Now choose a number, or else.")

    # continue?
    continue_game = input("Would you like to continue? (yes/no): ").lower()
    if continue_game == 'no':
        print("Thank you for playing!")
        print(f"Your final score was: {score}")
        break