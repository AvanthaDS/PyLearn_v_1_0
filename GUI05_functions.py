__author__ = 'Avantha'
from tkinter import *

base =Tk()

def prinName():
    print('Hello My name is Avantha')

def myfunc(event):
    print('What a cool way')

but_01=Button(base, text='Print my name', command=prinName)
but_01.pack()

but_02=Button(base, text='the text')
but_02.bind('<Button-1>', myfunc)
but_02.pack()

base.mainloop()