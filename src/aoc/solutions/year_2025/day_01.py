# --- Day 1: Secret Entrance ---


MIN = 0
MAX = 99
N_INDICIES = MAX - MIN + 1


def part_1(puzzle: str) -> int:
    count = 0

    cur = 50
    print("Begin: ", cur)
    for instruction in puzzle.splitlines():
        cur += turn(instruction)

        while cur < MIN:
            cur += N_INDICIES

        while cur > MAX:
            cur -= N_INDICIES

        count += int(cur == 0)

    return count


def part_2(puzzle: str) -> int:
    count = 0

    cur = 50
    for instruction in puzzle.splitlines():
        cur += turn(instruction)

        while cur < MIN:
            cur += N_INDICIES
            count += 1

        while cur > MAX:
            cur -= N_INDICIES
            count += 1

    return count


def turn(instruction: str) -> int:
    if instruction[0] == "L":
        return -int(instruction[1:])
    elif instruction[0] == "R":
        return int(instruction[1:])
    else:
        return 0
