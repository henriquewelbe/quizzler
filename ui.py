from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # WINDOW
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # SCORE
        self.score_label = Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # WHITE CANVAS WITH A QUESTION FROM THE API
        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 125,
                                            text='Amazon acquired Twitch in August 2014 for $70 million dollars.',
                                            font=('Arial', 20, 'italic'),
                                            fill="black",
                                            width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # CORRECT BUTTON
        self.true_img = PhotoImage(file='images/true.png')
        self.correct_button = Button(image=self.true_img, command=self.button_right)
        self.correct_button.grid(column=0, row=2)

        # FALSE BUTTON
        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, command=self.button_wrong)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text='You reached the end of the quiz')
            self.correct_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def button_right(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def button_wrong(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, self.get_next_question)
