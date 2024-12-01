"""Advent of Code 2024 - Unit tests for day 1 tasks"""
from .. import util
from ..day01 import part_one, part_two


example_data = """3   4
4   3
2   5
1   3
3   9
3   3""".split("\n")

def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by asserting the expected output

    Returns:
        None
    """
    assert part_one(example_data) == 11


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output

    Returns:
        None
    """
    assert part_two(example_data) == 31
