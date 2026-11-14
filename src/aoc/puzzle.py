import os
import httpx

from dotenv import load_dotenv

load_dotenv()

INPUT_URL = "https://adventofcode.com/{}/day/{}/input".format
CACHE_PATH = "./inputs/{}-{:02d}".format


def input(year: int, day: int) -> str:
    """input takes the year and the day as integers and returns the "puzzle input"
    for that combination. It will first try to retrieve the input from a local
    cache. If the input is not found in that cache, it will try to fetch the input
    from the Advent of Code server (this requires a SESSION environment variable).
    The result of this fetch will be cached for future retrievals.
    """

    try:
        return __read_from_cache(year, day)
    except FileNotFoundError:
        __fetch_from_server(year, day)
        return __read_from_cache(year, day)


def __read_from_cache(year: int, day: int) -> str:
    with open(CACHE_PATH(year, day), "r") as f:
        return "".join(f.readlines())


def __fetch_from_server(year: int, day: int):
    session = os.getenv("SESSION")
    if session is None:
        raise os.error("Missing env var SESSION")

    resp = httpx.get(
        INPUT_URL(year, day),
        cookies={"session": session},
        headers={
            "User-Agent": "github.com/t-eckert/aoc by thomas.james.eckert@gmail.com"
        },
    )

    if resp.status_code != 200:
        raise os.error("Could not fetch from server: " + resp.text)

    puzzle_input = resp.text

    with open(CACHE_PATH(year, day), "w") as f:
        f.writelines(puzzle_input)
