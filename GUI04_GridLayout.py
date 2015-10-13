__author__ = 'Avantha'

from tkinter import *

base =Tk()

lbl_1 = Label(base, text='Name')
lbl_2 = Label(base, text='Password')
entry_1 = Entry(base)
entry_2 = Entry(base)

lbl_1.grid(row=0, sticky=E)
lbl_2.grid(row=1, sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(base, text='Keep me logged in')
c.grid(columnspan=2)

base.mainloop()