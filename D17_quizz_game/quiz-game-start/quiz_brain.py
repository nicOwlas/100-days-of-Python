class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        question = self.question_bank[self.question_number]
        user_answer = input(
            f"Q.{self.question_number+1} {question.text} (True/False)?: "
        )
        self.check_answer(user_answer, question.answer)
        self.question_number += 1
        return user_answer

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("This is correct!")
            self.score += 1
        else:
            print("This is wrong")
        print(f"The correst answer was: {question_answer}")
        print(f"Score: {self.score}/{self.question_number+1}")
        print("\n")
