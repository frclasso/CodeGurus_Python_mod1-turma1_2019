from tkinter import *

root = Tk()
root.title("Mouse click events")

# definir 3 diferentes funções para eventos

def left_click(event):
    Label(root, text="Left click").pack()

def middle_click(event):
    Label(root, text="Middle click").pack()

def right_click(event):
    Label(root, text="Right click").pack()


root.bind('<Button-1>', left_click)
root.bind('<Button-2>', right_click)
root.bind('<Button-3>', middle_click)

root.mainloop()