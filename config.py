import os
import pathlib
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

YEAR = int(os.getenv("YEAR", 2021))
DATA_DIR = pathlib.Path(__file__).parent / "DATA"
