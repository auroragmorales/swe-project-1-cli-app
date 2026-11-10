# Rock-Paper-Scissors CLI Game

## About the Project

This is a command-line Rock-Paper-Scissors game built with Python. The player plays against the computer by choosing rock, paper, or scissors. The computer randomly selects its choice, and the game determines who wins each round. The game also keeps track of wins, losses, and ties, and allows players to view their game statistics.

## Features

- Play Rock-Paper-Scissors against the computer
- Computer randomly selects rock, paper, or scissors
- Determine whether the player wins, loses, or ties
- Track wins, losses, and ties
- View total games played and win rate
- Handle invalid menu choices and player inputs
- View final statistics before exiting the game

## How to Run the Game

1. Clone the repository:

    git clone git@github.com:auroragmorales/swe-project-1-cli-app.git

2. Navigate into the project folder:

     ```bash
   cd swe-project-1-cli-app
   ```

3. Create a virtual environment:

    ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```
5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Start the game:

   ```bash
   python3 src/main.py
   ```

## How to Play

When the game starts, a menu will appear with three options:

1. Play Round – Start a round of Rock-Paper-Scissors.

2. View Stats – See your wins, losses, ties, total games played and win rate.

3. Exit – Display your final statistics and end the game.

When you choose to play, you enter rock, paper, or scissors. The computer will randomly choose its move, and the game will display both choices and the result.

## Example Usage

```text
🎮 Welcome to Rock-Paper-Scissors! 🎮

☰ Menu:
1. Play Round 🎯
2. View Stats 📊
3. Exit 🚪


Choose an Action (Enter 1-3): 1

Choose rock, paper, or scissors: rock

👤 You chose: rock
💻 Computer chose: scissors

You win!! 🎉
```

The example above shows one possible round. The computer's choice and the result will vary each time you play. To view your statistics, select option 2 from the menu. To exit the game, select option 3.

## Running Tests

To run the project's tests, activate your virtual environment and enter:

```bash
pytest
```

The tests check that the game statistics functions correctly update wins, losses, and ties and display the correct game statistics.