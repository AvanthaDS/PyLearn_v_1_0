__author__ = 'Avantha'
from tkinter import *

root =Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackline = canvas.create_line(10,10,190,80)
redline = canvas.create_line(10,80,190,10,fill='red')

greenBox = canvas.create_rectangle(50,50,150,80, fill='Green')

# the following line will delete the created red line
# canvas.delete(redline)
#The following will delete all teh content in the canvas
# canvas.delete(ALL)

root.mainloop()