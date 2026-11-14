import importlib
from types import ModuleType


def get(year: int, day: int) -> ModuleType:
    """Return the solution module for the given year and day.

    Solutions live at aoc/solutions/year_<YYYY>/day_<DD>.py and must define
    part_1(puzzle: str) and part_2(puzzle: str).
    """
    name = f"{__name__}.year_{year}.day_{day:02}"
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError as e:
        if e.name is not None and name.startswith(e.name):
            raise LookupError(f"No solution for {year} day {day} (expected module {name})") from e
        raise
