"""Advent of Code 2024 - Day 4 tasks"""

if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    --- Day 4: Ceres Search ---
    "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes
    the only button on it. After a brief flash, you recognize the interior of the Ceres
    monitoring station!

    As the search for the Chief continues, a small Elf who lives on the station tugs on your
    shirt; she'd like to know if you could help her with her word search (your puzzle input).
    She only has to find one word: XMAS.

    This word search allows words to be horizontal, vertical, diagonal, written backwards, or
    even overlapping other words. It's a little unusual, though, as you don't merely need to
    find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might
    appear, where irrelevant characters have been replaced with .:


    ..X...
    .SAMX.
    .A..A.
    XMAS.S
    .X....
    The actual word search will be full of letters instead. For example:

    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    In this word search, XMAS occurs a total of 18 times; here's the same word search again,
    but where letters not involved in any XMAS have been replaced with .:

    ....XXMAS.
    .SAMXMS...
    ...S..A...
    ..A.A.MS.X
    XMASAMX.MM
    X.....XA.A
    S.S.S.S.SS
    .A.A.A.A.A
    ..M.M.M.MM
    .X.X.XMASX
    Take a look at the little Elf's word search. How many times does XMAS appear?

    """

    x = len(lines[0])
    y = len(lines)
    count = 0

    # horizontal check
    for i in range(y):
        count += lines[i].count("XMAS")
        count += lines[i].count("SAMX")

    # vertical check
    for i in range(x):
        row = "".join([line[i] for line in lines])
        count += row.count("XMAS")
        count += row.count("SAMX")

    # diagonal check (top left to bottom right)
    for yy in range(y - 3):
        for xx in range(x - 3):
            count += "".join([lines[yy + j][xx + j] for j in range(4)]).count("XMAS")
            count += "".join([lines[yy + j][xx + j] for j in range(4)]).count("SAMX")

    # diagonal check (top right to bottom left)
    for yy in range(3, y):
        for xx in range(x - 3):
            count += "".join([lines[yy - j][xx + j] for j in range(4)]).count("XMAS")
            count += "".join([lines[yy - j][xx + j] for j in range(4)]).count("SAMX")

    return count


def part_two(lines: list[str]) -> int:
    """
    --- Part Two ---
    The Elf looks quizzically at you. Did you misunderstand the assignment?

    Looking for the instructions, you flip over the word search to find that this isn't actually an
    XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.
    One way to achieve that is like this:
      M.S
      .A.
      M.S
    Irrelevant characters have again been replaced with . in the above diagram. Within the X, each
    MAS can be written forwards or backwards.

    Here's the same example from before, but this time all of the X-MASes have been kept instead:

    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........
    In this example, an X-MAS appears 9 times.

    Flip the word search from the instructions back over to the word search side and try again.
    How many times does an X-MAS appear?
    """
    count = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            x_mas_pattern_found = 0
            if lines[i][j] != "A":
                continue
            if lines[i - 1][j - 1] == "M" and lines[i + 1][j + 1] == "S":
                x_mas_pattern_found += 1
            if lines[i - 1][j + 1] == "M" and lines[i + 1][j - 1] == "S":
                x_mas_pattern_found += 1
            if lines[i - 1][j - 1] == "S" and lines[i + 1][j + 1] == "M":
                x_mas_pattern_found += 1
            if lines[i - 1][j + 1] == "S" and lines[i + 1][j - 1] == "M":
                x_mas_pattern_found += 1

            if x_mas_pattern_found == 2:
                count += 1
    return count


if __name__ == "__main__":
    file_lines = util.get_lines("day04")
    print("Part one: " + str(part_one(file_lines)))
    print("Part two: " + str(part_two(file_lines)))
