import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("tk")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", width = 15)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width = 15)
x = tk.Label(window, text= "X")
equal = tk.Button(window, text = "=")
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width = 15)

entry1.grid(row = 1, column= 1)
x.grid(row = 1 , column = 2)
entry2.grid(row = 1, column= 3)
equal.grid(row=1, column = 4)
entry3.grid(row = 1, column= 5)

window.mainloop()