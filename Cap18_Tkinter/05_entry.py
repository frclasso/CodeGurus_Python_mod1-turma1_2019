from tkinter import *

root = Tk()

L1 = Label(root, text="Nome do usuário:")
L1.pack(side=LEFT)

E1 = Entry(root, bd=1) # bd => borda, de 1 a 5
E1.pack(side=RIGHT)



root.mainloop()