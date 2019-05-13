

# Listas


cursos = ('Python', 'Django', 'Kivy', 'C#', 'Ruby','Rails')

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


# copias

cursos3 = cursos[:]
print(cursos3)

print(id(cursos))
print(id(cursos3))



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

i = 1
while i < len(cursos):
    print(i, cursos[i])
    i+=1

print()

cursos_str = ', '.join(cursos)
print(cursos_str)

print()

# zip
question = ['Name', 'Question', 'Favorite Color']
answer = ['Lancelot', 'the holy grail', 'blue']

for q, a in zip(question, answer):
    print("What's yours {}? It's {}".format(q,a))
