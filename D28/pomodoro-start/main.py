
from tkinter import *
from functools import partial
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = {"duration": 3 / 60, "title": "WORK", "color": GREEN}
SHORT_BREAK_MIN = {"duration": 1 / 60, "title": "BREAK", "color": PINK}
LONG_BREAK_MIN = {"duration": 4 / 60, "title": "LONG BREAK", "color": RED}
WORK_SERIE = [WORK_MIN,SHORT_BREAK_MIN]*2 + [LONG_BREAK_MIN]
task_index = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    pass
    # window.after_cancel(start_button)
    # canvas.itemconfig(timer_text, text=5)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global task_index
    serie = WORK_SERIE[task_index]
    count_down(serie["duration"] * 60, serie)
    timer_label.config(text=serie["title"], fg=serie["color"])
    timer_label.config(text=serie["title"], fg=serie["color"])
    task_index += 1
    task_index %= len(WORK_SERIE) # Resume to initial task
    print(f"Task index: {task_index}")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, serie):
    count_minutes = int(count // 60)
    count_seconds = int(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_minutes:02}:{count_seconds:02}")
    if count > 0:
        window.after(1000, count_down, count - 1, serie)
        print(count)
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
canvas = Canvas(width=240, height=240, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(120,120,image = tomato_image)
timer_text = canvas.create_text(120, 145, text="00:00", font=(FONT_NAME,35,"bold"), fill="white")
canvas.grid(row=1,column=1)

# Buttons
# start_timer_with_arguments = partial(start_timer, task_index)
start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, borderwidth=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",  highlightthickness=0, bg=YELLOW, borderwidth=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="✔", fg= GREEN, bg=YELLOW)
check_marks.grid(row=2, column=1)


window.mainloop()