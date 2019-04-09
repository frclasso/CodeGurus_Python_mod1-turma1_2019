# strings
# imutaveis


nome = 'Code Cla'
# indice
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print()
# fatia
print(nome[0:4])
# concatenacao
nome = nome + ' Escola de tecnologia'
print(nome)

# member in, not in
print('Code' in nome)   # Code Cla Escola de tecnologia
print('CODE' in nome)
print('CODE' not in nome)

# comprimento , len
print(len(nome))
print()

# laço
for indice, letra in enumerate(nome):
    print(indice, letra)

print()

# find
print(nome.find('Cla'))
print(str.find(nome, 'Cla'))


# contar, count
print(nome.count('e'))
print(str.count(nome, 'e'))

# mudar o caso
nome = 'Fabio Classo'
print(nome.upper())
print(nome.lower())
print(nome.title())
print(nome.capitalize())
print(nome.swapcase())

