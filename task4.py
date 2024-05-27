import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("258x136")


doggie = PhotoImage(file="dog.png")
dogimage = tk.Label(window, image= doggie)

word = tk.Label(window, text="Pochacco!")

text = tk.Label(window, text = "A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", background= "#A1EDFE")

dogimage.place(x=60, y=5)
word.place(x=130, y=50)
text.place(x=0, y=100)

window.mainloop()