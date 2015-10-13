__author__ = 'Avantha'
from tkinter import *

root = Tk()

labl01 = Label(root, text='First Label', fg='blue', bg='red')
labl01.pack()

labl02 = Label(root, text='second label', fg='blue', bg='green')
labl02.pack(fill=X)
labl03 = Label(root, text='third label', fg='blue', bg='yellow')
labl03.pack(side=LEFT, fill=Y)



root.mainloop()