import time
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen",True)

def check_key():
    if str(entry.get()) == "hello":
        exit()
    else:
        label.configure(text = "Wrong code inserted")
        time.sleep(2)
        label.configure(text = "Please enter code")

def donothing():
    print("Close Function Disabled")

root.protocol("WM_DELETE_WINDOWS", donothing)
label = Label(root, text = "Please enter code", font = ((""),15))
label.place(relx = 0.5, rely = 0.4, anchor = CENTER)

entry = Entry(root)
entry.place(width = 250, height = 50, relx = 0.5, rely = 0.5, anchor = CENTER)

button = Button(root, text = "Unlock", bg = "red", fg = "white", command = check_key)
button.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()
