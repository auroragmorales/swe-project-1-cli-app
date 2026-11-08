def show_menu():
    while True:
        print()
        print("Menu:")
        print("1. Play Round")
        print("2. View Stats")
        print("3. Exit")
        print()
        
        choice = input("Choose an Action (Enter 1-3): ").strip()

        if choice == "1":
            print()
            print("Starting game...")
        elif choice == "2":
            print()
            print("Showing stats...")
        elif choice == "3":
            print()
            break
        else:
            print()
            print("Invalid choice. Please try again")

        print()










"""
1. def show_menu(): creates a function named show_menu.
2. Everything indented underneath it belongs to that function.
3. print() displays text in the terminal.
4. When we call show_menu(), Python executes the code inside it

.strip() removes extra spaces at the beginning and 
end of what someone types.
"""