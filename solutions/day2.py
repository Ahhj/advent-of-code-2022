# %%
from __future__ import annotations
import itertools
import aocd
import config
from solutions.day1 import read_input_data

DAY = 2

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3
WIN_SCORE = 6
LOSE_SCORE = 0
DRAW_SCORE = 3

# %% # Part a
# Mapping opponent's play --> my play --> score
scores_map_a = {
    "ROCK": {
        "ROCK": ROCK_SCORE + DRAW_SCORE,
        "PAPER": PAPER_SCORE + WIN_SCORE,
        "SCISSORS": SCISSORS_SCORE + LOSE_SCORE,
    },
    "PAPER": {
        "ROCK": ROCK_SCORE + LOSE_SCORE,
        "PAPER": PAPER_SCORE + DRAW_SCORE,
        "SCISSORS": SCISSORS_SCORE + WIN_SCORE,
    },
    "SCISSORS": {
        "ROCK": ROCK_SCORE + WIN_SCORE,
        "PAPER": PAPER_SCORE + LOSE_SCORE,
        "SCISSORS": SCISSORS_SCORE + DRAW_SCORE,
    },
}

# Decode opponent's play
opponent_play_map = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
}

# Decode my play
my_play_map_a = {
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}


def decrypt_plays_a(opponent_play_encrypted: str, my_play_encrypted: str) -> list[str]:
    opponent_play = opponent_play_map[opponent_play_encrypted]
    my_play = my_play_map_a[my_play_encrypted]
    return opponent_play, my_play


def get_score_a(opponent_play: str, my_play: str) -> int:
    return scores_map_a[opponent_play][my_play]


input_data = read_input_data(DAY)
encrypted_plays = [row.split(" ") for row in input_data.split("\n")]

plays_a = itertools.starmap(decrypt_plays_a, encrypted_plays)
scores_a = list(itertools.starmap(get_score_a, plays_a))
total_score_a = sum(scores_a)
aocd.submit(total_score_a, part="a", year=config.YEAR, day=DAY)

# %% # Part b
# Mapping opponents play --> outcome --> score
scores_map_b = {
    "ROCK": {
        "WIN": PAPER_SCORE + WIN_SCORE,
        "LOSE": SCISSORS_SCORE + LOSE_SCORE,
        "DRAW": ROCK_SCORE + DRAW_SCORE,
    },
    "PAPER": {
        "WIN": SCISSORS_SCORE + WIN_SCORE,
        "LOSE": ROCK_SCORE + LOSE_SCORE,
        "DRAW": PAPER_SCORE + DRAW_SCORE,
    },
    "SCISSORS": {
        "WIN": ROCK_SCORE + WIN_SCORE,
        "LOSE": PAPER_SCORE + LOSE_SCORE,
        "DRAW": SCISSORS_SCORE + DRAW_SCORE,
    },
}

# Decode outcome
outcome_map_b = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}


def decrypt_plays_b(opponent_play_encrypted: str, outcome_encrypted: str) -> list[str]:
    opponent_play = opponent_play_map[opponent_play_encrypted]
    outcome = outcome_map_b[outcome_encrypted]
    return opponent_play, outcome


def get_score_b(opponent_play: str, outcome: str) -> int:
    return scores_map_b[opponent_play][outcome]


plays_b = itertools.starmap(decrypt_plays_b, encrypted_plays)
scores_b = list(itertools.starmap(get_score_b, plays_b))
total_score_b = sum(scores_b)
aocd.submit(total_score_b, part="b", year=config.YEAR, day=DAY)

# %%
