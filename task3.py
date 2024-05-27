import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")


doggie = PhotoImage(file="dog.png")
dogimage = tk.Label(window, image= doggie)

word = tk.Label(window, text="Pochacco!")

text = tk.Label(window, text = "A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", background= "#A1EDFE")

dogimage.grid(row=1, column=2, rowspan=3)
word.grid(row=2, column=3)
text.grid(row=4, column=1, columnspan=4)

window.mainloop()