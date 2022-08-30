import random
from tkinter import N

computer_choice = random.choice(["rock", "paper", "scissors"])

N = [1, 2, 3, 4]

for i in N:

    user_choice = input("Do you choose - rock, paper or scissors?\n")

    if user_choice == computer_choice:
        print("TIE")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("WIN")

    elif user_choice == "paper" and computer_choice == "rock":
        print("WIN")

    elif user_choice == "scissors" and computer_choice == "paper":
        print ("WIN")

    else:
        print("You loose, computer wins")