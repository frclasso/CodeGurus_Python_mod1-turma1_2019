from tkinter import *

root = Tk()

Lb1 = Listbox(root)

Lb1.insert(1, 'Python')
Lb1.insert(2, 'Django')
Lb1.insert(3, 'C#')
Lb1.insert(4, 'Kivy')
Lb1.insert(5, 'PHP')
Lb1.insert(6, 'C++')
Lb1.insert(7, 'JavScript')
Lb1.insert(8, 'Go')


Lb1.pack()


root.mainloop()