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
LONG_BREAK_MIN = 0.1
REPS=0
check="✔"
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    lbl1.config(text="Timer",fg=GREEN)
    lbl2.config(text="")
    canvas.itemconfig(timer_text,text=f"00:00")
    global REPS
    REPS=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS,check
    REPS+=1
    if REPS%8==0:
        window.attributes('-topmost', True)
        count_down(LONG_BREAK_MIN*60,text="Break",color=RED)
        check += " | "
        lbl2.config(text=check)
    elif REPS % 2 == 0:
        window.attributes('-topmost', True)
        count_down(SHORT_BREAK_MIN * 60, text="Break", color=PINK)
    else:
        window.attributes('-topmost', True)
        count_down(WORK_MIN*60,text="Work",color=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count,text,color):
    global check,timer
    count_min=math.floor(count / 60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    lbl1.config(text=text,font=(FONT_NAME,30, "bold"),fg=color,bg=YELLOW)
    if count>0:
        timer=window.after(1000,count_down,count-1,text,color)
    else:
        start_timer()
        if REPS%2==0:
            lbl2.config(text=check)
            check += "✔"


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
t_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=t_img)
timer_text=canvas.create_text(108,130,text=f"00:00",fill="white",font=(FONT_NAME,30, "bold"))
canvas.grid(column=1,row=1)

lbl1=Label(text="Timer", font=(FONT_NAME,30, "bold"),fg=GREEN,bg=YELLOW)
lbl1.grid(column=1,row=0)

lbl2=Label(font=(FONT_NAME,10, "bold"),fg=GREEN,bg=YELLOW)
lbl2.grid(column=1,row=3)

btn_start=Button(text="Start",font=(FONT_NAME,10, "bold"),fg=RED,command=start_timer)
btn_start.grid(column=0,row=2)

btn2=Button(text="Reset",font=(FONT_NAME,10, "bold"),fg=RED,command=reset_timer)
btn2.grid(column=2,row=2)



window.mainloop()