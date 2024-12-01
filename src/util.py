""" Utility functions for the project """

import os


def get_lines(file_name: str) -> list[str]:
    """
    Read the lines from the input file and return them as a list.

    Returns:
        list: A list of strings representing the lines from the input file.
    """
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/inputs/" + file_name + ".txt"
    with open(file_path, "r", encoding="utf-8") as file:
        return list(map(str.strip, file.readlines()))
