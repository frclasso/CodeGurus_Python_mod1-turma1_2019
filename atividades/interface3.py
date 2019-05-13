from tkinter import *

root = Tk()

root.title("Cadastro de usuários")

root.geometry('380x200')

dados =[]


def salvaDados():
    nome = entrada1.get()
    sobrenome = entrada2.get()
    email = entrada3.get()

    dados_recebidos = [nome + ',' + sobrenome + ',' + email]
    dados.append(dados_recebidos)


def exporta_dados():
    with open('cadastro.csv','a') as file:
        for data in dados:
            file.writelines(str(data))


def close_window():
    root.quit()


campo1 = Label(root, text='Insira seu nome:')
campo1.place(x=10, y=10)

entrada1 = Entry(root, bd=1)
entrada1.place(x=160, y=10)

campo2 = Label(root, text='Insira seu sobrenome:')
campo2.place(x=10, y=40)

entrada2 = Entry(root, bd=1)
entrada2.place(x=160, y=40)


campo3 = Label(root, text='Insira seu e-mail:')
campo3.place(x=10, y=60)

entrada3 = Entry(root, bd=1)
entrada3.place(x=160, y=60)


botao1 = Button(root, text='Submit', command=salvaDados)
botao1.place(x=160, y=100)

botao2 = Button(root, text='Exportar', command=exporta_dados)
botao2.place(x=160, y=140)
print(dados)

botao3 = Button(root, text='Sair', command=close_window)
botao3.place(x=160, y=180)

root.mainloop()