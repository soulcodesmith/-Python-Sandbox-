import random

# project - Rock, Paper and Scissors.

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_pick == "q":
        break
        print("Goodbye!")
        
    if user_pick not in options:
        print("Invalid Input, Try again!")
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    
    elif user_pick == computer_pick:
        print("It's a tie!")

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")
