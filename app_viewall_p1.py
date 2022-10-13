import tkinter as tk
from tkinter import *
import os
import print_db
import subprocess as sub


# BASIC COMPONENTS
v_root = tk.Tk()
v_root.title('Pythonees Recipe Book')
v_root.resizable(False, False) # WINDOW NOT RESIZABLE
canvas = tk.Canvas(v_root, height = "700", width = "700", bg = "#e3e398")
canvas.pack()
frame = tk.Frame(v_root, bg = "#FFF")
frame.place(relheight = 0.7, relwidth = 0.7, relx = 0.5, rely = 0.5, anchor = CENTER) 

msg = tk.Label(frame, text = "Pythonees Recipe Book Menu",
                fg = "#000", bg = "#e3e398", 
                font = ("Consolas 15", 20))
msg.place(anchor = CENTER, relx = 0.5, rely = 0.1)

# BACK TO START
def prev(): 
    v_root.destroy()
    import app
    app.root.deiconify()
     
    
prev = tk.Button(frame, text = "Previous", padx = 5, pady = 5, 
                    fg="#000", bg="gray", font=('Consolas 15', 14),
                    command = prev)
prev.place(anchor = CENTER, relx= 0.5, rely=0.8)