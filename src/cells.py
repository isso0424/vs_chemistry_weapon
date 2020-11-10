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
