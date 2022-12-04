import config


def read_input_data(day) -> str:
    input_path = config.DATA_DIR / f"input_{config.YEAR}_{day}.txt"

    with input_path.open("r") as input_file:
        input_data = input_file.read()

    return input_data
