import tkinter 
from tkinter import Entry, Button, Label


window= tkinter.Tk()
window.title("Converter miles to Km")
window.minsize(300,300)


#Entry
input=Entry(width=10)
input.grid(row=1,column=2)




#label 
label=Label(text=f"is equal to",font=("Aerial",24))
label.grid(column=1,row=2)

miles_label=Label(text="Miles",font=("Aerial",24))
miles_label.grid(column=3,row=1)


def on_click_calulation():
    a=float(input.get()) *1.609
    answer_label["text"]= a



#label 
answer_label=Label(text="0",font=("Aerial",24))
answer_label.grid(column=2,row=2)

#label 
unit_label=Label(text="KM",font=("Aerial",24))
unit_label.grid(column=3,row=2)
#button
calculate=Button(text="Calculate",command= on_click_calulation)
calculate.grid(row=3,column=2)



window.mainloop()