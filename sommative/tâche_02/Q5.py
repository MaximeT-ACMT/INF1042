# Maxime Talbot
# Rock, Paper, Scissors game that tracks the score against the computer.

import random

wins = 0
losses = 0

while True:
    user_choice = input("Choose (rock, paper, scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if (user_choice == computer_choice):
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You won!")
        wins += 1
    else:
        print("You lost!")
        losses += 1

    print(f"Score -> Wins: {wins} | Losses: {losses}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if (play_again != "yes"):
        break
    
    # This is a rock papier scissors code. We make all thepossibilites for wins and then everything else is a lost.