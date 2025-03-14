from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizler")

        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text= "Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.quote_text =  self.canvas.create_text(150, 125, text="Question here", width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quote_text, text= q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text= "You've reached to the end of the quiz.s")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_ques)