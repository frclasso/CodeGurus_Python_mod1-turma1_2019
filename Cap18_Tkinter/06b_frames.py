from tkinter import *

root = Tk()

root.title("Frame")


top_frame = Frame(root).pack()
bottom_frame = Frame(root).pack(side='bottom')

btn1 = Button(top_frame, text='Botão 1', fg='red').pack()
btn2 = Button(top_frame, text='Botão 2', fg='green').pack()

btn3 = Button(bottom_frame, text='Botão 3', fg='purple').pack(side='left')
btn4 = Button(bottom_frame, text='Botão 4', fg='blue').pack(side=LEFT)

root.mainloop()