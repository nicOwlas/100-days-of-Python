
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = {"duration": 25, "title": "WORK", "color": GREEN}
SHORT_BREAK_MIN = {"duration": 5, "title": "BREAK", "color": PINK}
LONG_BREAK_MIN = {"duration": 20, "title": "BREAK", "color": RED}
WORK_SERIE = [WORK_MIN,SHORT_BREAK_MIN]*4 + [LONG_BREAK_MIN]
task_index = 0
timer = None

def lift_window():
    window.attributes('-topmost', True)
    window.focus_force() 
    window.attributes('-topmost', False)
    #window.attributes('-topmost', 0)  

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    check_marks.config(text="", fg= GREEN, bg=YELLOW)
    timer_label.config(text="Timer",font=(FONT_NAME,60,"normal"),fg=GREEN, bg=YELLOW)
    count_minutes = int(WORK_MIN["duration"]*60 // 60)
    count_seconds = int(WORK_MIN["duration"]*60 % 60)
    canvas.itemconfig(timer_text, text=f"{count_minutes:02}:{count_seconds:02}")
    global task_index
    task_index = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global task_index
    window.after(1000, lift_window)
    serie = WORK_SERIE[task_index]
    count_down(serie["duration"] * 60, serie)
    timer_label.config(text=serie["title"], fg=serie["color"])
    timer_label.config(text=serie["title"], fg=serie["color"])
    task_index += 1
    task_index %= len(WORK_SERIE) # Resume to initial task

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, serie):
    count_minutes = int(count // 60)
    count_seconds = int(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_minutes:02}:{count_seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, serie)
    else:
        start_timer()        
        if serie["title"] == "WORK":        
            check_marks.config(text=check_marks.cget("text")+"✔")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer_label = Label(text="Timer",font=(FONT_NAME,60,"normal"),fg=GREEN, bg=YELLOW)
timer_label.grid(row=0,column=1)

# Canvas
count_minutes = int(WORK_MIN["duration"]*60 // 60)
count_seconds = int(WORK_MIN["duration"]*60 % 60)
canvas = Canvas(width=240, height=240, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(120,120,image = tomato_image)
timer_text = canvas.create_text(120, 145, text=f"{count_minutes:02}:{count_seconds:02}", font=(FONT_NAME,35,"bold"), fill="white")
canvas.grid(row=1,column=1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, borderwidth=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",  highlightthickness=0, bg=YELLOW, borderwidth=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", fg= GREEN, bg=YELLOW)
check_marks.grid(row=2, column=1)

window.mainloop()