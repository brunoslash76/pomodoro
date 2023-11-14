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
CHECK_MARK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global timer
  window.after_cancel(timer)

  main_label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1

  work_min = WORK_MIN * 60
  short_break = SHORT_BREAK_MIN * 60
  long_break = LONG_BREAK_MIN * 60

  if reps % 8 == 0:
    count_down(long_break)
    main_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    count_down(short_break)
    main_label.config(text="Break", fg=PINK)
  else:
    count_down(work_min)
    main_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

  count_min = math.floor(count / 60)
  count_sec = count % 60

  count_min_str = ""
  count_sec_str = ""

  if count_min < 10:
    count_min_str = f"0{count_min}"
  else:
    count_min_str = f"{count_min}"

  if count_sec < 10:
    count_sec_str = f"0{count_sec}"
  else:
    count_sec_str = f"{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min_str}:{count_sec_str}")

  if count > 0:
    global timer 
    timer = window.after(1, count_down, count - 1)
  else:
    start_timer()
    mark = ""
    work_session = math.floor(reps / 2)

    for _ in range(work_session):
      mark += CHECK_MARK

    check_marks.config(text=mark)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, height=224, bg=YELLOW)

# MAIN LABEL
main_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
main_label.grid(column=1, row=0)

# CANVAS
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

image = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=image)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

# BUTTON START
def start_pomodoro(): 
  print("START POMODORO")
  start_timer()

start_button = Button(text="Start", highlightthickness=0, bg="white")
start_button.config(command=start_pomodoro)
start_button.grid(column=0, row=2)

# BUTTON RESET
def reset_pomodoro(): 
  print("RESET POMODORO")
  reset_timer()

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.config(command=reset_pomodoro)
reset_button.grid(column=2, row=2)

# CHECK MARK
check_marks = Label(fg=GREEN, highlightthickness=0)
check_marks.grid(column=1, row=3)



# Last Line
window.mainloop()