import argparse
import os

from aoc import puzzle, solutions

parser = argparse.ArgumentParser(
    description="CLI for running Advent of Code solutions."
)
parser.add_argument(
    "year", metavar="int", type=int, help="The year of the puzzle (e.g. 2026)"
)
parser.add_argument(
    "day", metavar="int", type=int, help="The day of the puzzle (e.g. 12)"
)
parser.add_argument("--part", metavar="int", type=int, help="Part 1 or 2 of the puzzle")


def main():
    args = parser.parse_args()

    create_blank_soln_if_none_exists(args.year, args.day)
    solution = solutions.get(args.year, args.day)

    puzzle_input = puzzle.input(args.year, args.day)

    if args.part is None:
        print(solution.part_1(puzzle_input))
        print(solution.part_2(puzzle_input))
    elif args.part == 1:
        print(solution.part_1(puzzle_input))
    elif args.part == 2:
        print(solution.part_2(puzzle_input))


def create_blank_soln_if_none_exists(year: int, day: int):
    try:
        with open(f"./src/aoc/solutions/year_{year}/day_{day:02d}.py", "x") as f:
            f.write("""def part_1(puzzle: str) -> int:
    return 1


def part_2(puzzle: str) -> int:
    return 2
""")
    except FileExistsError:
        return
