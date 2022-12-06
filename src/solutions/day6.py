# %%

import aocd
from itertools import islice
import collections
import config
from src.utils.read_input import read_input_data

DAY = 6


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def count_until_all_chars_distinct(input_data, window_length):
    chars_processed = window_length

    for window in sliding_window(input_data, window_length):
        # All windows chars are different
        all_chars_distinct = len(window) == len(set(window))

        if all_chars_distinct:
            return chars_processed

        chars_processed += 1


input_data = read_input_data(DAY)

chars_processed = count_until_all_chars_distinct(input_data, 4)
aocd.submit(chars_processed, part="a", year=config.YEAR, day=DAY)

# %%

chars_processed = count_until_all_chars_distinct(input_data, 14)
aocd.submit(chars_processed, part="b", year=config.YEAR, day=DAY)
