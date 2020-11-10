"""
This file is entry point
"""
from src.load import get_worksheet
from src.questioner import Questioner


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
    worksheet = get_worksheet(class_name)
    interprinter = Questioner(worksheet)
    interprinter.start()

if __name__ == "__main__":
    main("2-2")
