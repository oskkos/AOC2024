"""Advent of Code 2024 - Day 6 tasks"""

from collections import defaultdict
from copy import deepcopy


if not __package__:
    import util  # type: ignore
else:
    from . import util


next_coord_map = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
next_direction_map = {"up": "right", "right": "down", "down": "left", "left": "up"}

def part_one(lines: list[str]) -> int:
    """
        --- Day 6: Guard Gallivant ---
    The Historians use their fancy device again, this time to whisk you all away to the North Pole
    prototype suit manufacturing lab... in the year 1518! It turns out that having direct access
    to history is very convenient for a group of historians.

    You still have to be careful of time paradoxes, and so it will be important to avoid anyone
    from 1518 while The Historians search for the Chief. Unfortunately, a single guard is
    patrolling this part of the lab.

    Maybe you can work out where the guard will go ahead of time so that The Historians can
    search safely?

    You start by making a map (your puzzle input) of the situation. For example:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    The map shows the current position of the guard with ^ (to indicate the guard is currently
    facing up from the perspective of the map). Any obstructions - crates, desks, alchemical
    reactors, etc. - are shown as #.

    Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following
    these steps:
    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.

    Following the above protocol, the guard moves up several times until she reaches an obstacle
    (in this case, a pile of failed suit prototypes):
    Because there is now an obstacle in front of the guard, she turns right before continuing
    straight in her new facing direction:
    Reaching another obstacle (a spool of several very long polymers), she turns right again and
    continues downward:
    This process continues for a while, but the guard eventually leaves the mapped area (after
    walking past a tank of universal solvent):
    By predicting the guard's route, you can determine which specific positions in the lab will be
    in the patrol path. Including the guard's starting position, the positions visited by the guard
    before leaving the area are marked with an X:

    ....#.....
    ....XXXXX#
    ....X...X.
    ..#.X...X.
    ..XXXXX#X.
    ..X.X.X.X.
    .#XXXXXXX.
    .XXXXXXX#.
    #XXXXXXX..
    ......#X..
    In this example, the guard will visit 41 distinct positions on your map.

    Predict the path of the guard. How many distinct positions will the guard visit before leaving
    the mapped area?
    """
    coords, position = lines_to_coords(lines)
    direction = "up"

    while (0 <= position[0] < len(lines[0])) and (0 <= position[1] < len(lines)):
        coords[position[0]][position[1]] = "X"
        position, direction = get_next_position_and_direction(
            position, direction, coords
        )

    visited_positions = 0
    for row in coords.values():
        for char in row.values():
            if char == "X":
                visited_positions += 1
    return visited_positions


def part_two(lines: list[str]) -> int:
    """
    --- Part Two ---
    While The Historians begin working around the guard's patrol route, you borrow their fancy
    device and step outside the lab. From the safety of a supply closet, you time travel through
    the last few months and record the nightly status of the lab's guard post on the walls of
    the closet.

    Returning after what seems like only a few seconds to The Historians, they explain that the
    guard's patrol area is simply too large for them to safely search the lab without getting
    caught.

    Fortunately, they are pretty sure that adding a single new obstruction won't cause a time
    paradox. They'd like to place the new obstruction in such a way that the guard will get stuck
    in a loop, making the rest of the lab safe to search.

    To have the lowest chance of creating a time paradox, The Historians would like to know all of
    the possible positions for such an obstruction. The new obstruction can't be placed at the
    guard's starting position - the guard is there right now and would notice.

    In the above example, there are only 6 different positions where a new obstruction would cause
    the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new
    obstruction, | to show a position where the guard moves up/down, - to show a position where
    the guard moves left/right, and + to show a position where the guard moves both up/down and
    left/right.

    - Option one, put a printing press next to the guard's starting position:
    - Option two, put a stack of failed suit prototypes in the bottom right quadrant of the area
    - Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in
      the bottom right quadrant:
    - Option four, put an alchemical retroencabulator near the bottom left corner:
    - Option five, put the alchemical retroencabulator a bit to the right instead:
    - Option six, put a tank of sovereign glue right next to the tank of universal solvent:

    It doesn't really matter what you choose to use as an obstacle so long as you and The
    Historians can put it into position without the guard noticing. The important thing is having
    enough options that you can find one that minimizes time paradoxes, and in this example, there
    are 6 different positions you could choose.

    You need to get the guard stuck in a loop by adding a single new obstruction. How many different
    positions could you choose for this obstruction?
    """
    initial_coords, initial_position = lines_to_coords(lines)

    blocked = 0
    for x, col in initial_coords.items():
        for y, char in col.items():
            if char == ".":
                steps = set()
                direction = "up"
                position = initial_position
                coords = deepcopy(initial_coords)
                coords[x][y] = "#"
                while (0 <= position[0] < len(lines[0])) and (
                    0 <= position[1] < len(lines)
                ):
                    if (position, direction) in steps:
                        blocked += 1
                        break
                    steps.add((position, direction))
                    position, direction = get_next_position_and_direction(
                        position, direction, coords
                    )
    return blocked


def lines_to_coords(
    lines: list[str],
) -> tuple[dict[int, dict[int, str]], tuple[int, int]]:
    """
    Converts a list of strings into a dictionary of coordinates and identifies
    the starting position.
    """
    start = (-1, -1)
    coords: dict[int, dict[int, str]] = defaultdict(dict)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coords[x][y] = char
            if char == "^":
                start = (x, y)
    return coords, start


def get_next_position_and_direction(
    position: tuple[int, int], direction: str, coords: dict[int, dict[int, str]]
) -> tuple[tuple[int, int], str]:
    """
    Calculate the next position and direction based on the current position,
    direction, and coordinates.
    """
    next_position = (
        position[0] + next_coord_map[direction][0],
        position[1] + next_coord_map[direction][1],
    )

    if (
        next_position[0] not in coords
        or next_position[1] not in coords[next_position[0]]
    ):
        return next_position, direction

    if coords[next_position[0]][next_position[1]] == "#":
        direction = next_direction_map[direction]
    else:
        position = next_position

    return position, direction


if __name__ == "__main__":
    file_lines = util.get_lines("day02")
    print("Part one: " + str(part_one(file_lines)))
    print("Part two: " + str(part_two(file_lines)))
