__author__ = 'Avantha'
from tkinter import *


root =Tk()

photo = PhotoImage(file='Apple.png')
lbl = Label(root, image=photo)
lbl.pack()

root.mainloop()