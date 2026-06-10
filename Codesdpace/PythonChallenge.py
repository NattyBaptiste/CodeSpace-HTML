# Rock, Paper, Scissors game using Python

import random  # Import random module to let computer choose randomly

# Function to get computer's choice
def get_computer_choice():
    choices = ["r", "p", "s"]
    return random.choice(choices)

# Function to decide the winner of a round
def decide_winner(user, computer):
    # If both choices are the same, it's a tie
    if user == computer:
        return "tie"

    # Winning conditions for the user
    if (user == "r" and computer == "s") or \
       (user == "p" and computer == "r") or \
       (user == "s" and computer == "p"):
        return "user"

    # Otherwise computer wins
    return "computer"


# Score tracking variables
user_score = 0
computer_score = 0

# Game loop
while True:
    # Take user input
    user_choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()

    # Get computer choice
    computer_choice = get_computer_choice()

    # Display choices
    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Decide winner
    result = decide_winner(user_choice, computer_choice)

    # Update scores and show result
    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    # Ask if user wants to play again
    play_again = input("\nPlay again? (y/n): ").lower()

    # Break loop if user enters 'n'
    if play_again != "y":
        break

# Final scores
print("\nFinal Scores:")
print("Player:", user_score)
print("Computer:", computer_score)