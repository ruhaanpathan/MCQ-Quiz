import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fun Quiz App for Kids")
        self.master.geometry("800x600")
        self.master.config(bg="#FFDD57")

        self.questions = [
            {
                "question": "What does the Preamble of India declare as its primary objective? _____",
                "options": ["To establish a monarchy", "To promote socialism", "To secure justice, liberty, equality, and fraternity", "To enhance military power"],
                "answer": "To secure justice, liberty, equality, and fraternity"
            },
            {
                "question": "The Preamble emphasizes the dignity of the individual. What is this dignity linked to? _____",
                "options": ["Economic status", "Political power", "Social status", "Liberty and equality"],
                "answer": "Liberty and equality"
            },
            {
                "question": "Which term is NOT mentioned in the Preamble of the Constitution of India? _____",
                "options": ["Sovereign", "Socialist", "Democratic", "Authoritarian"],
                "answer": "Authoritarian"
            },
            {
                "question": "The Preamble proclaims India to be a SOVEREIGN nation. What does SOVEREIGN imply? _____",
                "options": ["Dependence on foreign nations", "Absolute power to govern itself", "Limited autonomy", "Subordination to another country"],
                "answer": "Absolute power to govern itself"
            },
            {
                "question": "Which value is highlighted in the Preamble as essential for ensuring fraternity among the people? _____",
                "options": ["Division", "Hatred", "Unity", "Indifference"],
                "answer": "Unity"
            }
        ]

        self.score = 0
        self.question_number = 0
        self.timer_running = False
        self.timer_id = None

        self.title_label = tk.Label(master, text="🎉 Fun Quiz Time! 🎉", bg="#FFDD57", font=("Comic Sans MS", 24, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Timer Label
        self.timer_label = tk.Label(master, text="", bg="#FFDD57", font=("Comic Sans MS", 16))
        self.timer_label.grid(row=1, column=0, sticky='nw', padx=10, pady=(0, 10))

        self.question_frame = tk.Frame(master, bg="#FFEEAA", bd=5, relief="ridge", padx=10, pady=10)
        self.question_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

        self.question_label = tk.Label(self.question_frame, text="", wraplength=400, bg="#FFEEAA", font=("Comic Sans MS", 18))
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self.question_frame, bg="#FFEEAA")
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.options_frame, text="", command=lambda option="": self.fill_blank(option),
                            bg="#FFCC00", font=("Comic Sans MS", 14), padx=10, pady=5)
            btn.pack(fill='x', pady=5)
            self.option_buttons.append(btn)

        self.blank_entry = tk.Entry(self.question_frame, font=("Comic Sans MS", 20), width=40)
        self.blank_entry.pack(pady=10)
        self.blank_entry.config(state='readonly')  # Set to read-only initially

        # Navigation Buttons
        self.navigation_frame = tk.Frame(master, bg="#FFDD57")
        self.navigation_frame.grid(row=3, column=0, columnspan=2, pady=20)

        self.next_button = tk.Button(self.navigation_frame, text="Next Question ➜", command=self.next_question,
                                     bg="#4CAF50", fg="white", font=("Comic Sans MS", 16), borderwidth=0, padx=10, pady=5)
        self.next_button.pack(side='left', padx=10)

        self.restart_button = tk.Button(self.navigation_frame, text="Restart 🔄", command=self.restart_quiz,
                                        bg="#FF5722", fg="white", font=("Comic Sans MS", 16), borderwidth=0, padx=10, pady=5)
        self.restart_button.pack(side='right', padx=10)

        self.show_question()

    def show_question(self):
        current_question = self.questions[self.question_number]
        self.question_label.config(text=current_question["question"])

        for i, option in enumerate(current_question["options"]):
            self.option_buttons[i].config(text=option, command=lambda opt=option: self.fill_blank(opt))

        self.blank_entry.config(state='readonly')  # Make the entry read-only initially
        self.blank_entry.delete(0, tk.END)  # Clear previous entry

        self.start_timer(30)  # Start a 30-second timer

    def fill_blank(self, option):
        self.blank_entry.config(state='normal')  # Allow editing
        self.blank_entry.delete(0, tk.END)  # Clear previous entry
        self.blank_entry.insert(0, option)  # Fill in the blank with the selected option
        self.blank_entry.config(state='readonly')  # Set back to read-only

    def check_answer(self):
        selected_option = self.blank_entry.get()
        correct_answer = self.questions[self.question_number]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done!")
        else:
            messagebox.showinfo("Oops!", f"Wrong! The correct answer is: {correct_answer}")

    def start_timer(self, count):
        if self.timer_running:
            self.master.after_cancel(self.timer_id)  # Cancel the previous timer if running

        self.timer_running = True
        self.update_timer(count)

    def update_timer(self, count):
        if count > 0:
            self.timer_label.config(text=f"Time remaining: {count} seconds")
            self.timer_id = self.master.after(1000, self.update_timer, count - 1)
        else:
            self.check_answer()  # Check the answer when time is up
            self.timer_running = False
            self.next_question()  # Automatically go to the next question

    def next_question(self):
        self.check_answer()  # Check answer before moving to next question
        self.question_number += 1
        if self.question_number < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(self.questions)}")
            self.master.quit()

    def restart_quiz(self):
        self.score = 0
        self.question_number = 0
        self.show_question()

# Create the main window
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
