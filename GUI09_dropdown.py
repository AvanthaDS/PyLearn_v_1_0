__author__ = 'Avantha'

from tkinter import *

def doNothing():
    print('Ok I wont')

root =Tk()

menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)

menu.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label='New Project...', command=doNothing)
subMenu.add_command(label='New ...', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Redo', command=doNothing)

# This section created the tool bar

toolbar = Frame(root, bg='blue')
inserButt = Button(toolbar, text ='Insert Immage', command=doNothing)
inserButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text='Print', command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Status Bar ....

status = Label(root, text='status of the status....', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()