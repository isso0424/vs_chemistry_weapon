"""
This file is entry point
"""
import openpyxl

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
    workbook = openpyxl.Workbook("questions.xlsx");
