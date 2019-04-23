# argumentos de palavra chave /key word arguments


def info(nome, idade):
    print(f'Nome:{nome}')
    print(f'Idade:{idade}')


# info('Fabio', 40)
# info(40, 'Fabio')

# argumentos padrão

def info2(nome, idade=40):
    print(f'Nome:{nome}')
    print(f'Idade:{idade}')


info2(idade=30, nome='Jurandir')  # valores nomeados