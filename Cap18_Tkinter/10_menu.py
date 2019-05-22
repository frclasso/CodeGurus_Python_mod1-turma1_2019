from tkinter import *


root = Tk()
root.title("Menu bar")
menubar = Menu(root)


filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save as')
filemenu.add_command(label='Close')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo')
editmenu.add_separator()
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Select all')

menubar.add_cascade(label='Edit', menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help index')
helpmenu.add_command(label='About')
menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)
root.mainloop()