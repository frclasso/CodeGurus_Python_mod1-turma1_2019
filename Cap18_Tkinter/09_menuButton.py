from tkinter import *

root = Tk()

mb = Menubutton(root, text='Condimentos', relief=RAISED)

mb.grid()

mb_menu = Menu(mb, tearoff=0) # nao permite destacar menu
mb['menu'] = mb_menu

mayoVar = IntVar()
ketVar = IntVar()

mb_menu.add_checkbutton(label='Maionese', variable=mayoVar)
mb_menu.add_checkbutton(label='Ketchup', variable=ketVar)

mb.pack()

root.mainloop()