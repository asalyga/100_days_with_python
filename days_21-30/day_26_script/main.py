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
LONG_BREAK_MIN = 10
REPS = 0
COUNTER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_counter():
    window.after_cancel(COUNTER)
    canvas.itemconfig(timer_txt, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text=" ")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_min)
        timer.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_min)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_min)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global COUNTER
        COUNTER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS / 2)):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

# window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
# Buttons/Labels setup
timer = Label(text="Timer", font=(FONT_NAME, 60), fg=GREEN, bg=YELLOW)
start = Button(text="Start", font=(FONT_NAME, 18), highlightbackground=YELLOW, command=start_timer)
reset = Button(text="Reset", font=(FONT_NAME, 18), highlightbackground=YELLOW, command=reset_counter)
checkmark = Label(font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)

# Tomato img setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))

# Grid setup
timer.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start.grid(column=0, row=2)
reset.grid(column=3, row=2)
checkmark.grid(column=1, row=3)

window.mainloop()
