# https://tkdocs.com/tutorial/canvas.html           --canvas docs
# https://www.w3schools.com/python/python_file_write.asp        --writing to file docs
# https://tkdocs.com/tutorial/widgets.html#entry                --entry widget docs
# https://www.w3schools.com/python/ref_string_join.asp          --join()
# https://pypi.org/project/pyperclip/                           --pyperclip docs

from tkinter import *
from tkinter import messagebox
import pyperclip
import PasswordGenerator as pg

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    passwrd = pg.password()
    pyperclip.copy(passwrd)
    pass_entry.insert(0, passwrd)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(website_entry.get()) == 0 or   len(pass_entry.get()) == 0:
        messagebox.showinfo(title="oops", message="Please do not leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"You have entered the following details: \n Website: {website_entry.get()}"
                                    f"\n Email: {email_entry.get()} \n Password {pass_entry.get()}")

        if is_ok:
            with open('/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY29-Passwordmanager/data.txt', 'a') as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {pass_entry.get()} \n")
                delete_text()

    
def delete_text():
    website_entry.delete(0,END)
    pass_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("Password manager")
windows.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
lock_img=PhotoImage(file="/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY29-Passwordmanager/logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

#label
website=Label(text="Website:")
website.grid(row=1, column=0)

email=Label(text="Email/Username:")
email.grid(row=2, column=0)

password=Label(text="Password:")
password.grid(row=3, column=0)

#entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"xyz@gmail.com")

pass_entry=Entry(width=21)
pass_entry.grid(row=3,column=1)

genrate_pass=Button(text="Generate Password", width=14, command=gen_password)
genrate_pass.grid(row=3,column=2,columnspan=2)

#Buttons
add=Button(text="Add",width=36, command=save)
add.grid(row=4,column=1,columnspan=2)

windows.mainloop()