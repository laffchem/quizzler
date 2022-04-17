from mimetypes import init
from tkinter import *
import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, bg= THEME_COLOR)

        self.canvas = Canvas(width= 300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width= 280,
            text="Some Question Text", 
            font= ("Arial", 20, "italic"), 
            fill=THEME_COLOR
            )
        
        self.canvas.grid(row= 1, column= 0, columnspan= 2, pady= 50)
        
        correct = PhotoImage(file= "images/true.png")
        incorrect = PhotoImage(file= "images/false.png")
        
        self.right = Button(image=correct, highlightthickness=0, command= self.true_press)
        self.right.grid(row= 2, column= 0)

        self.wrong = Button(image=incorrect, highlightthickness=0, command= self.false_press)
        self.wrong.grid(row= 2, column= 1)

        self.score_label = Label(text="Score: 0", font= ("Ubuntu", 12),
        bg= THEME_COLOR, fg="white")
        self.score_label.grid(row= 0, column= 1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():        
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    
    def true_press(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
    