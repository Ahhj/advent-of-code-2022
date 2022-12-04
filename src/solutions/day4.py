#%%
from toolz.functoolz import curry, compose
from itertools import starmap, tee
import aocd
from src.utils.read_input import read_input_data
import config

DAY = 4

input_data = read_input_data(DAY)
# %%
@curry
def split_by(delim, s):
    return s.split(delim)


@curry
def map_over_inner(func, iter):
    return map(curry(map, func), iter)


def fully_contained(p1, p2):
    start1, end1 = p1
    start2, end2 = p2

    min_start = start1 if start1 < start2 else start2
    max_end = end1 if end1 > end2 else end2

    if min_start == start1 and max_end == end1:
        return True
    elif min_start == start2 and max_end == end2:
        return True
    else:
        return False


def get_overlap(p1, p2):
    start1, end1 = p1
    start2, end2 = p2

    sections1 = set(range(start1, end1 + 1))
    sections2 = set(range(start2, end2 + 1))

    return sections1.intersection(sections2)


any_overlap = compose(bool, get_overlap)


# %% Tests for the functions above
assert not fully_contained((1, 2), (3, 4))
assert fully_contained((1, 4), (3, 4))
assert fully_contained((1, 1), (1, 4))

assert get_overlap((1, 1), (1, 4)) == set([1])
assert not get_overlap((1, 2), (3, 4))
assert get_overlap((1, 2), (2, 4)) == set([2])

assert any_overlap((1, 1), (1, 4))
assert not any_overlap((1, 2), (3, 4))
assert any_overlap((1, 2), (2, 4))

# %%
# Extract limits for each pair (e.g. [1, 2], [3, 4])
pairs = split_by("\n", input_data)
pair_ranges = map(split_by(","), pairs)
get_integer_limits = compose(compose(list, curry(map, int)), split_by("-"))
pair_limits = zip(*map_over_inner(get_integer_limits, zip(*pair_ranges)))

# Tee for reusing in 2 parts
pair_limits_a, pair_limits_b = tee(pair_limits)

n_fully_contained = sum(starmap(fully_contained, pair_limits_a))
aocd.submit(n_fully_contained, part="a", year=config.YEAR, day=DAY)

n_overlapping = sum(starmap(any_overlap, pair_limits_b))
aocd.submit(n_overlapping, part="b", year=config.YEAR, day=DAY)

# %%
