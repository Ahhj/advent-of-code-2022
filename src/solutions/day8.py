# %%
import aocd
import numpy as np
from itertools import product
import config
from src.utils.read_input import read_input_data

DAY = 8

input_data = read_input_data(DAY)

# %% Part a

heights = np.array(list(map(list, input_data.split()))).astype(np.int32)

# Pad such that outer edge is always visible
heights = np.pad(heights, pad_width=1, constant_values=(-1))

nrows, ncols = heights.shape
assert nrows == ncols, "Array is not square!"

visible = np.zeros(heights.shape).astype(bool)

for i in range(1, nrows - 1):
    # Visible along columns?
    max_above = np.max(heights[:i], axis=0)
    max_below = np.max(heights[i + 1 :], axis=0)
    visible_y = (heights[i] > max_above) | (heights[i] > max_below)
    visible[i, :] |= visible_y

    # Visible along rows?
    max_left = np.max(heights[:, :i], axis=1)
    max_right = np.max(heights[:, i + 1 :], axis=1)
    visible_x = (heights[:, i] > max_left) | (heights[:, i] > max_right)
    visible[:, i] |= visible_x

total_visible = visible.sum()
aocd.submit(total_visible, part="a", year=config.YEAR, day=DAY)

# %% Part b
heights = np.array(list(map(list, input_data.split()))).astype(np.int32)
nrows, ncols = heights.shape

score = np.zeros(heights.shape)

for i, j in product(range(1, nrows - 1), range(1, ncols - 1)):
    tree_scores = np.zeros(4)

    # Above, below, left, right
    blocks = [
        heights[:i, j][::-1],
        heights[i + 1 :, j],
        heights[i, :j][::-1],
        heights[i, j + 1 :],
    ]

    for k, block in enumerate(blocks):
        for h in block:
            tree_scores[k] += 1

            if h >= heights[i, j]:
                break

    score[i, j] = np.prod(np.maximum(tree_scores, 1))

aocd.submit(int(np.max(score)), part="b", year=config.YEAR, day=DAY)
