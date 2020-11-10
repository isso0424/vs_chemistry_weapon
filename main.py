"""
This file is entry point
"""
from src.load import get_worksheets
from src.questioner import Questioner


def main() -> None:
    """
    Entry function
    params
    ------
    class_name: str
        Your class name.
        It use for search sheet.
        Ex: "2-2", "2-5"
    """
    worksheets = get_worksheets()
    for i in range(0, len(worksheets)):
        interprinter = Questioner(worksheets[i])
        interprinter.start()
    Questioner.finish()

if __name__ == "__main__":
    main()
