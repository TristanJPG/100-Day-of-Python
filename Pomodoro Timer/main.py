from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    wSec = WORK_MIN * 60
    sBreak = SHORT_BREAK_MIN * 60
    lBreak = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(lBreak)
        title.config(text="Take a Longer Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(sBreak)
        title.config(text="Take a Break!", fg=PINK)
    else:
        count_down(wSec)
        title.config(text="Working!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    minutes = math.floor(count / 60)
    second = count % 60
    if second <= 9:
        second = f"0{second}"
    canvas.itemconfig(timer, text=f"{minutes}:{second}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        workSessions = math.floor(reps/2)
        if _ in range(workSessions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro!")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title.grid(column=1, row=0)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start!", font=(FONT_NAME), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset!", font=(FONT_NAME), highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)
window.mainloop()
