__author__ = 'Avantha'
from tkinter import *

base =Tk()

def leftclick(event):
    print('LEFT')

def rightclick(event):
    print('Right')

def middleclick(event):
    print('middle click')

frame = Frame(base, width=300, height=250)
frame.bind('<Button-1>', leftclick)
frame.bind('<Button-2>', middleclick)
frame.bind('<Button-3>', rightclick)
frame.pack()



base.mainloop()