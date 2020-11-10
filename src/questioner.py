"""
Question interprinter
"""
from src.types.question import Question


class Questioner:
    """
    Question proposing interprinter
    """
    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.collect_count = 0
        self.wrong_count = 0

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
        index = 4
        fuck = 0
        while True:
            question = Question.create_from_cell(index, self.worksheet)
            if question.answer is None:
                fuck += 1
                index += 1
                if fuck >= 3:
                    break
                continue
            else:
                fuck = 0
            self.proposing(question)
            index += 1
        print("finish!!!")
        acc = self.collect_count / 41
        print(f"Result\n------\nCollect: {self.collect_count} Wrong: {self.wrong_count} ACC: {acc}")
