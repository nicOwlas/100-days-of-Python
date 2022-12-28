from tkinter import *
from json.decoder import JSONDecodeError
import json
BACKGROUND_COLOR = "white"
FOREGROUND_COLOR = "black"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("./data.json") as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            data = []
    
    new_item = {"website":website_entry.get(), "login":login_entry.get(), "password":password_entry.get()}
    
    if not website_entry.get() or not login_entry.get():
        pass
    else:
        data.append(new_item)
        with open("./data.json", mode="w") as file:
            json.dump(data, file, indent=2)
    
    website_entry.delete(first=0,last=END)
    password_entry.delete(first=0,last=END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

# Image canvas
canvas = Canvas(width=220, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
lock_image = PhotoImage(file="/Users/nicolas/git/100-days-of-Python/D29/password-manager-start/logo.png")
canvas.create_image(150,100,image = lock_image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
website_label.grid(row=1,column=0)

website_entry = Entry(width=40, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

login_label = Label(text="Email / Username:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
login_label.grid(row=2,column=0)

login_entry = Entry(width=40, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0)
login_entry.grid(row=2,column=1,columnspan=2)
login_entry.insert(0, "nicolas@example.com")

password_label = Label(text="Password:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
password_label.grid(row=3,column=0)

password_entry = Entry(width=23, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0)
generate_password_button.grid(row=3,column=2)

add_button = Button(width=37, text="Add", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0, command=save)
add_button.grid(row=4,column=1, columnspan=2)

window.mainloop()