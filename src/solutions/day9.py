# %%
import aocd
import re
import numpy as np
import config
from src.utils.read_input import read_input_data

DAY = 9
GRID_SIZE = 1000

direction_magnitude_pattern = r"([UDLR]) (\d+)"
head_deltas = {
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
    "L": np.array([-1, 0]),
    "R": np.array([1, 0]),
}


def update_head_1step(current_pos, direction):
    prev_pos = current_pos[:]
    current_pos += head_deltas[direction]
    assert np.abs(current_pos - prev_pos).sum() <= 1
    return current_pos


def update_tail_1step(current_pos, head_pos):
    updated = False
    segment_vector = head_pos - current_pos
    segment_length = np.max(np.abs(segment_vector))

    if segment_length > 1:
        current_pos += np.sign(segment_vector)
        updated = True

    return current_pos, updated


def evolve_knots(head_movements, n_knots):
    # Initial conditions
    p0 = GRID_SIZE // 2
    knots = (np.ones((n_knots, 2)) * p0).astype(int)  # Current position
    knot_heatmap = np.zeros((n_knots, GRID_SIZE, GRID_SIZE))  # history
    knot_heatmap[:, p0, p0] += 1

    for direction, n_steps in head_movements:
        for _ in range(int(n_steps)):
            knots[0] = update_head_1step(knots[0], direction)
            xh, yh = knots[0]
            knot_heatmap[0, xh, yh] += 1

            for k in range(1, n_knots):
                knots[k], tail_updated = update_tail_1step(knots[k], knots[k - 1])
                if tail_updated:
                    xt, yt = knots[k]
                    knot_heatmap[k, xt, yt] += 1

    return knot_heatmap


input_data = read_input_data(DAY)
head_movements = re.findall(direction_magnitude_pattern, input_data)

# %% Part a
n_knots = 2
knot_heatmap = evolve_knots(head_movements, n_knots)
aocd.submit(np.count_nonzero(knot_heatmap[-1]), part="a", day=DAY, year=config.YEAR)

# %% Part b

n_knots = 10
knot_heatmap = evolve_knots(head_movements, n_knots)
aocd.submit(np.count_nonzero(knot_heatmap[-1]), part="b", day=DAY, year=config.YEAR)

# %%
