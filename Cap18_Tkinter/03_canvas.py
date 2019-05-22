from tkinter import *

root = Tk()

root.title('Canvas')

tela = Canvas(root, bg='Blue', height=250, width=300)

coordenadas = 10, 50, 240, 210

# desenhando arco
arco = tela.create_arc(coordenadas, start=0, extent=150, fill='red')


# desenhando linha
linha = tela.create_line(10,10,200,200, fill='yellow')


tela.pack()

root.mainloop()