# %%

import aocd
import re
from collections import OrderedDict
from copy import deepcopy
from itertools import chain
from toolz.functoolz import curry
import config
from src.utils.read_input import read_input_data

DAY = 5

input_data = read_input_data(DAY)


crates_data, moves_data = input_data.split("\n\n")

moves = map(curry(re.findall, r"move (\d+) from (\d) to (\d)"), moves_data.split("\n"))
moves = chain.from_iterable(moves)
moves = list(moves)

rows = crates_data.split("\n")
indexes = list(rows.pop(-1)[1::4])

rows = map(lambda row: row[1::4], rows)
columns = zip(*rows)

stacks = OrderedDict({})
for i, col in zip(indexes, columns):
    # Stacks are ordered left-to-right from top-to-bottom
    stacks[i] = list(filter(None, map(str.strip, col)))

# %% Part a


def solve_a(stacks, moves):
    stacks = deepcopy(stacks)

    for n, i, j in moves:
        n = int(n)

        # Reverse order since crates are added 1-by-1
        crates = stacks[i][:n][::-1]

        # Move the crates
        stacks[j] = crates + stacks[j]
        stacks[i] = stacks[i][n:]

    top_level_concat = "".join([crates[0] for _, crates in stacks.items()])
    aocd.submit(top_level_concat, part="a", year=config.YEAR, day=DAY)


solve_a(stacks, moves)
# %% Part b


def solve_b(stacks, moves):
    stacks = deepcopy(stacks)
    for n, i, j in moves:
        n = int(n)

        # No need to reverse order
        crates = stacks[i][:n]

        # Move the crates
        stacks[j] = crates + stacks[j]
        stacks[i] = stacks[i][n:]

    top_level_concat = "".join([crates[0] for _, crates in stacks.items()])
    aocd.submit(top_level_concat, part="b", year=config.YEAR, day=DAY)


solve_b(stacks, moves)
# %%
