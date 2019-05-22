from tkinter import *

root = Tk()
root.title("Pack manager")

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(bottomframe, text='Red', fg='red')
redbutton.pack(side=LEFT)

browbutton = Button(bottomframe, text='Brown', fg='brown')
browbutton.pack(side=LEFT)

bluebutton = Button(bottomframe, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)

root.mainloop()