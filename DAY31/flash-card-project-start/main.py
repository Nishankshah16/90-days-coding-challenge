# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
# https://cloud.google.com/translate/docs/languages?hl=en       --google translate google code
# https://support.google.com/docs/answer/3093331?hl=en-GB       --google translate for google sheet

BACKGROUND_COLOR = "#B1DDC6"
list1={}

from tkinter import *
import pandas as pd
import random as r

windows=Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, background=BACKGROUND_COLOR, highlightthickness=0)
# windows.minsize(500,500)
#--------------------------------------------------------------------------

try:
    data=pd.read_csv("/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY31/flash-card-project-start/data/Words_to_learn.csv")
except FileNotFoundError:
    df=pd.read_csv("/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY31/flash-card-project-start/data/french_words.csv")
    list1 = df.to_dict(orient="records")

else:
    list1 = data.to_dict(orient="records")

card = {}

def generate_word():
    global card, timer
    windows.after_cancel(timer)
    card=r.choice(list1)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_image)
    timer = windows.after(3000, flip)


def flip():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_image)


def isknown():
    list1.remove(card)
    data=pd.DataFrame(list1)
    data.to_csv("/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY31/flash-card-project-start/data/Words_to_learn.csv")
    generate_word()


timer = windows.after(3000, flip)



#--------------------------------------------------------------------------




#--------------------------------------------------------------------------

#canvas
canvas=Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)


card_front_image=PhotoImage(file="/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY31/flash-card-project-start/images/card_front.png")
card_back_image= PhotoImage(file="/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY31/flash-card-project-start/images/card_back.png")
canvas_img = canvas.create_image(400,263,image=card_front_image)
title=canvas.create_text(400,150,text="",font=("Ariel",40, "italic"))
word=canvas.create_text(400,263,text="",font=("Ariel",60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


#buttons
right_button_image=PhotoImage(file="/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY31/flash-card-project-start/images/right.png")
right_button=Button(image=right_button_image,highlightthickness=0,background=BACKGROUND_COLOR,command=isknown)
right_button.grid(row=1, column=1)

left_button_image=PhotoImage(file="/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY31/flash-card-project-start/images/wrong.png")
left_button=Button(image=left_button_image, highlightthickness=0, background=BACKGROUND_COLOR,command=generate_word)
left_button.grid(row=1, column=0)

generate_word()

windows.mainloop()