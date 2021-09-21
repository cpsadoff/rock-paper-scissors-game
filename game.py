# game.py

print("Rock, Paper, Scissors, Shoot!")

#PROMPT USER FOR INPUT

user_choice = input("Choose 'rock', 'paper', or 'scissors': ")

if (user_choice in ("rock", "paper", "scissors")):
    print("You chose: ", user_choice)
    
else :
    print("Invalid choice.")
    user_choice = input("Choose 'rock', 'paper', or 'scissors': ")

#i want to run this recursively

#COMPUTER CHOICE (AT RANDOM)

import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose: ", computer_choice)
