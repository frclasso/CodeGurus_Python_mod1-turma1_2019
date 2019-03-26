# dicionarios
# dict = {key : value}

dados_pessoais = {
	'nome':'Fabio',
 	'sobrenome':'Classo',
  	'email':'fabio.classo@eail.com',
  	'Profissão':'Developer',
  	'nacionalidade':'Brasileiro'
  }

# print(dados_pessoais['nome'])
# print(dados_pessoais['sobrenome'])

print()
# print("Usuario: {} {} \nemail:{}\nProfissão:{}\nNacionalidade:{}".format(
# 		dados_pessoais['nome'],
# 		dados_pessoais['sobrenome'],
# 		dados_pessoais['email'],
# 		dados_pessoais['Profissão'],
# 		dados_pessoais['nacionalidade']
# 		)
# 	)


# reatribuir valor
dados_pessoais['Profissão'] = 'Programador'
print(dados_pessoais['Profissão'])

# inserir novo campo
dados_pessoais['telefone'] = '(48)999977777'

# remover um campo

# del dados_pessoais['nacionalidade']  # colchetes
dados_pessoais.pop('nacionalidade') # parenteses

# get 
#print(dados_pessoais['nacionalidade'])
print(dados_pessoais.get('nacionalidade'))


# print("Usuario: {} {} \nemail:{}\nProfissão:{}\nTelefone:{}".format(
# 		dados_pessoais['nome'],
# 		dados_pessoais['sobrenome'],
# 		dados_pessoais['email'],
# 		dados_pessoais['Profissão'],
# 		#dados_pessoais['nacionalidade'],
# 		dados_pessoais['telefone']
# 		)
# 	)

print(dados_pessoais.keys())
print(dados_pessoais.values())
print(dados_pessoais.items())


myDict = {}
print(type(myDict))


