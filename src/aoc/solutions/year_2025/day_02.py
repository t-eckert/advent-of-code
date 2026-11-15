# --- Day 2: Gift Shop ---
# adventofcode.com/2025/day/2


from itertools import batched


def part_1(puzzle: str) -> int:
    total = 0

    ranges = [r.split("-") for r in puzzle.split(",")]

    for r in ranges:
        for x in range(int(r[0]), int(r[1]) + 1):
            n = str(x)
            midpt = len(n) // 2
            if n[:midpt] == n[midpt:]:
                total += x

    return total


def part_2(puzzle: str) -> int:
    total = 0

    ranges = [r.split("-") for r in puzzle.split(",")]

    for r in ranges:
        for x in range(int(r[0]), int(r[1]) + 1):
            if sequence_repeats(str(x)):
                total += x

    return total


def sequence_repeats(n: str) -> bool:
    if len(n) == 1:
        return False

    if len({c for c in n}) == 1:
        return True

    for step in range(2, len(n) // 2 + 1):
        if len(n) % step == 0:
            if len({b for b in batched(n, n=step)}) == 1:
                return True

    return False
