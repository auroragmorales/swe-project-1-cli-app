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
    print()
    print("📊 Your Game Statistics:")
    print()
    print(f"🏆 Wins: {game_stats['wins']}")
    print(f"💔 Losses: {game_stats['losses']}")
    print(f"🤝 Ties: {game_stats['ties']}")

    total = sum(game_stats.values())
# game_stats.values() gets the #s stored in dictionary: wins, losses, and ties
# sum() adds those numbers together
    print(f"🎮 Total Games: {total}")

    if total > 0:
        win_rate = (game_stats["wins"] / total) * 100
    else:
        win_rate = 0
    print()
    print(f"📈 Win Rate: {win_rate:.1f}%")
    # :.1f displays one decimal place
    '''
    the total number of games is calculated. 
    If at least 1 game has been played, we calculate the percentage of games won. 
    If no games have been played, the win rate is 0 instead of causing an error
    '''

    print("\n" + "-" * 35)
