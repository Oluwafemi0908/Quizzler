from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain: QuizBrain):  # This means the quiz datatype must be same as that of Quizbrain class
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.text = self.canvas.create_text(150, 125, width=280, text='Questions here', font=('Arial', 15, 'italic'),
                                            fill=THEME_COLOR, justify='center')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)

        self.scoreboard = Label(text=f"Score : {self.quiz.score}", font=('Arial', 15, 'bold'), bg=THEME_COLOR, fg='white',
                                pady=10)
        self.scoreboard.grid(column=1, row=0)
        self.t_image = PhotoImage(file="images/true.png")
        self.f_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.t_image, command=self.true_click,  borderwidth=0)
        self.false_button = Button(image=self.f_image, command=self.false_click, borderwidth=0)
        self.true_button.grid(column=0, row=2, pady=20, padx=10)
        self.false_button.grid(column=1, row=2, pady=20, padx=10)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if len(self.quiz.question_list) == 0:
            self.canvas.itemconfig(self.text, text=f"Quiz ended\n Score = {self.quiz.score}/{self.quiz.max_score}",
                                   justify='center')
        else:
            self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=f'Q.{self.quiz.max_score} {self.quiz.q_text}')

    def true_click(self):
        self.quiz.answer = 'True'
        self.quiz.calculate_score()
        self.bg_changer()
        self.scoreboard.config(text=f"Score : {self.quiz.score}")
        self.window.after(500, self.get_next_question)

    def false_click(self):
        self.quiz.answer = 'False'
        self.quiz.calculate_score()
        self.bg_changer()
        self.scoreboard.config(text=f"Score : {self.quiz.score}")
        self.window.after(500, self.get_next_question)

    def bg_changer(self):
        if self.quiz.answer == self.quiz.correct_answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
