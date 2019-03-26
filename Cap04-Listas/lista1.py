

disciplinas = ['Fisica', 'Quimica', 'Matematica', 'Biologia']

# print(disciplinas)

# indexing
# print(disciplinas[0])
# print(disciplinas[1])
# print(disciplinas[2])
# print(disciplinas[3])
# print(disciplinas[-1])

# print(disciplinas.index('Fisica'))
# print(disciplinas.index('Quimica'))
# print(disciplinas.index('Matematica'))
# print(disciplinas.index('Biologia'))

#slicing/ fatias

#print(disciplinas[2:])

disciplinas2 = disciplinas[1:3]
# print(disciplinas2)

#append - adiciona no final da lista

disciplinas.append('Psicologia')
disciplinas.append('Historia')
disciplinas.append('Informatica')
# print(disciplinas)

#insert - insere no inicio da lista
disciplinas.insert(0, 'Geografia')
disciplinas.insert(2, 'Artes')
# print(disciplinas)

#extend
nova_disciplinas = ['Musica']
nova_disciplinas.extend(disciplinas)
# print(nova_disciplinas)


## removing items
#del - indice

# del nova_disciplinas[0]
# del nova_disciplinas[2]
# print(nova_disciplinas)

# #remove
# nova_disciplinas.remove('Matematica')
print(nova_disciplinas)


#pop
# nova_disciplinas.pop() # deleta o ultimo item
# nova_disciplinas.pop(0)
# print(nova_disciplinas)



#ordenando
numeros = [10,8,5,4,3,9,6,1,2,0]
numeros.sort(reverse=True)
print(numeros)


nova_disciplinas.sort()
# print(nova_disciplinas)


# copiar lista [:]
num2 = numeros[:]
num2[0] = 'Dez'  # reatribuição

print(num2)
print(numeros)
print(id(numeros))
print(id(num2))







