# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.

from menu import show_menu

def start_app():
    print()
    print("🎮 Welcome to Rock-Paper-Scissors! 🎮")
    show_menu()
    print("\n👋 Goodbye!")
    print()

if __name__ == "__main__":
    start_app()



'''
main.py starts the application.
menu.py displays the menu and handles the user's selection.
game.py handles the Rock-Paper-Scissors rounds.
game_data.py keeps track of the game statistics.
'''