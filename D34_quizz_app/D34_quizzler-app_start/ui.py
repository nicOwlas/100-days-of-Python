from tkinter import Tk, Canvas, Label, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    """Interface to answer open trivia yes/no questions"""

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=10)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Test", font=FONT, fill=THEME_COLOR
        )

        # Score
        self.score_label = Label(text="Score: 0", padx=-10, bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=10)

        # Buttons
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.is_true)
        self.true_button.grid(row=2, column=1, pady=10)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, command=self.is_false)
        self.false_button.grid(row=2, column=0, pady=10)
        self.get_next_question()

        self.window.mainloop()

    def is_true(self):
        self.quiz.check_answer("True")

    def is_false(self):
        self.quiz.check_answer("False")

    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question)


if __name__ == "__main__":
    ui = QuizInterface()
