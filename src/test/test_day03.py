"""Advent of Code 2024 - Unit tests for day 3 tasks"""

from src.util import get_lines
from ..day03 import part_one, part_two


def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by asserting the expected output

    Returns:
        None
    """
    example_data = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ]
    assert part_one(example_data) == 161
    assert part_one(get_lines("day03")) == 161289189


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output

    Returns:
        None
    """
    example_data = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]
    assert part_two(example_data) == 48
    assert part_two(get_lines("day03")) == 83595109
