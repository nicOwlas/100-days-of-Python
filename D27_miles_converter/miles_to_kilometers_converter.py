from tkinter import *

window = Tk()
window.title("Miles to Kms")
# window.minsize(width=100,height=100)
window.config(padx=10,pady=10)

# Inputs
entry = Entry()
entry.grid(row=0,column=1)

kilometers = 0

# Labels
text_miles = Label(text="Miles")
text_miles.grid(row=0,column=2)

text_equals = Label(text="is equal to")
text_equals.grid(row=1,column=0)

text_value = Label(text="0")
text_value.grid(row=1,column=1)

text_kms = Label(text="Kms")
text_kms.grid(row=1,column=2)

# Buttons
def button_clicked():
    miles = float(entry.get())
    kilometers = round(miles * 1.6,2)
    text_value.config(text=kilometers)

button_calculate = Button(text = "Calculate", command=button_clicked)
button_calculate.grid(row=2,column=1)




window.mainloop()