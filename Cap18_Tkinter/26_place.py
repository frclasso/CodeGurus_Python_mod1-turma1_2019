from tkinter import *

root = Tk()

L1 = Label(root, text='Fisica')
L1.place(x=10, y=10)
E1 = Entry(root, bd=1)
E1.place(x=90, y=10)

L2 = Label(root, text='Matematica')
L2.place(x=10, y=50)
E2 = Entry(root, bd=1)
E2.place(x=90, y=50)

L3 = Label(root, text='Total')
L3.place(x=10, y=150)
E3 = Entry(root, bd=1)
E3.place(x=90, y=150)

b = Button(root, text='Add')
b.place(x=100, y=100)

root.geometry("280x230")

root.mainloop()