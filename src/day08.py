"""Advent of Code 2024 - Day 8 tasks"""

if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    --- Day 8: Resonant Collinearity ---
    You find yourselves on the roof of a top-secret Easter Bunny installation.

    While The Historians do their thing, you take a look at the familiar huge antenna. Much to
    your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1%
    more likely to buy Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift!
    Unthinkable!

    Scanning across the city, you find that there are actually many such antennas. Each antenna
    is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter,
    or digit. You create a map (your puzzle input) of these antennas. For example:

    ............
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
    ............
    The signal only applies its nefarious effect at specific antinodes based on the resonant
    frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly
    in line with two antennas of the same frequency - but only when one of the antennas is twice
    as far away as the other. This means that for any pair of antennas with the same frequency,
    there are two antinodes, one on either side of them.

    So, for these two antennas with frequency a, they create the two antinodes marked with #:

    ..........
    ...#......
    ..........
    ....a.....
    ..........
    .....a....
    ..........
    ......#...
    ..........
    ..........
    Adding a third antenna with the same frequency creates several more antinodes. It would ideally
    add four antinodes, but two are off the right side of the map, so instead it adds only two:

    ..........
    ...#......
    #.........
    ....a.....
    ........a.
    .....a....
    ..#.......
    ......#...
    ..........
    ..........
    Antennas with different frequencies don't create antinodes; A and a count as different
    frequencies. However, antinodes can occur at locations that contain antennas. In this diagram,
    the lone antenna with frequency capital A creates no antinodes but has a lowercase-a-frequency
    antinode at its location:

    ..........
    ...#......
    #.........
    ....a.....
    ........a.
    .....a....
    ..#.......
    ......A...
    ..........
    ..........
    The first example has antennas with two different frequencies, so the antinodes they create
    look like this, plus an antinode overlapping the topmost A-frequency antenna:

    ......#....#
    ...#....0...
    ....#0....#.
    ..#....0....
    ....0....#..
    .#....A.....
    ...#........
    #......#....
    ........A...
    .........A..
    ..........#.
    ..........#.
    Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14
    total unique locations that contain an antinode within the bounds of the map.

    Calculate the impact of the signal. How many unique locations within the bounds of the map
    contain an antinode?
    """
    antinodes = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == ".":
                continue
            antinodes.update(check_possibilities(lines, row, col, char))
    return len(antinodes)


def part_two(lines: list[str]) -> int:
    """
    --- Part Two ---
    Watching over your shoulder as you work, one of The Historians asks if you took the effects
    of resonant harmonics into your calculations.

    Whoops!

    After updating your model, it turns out that an antinode occurs at any grid position exactly in
    line with at least two antennas of the same frequency, regardless of distance. This means
    that some of the new antinodes will occur at the position of each antenna (unless that antenna
    is the only one of its frequency).

    So, these three T-frequency antennas now create many antinodes:

    T....#....
    ...T......
    .T....#...
    .........#
    ..#.......
    ..........
    ...#......
    ..........
    ....#.....
    ..........
    In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are
    all also antinodes! This brings the total number of antinodes in the above example to 9.

    The original example now has 34 antinodes, including the antinodes that appear on every antenna:

    ##....#....#
    .#.#....0...
    ..#.#0....#.
    ..##...0....
    ....0....#..
    .#...#A....#
    ...#..#.....
    #....#.#....
    ..#.....A...
    ....#....A..
    .#........#.
    ...#......##
    Calculate the impact of the signal using this updated model. How many unique locations within
    the bounds of the map contain an antinode?
    """
    antinodes = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == ".":
                continue
            antinodes.update(check_possibilities(lines, row, col, char, True))
    return len(antinodes)


def check_possibilities(
    lines: list[str], row: int, col: int, char: str, part2: bool = False
) -> set[tuple[int, int]]:
    """
    Check possible positions in a grid based on a given character.

    This function iterates through a list of strings (representing lines in a grid)
    and checks for possible positions (antinodes) relative to a specified row and column
    where the given character appears. It uses the differences in row and column indices
    to determine potential positions and validates them based on certain conditions.
    """
    antinodes = set()
    for row2, line2 in enumerate(lines):
        for col2, char2 in enumerate(line2):
            if char != char2:
                continue
            row_diff = row2 - row
            col_diff = col2 - col
            if not row_diff and not col_diff:
                continue

            if part2:
                options = get_options2(
                    row_diff, col_diff, row, col, (len(lines), len(lines[0]))
                )
                for option in options:
                    if option[0] < 0 or option[1] < 0:
                        pass  # continue
                    if in_range(lines, option[0], option[1]):
                        antinodes.add((option[0], option[1]))
            else:
                options = get_options(row_diff, col_diff)
                for option in options:
                    if in_range(lines, row + option[0], col + option[1]):
                        antinodes.add((row + option[0], col + option[1]))
    return antinodes


def in_range(lines: list[str], row: int, col: int) -> bool:
    """
    Check if the given row and column indices are within the bounds
    of the 2D grid represented by lines.
    """
    return 0 <= row < len(lines) and 0 <= col < len(lines[0])


def get_options(row_diff: int, col_diff: int) -> list[tuple[int, int]]:
    """
    Generate a list of option tuples based on the differences in row and column values.

    This function takes two integer inputs, `row_diff` and `col_diff`, and returns a list of tuples.
    Each tuple contains two integers that represent possible options derived from the input
    differences. The options are calculated based on specific conditions related to the signs
    of `row_diff` and `col_diff`.
    """
    options: list[tuple[int, int]] = []

    if not row_diff and not col_diff:
        return options

    if (row_diff >= 0 and col_diff >= 0) or (row_diff <= 0 and col_diff <= 0):
        options = [
            (row_diff * -1, col_diff * -1),
            (row_diff * 2, col_diff * 2),
        ]
    else:
        options = [
            (row_diff * -1, col_diff * -1),
            (row_diff * 2, col_diff * 2),
        ]
    return options


def get_options2(
    row_diff: int, col_diff: int, row: int, col: int, dimensions: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Generate a list of option tuples based on the differences in row and column values.

    This function takes two integer inputs, `row_diff` and `col_diff`, and returns a list of tuples.
    Each tuple contains two integers that represent possible options derived from the input
    differences. The options are calculated based on specific conditions related to the signs
    of `row_diff` and `col_diff`.
    """

    options: list[tuple[int, int]] = []
    options.append((row, col))

    if not row_diff and not col_diff:
        return options
    descending_row = row
    descending_col = col
    while 0 <= descending_row <= dimensions[0] and 0 <= descending_col <= dimensions[1]:
        descending_row = descending_row - row_diff
        descending_col = descending_col - col_diff
        options.append((descending_row, descending_col))

    ascending_row = row
    ascending_col = col
    while 0 <= ascending_row <= dimensions[0] and 0 <= ascending_col <= dimensions[1]:
        ascending_row = ascending_row + row_diff
        ascending_col = ascending_col + col_diff
        options.append((ascending_row, ascending_col))

    return options


if __name__ == "__main__":
    file_lines = util.get_lines("day08")
    print("Part one: " + str(part_one(file_lines)))
    print("Part two: " + str(part_two(file_lines)))
