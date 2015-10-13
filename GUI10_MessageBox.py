__author__ = 'Avantha'
from tkinter import *
import tkinter.messagebox

base =Tk()

tkinter.messagebox.showinfo("Avantha's Window", 'My Bla.. Bla.. Bla...')

answer = tkinter.messagebox.askquestion('Question 01','Ok this is my message?')
if answer == 'yes':
    print(' you answered yes')

base.mainloop()