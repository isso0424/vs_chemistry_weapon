"""
Question interprinter
"""
from src.load import get_cells
from src.types.question import Question


class Questioner:
    """
    Question proposing interprinter
    """
    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.collect_count = 0
        self.wrong_count = 0

    def load_question(self, index: int) -> Question:
        """
        Create question object from index
        params
        ------
        index: int
            question row number
        """
        question_text = get_cells(self.worksheet, f"I{index}").value
        answer = get_cells(self.worksheet, f"J{index}").value
        wrong_cells = get_cells(self.worksheet, f"K{index}:M{index}")[0]
        wrongs = [wrong_cells[i].value for i in range(3)]
        question = Question(question_text, answer, wrongs)

        return question

    def proposing(self, question: Question):
        """
        Proposing a question
        params
        ------
        question: Question
            question is proposed.
        """
        text = question.create_question()
        print(text)
        answer = int(input(">>>"))
        if question.check_answer(answer):
            self.collect_count += 1
            print("Collect!!!")
            return
        self.wrong_count += 1
        print("Wrong...")
        print(f"answer is {question.answer}")


    def start(self):
        """
        start interprinter
        """
        for index in range(4, 45):
            question = self.load_question(index)
            self.proposing(question)
        print("finish!!!")
        acc = self.collect_count / 41
        print(f"Result\n------\nCollect: {self.collect_count} Wrong: {self.wrong_count} ACC: {acc}")

