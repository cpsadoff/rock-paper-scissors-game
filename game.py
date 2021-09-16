# game.py

print("Rock, Paper, Scissors, Shoot!")

#PROMPT USER FOR INPUT

user_choice = input("Choose 'rock', 'paper', or 'scissors': ")
print("You chose: ")
print(user_choice)
#if (user_choice == "rock"):
#    print("You chose: ")
#    print(user_choice)
#elif (user_choice == "paper"):
#    print("You chose: ")
#    print(user_choice)
#elif (user_choice == "scissors"):
#    print("You chose: ")
#    print(user_choice)
#else :
#    print("Invalid choice.")
#    user_choice = input("Choose 'rock', 'paper', or 'scissors': ")

#have to run this recursively

#COMPUTER CHOICE (AT RANDOM)

import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose: ")
print(computer_choice)