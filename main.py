from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizzInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

"""from tkinter import *
from question_model import Question


# REQUEST FROM THE API
def generate_question():
    new_question = Question()
    question = new_question.new_question()
    answer = new_question.question_answer()
    canvas.itemconfig(text, text=question)


# WHITE CANVAS WITH A QUESTION FROM THE API
window = Tk()
window.title('Quizzer')
window.config(padx=100, pady=100, bg='#2D414A')
canvas = Canvas(width=300, height=300)
text = canvas.create_text(150, 150, text='Welcome to Quizzer!', font=('Arial', 32), width=280)
canvas.pack()


# CORRECT BUTTON
true_img = PhotoImage(file='images/true.png')
correct_button = Button(image=true_img, command=generate_question)
correct_button.pack()


# FALSE BUTTON
false_img = PhotoImage(file='images/false.png')
false_button = Button(image=false_img, command=generate_question)
false_button.pack()


# create a json file formatted equal to the one from the api that contains all the questions asked
# if no questions are left, print "quizz ended"

mainloop()
"""