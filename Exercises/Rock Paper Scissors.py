import random
options = ("rock", "paper", "scissors")

replay = True
while replay:

    player = None
    # computer chooses
    computer = random.choice(options)
    # player chooses
    while player not in options:
        # player input
        player = input("Enter either rock, paper, or scissors: ")

        # game decision

        print(computer)

    if player == computer:
        print("Draw!")
    #player wins
    elif player == 'rock' and computer == 'scissors':
        print("You win!")
    elif player == 'paper' and computer == 'rock':
        print("You win!")
    elif player == 'scissors' and computer == 'paper':
        print("You win!")
    #opponent wins
    else:
        print("You lose, you should be ashamed.")

    if not input("Play again? (Y/N)").lower() == "y":
        replay = False
        print("The end.")


