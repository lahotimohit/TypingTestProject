import english_words
import random

list = english_words.get_english_words_set(['web2'], lower=True)

sentence = ""
for item in list:
    sentence += item


# import logo
# import tkinter
#
# window = tkinter.Tk()
# window.title("Typing Speed Tester")
# window.config(bg="#FFE17B")
# window.minsize(width=900, height=900)
#
# canvas = tkinter.Canvas(master=window, width=800, height=850)
# canvas.config(bg="#CECE5A")
#
# canvas_title = canvas.create_text(400, 150, text="Typing Speed Tester", font=("Ariel", 40, "italic"))
# canvas.subtitle = canvas.create_text(400,200, text="How fast are your fingers? Do the one-minute typing test to find out! Press the space bar after each word.\nAt the end, you'll get your typing speed in CPM and WPM. Good luck!",
#                                      font=("Ariel", 8, "italic"))
#
# canvas.pack()

#
#
# window.mainloop()
