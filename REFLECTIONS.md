# Reflections


1. Share one aspect of building this project you found challenging and how you overcame it.

One of the most challenging parts of this project was figuring out how to organize my code into different files and get everything working together. At first, I wasn't really sure what code belonged in each file or how to connect them using imports. I had to understand the purpose of having separate modules instead of putting all of my code into one file since that's what I was most used to. As I worked on the project, I started organizing the code based on what each file was responsible for. For example, I used main.py as the main entry point for the program, menu.py to display the menu and handle the user's choices, game.py to manage each round, and game_data.py to keep track of the statistics. I also had to use imports so the different files could access the functions they needed. Testing the game and running into errors helped me understand how the files connected. I learned that separating code into modules makes a project more organized and easier to work on. Although it was confusing at first, working through the project helped me become more comfortable with organizing a Python program.


2. Share one technical concept that you gained a deeper understanding of
   through building this project. Explain that concept in simple terms and
   explain how it is used in your project.

I think a concept I understand better was conditional statements. Conditional statements are really helpful as they allow a program to make decisions based on whether certain conditions are true or false. Before working on this project, I understood the basic idea of `if, elif`, and `else`, but building the game helped me understand how they work together in a program. I used those conditional statements in game.py to compare the player's choice with the computer's choice and determine the result of each round. For example, the game first checks whether both choices are the same, which means the round ends up a tie. Then it checks whether the player's choice beats the computer's choice. If neither of those conditions is true, the computer wins. I also used conditional statements in menu.py to determine what should happen when the player selects an option. Depending on whether the player chooses to play a round, view statistics, or exit, the program performs a different action. Building this project helped me better understand how conditional statements are used to control what happens in a program and make decisions based on user input.

