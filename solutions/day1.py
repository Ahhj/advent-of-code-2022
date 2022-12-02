from __future__ import annotations
from typing import Iterable
import aocd
import config

DAY = 1


def tokenize_integers(text: str, delimiter="\n") -> Iterable[int]:
    return map(int, text.split(delimiter))


def reduce_map_of_map(x):
    return list(map(list, x))


def read_input_data(day) -> str:
    input_path = config.DATA_DIR / f"input_{config.YEAR}_{day}.txt"

    with input_path.open("r") as input_file:
        input_data = input_file.read()

    return input_data


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


if __name__ == "__main__":
    input_data = read_input_data(DAY)
    calories_cleaned = clean_input_data(input_data)
    total_calories_asc = get_total_calories_ascending(calories_cleaned)

    largest_calories_idx, largest_calories = total_calories_asc[0]
    print(f"Largest total calories: {largest_calories:,}")

    aocd.submit(largest_calories, part="a", year=config.YEAR, day=DAY)

    _, largest_3_calories = zip(*total_calories_asc[:3])
    solution_b = sum(largest_3_calories)
    print(f"Sum of top-3 largest calories: {solution_b:,}")

    aocd.submit(solution_b, part="b", year=config.YEAR, day=DAY)
