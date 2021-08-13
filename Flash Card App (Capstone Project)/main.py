from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_list = data.values.tolist()
french_words = None


# -------------------------------------------Wrong Answer------------------------------------------- #
def wrong_ans():
    ask_question()


# -------------------------------------------Correct Answer------------------------------------------- #
def correct_ans():
    data_list.pop(data_list.index(french_words))
    ask_question()


# -------------------------------------------Show Answers------------------------------------------- #
def show_ans():
    ans = french_words[2]
    canvas.itemconfig(question_img, image=back_card)
    canvas.itemconfig(title, text="English")
    canvas.itemconfigure(word, text=ans)
# -------------------------------------------Ask Question------------------------------------------- #


def ask_question():
    global french_words
    canvas.itemconfig(question_img, image=front_card)
    french_words = random.choice(data_list)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=french_words[1])
    window.after(3000, show_ans)


# -------------------------------------------UI SETUP------------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# image creation
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
image_correct = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images/wrong.png")

# question/answer area
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
question_img = canvas.create_image(400, 263, image=front_card)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# correct button
button_correct = Button(image=image_correct, highlightthickness=0, bg=BACKGROUND_COLOR, command=correct_ans)
button_correct.grid(row=1, column=0)

# incorrect button
button_wrong = Button(image=image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=ask_question)
button_wrong.grid(row=1, column=1)

ask_question()
window.mainloop()

words_not_learned = {
    "French": [words[0] for words in data_list],
    "English": [words[1] for words in data_list],
}

words_to_learn = pandas.DataFrame(words_not_learned)
words_to_learn.to_csv('data/words_to_learn.csv')
