"""Advent of Code 2024 - Day 1 tasks"""

if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    --- Day 2: Red-Nosed Reports ---
    Fortunately, the first location The Historians want to search isn't a long walk from the 
    Chief Historian's office.

    While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the 
    Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they 
    still talk about the time Rudolph was saved through molecular synthesis from a single electron.

    They're quick to add that - since you're already here - they'd really appreciate your help 
    analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are 
    waiting for you, but they seem to have already divided into groups that are currently searching 
    every corner of the facility. You offer to help with the unusual data.

    The unusual data (your puzzle input) consists of many reports, one report per line. Each report 
    is a list of numbers called levels that are separated by spaces. For example:

    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    This example data contains six reports each containing five levels.

    The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety 
    systems can only tolerate levels that are either gradually increasing or gradually decreasing. 
    So, a report only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    
    In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
    So, in this example, 2 reports are safe.

    Analyze the unusual data from the engineers. How many reports are safe?
    """
    safe = 0
    for line in lines:
        levels = list(map(int, line.split(" ")))

        if check_is_safe(levels):
            safe += 1

    return safe

def part_two(lines: list[str]) -> int:
    """
    --- Part Two ---
    The engineers are surprised by the low number of safe reports until they realize they forgot 
    to tell you about the Problem Dampener.

    The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate 
    a single bad level in what would otherwise be a safe report. It's like the bad level never 
    happened!

    Now, the same rules apply as before, except if removing a single level from an unsafe report 
    would make it safe, the report instead counts as safe.

    More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.
    Thanks to the Problem Dampener, 4 reports are actually safe!

    Update your analysis by handling situations where the Problem Dampener can remove a single 
    level from unsafe reports. How many reports are now safe?

    """
    safe = 0
    for line in lines:
        levels = list(map(int, line.split(" ")))

        if check_is_safe(levels):
            safe += 1
        else:
            # Sloppy implementation, one could optimize this a lot
            for i, _ in enumerate(levels):
                new_levels = levels.copy()
                new_levels.pop(i)
                if check_is_safe(new_levels):
                    safe += 1
                    break

    return safe

def check_is_safe(levels: list[int]) -> bool:
    """
    Check if the levels are safe.

    Args:
        levels (list[int]): The levels to check.

    Returns:
        bool: True if the levels are safe, False otherwise.
    """
    ok_transitions = 0
    increasing = None
    for i, level in enumerate(levels):
        if i == len(levels) - 1:
            break

        next_level = levels[i+1]
        diff = int(next_level) - int(level)

        if abs(diff) > 3 or not diff:
            break
        if (diff and increasing is None):
            increasing = diff > 0

        if (increasing is True and diff < 0):
            break
        if (increasing is False and diff > 0):
            break

        ok_transitions += 1

    return ok_transitions == len(levels) - 1

if __name__ == "__main__":
    file_lines = util.get_lines("day02")
    print("Part one: " + str(part_one(file_lines)))
    # print("Part two: " + str(part_two(file_lines)))
