# https://colorhunt.co/                 --choose color
# https://www.tcl-lang.org/man/tcl8.6/TclCmd/after.htm          --after()

import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text="Timer")
    checkmarks.config(text="")
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = 1 * 60
    short_break_sec = 1 * 60
    long_break_sec = 2 * 60

   
    if reps% 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        reset_timer()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark +="✔️"
        checkmarks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


title_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
title_label.grid(row=0,column=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY28/pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
# canvas.pack()
canvas.grid(row=1,column=1)

start_button=Button(text="Start",highlightthickness=0, command = start_timer)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2,column=2)

checkmarks=Label(fg=GREEN,bg=YELLOW)
checkmarks.grid(row=3,column=1)

window.mainloop()