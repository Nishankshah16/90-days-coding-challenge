from tkinter import *
from tkinter import messagebox
import pyperclip
import PasswordGenerator as pg
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    passwrd = pg.password()
    pyperclip.copy(passwrd)
    pass_entry.insert(0, passwrd)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=pass_entry.get()

    new_dict={
        website:
        {
        "Email":email,
        "Password":password
        }
        }
    

    if len(website_entry.get()) == 0 or   len(pass_entry.get()) == 0:
        messagebox.showinfo(title="oops", message="Please do not leave any field empty!")
    else:
        try:
            #open with read mode and reading old data
            with open('/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY30/file.json', 'r') as doc:
                data=json.load(doc)
    
                
        except FileNotFoundError:
            with open("/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY30/file.json","w") as doc:
                json.dump(new_dict,doc, indent=4)

        else:
            #updating the file
            data.update(new_dict)

            with open("/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY30/file.json","w") as doc:
                json.dump(data,doc, indent=4)
        
        finally:
            delete_text()

        

    
def delete_text():
    website_entry.delete(0,END)
    pass_entry.delete(0,END)
# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website=website_entry.get()

    try:
        with open('/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY30/file.json', 'r') as doc:
            data=json.load(doc)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="file is not found")
    
    else:
        if website in data:
            email= data[website]["Email"]
            password=data[website]["Password"]
            messagebox.showinfo(title=website ,message=f"For {website} \n email: {email} \n password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"{website} not found sorry")


        # if pass_entry == data.website.password

# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("Password manager")
windows.config(padx=50,pady=50)

canvas=Canvas(width=800,height=526)
lock_img=PhotoImage(file="/Users/nishanknitinshah/Documents/Python/90 DAYS OF PYTHON/DAY29-Passwordmanager/logo.png")
canvas.create_image(400,263,image=lock_img)
canvas.grid(row=0,column=1)

#label
website=Label(text="Website:")
website.grid(row=1, column=0)

email=Label(text="Email/Username:")
email.grid(row=2, column=0)

password=Label(text="Password:")
password.grid(row=3, column=0)

#entries
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"xyz@gmail.com")

pass_entry=Entry(width=21,show="*")
pass_entry.grid(row=3,column=1)

#Buttons
genrate_pass=Button(text="Generate Password", width=14, command=gen_password)
genrate_pass.grid(row=3,column=2,columnspan=2)

add=Button(text="Add",width=36, command=save)
add.grid(row=4,column=1,columnspan=2)

search=Button(text="Search",width=14, command=find_password)
search.grid(row=1,column=2,columnspan=2)

windows.mainloop()