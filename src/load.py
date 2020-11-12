"""
Load data from worksheet
"""
import openpyxl
from src.types.question import Question
from src.cells import get_cells

def get_worksheets():
    """
    Get worksheet
    return
    ------
    workbook: openpyxl.WorkSheet
        Got workbook
    """
    workbook = openpyxl.load_workbook("questions.xlsx");
    worksheets = workbook.worksheets

    return worksheets

def get_worksheet(worksheets, index):
    worksheet = worksheets[index]
    for row in range(1, 6):
        char_code = ord("A")
        for _ in range(0, 15):
            judge_value = get_cells(worksheet, f"{chr(char_code)}{row}").value
            if "問題" in str(judge_value):
                Question.set_column(char_code)
                break
            char_code += 1
        if Question.question_column != "":
            break
    if Question.question_column == "":
        raise NameError("Question Column not found")
    return worksheet
