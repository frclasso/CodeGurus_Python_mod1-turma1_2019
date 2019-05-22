from tkinter import *

root = Tk()

root.title("Lables")

label = Label(root, text="Hey, How are you doing?", relief=RAISED)

label.pack()

Label(root, text='Sufficient width', fg='white', bg='purple', relief=RAISED).pack()
Label(root, text='Width of x', fg='white', bg='green', relief=RAISED).pack(fill='x')
Label(root, text='Height of y', fg='white', bg='black', relief=RAISED).pack(side='left', fill='y')
Label(root, text='Height of y', fg='white', bg='blue', relief=RAISED).pack(side='left',fill='y')
root.mainloop()