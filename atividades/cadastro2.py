# print('Esse programa foi importado com sucesso')


def inserirDados():
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    email = nome.lower() + '.' + sobrenome.lower() + '@email.com'
    return nome, sobrenome, email


pessoas = []  # variavel global


def cadastrar():
    pessoas.append(inserirDados())
    return pessoas


def salvaDados():
    cadastrar()
    with open('cadastropessoas.txt', 'a') as file:
        for pessoa in pessoas:
            file.write(str(pessoa))
            file.write('\n')


# def main():
#     salvaDados()
#
#
# if __name__ == "__main__":
#     main()
#     print('Feito...')
#

