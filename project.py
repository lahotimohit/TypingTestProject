import tkinter as tk
import random
import time

SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "The only thing we have to fear is fear itself.",
    "To be or not to be, that is the question.",
    "Ask not what your country can do for you, ask what you can do for your country.",
    "Life is what happens when you're busy making other plans.",
]


class TypingSpeedTestApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Typing Speed Test")
        self.window.config(bg="#3E001F")
        self.current_sentence = tk.StringVar()
        self.current_input = tk.StringVar()
        self.start_time = None

        self.setup_ui()

    def setup_ui(self):
        canvas = tk.Canvas(width=800, height=800)
        canvas.config(bg="#FFE5AD")
        self.current_sentence.set("Click 'Start' to begin the typing test.")
        self.sentence_label = tk.Label(self.window, textvariable=self.current_sentence, wraplength=400, font=("Arial", 16))
        self.sentence_label.pack(pady=20)

        self.input_entry = tk.Entry(self.window, textvariable=self.current_input, font=("Arial", 16))
        self.input_entry.pack(pady=10)

        self.start_button = tk.Button(self.window, text="Start", command=self.start_typing_test)
        self.start_button.pack(pady=20)

        canvas.pack()

    def start_typing_test(self):
        self.start_button.config(state=tk.DISABLED)
        self.current_input.set("")
        self.current_sentence.set(random.choice(SENTENCES))
        self.input_entry.config(state=tk.NORMAL)
        self.input_entry.focus()
        self.start_time = time.time()
        self.window.bind("<Return>", self.check_typing)

    def check_typing(self, event):
        user_input = self.current_input.get()
        if user_input == self.current_sentence.get():
            elapsed_time = time.time() - self.start_time
            words_per_minute = int(len(user_input.split()) / (elapsed_time / 60))
            accuracy = self.calculate_accuracy(user_input, self.current_sentence.get())
            result_text = f"Typing Speed: {words_per_minute} words per minute\nAccuracy: {accuracy}%"
            self.current_sentence.set(result_text)
        else:
            self.current_sentence.set("Try again. Your typing does not match the given sentence.")

        self.start_button.config(state=tk.NORMAL)
        self.input_entry.config(state=tk.DISABLED)
        self.window.unbind("<Return>")

    def calculate_accuracy(self, user_input, actual_sentence):
        correct_characters = sum(a == b for a, b in zip(user_input, actual_sentence))
        total_characters = max(len(user_input), len(actual_sentence))
        accuracy = (correct_characters / total_characters) * 100
        return round(accuracy, 2)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
