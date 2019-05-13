

# Listas


cursos = ['Python', 'Django', 'Kivy', 'C#', 'Ruby','Rails']

# indices
print(cursos[0])
print(cursos[1])
print(cursos[-1])

print(cursos.index('Python'))
print(cursos.index('Kivy'))
print(cursos.index('Rails'))

print()

# slicing
print(cursos[1:4])  #'Django', 'Kivy', 'C#']

# adicionar itens
cursos.append('Android')  # vai adicionar Android no final da lista
print(cursos)

cursos.insert(1, 'JavScript')
print(cursos)


cursos2 = ['PHP', 'C++']

cursos.extend(cursos2)
print(cursos)

# copias

cursos3 = cursos[:]
print(cursos3)

print(id(cursos))
print(id(cursos3))


# removendo items
cursos3.remove('PHP')
print(cursos3)

cursos3.pop(1)  # vazio deleta o último item
print(cursos3)

del cursos3[3]
print(cursos3)

del cursos3[:]  # apaga todo conteudo
print(cursos3)

# del cursos3
# print(cursos3)



# ordenar

cursos.sort(reverse=False)
print(cursos)

cursos4 = sorted(cursos)
print(cursos4)

# Membro do grupo

print('Pascal' in cursos)
print('Pascal' not in cursos)
print('Python' not in cursos)
print('Python' in cursos)

print()

#loops

for num, curso in enumerate(cursos, start=1):
    print(num, '=>', curso)

print()

cursos_str = ', '.join(cursos)
print(cursos_str)

print()

# zip
question = ['Name', 'Question', 'Favorite Color']
answer = ['Lancelot', 'the holy grail', 'blue']

for q, a in zip(question, answer):
    print("What's yours {}? It's {}".format(q,a))
