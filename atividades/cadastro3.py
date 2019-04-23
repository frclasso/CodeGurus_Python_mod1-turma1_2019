# print('Esse programa foi importado com sucesso')

# ler o arquivo cadastropessoas.txt

def leitor():
    with open('cadastropessoas.txt', 'r') as file:
        leitor = file.read()
        print(leitor)

    print('feito')

# leitor()
