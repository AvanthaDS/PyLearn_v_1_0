__author__ = 'Avantha'
from tkinter import *

class adsbuttons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='Print Massage', command=self.printmassage)
        self.printButton.pack(side=LEFT)

        self.quitbutton = Button(frame, text='Quit', command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmassage(selfs):
        print('Woow, this works')

root =Tk()

b = adsbuttons(root)

root.mainloop()