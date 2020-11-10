"""
This file is entry point
"""
from src.load import get_cells


def main(class_name: str) -> None:
    """
    Entry function
    params
    ------
    class_name: str
        Your class name.
        It use for search sheet.
        Ex: "2-2", "2-5"
    """
    cells = get_cells
