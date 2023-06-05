import tkinter as tk
from tkinter import messagebox
import random

class MathDrillApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Math Drill App")

        self.score = 0
        self.question_number = 0

        self.num_problems = 10
        self.max_add_sub = 50
        self.max_mul = 12

        self.create_widgets()
        self.generate_problem()

    def create_widgets(self):
        # Frame to hold all the widgets
        self.frame = tk.Frame(self.root, padx=50, pady=20, bd=10, bg="khaki1", relief="groove")
        self.frame.pack()

        # Problem label
        self.label_problem = tk.Label(self.frame, text="Problem", fg="black", font=("Arial", 30, "bold"))
        self.label_problem.pack(pady=10)

        # Answer entry
        self.entry_answer = tk.Entry(self.frame, font=("Arial", 24), justify="right")
        self.entry_answer.pack(pady=5)

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.frame)
        self.buttons_frame.pack(pady=5)

        # Number buttons
        number_buttons = [
            ("7", "darkgray"), ("8", "darkgray"), ("9", "darkgray"),
            ("4", "darkgray"), ("5", "darkgray"), ("6", "darkgray"),
            ("1", "darkgray"), ("2", "darkgray"), ("3", "darkgray"),
            ("0", "darkgray"), (".", "darkgray"), ("C", "darkgray")
        ]
        row = 0
        col = 0
        for number, color in number_buttons:
            button = tk.Button(self.buttons_frame, text=number, font=("Arial", 18), width=5, height=2, bg=color, command=lambda num=number: self.append_to_answer(num))
            button.grid(row=row, column=col, padx=3, pady=3)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Submit button
        self.button_submit = tk.Button(self.frame, text="Submit", command=self.check_answer, bg="green", fg="white", font=("Arial", 18, "bold"), width=16, height=1)
        self.button_submit.pack(pady=2)

        # Restart button
        self.button_restart = tk.Button(self.frame, text="Restart", command=self.restart_drill, bg="orange", fg="white", font=("Arial", 18, "bold"), width=16, height=1)
        self.button_restart.pack(pady=2)

        # Exit button
        self.button_exit = tk.Button(self.frame, text="Exit", command=self.root.quit, bg="red", fg="white", font=("Arial", 18, "bold"), width=16, height=1)
        self.button_exit.pack(pady=2)

        # Score label
        self.label_score = tk.Label(self.frame, text="Score: 0/10", bg="black", fg="white", font=("Arial", 18, "bold"))
        self.label_score.pack(pady=1)

    def generate_problem(self):
        """
        Generates a random math problem with an operator and operands.
        Updates the problem label and stores the correct answer.
        """
        operators = ['+', '-', '×', '÷']
        operator = random.choice(operators)

        if operator == '+':
            operand1 = random.randint(0, 49)
            operand2 = random.randint(0, 49)
            answer = operand1 + operand2
        elif operator == '-':
            operand1 = random.randint(0, 49)
            operand2 = random.randint(0, 49)
            if operand2 > operand1:
                operand1, operand2 = operand2, operand1
            answer = operand1 - operand2
        elif operator == '×':
            operand1 = random.randint(1, 12)
            operand2 = random.randint(1, 12)
            answer = operand1 * operand2
        else:  # operator == '÷'
            operand1 = random.randint(1, 12)
            operand2 = random.randint(1, 12)
            answer = round((operand1 / operand2), 2)

        self.current_problem = f"{operand1} {operator} {operand2} ="
        self.correct_answer = answer

        self.label_problem.config(text=self.current_problem)

    def append_to_answer(self, value):
        """
        Appends the selected number or action to the answer entry.
        If 'C' is pressed, clears the answer entry.
        """
        current_answer = self.entry_answer.get()
        if value == "C":
            self.entry_answer.delete(0, tk.END)
        else:
            self.entry_answer.insert(tk.END, value)

    def check_answer(self):
        """
        Checks the user's answer against the correct answer.
        Updates the score, displays a message box indicating correctness, and generates the next problem.
        """
        user_answer = self.entry_answer.get()
        self.entry_answer.delete(0, tk.END)

        if user_answer == str(self.correct_answer):
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Wrong answer! The correct answer is {self.correct_answer}")

        self.question_number += 1
        self.label_score.config(text=f"Score: {self.score}/{self.question_number}")

        if self.question_number < self.num_problems:
            self.generate_problem()
        else:
            self.end_drill()

    def end_drill(self):
        """
        Displays a message box indicating the end of the drill and the final score.
        Disables the submit button and answer entry.
        """
        messagebox.showinfo("Drill Complete", f"Your drill is complete. Your score is {self.score}/{self.num_problems}")
        self.button_submit.config(state=tk.DISABLED)
        self.entry_answer.config(state=tk.DISABLED)

    def restart_drill(self):
        """
        Restarts the drill by resetting the score and question number.
        Enables the submit button and answer entry.
        Generates a new problem.
        """
        self.score = 0
        self.question_number = 0
        self.label_score.config(text=f"Score: {self.score}/{self.question_number}")
        self.button_submit.config(state=tk.NORMAL)
        self.entry_answer.config(state=tk.NORMAL)
        self.generate_problem()

# Create an instance of the MathDrillApp class
app = MathDrillApp()

# Start the main event loop
app.root.mainloop()
