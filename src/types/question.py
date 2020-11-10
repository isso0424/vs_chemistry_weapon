"""
Type for a question.
"""
from typing import List
from random import sample

from src.load import get_cells


class Question:
    """
    Type for a question
    """
    def __init__(self, question: str, answer: str, wrongs: List[str]):
        self.question = question
        self.answer = answer
        self.wrongs = wrongs
        self.answer_list = sample([self.answer, self.wrongs[0], self.wrongs[1], self.wrongs[2]], 4)

    @staticmethod
    def create_from_cell(index: int, worksheet):
        """
        Create question from cell
        params
        ------
        index: int
            row of question
        worksheet: openpyxl.WorkSheet
            worksheet containing questions
        return
        ------
        Question
            created question
        """
        question_text = get_cells(worksheet, f"I{index}").value
        answer = get_cells(worksheet, f"J{index}").value
        wrong_cells = get_cells(worksheet, f"K{index}:M{index}")[0]
        wrongs = [wrong_cells[i].value for i in range(3)]

        return Question(question_text, answer, wrongs)

    def create_question(self) -> str:
        """
        Create question
        returns
        -------
        text: str
            question text
        """
        text = f"{self.question}\n"\
            f"1: {self.answer_list[0]} "\
            f"2: {self.answer_list[1]} "\
            f"3: {self.answer_list[2]} "\
            f"4: {self.answer_list[3]}"

        return text

    def check_answer(self, response: int) -> bool:
        """
        Check answer in question
        params
        ------
        response: str
            user answer.
        return
        ------
        question result
        """
        return self.answer_list[response - 1] == self.answer
