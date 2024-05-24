import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T=Town Veterinary Clinic Database")

doggie = PhotoImage(file="dog.png")
dogimage = tk.Label(window, image= doggie)  

searchbutton = tk.Button(window, text = "Search by Name")

entry1 = tk.Entry(window, text="search dog name here")

title = tk.Label(window, text="Client Database")

name = tk.Label(window, text="Name")
type = tk.Label(window, text="Type")
breed = tk.Label(window, text="Breed")
owner = tk.Label(window, text="Owner")
birthdate = tk.Label(window, text="Birthdate")

name1 = tk.Entry(window, text="Name")
type1 = tk.Entry(window, text="Type")
breed1 = tk.Entry(window, text="Breed")
owner1 = tk.Entry(window, text="Owner")
birthdate1 = tk.Entry(window, text="Birthdate")

previous = tk.Button(window, text="<Previous")

save = tk.Button(window, text="Save Entry", bg="#ADB2AB")

next = tk.Button(window, text="Next>")

dogimage.grid(row=1, column=1, rowspan=3)
searchbutton.grid(row=1, column= 4)
entry1.grid(row=1, column=5)
title.grid(row=2, column=3)
name.grid(row=4, column = 1)
type.grid(row=4, column = 2)
breed.grid(row=4, column = 3)
owner.grid(row=4, column = 4)
birthdate.grid(row=4, column = 5)

name1.grid(row=5, column=1)
type1.grid(row=5, column=2)
breed1.grid(row=5, column=3)
owner1.grid(row=5, column=4)
birthdate1.grid(row=5, column=5)
previous.grid(row=6, column=1)
save.grid(row=6, column=3)
next.grid(row=6, column= 5)

window.mainloop()