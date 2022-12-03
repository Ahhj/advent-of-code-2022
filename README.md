# Advent of code 2022

This is my attempt at advent of code 2022.

The problems can be found [here](https://adventofcode.com/2022)

# Getting started

## Initial setup

Config is passed via a .env file (which is excluded from the repo via .gitignore).

The package `advent-of-code-data` is used to download the data and upload solutions.
A variable called `AOC_SESSION` must be added to the environmental variables (I'd recommend doing this via the .env file, but whatever works for you!).
This is a cookie which is set when you login to AoC. You can find it with your browser inspector.

## Downloading the data

To download the data, from the project root:

```
python -m src.utils.download_data
```

This will add data files up to and including the current day of the month (in December) to the `data` directory.
If the month is not December, it'll download data for all of last years problems.
