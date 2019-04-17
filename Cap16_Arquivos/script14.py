# .csv

dados = []

nome = input('Digite seu nome:')
sobrenome = input('Digite seu sobrenome:')
email = nome.lower()+'.'+sobrenome.lower()+'@email.com'

# adicionando items em lista (append)
dados.append(nome)
dados.append(sobrenome)
dados.append(email)

# check
#print(dados)


arq = open('pessoas.csv', 'a')
for x in dados:
    arq.write(x + ',')
arq.write('\n')

arq.close()
