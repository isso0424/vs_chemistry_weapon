"""
Load data from worksheet
"""
import openpyxl


def get_worksheet():
    """
    Get worksheet
    return
    ------
    workbook: openpyxl.WorkSheet
        Got workbook
    """
    workbook = openpyxl.load_workbook("questions.xlsx");
    worksheet = workbook.worksheets[0]

    return worksheet


def get_cells(worksheet, get_range: str):
    """
    Get cells from sheet
    params
    ------
    workbook: openpyxl.WorkSheet
        loaded worksheet.
    get_range: str
        Get cells range.
        Ex: "A1:B3"

    return
    ------
    cells: Tuple[Cell]
        Got cells tuple
    """
    cells = worksheet[get_range]

    return cells
