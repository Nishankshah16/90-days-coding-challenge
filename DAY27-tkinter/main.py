# https://docs.python.org/3/library/tkinter.html#the-packer         --packer docs
# https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm                --pack()
# https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm               --enytry()

import tkinter
from tkinter import Entry, Button

window= tkinter.Tk()
window.title("My first gui program")
window.minsize(500,400)


#label
my_label=tkinter.Label(text="This is a label", font=("Aerial",24,"bold"))
# my_label.pack(side="top")
my_label.grid(column=1,row=1)

def button_clicked():
    
    my_label["text"]=input.get()
    print("button got clicked")

button=tkinter.Button(text="click me",command=button_clicked)
button.grid(column=2,row=2)

new_button=Button(text="New Button")
new_button.grid(row=1,column=3)


#entry

input=Entry(width=10)
input.grid(row=3,column=4)



window.mainloop()