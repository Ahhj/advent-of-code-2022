# %%
import aocd
from itertools import repeat, tee
import config
from src.utils.read_input import read_input_data

DAY = 10

# %% Part a

input_data = read_input_data(DAY)

ops = []
register_X = [1]

for operation in input_data.split("\n"):
    if operation == "noop":
        register_X.extend(repeat(register_X[-1], 1))
    else:
        addx, magnitude = operation.split()
        assert addx == "addx"
        register_X.extend(repeat(register_X[-1], 1))
        register_X.append(register_X[-1] + int(magnitude))


aocd.submit(
    sum(register_X[i - 1] * i for i in range(20, 221, 40)),
    part="a",
    day=DAY,
    year=config.YEAR,
)

# %% Part b

nrows = 6
ncols = 40
crt = list(map(list, tee(repeat(" ", ncols), nrows)))

for i, x in enumerate(register_X[:-1]):
    pixel_col = i % 40
    pixel_row = i // 40
    sprite_pixels = [x - 1, x, x + 1]
    if pixel_col in sprite_pixels:
        crt[pixel_row][pixel_col] = "#"


def get_image(crt):
    return "\n".join(map(" ".join, crt))


def display(crt):
    return print(get_image(crt))


display(crt)

# %%

visible_letters = "PZULBAUA"
aocd.submit(visible_letters, part="b", day=DAY, year=config.YEAR)

# %%
