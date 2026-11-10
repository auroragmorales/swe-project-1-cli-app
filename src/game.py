import random

from game_data import record_win, record_loss, record_tie


def play_round():
    choices = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower().strip()

        if player_choice in choices:
            break

        else:
            print("Invalid choice. Please try again")

    computer_choice = random.choice(choices)

    print()
    print(f"👤 You chose: {player_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print()
        print("It's a tie! 🤝")
        record_tie()
        
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or 
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print()
        print("You win!! 🎉")
        record_win()

    else:
        print()
        print("Computer wins! You lose! 😢")
        record_loss()

    print("\n" + "-" * 35)