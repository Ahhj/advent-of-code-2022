# %%
from __future__ import annotations
from typing import Iterable
import aocd
import config as config
from src.utils.read_input import read_input_data

DAY = 1


def tokenize_integers(text: str, delimiter="\n") -> Iterable[int]:
    return map(int, text.split(delimiter))


def reduce_map_of_map(x):
    return list(map(list, x))


def clean_input_data(input_data: str) -> Iterable[Iterable[int]]:
    calories_cleaned = map(tokenize_integers, input_data.split("\n\n"))
    calories_cleaned = reduce_map_of_map(calories_cleaned)
    return calories_cleaned


def get_total_calories_ascending(calories_data: Iterable[Iterable[int]]):
    total_calories_indexed = enumerate(map(sum, calories_data))
    total_calories_asc = sorted(
        total_calories_indexed, key=lambda x: x[1], reverse=True
    )
    return total_calories_asc


input_data = read_input_data(DAY)
calories_cleaned = clean_input_data(input_data)
total_calories_asc = get_total_calories_ascending(calories_cleaned)

# %% # Part a
largest_calories_idx, largest_calories = total_calories_asc[0]
aocd.submit(largest_calories, part="a", year=config.YEAR, day=DAY)

# %% # Part b
_, largest_3_calories = zip(*total_calories_asc[:3])
aocd.submit(sum(largest_3_calories), part="b", year=config.YEAR, day=DAY)
