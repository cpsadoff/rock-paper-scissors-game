# game.py

print("Rock, Paper, Scissors, Shoot!")

#PROMPT USER FOR INPUT

user_choice = input("Choose 'rock', 'paper', or 'scissors': ")

#CHECK USER INPUT

if (user_choice in ("rock", "paper", "scissors")) :
    print("You chose: ", user_choice)

else :
    print("Invalid choice.")
    user_choice = input("Choose 'rock', 'paper', or 'scissors': ")

# i want to run this recursively

#COMPUTER CHOICE (AT RANDOM)

import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose: ", computer_choice)

#CALCULATING WINNER
user_wins = "Congratulations! You won."
computer_wins = "The computer won. Sorry :("
tie = "It was a tie! Try again."

if (user_choice == computer_choice) :
    winner = tie
elif ((user_choice == "rock") and (computer_choice == "scissors")) :
    winner = user_wins
elif ((user_choice == "rock") and (computer_choice == "paper")) :
    winner = computer_wins
elif ((user_choice == "paper") and (computer_choice == "scissors")) :
    winner = computer_wins
elif ((user_choice == "paper") and (computer_choice == "rock")) :
    winner = user_wins
elif ((user_choice == "scissors") and (computer_choice == "paper")) :
    winner = user_wins
elif ((user_choice == "scissors") and (computer_choice == "rock")) :
    winner = computer_wins
else :
    winner = tie

# if (winner = tie):

print(winner)