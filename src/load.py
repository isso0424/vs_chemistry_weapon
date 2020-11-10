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
    workbook = openpyxl.Workbook("questions.xlsx");
    worksheet = workbook[class_name]


    if workbook is None:
        raise NameError(f"work sheet {class_name} is not found")

    return workbook


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
