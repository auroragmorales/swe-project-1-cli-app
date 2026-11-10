import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import game_data
import pytest


@pytest.fixture(autouse=True)
def reset_game_stats():
    game_data.game_stats.update({
        "wins": 0,
        "losses": 0,
        "ties": 0
    })

def test_record_win():
#creates a test for win function
    game_data.record_win()
#runs  actual function
    assert game_data.game_stats["wins"] == 1
#assert checks whether the wins counter equals 1


def test_record_loss():
    game_data.record_loss()

    assert game_data.game_stats["losses"] == 1
# Checks whether the losses counter increased to 1

def test_record_tie():
    game_data.record_tie()

    assert game_data.game_stats["ties"] == 1
#Checks whether the ties counter increased to 1

def test_show_stats(capsys):
#checking whether statistics function displays the correct info    
    game_data.record_win()
    game_data.record_loss()

    game_data.show_stats()

    captured = capsys.readouterr()

    assert "Total Games: 2" in captured.out
    assert "Win Rate: 50.0%" in captured.out