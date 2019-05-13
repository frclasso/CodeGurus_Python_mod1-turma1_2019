

zara_lista = ['Nome', 'Idade', 'Profissao', 'id']

zara_dict = dict.fromkeys(zara_lista,'Nulo')

print(zara_dict)
print()

zara2 = {'Nome':'Zara', 'Idade': 2, 'Profissao':'Dentista', 'id':1}
print('O valor do campo: {}'.format(zara2['Nome']))
print('O valor do campo: {}'.format(zara2['Idade']))
print('O valor do campo: {}'.format(zara2['Profissao']))
print('O valor do campo: {}'.format(zara2['id']))

# print('O valor do campo: {}'.format(zara2['sexo']))
print('O valor do campo: {}'.format(zara2.get('sexo')))

# set default
print('O valor do campo: {}'.format(zara2.setdefault('sexo', 'Fem')))