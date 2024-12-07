"""Advent of Code 2024 - Unit tests for day 7 tasks"""

from src.util import get_lines
from ..day07 import part_one, part_two


example_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
    "\n"
)


def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by asserting the expected output

    Returns:
        None
    """
    assert part_one(example_data) == 3749
    assert part_one(get_lines("day07")) == 6083020304036


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output

    Returns:
        None
    """
    assert part_two(example_data) == 11387
    # this is a bit slow with actual input
    # assert part_two(get_lines("day07")) == 59002246504791
