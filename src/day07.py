"""Advent of Code 2024 - Day 7 tasks"""

from itertools import product
import re

if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    --- Day 7: Bridge Repair ---
    The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The
    Chief isn't on this side of the bridge, though; maybe he's on the other side?

    When you go to cross the bridge, you notice a group of engineers trying to repair it.
    (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

    You ask how long it'll take; the engineers tell you that it only needs final calibrations, but
    some young elephants were playing nearby and stole all the operators from their calibration
    equations! They could finish the calibrations if only someone could determine which test values
    could possibly be produced by placing any combination of operators into their calibration
    equations (your puzzle input).

    For example:

    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
    Each line represents a single equation. The test value appears before the colon on each line;
    it is your job to determine whether the remaining numbers can be combined with operators to
    produce the test value.

    Operators are always evaluated left-to-right, not according to precedence rules. Furthermore,
    numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants
    holding two different types of operators: add (+) and multiply (*).

    Only three of the above equations can be made true by inserting operators:

    - 190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would
      give 29, but choosing * would give the test value (10 * 19 = 190).
    - 3267: 81 40 27 has two positions for operators. Of the four possible configurations of the
      operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27
      both equal 3267 (when evaluated left-to-right)!
    - 292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.

    The engineers just need the total calibration result, which is the sum of the test values from
    just the equations that could possibly be true. In the above example, the sum of the test values
    for the three equations listed above is 3749.

    Determine which equations could possibly be true. What is their total calibration result?


    """
    operators = ["+", "*"]
    total = 0
    for line in lines:
        row_value = int(line.split(":")[0])
        numbers = re.findall(r"\d+", line.split(":")[1])
        expressions = form_expressions(numbers, operators)
        if has_valid_expression(expressions, row_value):
            total += int(row_value)

    return total


def part_two(lines: list[str]) -> int:
    """
    --- Part Two ---
    The engineers seem concerned; the total calibration result you gave them is nowhere close to
    being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants
    are holding a third type of operator.

    The concatenation operator (||) combines the digits from its left and right inputs into a
    single number. For example, 12 || 345 would become 12345. All operators are still evaluated
    left-to-right.

    Now, apart from the three equations that could be made true using only addition and
    multiplication, the above example has three more equations that can be made true by
    inserting operators:
    - 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
    - 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
    - 192: 17 8 14 can be made true using 17 || 8 + 14.
    Adding up all six test values (the three that could be made before using only + and * plus the
    new three that can now be made by also using ||) produces the new total calibration
    result of 11387.

    Using your new knowledge of elephant hiding spots, determine which equations could possibly
    be true. What is their total calibration result?
    """
    operators = ["+", "*"]
    operators2 = ["+", "*", "||"]
    total = 0
    for line in lines:
        row_value = int(line.split(":")[0])
        numbers = re.findall(r"\d+", line.split(":")[1])
        expressions = form_expressions(numbers, operators)
        if has_valid_expression(expressions, row_value):
            total += int(row_value)
        else:
            expressions = form_expressions(numbers, operators2)
            if has_valid_expression(expressions, row_value):
                total += int(row_value)

    return total


def form_expressions(numbers: list[int], operators: list[str]) -> list[str]:
    """
    Forms all possible expressions from the given numbers and operators.
    """
    expressions = []
    for ops in product(operators, repeat=len(numbers) - 1):
        expression = "".join(f"{n}{o}" for n, o in zip(numbers, ops + ("",)))
        expressions.append(expression)
    return expressions


def has_valid_expression(expressions: list[str], target: int) -> bool:
    """
    Checks if any of the given expressions evaluate to the target value.
    """
    for expression in expressions:
        evaluated_value = evaluate_expression(expression)
        if evaluated_value == target:
            return True
    return False


def evaluate_expression(expression: str) -> int:
    """
    Evaluates a mathematical expression containing integers and the operators
    '+' and '*' (and '||'). The expression is evaluated from left to right without
    considering operator precedence.
    """
    tokens = re.findall(r"\d+|[+*]|\|\|", expression)
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_number = int(tokens[i + 1])
        if operator == "+":
            result += next_number
        elif operator == "*":
            result *= next_number
        elif operator == "||":
            result = int(f"{result}{next_number}")
        i += 2

    return result


if __name__ == "__main__":
    file_lines = util.get_lines("day07")
    print("Part one: " + str(part_one(file_lines)))
    print("Part two: " + str(part_two(file_lines)))
