from tkinter import *

root = Tk()

root.title("Interface GUI")

root.geometry('380x200')

campo = Label(root, text='Insira seu nome:')
campo.place(x=10, y=10)

entrada = Entry(root, bd=1)
entrada.place(x=160, y=10)

campo2 = Label(root, text='Insira seu sobrenome:')
campo2.place(x=10, y=40)

entrada2 = Entry(root, bd=1)
entrada2.place(x=160, y=40)


campo3 = Label(root, text='Insira seu e-mail:')
campo3.place(x=10, y=60)

entrada3 = Entry(root, bd=1)
entrada3.place(x=160, y=60)


botao = Button(root, text='Submit')
botao.place(x=160, y=100)

root.mainloop()