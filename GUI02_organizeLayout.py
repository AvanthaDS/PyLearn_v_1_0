__author__ = 'Avantha'

from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

butt01 = Button(topFrame, text="BUT01", fg='blue')
butt02 = Button(topFrame, text='BUT02', fg='Green')
butt03 = Button(topFrame, text='BUT03', fg='brown')
butt04 = Button(botFrame, text='BUT04')

butt01.pack(side=LEFT)
butt02.pack(side=LEFT)
butt03.pack(side=LEFT)
butt04.pack(side=BOTTOM)

root.mainloop()