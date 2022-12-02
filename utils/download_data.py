from aocd import get_data
import datetime
import config


def download_data(year=None, day=None):
    data = get_data(year=year, day=day)

    file_path = config.DATA_DIR / f"input_{year}_{day}.txt"

    with file_path.open("w+") as f:
        f.write(data)


if __name__ == "__main__":
    today_dt = datetime.datetime.now()
    if today_dt.month != 12:
        year = min(config.YEAR, today_dt.year - 1)
        n_days = 25
    else:
        year = min(config.YEAR, today_dt.year)
        n_days = today_dt.day

    for day in range(1, n_days+1):
        download_data(year=year, day=day)