
from tkinter import *

root = Tk()
root.title("Interface Gui Tkinter")

frame = Frame(root)  # herança fram é filha de root
frame.pack() # pack é o gerenciado

botomframe = Frame(root)
botomframe.pack(side=BOTTOM)

redbutton = Button(frame, text='Red', fg='red')  # fg = foreground
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text='Green', fg='green')
greenbutton.pack(side=LEFT)

bluebutton = Button(frame, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)

blackbutton = Button(frame, text='Black', fg='black')
blackbutton.pack(side=LEFT)


root.mainloop()