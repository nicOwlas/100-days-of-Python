from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(width=600,height=400)

# Labels
my_label = Label(text="This is a test")
my_label.pack(side="top")

# Buttons
def button_clicked():
    print("Button got clicked")
    my_label.config(text=entry.get())

my_button = Button(text = "Click here!", command=button_clicked)
my_button.pack()

# Inputs
entry = Entry()
entry.pack()
print()


window.mainloop()