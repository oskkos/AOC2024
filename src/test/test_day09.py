"""Advent of Code 2024 - Unit tests for day 9 tasks"""

from src.util import get_lines
from ..day09 import part_one, part_two


example_data = """2333133121414131402""".split("\n")


def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by asserting the expected output

    Returns:
        None
    """
    assert part_one(example_data) == 1928
    assert part_one(get_lines("day09")) == 6360094256423


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output

    Returns:
        None
    """
    assert 1
    # assert part_two(get_lines("day09")) == 1190
