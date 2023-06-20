import customtkinter as tk
from Timerr import StartPlay
import time

loopit = False
timerNumber = "Select a Timer"


def SelectTimer(Timer=None):
    global timerNumber
    if Timer is not None:
        timerNumber = Timer
    text_label.configure(text=timerNumber)
    buttonStart.configure(state=tk.NORMAL)


def button_command():
    if buttonStart.cget("text") == "Start":
        StartTimer()
    else:
        StopTimer()


def StartTimer():
    global loopit
    loopit = True
    countdown(int(timerNumber))
    buttonStart.configure(text="Stop")


def StopTimer():
    global loopit
    loopit = False
    buttonStart.configure(text="Start")
    print("Stopped")





def countdown(t):
    
    if t >= 0 and loopit:
        print(t)
        text_label.configure(text=t)
        root.after(1000, countdown, t - 1)
    elif t <= 0 and loopit:
        StartPlay(int(timerNumber))
        StartTimer()
        
        
    


root = tk.CTk()
root.geometry("361x540")
root.resizable(False, False)

# Create a title label
title_label = tk.CTkLabel(master=root, text="LOL's Timer", font=("Roboto", 50))
title_label.pack(pady=20, padx=10)

# Create a text label
text_label = tk.CTkLabel(master=root, text=timerNumber, font=("Roboto", 20))
text_label.pack(pady=30, padx=10)
text_label.anchor = "center"

# Create a button
buttonStart = tk.CTkButton(master=root, text="Start", command=button_command, state=tk.DISABLED)
buttonStart.pack(pady=12, padx=10)
buttonStart.anchor = "center"

# Create 3 buttons
button10 = tk.CTkButton(master=root, text="10", command=lambda: SelectTimer(10))
button10.pack(side="left", expand=True, anchor="center")

button15 = tk.CTkButton(master=root, text="15", command=lambda: SelectTimer(15))
button15.pack(side="left", expand=True, anchor="center")

button30 = tk.CTkButton(master=root, text="30", command=lambda: SelectTimer(30))
button30.pack(side="left", expand=True, anchor="center")

root.mainloop()
