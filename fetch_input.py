import argparse
import httpx
import os

from dotenv import load_dotenv

load_dotenv()

INPUT_URL = "https://adventofcode.com/2026/day/{}/input".format

parser = argparse.ArgumentParser(description="Fetch the puzzle input for a given day.")
parser.add_argument(
    "day",
    metavar="int",
    type=int,
    help="The day of the puzzle whose input will be fetched.",
)


def fetch_input(day: int):
    print(f"Fetching Day {day}")

    session = os.getenv("SESSION")
    if session is None:
        raise os.error("Missing env var SESSION")

    resp = httpx.get(INPUT_URL(day), cookies={"session": session})

    puzzle_input = resp.text

    with open(f"./inputs/{day:02d}", "w") as f:
        f.writelines(puzzle_input)


if __name__ == "__main__":
    args = parser.parse_args()
    fetch_input(args.day)
