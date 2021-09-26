# game.py

print("Rock, Paper, Scissors, Shoot!")
print("-------------------------")

#PROMPT USER FOR INPUT

#user_name = input("Welcome! What is your name? ")
import os 
from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("PLAYER_NAME")
print("Welcome to the game,", user_name)

def take_choice() :
    user_choice = input("Choose 'rock', 'paper', or 'scissors': ")
    print("-------------------------")

#CHECK USER INPUT

    if (user_choice in ("rock", "paper", "scissors")) :
        print(user_name, "chose: ", user_choice)
        return user_choice

    else :
        print("Invalid choice.")
        #exit()
        return take_choice()

user_choice = take_choice()

#COMPUTER CHOICE (AT RANDOM)

import random
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose: ", computer_choice)

print("-------------------------")

#CALCULATING WINNER 

user_wins = "Congratulations! You won."
computer_wins = "The computer won. Sorry :("
tie = "It was a tie! Try again."
#result = " "

if (user_choice == computer_choice) :
    result = tie
elif ((user_choice == "rock") and (computer_choice == "scissors")) :
    result = user_wins
elif ((user_choice == "rock") and (computer_choice == "paper")) :
    result = computer_wins
elif ((user_choice == "paper") and (computer_choice == "scissors")) :
    result = computer_wins
elif ((user_choice == "paper") and (computer_choice == "rock")) :
    result = user_wins
elif ((user_choice == "scissors") and (computer_choice == "paper")) :
    result = user_wins
elif ((user_choice == "scissors") and (computer_choice == "rock")) :
    result = computer_wins
else :
    result = result

# if (result = tie):

print(result)
print("Thanks for playing,", user_name)