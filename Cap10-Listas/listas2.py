

# listas aninhadas

cursos = [

    ['Python1', 'Python2', 'Django'],
    ['PHP1', 'PHP2', 'Laravel'],
    ['Ruby1', 'Ruby2', 'Rails'],

]

for modulo in cursos:
    print(modulo)

print()

for modulo in cursos:
    for num, curso in enumerate(modulo, start=1):
        print(f'{num} ==> {curso}')


p = ['Python1', 'Python2', 'Django']
print(type(p))

t = tuple(p)
print(t)
print(type(t))

p2 = list(t)
print(type(p2))

print(p)
p.reverse()  # inverter
print(p)

print(len(p))
print(min(p))
print(max(p))