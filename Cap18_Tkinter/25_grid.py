from tkinter import *


root = Tk()

root.title("Grid Layout")

Label(root, text='Username').grid(row=0)
Entry(root).grid(row=0, column=1)


Label(root, text='PASSWORD').grid(row=1)
Entry(root).grid(row=1, column=1)

Checkbutton(root, text='Keep me Logged in').grid(columnspan=2)


root.mainloop()