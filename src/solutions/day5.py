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


def process_moves(moves_data):
    moves = map(
        curry(re.findall, r"move (\d+) from (\d) to (\d)"), moves_data.split("\n")
    )
    moves = chain.from_iterable(moves)
    moves = list(moves)
    return moves


def process_stacks(crates_data):
    rows = crates_data.split("\n")
    indexes = list(rows.pop(-1)[1::4])

    rows = map(lambda row: row[1::4], rows)
    columns = zip(*rows)

    stacks = OrderedDict({})
    for i, col in zip(indexes, columns):
        # Stacks are ordered left-to-right from top-to-bottom
        stacks[i] = list(filter(None, map(str.strip, col)))

    return stacks


def rearrange_crates(stacks, moves, one_by_one=True):
    stacks = deepcopy(stacks)
    for n, i, j in moves:
        n = int(n)

        crates = stacks[i][:n][:: 1 - 2 * one_by_one]

        # Move the crates
        stacks[j] = crates + stacks[j]
        stacks[i] = stacks[i][n:]

    return stacks


input_data = read_input_data(DAY)

crates_data, moves_data = input_data.split("\n\n")
stacks = process_stacks(crates_data)
moves = process_moves(moves_data)

stacks_a = rearrange_crates(stacks, moves)
top_level_concat = "".join([crates[0] for _, crates in stacks_a.items()])
aocd.submit(top_level_concat, part="a", year=config.YEAR, day=DAY)

stacks_b = rearrange_crates(stacks, moves, one_by_one=False)
top_level_concat = "".join([crates[0] for _, crates in stacks_b.items()])
aocd.submit(top_level_concat, part="b", year=config.YEAR, day=DAY)

# %%
