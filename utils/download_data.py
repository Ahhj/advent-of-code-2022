import os
import pathlib
from dotenv import load_dotenv
from aocd import get_data
import datetime

load_dotenv()
DATA_DIR = pathlib.Path(os.getenv("DATA_DIR"))
YEAR = int(os.getenv("YEAR", 2021))


def download_data(year=None, day=None):
    data = get_data(year=year, day=day)

    file_path = DATA_DIR / f"input_{year}_{day}.txt"

    with file_path.open("w+") as f:
        f.write(data)


if __name__ == "__main__":
    today_dt = datetime.datetime.now()
    if today_dt.month != 12:
        year = min(YEAR, today_dt.year - 1)
        n_days = 25
    else:
        year = min(YEAR, today_dt.year)
        n_days = today_dt.day

    for day in range(1, n_days+1):
        download_data(year=year, day=day)