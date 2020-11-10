"""
Load data from worksheet
"""
import openpyxl


def get_worksheet(class_name: str):
    """
    Get worksheet
    params
    ------
    class_name: str
        Your class name.
        It use for search sheet.
        Ex: "2-2", "2-5"
    return
    ------
    workbook: openpyxl.WorkSheet
        Got workbook
    """
    workbook = openpyxl.load_workbook("questions.xlsx");
    worksheet = workbook[class_name]

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
