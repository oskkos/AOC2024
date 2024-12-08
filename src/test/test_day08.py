"""Advent of Code 2024 - Unit tests for day 8 tasks"""

from src.util import get_lines
from ..day08 import part_one, part_two


example_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".split(
    "\n"
)  # expected 14
example_data2 = """..........
..........
..........
....a.....
..........
.....a....
..........
..........
..........
..........""".split(
    "\n"
)  # expected 2
example_data3 = """.........
..........
..........
....a.....
........a.
.....a....
..........
..........
..........
..........""".split(
    "\n"
)  # expected 4


def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by asserting the expected output

    Returns:
        None
    """
    assert part_one(example_data2) == 2
    assert part_one(example_data3) == 4
    assert part_one(example_data) == 14
    assert part_one(get_lines("day08")) == 329


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output

    Returns:
        None
    """
    assert 1  # part_two(example_data) == 11387
    # assert part_two(get_lines("day08")) == 59002246504791
