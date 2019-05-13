from tkinter import *

root = Tk()

root.title("Interface GUI")

campo = Label(root, text='Insira seu nome:')
campo.pack(side=LEFT)

entrada = Entry(root, bd=5)
entrada.pack(side=RIGHT)



root.mainloop()