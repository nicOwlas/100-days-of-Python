from tkinter import *
from tkinter import messagebox
from json.decoder import JSONDecodeError
from password_generator import password_generator
import json
import pyperclip

BACKGROUND_COLOR = "white"
FOREGROUND_COLOR = "black"

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website = website_entry.get().lower()
    login = login_entry.get()
    password = password_entry.get()
    try:
        with open("./data.json", "r") as file:
            data = json.load(file)
    except:
        messagebox.showwarning(title=website_entry.get(), message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(
                title=website,
                message=f"Login: {data[website]['login']}\nPassword: {data[website]['password']}",
            )
        else:
            messagebox.showwarning(
                title=website_entry.get(), message="Website not found"
            )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_auto_complete():
    password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    login = login_entry.get()
    password = password_entry.get()
    new_data = {website: {"login": login, "password": password}}

    is_form_complete = not (not website or not login or not password)

    if is_form_complete:
        # is_ok = messagebox.askokcancel(
        #     title=website,
        #     message=f"Save?\n•website: {website}\n•login: {login} \n•password: {password}",
        # )
        # if is_ok:
        try:
            with open("./data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("./data.json", "w") as file:
                data = json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("./data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)
            messagebox.showinfo(title=website, message="Info saved to file")
    else:
        messagebox.showwarning(
            title=website,
            message="Website, login and password should not be left empty",
        )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

# Image canvas
canvas = Canvas(width=220, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
lock_image = PhotoImage(
    file="/Users/nicolas/git/100-days-of-Python/D29/password-manager-start/logo.png"
)
canvas.create_image(150, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
website_label.grid(row=1, column=0)

website_entry = Entry(
    width=23, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0
)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

search_button = Button(
    text="Search",
    fg=FOREGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=search_website,
    width=13,
)
search_button.grid(row=1, column=2)

login_label = Label(text="Email / Username:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
login_label.grid(row=2, column=0)

login_entry = Entry(
    width=40, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0
)
login_entry.grid(row=2, column=1, columnspan=2)
login_entry.insert(0, "nicolas@example.com")

password_label = Label(text="Password:", fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR)
password_label.grid(row=3, column=0)

password_entry = Entry(
    width=23, fg=FOREGROUND_COLOR, bg=BACKGROUND_COLOR, highlightthickness=0
)
password_entry.grid(row=3, column=1)

generate_password_button = Button(
    text="Generate Password",
    fg=FOREGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=password_auto_complete,
    width=13,
)
generate_password_button.grid(row=3, column=2)

add_button = Button(
    width=37,
    text="Add",
    fg=FOREGROUND_COLOR,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=save,
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
