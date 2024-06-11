# # write 'hello world' to the console
# Creating the game logic
# The winner of the game is determined by three simple rules:

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# Game interaction considerations
# The computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors). Your game interaction will be through the console (Terminal).

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.



# write the game logic as per above context

import random   #importing random module
import sys      #importing sys module

def game():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    while True:
        print(f"Player: {player_score} Computer: {computer_score}")
        player = input("Rock, Paper, or Scissors? (or 'quit' to end the game): ").lower()
        if player == "quit":
            print("Thanks for playing!")
            sys.exit()
        if player != "rock" and player != "paper" and player != "scissors":
            print("Invalid input. Please try again.")
            continue
        computer = random.choice(["rock", "paper", "scissors"])
        print(f"The computer chose: {computer}")
        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "paper":
            if computer == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "scissors":
            if computer == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
game()

# Run the code
# Run the code in the terminal using the following command: python app.py. The game will start, and you can play Rock, Paper, Scissors with the computer. The game will continue until you type quit. The game will display the final score at the end.p


