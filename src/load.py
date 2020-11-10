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
    print(len(worksheets))
    judge_value = get_cells(worksheets[0], "F3").value
    if judge_value == "問題（日本語）":
        Question.all_classes = True

    return worksheets
