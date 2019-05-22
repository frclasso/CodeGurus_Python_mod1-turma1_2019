from tkinter import *

root = Tk()
root.title("Check button")

CheckVar1 = IntVar()
CheckVar2 = IntVar()

c1 = Checkbutton(root, text="Musica", variable=CheckVar1, onvalue=1, offvalue=0, height=2, width=20)
c2 = Checkbutton(root, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=2, width=20)

c1.pack()
c2.pack()


root.mainloop()