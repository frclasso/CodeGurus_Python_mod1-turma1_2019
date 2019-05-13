

# dicionarios


zara = {'Nome':'Zara', 'Idade': 2, 'Profissao':'Dentista', 'id':1}

#ler dados
print(zara)
print(zara['Nome'])
print(zara['Idade'])
print(zara['Profissao'])
print(zara['id'])
print()

for k, v in zara.items():
    print(k,'==>', v)

print()
print('Chaves')
print(zara.keys())

print()
print('Valores')
print(zara.values())
print()

# Atualizar/alterar valores
print()
zara['Idade'] = 30
print(zara['Idade'])
print()

zara['email'] = 'zara@email.com'

for k, v in zara.items():
    print(k,'==>', v)

zara.update({'Telefone':'48 999993333', 'Idade': 28})

for k, v in zara.items():
    print(k,'==>', v)

print()

zara2 = zara.copy()

for k, v in zara2.items():
    print(k,'==>', v)

print()

# removendo items

del zara2['Telefone']
for k, v in zara2.items():
    print(k,'==>', v)

zara2.clear()
print(zara2)

del zara2

zara3 = {'Nome': 'Zara', 'Idade': 28, 'Profissao': 'Dentista','Nome':'Luli'}  # nome duplicado
print(zara3)

print(len(zara))