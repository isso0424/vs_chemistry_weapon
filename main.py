"""
This file is entry point
"""
from src.load import get_worksheets, get_worksheet
from src.questioner import Questioner
from src.class_choose import choose_class


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
    index = choose_class(worksheets)
    if index == -1:
        for i in range(0, len(worksheets)):
            worksheet = get_worksheet(worksheets, i)
            interprinter = Questioner(worksheet)
            interprinter.start()
    else:
        worksheet = get_worksheet(worksheets, index)
        interprinter = Questioner(worksheet)
        interprinter.start()
    Questioner.finish()

if __name__ == "__main__":
    main()
