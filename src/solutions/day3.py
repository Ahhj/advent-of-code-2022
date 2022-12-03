# %%
from __future__ import annotations
from itertools import starmap
import string
import aocd
import config as config
from src.solutions.day1 import read_input_data


DAY = 3


def get_common_elements(*s):
    return set(s[0]).intersection(*s[1:])


def pluck_first(seq):
    """Pluck the first item each iterable in a sequence"""
    return map(next, map(iter, seq))


def group_without_overlaps(iterable, n):
    return zip(*([iter(iterable)] * n))


priority_map = dict(zip(string.ascii_letters, range(1, 53)))

input_data = read_input_data(DAY)
rucksack_data = input_data.split("\n")

# %% Part a

# Split the compartments
compartment_data = map(lambda x: group_without_overlaps(x, len(x) // 2), rucksack_data)

# Find the duplicates
common_item_types = starmap(get_common_elements, compartment_data)
duplicated_item_types = pluck_first(common_item_types)

# Map the priorities of the duplicates
duplicate_priorities = map(priority_map.get, duplicated_item_types)

aocd.submit(sum(duplicate_priorities), part="a", year=config.YEAR, day=DAY)

# %% Part b

group_size = 3
grouped_rucksack_data = group_without_overlaps(rucksack_data, group_size)

# Find the common item types
common_item_types = starmap(get_common_elements, grouped_rucksack_data)
badge_item_types = pluck_first(common_item_types)

# Map the priorities of the duplicates
badge_priorities = map(priority_map.get, badge_item_types)

aocd.submit(sum(badge_priorities), part="b", year=config.YEAR, day=DAY)

# %%
