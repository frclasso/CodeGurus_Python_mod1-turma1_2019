# cadastro pessoas

# nome, sobrenome, email

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

email = nome.lower() + '.' + sobrenome.lower() + '@email.com'

pessoas = []

# adicionando a lista
pessoas.append(nome)  # adicionar nome em pessoas
pessoas.append(sobrenome)
pessoas.append(email)

#print(pessoas)   ## teste


with open('arquivo.txt', 'a') as file:
    for nome in pessoas:
        file.writelines(nome + ',')
    file.writelines('\n')  # ENTER

