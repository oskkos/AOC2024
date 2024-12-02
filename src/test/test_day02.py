"""Advent of Code 2024 - Unit tests for day 2 tasks"""
from src.util import get_lines
from ..day02 import part_one, part_two


example_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split("\n")

def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by asserting the expected output

    Returns:
        None
    """
    assert part_one(example_data) == 2
    assert part_one(get_lines("day02")) == 670


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output

    Returns:
        None
    """
    assert part_two(example_data) == 4
    assert part_two(get_lines("day02")) == 700
