# --- Day 1: Sonar Sweep ---
# adventofcode.com/2021/day/1


from itertools import pairwise


def part_1(puzzle: str) -> int:
    # Count the number of times a measurement increases over its predecessor.
    return sum(
        1
        for pair in pairwise(int(measurement) for measurement in puzzle.splitlines())
        if pair[0] < pair[1]
    )


def part_2(puzzle: str) -> int:
    # Count the nubmer of times the sum of measurements in a 3-wide sliding window increases over its predecessor.
    return sum(
        1
        for pair in pairwise(
            sum(x)
            for x in chunk([int(measurement) for measurement in puzzle.splitlines()], 3)
        )
        if pair[0] < pair[1]
    )


def chunk(iter, size: int):
    for i in range(0, len(iter) - size + 1):
        yield iter[i : i + size]
