from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("Message Box")

# geometry width x height + Left + Top
root.geometry("180x100+100+100")


def helloCallBack():
    msg = messagebox.showinfo(title='Hello Python', message="Hello World")


Botao = Button(root, text='Hello', command=helloCallBack)
Botao.place(x=50, y=50)  # posicionamento do botao

root.mainloop()