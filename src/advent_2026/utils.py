def read_input(day: int) -> str:
    with open(f"./inputs/{day:02}", "r") as f:
        return "".join(f.readlines())
