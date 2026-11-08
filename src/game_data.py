game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

def record_win():
    game_stats["wins"] += 1

def record_loss():
    game_stats["losses"] += 1

def record_tie():
    game_stats["ties"] += 1

def show_stats():
    print()
    print("Your Game Statistics")
    print(f"Wins: {game_stats['wins']}")
    print(f"Losses: {game_stats['losses']}")
    print(f"Ties: {game_stats['ties']}")