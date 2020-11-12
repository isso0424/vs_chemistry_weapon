"""
Question interprinter
"""
from src.types.question import Question


class Questioner:
    """
    Question proposing interprinter
    """
    collect_count = 0
    wrong_count = 0
    start_index = 4

    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.collect_count = 0
        self.wrong_count = 0

    @staticmethod
    def set_start_row(row: int):
        Questioner.start_index = row

    def reset(self):
        Question.answer_column = ""
        Question.question_column = ""
        Question.wrong_start = ""
        Question.wrong_end = ""

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
        answer = input(">>>")
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
        index = Questioner.start_index
        fuck = 0
        while True:
            question = Question.create_from_cell(index, self.worksheet)
            if question.answer is None:
                fuck += 1
                index += 1
                if fuck >= 5:
                    break
                continue
            else:
                fuck = 0
            self.proposing(question)
            index += 1
        Questioner.collect_count += self.collect_count
        Questioner.wrong_count += self.wrong_count
        self.reset()

    @staticmethod
    def finish():
        print("finish!!!")
        acc = Questioner.collect_count / (Questioner.collect_count + Questioner.wrong_count)
        print(f"Result\n------\nCollect: {Questioner.collect_count} Wrong: {Questioner.wrong_count} ACC: {acc}")
